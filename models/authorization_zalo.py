from odoo import models, fields

class ZaloAuthorization(models.Model):
    _name = 'zalo.author.message'

    access_token1 = fields.Char(string='Access token dùng để gọi các Official Account API', config_parameter='odoo_whatsapp_integration1.access_token1')
    