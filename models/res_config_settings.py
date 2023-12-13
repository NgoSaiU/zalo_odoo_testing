from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    access_token = fields.Char(string='Access token dùng để gọi các Official Account API', config_parameter='odoo_whatsapp_integration1.access_token')
