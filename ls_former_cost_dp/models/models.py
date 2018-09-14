# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.addons import decimal_precision as dp

class AdjustmentLines(models.Model):
    _inherit = 'stock.valuation.adjustment.lines'

    # quantity = fields.Float(
    #     'Quantity', default=1.0,
    #     digits=(16,6), required=True)
    former_cost_per_unit = fields.Float(
        'Former Cost(Per Unit)', compute='_compute_former_cost_per_unit', store=True,digits=(16,6))

    @api.one
    @api.depends('former_cost', 'quantity')
    def _compute_former_cost_per_unit(self):
        self.former_cost_per_unit = self.former_cost / (self.quantity or 1.0)