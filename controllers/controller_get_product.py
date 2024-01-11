import json
import requests
from urllib.parse import urlparse, parse_qs
from odoo import http
from odoo.http import request
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)


class GetProduct(http.Controller):

    # @http.route('/product',type='http', auth='public', methods=['GET'], cors="*", csrf=False)
    # def get_follower_info(self, id,**kwargs):
    #     url = http.request.httprequest.url
    #     parsed_url = urlparse(url)
  
    #     pass

    @http.route(['/order_confirmed'], auth='public', csrf=False) 
    def my_controller_method(self, redirect=None, **post):
        _logger.info('abc')
        url = http.request.httprequest.url

        parsed_url = urlparse(url)
        id = parse_qs(parsed_url.query)['id'][0]


        Order = http.request.env["sale.order"]
        orders = Order.search([('name', '=', id)])
        
        current_dateTime = datetime.now()


        for order in orders:
            order.order_line._validate_analytic_distribution()

            order.write({
                'state': 'sale',
                'date_order': current_dateTime
            })

        # games = games.filtered(lambda g: g.hidden == False)
        for order in orders:
            # _logger.info(game.order_line.order_id)
            _logger.info(order.name)
            _logger.info(order.create_date)
            _logger.info(order.amount_total)
        
        # return json.dumps({'test':'abc'})
        return http.request.render(
            "odoo_whatsapp_integration1.inf_suc",
            
        )
    

    @http.route("/order")
    def list(self):
        # Game = http.request.env["tutorial.game"]
        # games = Game.search([])
        # games = games.filtered(lambda g: g.hidden == False)
        url = http.request.httprequest.url

        parsed_url = urlparse(url)
        id = parse_qs(parsed_url.query)['id'][0]
        
        Order = http.request.env["sale.order"]
        orders = Order.search([('name', '=', id)])
                
        return http.request.render(
            "odoo_whatsapp_integration1.current_sale_order",
             {"orders":orders},
        )
    
