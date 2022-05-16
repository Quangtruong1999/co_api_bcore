# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def create(self, values):
        return super(SaleOrderLine, self).create(values)

    def write(self, values):
        return super(SaleOrderLine, self).write(values)