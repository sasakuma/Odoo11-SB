# -*- coding: utf-8 -*-

from odoo import models, fields

class StockvaluationInherit(models.Model):
    _inherit = 'stock.valuation.adjustment.lines'

former_cost_per_unit = fields.Float('Former Cost(Per Unit)', compute='_compute_former_cost_per_unit',
    digits=dp.get_precision('Product Price'), store=True)
