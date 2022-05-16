# -*- coding: utf-8 -*-
{
    'name': "API Bcore",

    'summary': """
        API của Bcore""",

    'description': """
        API của Bcore
    """,

    'author': "CLOUDMEDIA CO.,LTD",
    'website': "https://cloudmedia.vn/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'co_bcore', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
