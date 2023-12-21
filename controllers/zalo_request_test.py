from odoo import http
from odoo.http import request
from odoo.http import Response
import json

class WebhookController(http.Controller):

    @http.route('/webhooks', type='http', auth='public', methods=['POST'], csrf=False)
    def webhook_listener(self, **post):
        
        data = request.jsonrequest

        return Response(json.dumps({'status': 'success'}), content_type='application/json;charset=utf-8', status=200)
    

