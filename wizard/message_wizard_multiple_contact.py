from odoo import models, fields, api, _
import html2text
import urllib.parse as parse
import requests
import json

class SendMultipleContactMessage(models.TransientModel):
    _name = 'whatsapp.wizard.multiple.contact'

    user_id = fields.Many2one('res.partner', string="Tên người nhận", default=lambda self: self.env[self._context.get('active_model')].browse(self.env.context.get('active_ids')))
    partner_id = fields.Many2one('res.partner', string="Người nhận")
    mobile = fields.Char(required=True, string="Số điện thoại liên hệ")
    message = fields.Text(string="Tin nhắn", required=True)
    userid = fields.Char(related='user_id.userzalo_id', string="Mã người dùng zalo", readonly=True)

    def send_multiple_contact_message(self):
        if self.message and self.mobile:
            # message_string = ''
            # message = self.message.split(' ')
            # for msg in message:
            #     message_string = message_string + msg + ' '
            # message_string = parse.quote(message_string)
            # html2text.html2text(message_string)
            # message_string = message_string[:(len(message_string) - 3)]
            # number = self.mobile
            # link = "https://web.whatsapp.com/send?phone=" + number
            # send_msg = {
            #     'type': 'ir.actions.act_url',
            #     'url': link + "&text=" + message_string,
            #     'target': 'new',
            #     'res_id': self.id,
            # }
            # return send_msg


            ICP = self.env['ir.config_parameter'].sudo()
            access_token = ICP.get_param('odoo_whatsapp_integration1.access_token')

        
            #Thao tac gửi
            url = 'https://openapi.zalo.me/v3.0/oa/message/cs'
            headers = {
                'access_token': access_token,
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