from odoo import http
from odoo.http import request
import logging
import json

_logger = logging.getLogger(__name__)

class Testing(http.Controller):

    # @http.route('/testing', auth="public", cors="*", csrf=False, type='json', methods=['GET', 'POST'])
    @http.route('/testing', auth="public", website = True)
    def geting_value(self, **kw):
        # done
        config_settings = request.env['res.config.settings'].sudo().create({})
        value = config_settings.get_appid
        _logger.info(value)
        return value



    