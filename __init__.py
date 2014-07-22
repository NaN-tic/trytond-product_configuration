# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .helper import *
from .configuration import *
from .product import *


def register():
    Pool.register(
        Configuration,
        CategoryCompany,
        Category,
        TemplateCompany,
        Template,
        module='product_configuration', type_='model')
