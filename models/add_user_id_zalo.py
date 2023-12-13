from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    user_zalo = fields.Char(string='User Zalo', help='Zalo username for the user')

    @api.onchange('user_zalo')
    def _onchange_user_zalo(self):
        """Perform actions when UserZalo field is changed."""
        if self.user_zalo:
            self.other_field = "Updated value based on UserZalo: {}".format(self.user_zalo)
        else:
            self.other_field = False
