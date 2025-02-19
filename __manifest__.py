# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System 2",

    'summary': "Custom Module for Hospital Management",

    'description': """
    Custom Module for Hospital Management using models, menus, actions and views
    """,

    'author': "DunBot",
    'website': "https://github.com/Dunbot",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

