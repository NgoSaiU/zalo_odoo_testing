from odoo import models, fields, api, _
import requests
import json
import logging
_logger = logging.getLogger(__name__)


class SendContactMessage(models.TransientModel):
    _name = 'whatsapp.wizard.contact'

    user_id = fields.Many2one('res.partner', string="Tên người nhận", default=lambda self: self.env[self._context.get('active_model')].browse(self.env.context.get('active_ids')))
    mobile_number = fields.Char(related='user_id.mobile', required=True)
    message = fields.Text(string="Tin nhắn", required=True)
    userid = fields.Char(related='user_id.userzalo_id', string="Mã người dùng zalo", readonly=True)

    def send_custom_contact_message(self):
        ICP = self.env['ir.config_parameter'].sudo()
        # access_token = ICP.get_param('odoo_whatsapp_integration1.access_token')
        access_token = ICP.get_param('odoo_whatsapp_integration1.access_token')
        # Cách khác
        # c1
        # access_token = self.env['ir.config_parameter'].get_param('odoo_whatsapp_integration1.access_token')
        # c2
        # access_token = request.env['ir.config_parameter'].sudo().get_param('odoo_whatsapp_integration1.access_token')
        # print("Access Token:", access_token)
        _logger.info("Access Token mới là:")
        _logger.info(access_token)
        # _logger.info(type(access_token))
        
         # Thao tac gửi
        url = 'https://openapi.zalo.me/v3.0/oa/message/cs'
        headers = {
            "access_token": access_token,
        }
        data = {
            "recipient": {
                # "user_id": "1202890738565373280"
                "user_id": self.userid,
            },
            "message": {
                "text": self.message
            }
        }

        json_data = json.dumps(data)

        try:
            response = requests.post(url, headers=headers, data=json_data)
            response.raise_for_status()  # Nếu có lỗi, sẽ ném một exception
            result = response.json()
            print(result)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")