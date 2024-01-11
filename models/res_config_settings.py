from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    access_token = fields.Char(string='Access token dùng để gọi các Official Account API', config_parameter='odoo_whatsapp_integration1.access_token', readonly=True)
    authen_code = fields.Char(string='Authencation code zalo', config_parameter='odoo_whatsapp_integration1.authen_code', readonly=True)
    app_id = fields.Char(string='ID của ứng dụng', config_parameter='odoo_whatsapp_integration1.app_id')
    secret_key = fields.Char(string='Khóa bí mật của ứng dụng', config_parameter='odoo_whatsapp_integration1.secret_key')
    
    def test_button(self):
        # _logger.info("Acction Button:")
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://oauth.zaloapp.com/v4/oa/permission?app_id=' + self.app_id + '&redirect_uri=http%3A%2F%2Flocalhost%3A8069%2Fpermission',
        }
    
    @api.model
    def get_access_token(self):
        records = self.env['res.config.settings'].sudo().create({})
        value = records.get_accessToken
        _logger.info(value)
        return value

    @api.model
    def get_value(self):
        _logger.info(self.app_id)
        _logger.info("hầuusyf adsfaudysf")

        return self.app_id
        
    @property
    def get_appid(self):
        return self.app_id
    
    @property
    def get_accessToken(self):
        return self.access_token
    


    

    
