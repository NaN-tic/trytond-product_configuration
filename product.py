# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import Model, ModelSQL, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

from .helper import ByCompanyMixin

__all__ = ['CategoryCompany', 'Category', 'TemplateCompany', 'Template']
__metaclass__ = PoolMeta


class CategoryCompany(ModelSQL):
    '''Product Category by Company fields'''
    __name__ = 'product.category.company'

    category = fields.Many2One('product.category', 'Category', required=True,
        ondelete='CASCADE', select=True)
    company = fields.Many2One('company.company', 'Company', required=True,
        ondelete='CASCADE', select=True)

    @staticmethod
    def default_company():
        return Transaction().context.get('company')


class Category(object, ByCompanyMixin):
    __metaclass__ = PoolMeta
    __name__ = 'product.category'
    _by_company_model = 'product.category.company'
    _by_company_field = 'category'


class TemplateCompany(ModelSQL):
    '''Product Template by Company fields'''
    __name__ = 'product.template.company'

    template = fields.Many2One('product.template', 'Template', required=True,
        ondelete='CASCADE', select=True)
    company = fields.Many2One('company.company', 'Company', required=True,
        ondelete='CASCADE', select=True)

    @staticmethod
    def default_company():
        return Transaction().context.get('company')


class Template(object, ByCompanyMixin):
    __metaclass__ = PoolMeta
    __name__ = 'product.template'
    _by_company_model = 'product.template.company'
    _by_company_field = 'template'
