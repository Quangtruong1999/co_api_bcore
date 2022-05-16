# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        return super(SaleOrder, self).write(vals)

