import requests

from odoo import http
from odoo.http import request
from datetime import datetime
from num2words import num2words
import urllib.parse as urlparse
from urllib.parse import parse_qs
from odoo import models,fields,api
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    basic_synch_partner = fields.Char(string="Basic Synch Partner")



class ExecutiveAreaWise(models.Model):
    _inherit = 'executive.area.wise'

    basic_synch_area = fields.Char(string="Sync Area")



class ProductTemplate(models.Model):
    _inherit = "product.template"

    basic_synch_product = fields.Char(string='Sync Product')

