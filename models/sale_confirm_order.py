from odoo import models, fields, api, _
import urllib.parse as parse
from odoo.exceptions import UserError
from itertools import groupby
import logging
_logger = logging.getLogger(__name__)

class SaleConFirm(models.Model):
    _inherit = 'sale.order'
    
    # def action_confirm(self):
    #     _logger.info(self.order_line.order_id)

    #     pass 

