
import logging
import json

import requests

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class WebhookController(http.Controller):

    @http.route('/webhook', auth='public', methods=['POST'], cors="*", csrf=False)
    def get_follower_info(self, **kwargs):
        request_body = http.request.httprequest.data
        # data = request_body.data
        json_data = json.loads(request_body)
        data_user = json_data.get('app_id', None)
        _logger.info(data_user)
