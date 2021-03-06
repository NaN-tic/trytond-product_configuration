# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, ModelSingleton

__all__ = ['Configuration']


class Configuration(ModelSingleton, ModelSQL, ModelView):
    '''Product Configuration'''
    __name__ = 'product.configuration'
