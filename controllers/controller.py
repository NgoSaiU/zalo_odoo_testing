import logging
import json

import requests

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class WebhookController(http.Controller):

    @http.route('/permission',type='http', auth='none', methods=['GET'], cors="*", csrf=False)
    def get_follower_info(self, **kwargs):
        
        # Lấy giá trị "code" từ đối số truyền vào
        code = request.params.get('code')
        _logger.info("Authen code is:")
        _logger.info(code)
        _logger.info("=*=*=")

    
        if code:
            # _logger.info(f'The received code is: {code}')

            # Lấy bản ghi cần cập nhật trong model ResConfigSettings
            # settings_model = request.env['res.config.settings']
            # record = settings_model.sudo().search([])
            # if record:
            #     record.write({'authen_code': code})
            # else:
            #     settings_model.create({'authen_code': code}) 
            request.env['ir.config_parameter'].sudo().set_param('odoo_whatsapp_integration1.authen_code', code)

            _logger.info('=====')
            # for i in record:
            #     _logger.info(i['authen_code'])
            #     _logger.info(i['app_id'])
            
            # if not record:
            #     record = settings_model.sudo().create({})

            # Cập nhật trường authen_code với giá trị mới

            ICP = request.env['ir.config_parameter'].sudo()
            authen_code_up = ICP.get_param('odoo_whatsapp_integration1.authen_code')
            # # authen_code_up = self.env['ir.config_parameter'].get_param('odoo_whatsapp_integration1.authen_code')
            # _logger.info(f'authen code new: {authen_code_up}')

            _logger.info("Truy suất thông tin code đã lưu trữ: ")
            _logger.info(authen_code_up)
            _logger.info("===Tiến hành lấy acess_token")

            # done
            secret_key = ICP.get_param('odoo_whatsapp_integration1.secret_key')
            app_id = ICP.get_param('odoo_whatsapp_integration1.app_id')
            # _logger.info("app_id :")
            # _logger.info(app_id)
            # _logger.info("secret_key: ")
            # _logger.info(secret_key)


            # Lấy access_token!
            url = "https://oauth.zaloapp.com/v4/oa/access_token"
            headers = {
                "secret_key": secret_key
            }
            body = {
                "code": code,
                "app_id": app_id,
                "grant_type": "authorization_code"
            }

            response = requests.post(url, headers=headers, data=body)

            if response.status_code == 200:
                # Lấy access_token từ dữ liệu JSON trả về
                data = response.json()
                access_token = data.get("access_token")
                refresh_token = data.get("refresh_token")

                if access_token:
                    # print("Access Token:", access_token)
                    _logger.info("access token là: ")
                    _logger.info(access_token)
                    _logger.info("refresh token là: ")
                    _logger.info(refresh_token)

                    # Tiến hành lưu vào model và kiểm tra kết quả xem ntn

                    # failed
                    # request.env['zalo.author.message'].sudo().create({
                    # 'access_token1': access_token})
                    
                    # failed
                    # settings = request.env['res.config.settings']
                    # recording = settings.sudo().search([])
                    # if recording:
                    #     recording.write({'access_token': access_token})
                    #     request.env.cr.commit() 
                    #     recording.env.cr.commit() 
                    # else:
                    #     settings.sudo().create({'access_token': access_token})
                    #     request.env.cr.commit() 
                    #     recording.env.cr.commit() 
                    
                    # failed
                    # config_settings = request.env['res.config.settings'].sudo().search([('user_id', '=', request.env.user.id)], limit=1)
                    # if config_settings:
                    #     # Update the field value
                    #     config_settings.access_token = access_token
                    #     # Save the changes
                    #     config_settings.save()

                    # run
                    request.env['ir.config_parameter'].sudo().set_param('odoo_whatsapp_integration1.access_token', access_token)
                    _logger.info("lưu trạng thái mới")
                    


                    # config_settings = request.env['res.config.settings'].sudo().create({})
                    # config_settings.write({'access_token': access_token})


                    ICP = request.env['ir.config_parameter'].sudo()
                    access_token1_model = ICP.get_param('odoo_whatsapp_integration1.access_token')
                    _logger.info(access_token1_model)
                    # access_token1_model = recording.access_token1 if recording else None

                    _logger.info("access token đã được lưu vào model là: ")
                    # xuất hiện giá trị false
                    
                else:
                    _logger.info("Không tìm thấy Access Token trong dữ liệu trả về.")
            else:
                _logger.info("Request không thành công. Mã lỗi:", response.status_code)

        else:
            _logger.warning('No code parameter found in the request.')


        return "Cấu hình zalo thành công"

        # lấy authen code (xong)
        # có thể không cần lưu trữ giá trị authen_code làm gì cho mệt!!
        # từ đó fetch api để lấy được acsess_token và lưu vào model nốt. (xong)
        # Test thử ascess_token mới lấy xem, Liệu có thể nhắn tin được hay không? (xong)
    
        # vấn đề nan giải là chưa có lưu được giá trị vào model 

 




