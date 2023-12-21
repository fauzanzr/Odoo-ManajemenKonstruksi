# -*- coding: utf-8 -*-
# from odoo import http


# class Inventaris(http.Controller):
#     @http.route('/inventaris/inventaris', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventaris/inventaris/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventaris.listing', {
#             'root': '/inventaris/inventaris',
#             'objects': http.request.env['inventaris.inventaris'].search([]),
#         })

#     @http.route('/inventaris/inventaris/objects/<model("inventaris.inventaris"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventaris.object', {
#             'object': obj
#         })
