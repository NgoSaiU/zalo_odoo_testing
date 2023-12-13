from odoo import models, fields, api, _

class SaleOrderInherit(models.Model):
    _inherit = "res.partner"
    
    userzalo_id = fields.Char(string='User Id Zalo')

