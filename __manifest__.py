{
    'name': "Whatsapp Odoo Integration1 - Copyy",
    'summary': """
        This module allows you to send whatsapp messages about the sale orders, purchase orders, 
        invoice order amount, and delivery orders along with order items to the respective user.""",

    'description': """
    """,
    'author': "Techspawn Solutions Pvt. Ltd.",
    'website': "http://www.techspawn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'web', 'stock', 'purchase','account','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/sms_security.xml',
        'views/user_zalo.xml',
        'wizard/wizard_multiple_contact.xml',
        'views/views.xml',
        'views/template.xml',
        'views/res_config_settings_views.xml',
        'views/setting_inherit_view.xml',
        'views/view_conf_order.xml',
        'views/current_saleorder.xml',
        'views/connect_success.xml',
        'wizard/message_wizard.xml',
        'wizard/wizard.xml',
        'wizard/wizard_contact.xml',
        'wizard/share_action.xml',
    ],
     'assets': {
         'web.assets_backend': [
             'odoo_whatsapp_integration1/static/src/composer_path.js',

         ],
         'point_of_sale._assets_pos': [
              # PoS files
             'odoo_whatsapp_integration1/static/src/psend_zalo.js',
             'odoo_whatsapp_integration1/static/src/pos_send_zalo.xml',
            #  'odoo_whatsapp_integration1/static/src/**/*',
         ],

         
     },
    'images':['static/description/main.gif'],
    
    'application': True
}


