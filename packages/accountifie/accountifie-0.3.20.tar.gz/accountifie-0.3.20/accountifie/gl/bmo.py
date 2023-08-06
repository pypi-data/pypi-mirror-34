"""
Based on Andy Robinson's DoubleTalk accounting framework; used
with permission
"""

from decimal import Decimal
import logging
from deepdiff import DeepDiff

from django.db import transaction
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

import accountifie.query.query_manager_strategy_factory as QMSF
from accountifie.environment.models import Variable
from accountifie.gl.models import TranLine, Company, Account, Counterparty

DZERO = Decimal('0')

logger = logging.getLogger('default')
GL_STRATEGY = 'postgres'

def _model_to_id(x):
    return x if type(x) == str else x.id


def get_gl_strategy():
    dflt_strategy = Variable.objects \
                            .filter(key='DEFAULT_GL_STRATEGY') \
                            .first()
    return dflt_strategy.value if dflt_strategy else GL_STRATEGY


def recalc_all():
    for model in apps.get_models():
        if issubclass(model, BusinessModelObject):
            for bmo in model.objects.all():
                logger.info('Saving all objects for %s' % bmo, extra={'corrId': 'ACCOUNTIFIE.GL'})
                try:
                    bmo.save()
                except Exception as e:
                    msg = 'Recalc Fail. %s. %s' % (bmo.__dict__, e)
                    logger.exception(msg, extra={'corrId': 'ACCOUNTIFIE.GL'})

    # delete any orphan tranlines
    for tl in TranLine.objects.all():
        try:
            bmo_obj = tl.content_type.get_object_for_this_type(id=tl.object_id)
            if bmo_obj is None:
                tl.delete()
        except ObjectDoesNotExist as e:
            tl.delete()


class BusinessModelObject(object):
    """Something else which has an effect on the GL.

    BMOs will typically create General Ledger entries when
    saved.  They should efficiently update/change their
    GL entries and not create database churn unless there
    is a change.

    Make other models inherit from this as a mixin.

    Regrettably one then needs to override save() and
    delete() for the other models, until I find a cunning
    way to make it happen.

    """

    def delete_from_gl(self):
        "Find and remove all GL entries which depend on self"
        if get_gl_strategy() == 'remote':
            bmo_id = '%s.%s' %(self.short_code, self.id)
            QMSF.getInstance() \
                .get(strategy='remote') \
                .delete_bmo_transactions(self.company.id, bmo_id)
        elif GL_STRATEGY == 'postgres':
            TranLine.objects \
                    .filter(bmo_id='%s.%s' % (self.short_code, self.id)) \
                    .delete()

    def create_gl_transactions(self, trans):
        gl_strategy = get_gl_strategy()
        if GL_STRATEGY == 'postgres':
            self.create_postgres_gl_transactions(trans)
        else:
            self.create_remote_gl_transactions(trans)

    def create_postgres_gl_transactions(self, trans):
        for td in trans:
            
            lines = self._postgres_lines(td)
            if sum(l['amount'] for l in lines) == DZERO:
                db_tl_set = TranLine.objects.filter(bmo_id=td['bmo_id'])
                new_tl_set = [TranLine(**l) for l in lines]

                if db_tl_set.count() == 0:
                    save_tranlines(None, new_tl_set)
                else:
                    db_lines = [tl._to_dict() for tl in db_tl_set]
                    new_lines = [tl._to_dict() for tl in new_tl_set]
                    chgs = DeepDiff(db_lines, new_lines)
                    
                    if len(chgs) > 0:
                        # if any changes then just delete/set to historical
                        save_tranlines(db_tl_set, new_tl_set)
            else:
                logger.error('Imbalanced GL entries for %s' % td['bmo_id'])
    
    def _postgres_lines(self, td):
        return [{'company_id': _model_to_id(td['company']),
                 'date': date,
                 'date_end': date,
                 'comment': comment[:99] if comment else '',
                 'account_id': _model_to_id(account),
                 'amount': Decimal("{0:.2f}".format(amount)),
                 'counterparty_id': _model_to_id(counterparty),
                 'tags': ','.join(tags or []),
                 'bmo_id': td['bmo_id'],
                 'source_object': self,
                 'closing_entry': td.get('closing_entry', False)
                } for account, date, amount, counterparty, tags, comment, trans_id in td['lines']]

    def create_remote_gl_transactions(self, trans):
        for td in trans:
            try:
                comment = td['comment'][:99]
            except:
                comment = ''

            d2 = td.copy()
            if 'date_end' not in d2:
                d2['date_end'] = d2['date']

            try:
                tags = ','.join(d2.pop('tags'))
            except:
                tags = ''

            d2['company'] = d2['company'].id if isinstance (d2['company'], Company) else d2['company']

            lines = d2.pop('lines')
            trans_id = d2.pop('trans_id')
            bmo_id = d2.pop('bmo_id')

            lines = [{'account': account.id if isinstance (account, Account) else account,
                        'amount': "{0:.2f}".format(amount),
                        'counterparty': counterparty.id if isinstance (counterparty, Counterparty) else counterparty,
                        'tags': tags
                        } for account, amount, counterparty, tags in lines]

            QMSF.getInstance() \
                .get(strategy='remote') \
                .create_gl_transactions(d2, lines, trans_id, bmo_id)

    def update_gl(self):
        "Fix up GL after any kind of change"
        trans = self.get_gl_transactions()
        self.delete_from_gl()
        self.create_gl_transactions(trans)

    def get_gl_transactions(self):
        """Override this.  Create a list of transactions.

        Create a list of transactions in dictionary form
        which should exist.  It will create them all in the
        GL on saving if they do not already exist.
        """
        return []

    def get_company(self):
        return self.company.id


def _postgres_lines():
    pass


@transaction.atomic
def save_tranlines(old_tl_set, new_tl_set):
    if old_tl_set:
        old_tl_set.delete()

    for l in new_tl_set:
        try:
            l.save()
        except Exception as e:
            msg = 'Error saving tranlines. %s. %s' % (e, l.__dict__)
            print(msg)
            #logger.exception(msg, extra={'corrId': 'ACCOUNTIFIE.GL'})

def on_bmo_save(sender, **kwargs):
    """Alternative method - maintain GL through a signal

    Master-detail BMOs can't use a simple save hook, and
    instead need to set a signal to call this'
    """
    sender.update_gl()
