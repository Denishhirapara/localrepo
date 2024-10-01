# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    'name': 'Chakhdi Product',
    'version': '17.0.0.1.0',
    'description': """
""",
    'depends': ['base','product','point_of_sale','purchase','website_sale','project'],
    'data': [
    
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/product.xml',
        'views/product_attribute.xml',
        'views/product_brand.xml',
        'views/product_editable_list.xml',
        'views/qty_sum.xml',
        'report/product_label.xml',
        'views/project_portal.xml',
    ],

    'demo': [],
    'installable': True,
    'auto_install': False,
    'application':True,
}

