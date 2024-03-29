from odoo import models, fields, api, _
import html2text
import urllib.parse as parse
import requests
import json


class MessageError(models.TransientModel):
    _name='display.error.message'
    def get_message(self):
        if self.env.context.get("message", False):
            return self.env.context.get('message')
        return False
    name = fields.Text(string="Tin nhắn", readonly=True, default=get_message)


class SendMessage(models.TransientModel):
    _name = 'whatsapp.wizard'

    user_id = fields.Many2one('res.partner', string="Tên người nhận", default=lambda self: self.env[self._context.get('active_model')].browse(self.env.context.get('active_ids')).partner_id)
    mobile_number = fields.Char(related='user_id.mobile', required=True)
    message = fields.Text(string="Tin nhắn")
    model = fields.Char('mail.template.model_id')
    template_id = fields.Many2one('mail.template', 'Use template', index=True)
    userid = fields.Char(related='user_id.userzalo_id', string="Mã người dùng zalo", readonly=True)

    @api.onchange('template_id')
    def onchange_template_id_wrapper(self):
        self.ensure_one()
        res_id = self._context.get('active_id') or 1
        values = self.onchange_template_id(self.template_id.id, self.model, res_id)['value']
        for fname, value in values.items():
            setattr(self, fname, value)

    def onchange_template_id(self, template_id, model, res_id):
        if template_id:
            values = self.generate_email_for_composer(template_id, [res_id])[res_id]
        else:
            default_values = self.with_context(default_model=model, default_res_id=res_id).default_get(
                ['model', 'res_id', 'partner_ids', 'message'])
            values = dict((key, default_values[key]) for key in
                          ['body', 'partner_ids']
                          if key in default_values)
        values = self._convert_to_write(values)
        return {'value': values}

    def generate_email_for_composer(self, template_id, res_ids, fields=None):
        multi_mode = True
        if isinstance(res_ids, int):
            multi_mode = False
            res_ids = [res_ids]
        if fields is None:
            fields = ['body_html']
        returned_fields = fields + ['partner_ids']
        values = dict.fromkeys(res_ids, False)
        template_values = self.env['mail.template'].with_context(tpl_partners_only=True).browse(template_id)._generate_template(res_ids, render_fields=fields)
        for res_id in res_ids:
            res_id_values = dict((field, template_values[res_id][field]) for field in returned_fields if
                                 template_values[res_id].get(field))
            res_id_values['message'] = html2text.html2text(res_id_values.pop('body_html', ''))
            values[res_id] = res_id_values
        return multi_mode and values or values[res_ids[0]]

    def send_custom_message(self):
        # if self.message and self.mobile_number:
        #     message_string = parse.quote(self.message)
        #     message_string = message_string[:(len(message_string) - 3)]
        #     number = self.user_id.mobile
        #     link = "https://web.whatsapp.com/send?phone=" + number
        #     send_msg = {
        #         'type': 'ir.actions.act_url',
        #         'url': link + "&text=" + message_string,
        #         'target': 'new',
        #         'res_id': self.id,
        #     }
        #     return send_msg
        
        ICP = self.env['ir.config_parameter'].sudo()
        access_token = ICP.get_param('odoo_whatsapp_integration1.access_token')


         # Thao tac gửi
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