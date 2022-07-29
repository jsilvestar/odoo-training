# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Academy(http.Controller):

    @http.route('/academy/academy', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/academy/academy/objects', auth='public')
    def list(self, **kw):
        return request.render('academy.listing', {
            'root': '/academy/academy',
            'objects': request.env['academy.academy'].search([]),
        })

    @http.route('/academy/academy/objects/<model("academy.academy"):obj>', auth='public')
    def object(self, obj, **kw):
        return request.render('academy.object', {
            'object': obj
        })
