# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import Model
from trytond.pool import Pool
from trytond.transaction import Transaction

__all__ = ['ByCompanyMixin']


class ByCompanyMixin:
    '''Mixin with the getter/setter methods for fields dependant of company.'''
    _by_company_model = None
    _by_company_field = None

    @classmethod
    def get_by_company_fields(cls, records, names):
        assert cls._by_company_model, ('_by_company_model attribute not set '
            'to model %s' % cls.__name__)
        assert cls._by_company_field, ('_by_company_field attribute not set '
            'to model %s' % cls.__name__)

        pool = Pool()
        ByCompany = pool.get(cls._by_company_model)

        record_ids = [r.id for r in records]
        company_id = Transaction().context.get('company')
        by_company_records = ByCompany.search([
                (cls._by_company_field, 'in', record_ids),
                ('company', '=', company_id),
                ])

        res = {}
        for fname in names:
            res[fname] = {}.fromkeys(record_ids, None)
        for by_company_record in by_company_records:
            for fname in names:
                record_id = getattr(by_company_record,
                    cls._by_company_field).id
                val = getattr(by_company_record, fname)
                if isinstance(val, Model):
                    val = val.id
                res[fname][record_id] = val
        return res

    @classmethod
    def set_by_company_field(cls, records, name, value):
        assert cls._by_company_model, ('_by_company_model attribute not set '
            'to model %s' % cls.__name__)
        assert cls._by_company_field, ('_by_company_field attribute not set '
            'to model %s' % cls.__name__)

        pool = Pool()
        ByCompany = pool.get(cls._by_company_model)

        record_ids = [r.id for r in records]
        company_id = Transaction().context.get('company')
        by_company_records = ByCompany.search([
                (cls._by_company_field, 'in', record_ids),
                ('company', '=', company_id),
                ])
        if by_company_records:
            ByCompany.write(by_company_records, {
                    name: value,
                    })
            done_records = [getattr(bcr, cls._by_company_field)
                for bcr in by_company_records]
            todo_records = list(set(records) - set(done_records))
        else:
            todo_records = records

        if todo_records:
            ByCompany.create([{
                        cls._by_company_field: r.id,
                        'company': company_id,
                        name: value,
                        } for r in todo_records])
