# -*- coding: utf-8 -*-

from odoo import models, fields

class AdjustmentLines(models.Model):
    _inherit = 'stock.valuation.adjustment.lines'


former_cost_per_unit = fields.Float('Former Cost(Per Unit)', compute='_compute_former_cost_per_unit',
    digits=5), store=True)
