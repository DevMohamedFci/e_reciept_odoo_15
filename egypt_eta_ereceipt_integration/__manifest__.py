# -*- coding: utf-8 -*-
{
    'name': "ETA E-Receipt Egypt",
    'summary': """
        ETA E-Receipt Egypt With Tow Solutions
    """,
    'description': """
    
    our Module , We can Use to Integration With Pos And ETA Egypt E reciept

    """,
   'author': 'Eng Mohamed Abd El-haleem Farag Allah , Tel:+201024548085 ',
    'website': 'dev.mohamedfci@gmail.com',

    'contributors': [
        ' ',
    ],
    'version': '0.1',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_device_config_view.xml',
        'views/pos_config_view.xml',
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/account_tax_view.xml',
        'views/uom_uom_view.xml',
        'views/pos_payment_method_view.xml',
        'views/pos_order_view.xml',
    ],
}