# -*- coding: utf-8 -*-
from odoo import http

# class LsFormerCostDp(http.Controller):
#     @http.route('/ls_former_cost_dp/ls_former_cost_dp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ls_former_cost_dp/ls_former_cost_dp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ls_former_cost_dp.listing', {
#             'root': '/ls_former_cost_dp/ls_former_cost_dp',
#             'objects': http.request.env['ls_former_cost_dp.ls_former_cost_dp'].search([]),
#         })

#     @http.route('/ls_former_cost_dp/ls_former_cost_dp/objects/<model("ls_former_cost_dp.ls_former_cost_dp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ls_former_cost_dp.object', {
#             'object': obj
#         })