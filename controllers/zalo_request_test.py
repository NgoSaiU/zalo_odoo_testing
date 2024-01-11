from odoo import http
from odoo.http import request
from odoo.http import Response
import requests
import json

class WebhookController(http.Controller):

    @http.route('/webhooks', type='http', auth='public', methods=['POST'], csrf=False)
    def webhook_listener(self, **post):
        
        data = request.jsonrequest

        return Response(json.dumps({'status': 'success'}), content_type='application/json;charset=utf-8', status=200)
    

    @http.route("/pos/rpc/sendtemplate", auth="public", type="json", methods=["POST"], csrf=False)

    
    def pos_example3(self,**kwargs):
        phone =  kwargs['phone'] 
        api_url = 'https://business.openapi.zalo.me/message/template'   
        # access_token = "ZDYs9a_xCYkEsxSgJ_mp9epUiI55vaTS-9hD7p3qIME7hhKp6SzYTO_qamWxctzrXUc13ZcDOb-RoPifMv5lM-FIxoidgofikStL4Ikf3LIPtVKC68foTu_QaoKIg1T8eT3o21MEALEsxj5N5hjKKxVwhpCrWL1B_CIgBtQDTtUspeWQD8XI7VFOqMLfjYSqp9F2H4hZFYZ0nSPaMhyT6yF1vsS6cJCXkysrJWo3Dagc-CeP6fHENgQqgJzcbtj3--3mBq2_CYhVnT1w7vHJ5zRDqs5CjXaS-yF-73kd8rYdsgCa68KeHSNYp4XdhaqfqCkgJdNaVJFqfxTsI_fmE_sxZNvXsWr_zgUJB6J1TcFvdeqZOj17GVY8hW1X_MvInvcGFtsY6b37m_qM1PiQJaXKy1QpDKZWDoS"  # Replace with your actual access token
        access_token = kwargs['accessToken']

        data = {
            "phone": phone,
            "template_id": "305357",
            "template_data": {
                "price": 1000,
                "customer_name": "Ngo Sai U",
                "id": '123',
                "order_id": '123'
            },
            "tracking_id": 'tracking_id'
        }

        headers = {
            'access_token': access_token,
            
        }

        json_data = json.dumps(data)

        try:
            response = requests.post(api_url, headers=headers, data=json_data)
            response.raise_for_status()
            result = response.json()
            # return json.dumps({"hellp": "yui"})
            return result
            print(result)
            
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")

        