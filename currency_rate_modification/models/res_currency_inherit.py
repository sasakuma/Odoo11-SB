# -*- coding: utf-8 -*-

from odoo import models, fields

class ResCurrencyInherit(models.Model):
    _inherit = 'res.currency'

    rate = fields.Float(compute='_compute_current_rate', string='Current Rate', digits=(12, 8),
                        help='The rate of the currency to the currency of rate 1.')

class ResCurrencyRateInherit(models.Model):
    _inherit = 'res.currency.rate'

    rate = fields.Float(digits=(12, 8), help='The rate of the currency to the currency of rate 1')