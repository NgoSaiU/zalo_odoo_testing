from odoo import models, fields, tools, api, _
import urllib.parse as parse
from odoo.exceptions import UserError
from itertools import groupby   
import logging
from lxml import html
import requests
_logger = logging.getLogger(__name__)
from odoo.addons.mail.tools import link_preview


class TestSendDiscuss(models.Model):
    _inherit = 'mail.link.preview'

    @api.model
    def _create_from_message_and_notify(self, message):

        _logger.info('ham dang ow day')
        _logger.info(str(message.body))

        if tools.is_html_empty(message.body):
            return self
        urls = set(html.fromstring(message.body).xpath('//a[not(@data-oe-model)]/@href'))
        # _logger.info(str(html.fromstring(message.body).xpath('//a[not(@data-oe-model)]/@href')))
        link_previews = self.env['mail.link.preview']
        requests_session = requests.Session()
        # Some websites are blocking non browser user agent.
        requests_session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        })
        link_preview_values = []

        for url in list(urls):
            # _logger.info(url)
            if preview := link_preview.get_link_preview_from_url(url, requests_session):
                preview['message_id'] = message.id
                link_preview_values.append(preview)
            if len(link_preview_values) > 5:
                break
        if link_preview_values:
            _logger.info(link_preview_values)
            link_previews = self.env['mail.link.preview'].create(link_preview_values)
            self.env['bus.bus']._sendone(message._bus_notification_target(), 'mail.record/insert', {
                'LinkPreview': link_previews._link_preview_format()
            })



