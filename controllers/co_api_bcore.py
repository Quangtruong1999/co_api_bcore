# -*- coding: utf-8 -*-
from odoo import http


class CoApiBcore(http.Controller):
    @http.route('/api/get_investment_package', type='json', auth='public')
    def api_get_investment_package(self, **kw):
        investment_packge = http.request.env['product.product'].sudo().search([])
        data = []
        for package in investment_packge:
            data_tmp = {}
            data_tmp['id'] = package.id
            data_tmp['name'] = package.name
            data_tmp['interest_rate'] = package.interest_rate
            data_tmp['invest_period'] = package.invest_period
            data.append(data_tmp)

        return {
            "code": 200,
            "messages": "Lấy thông tin thành công",
            "data": data
        }

    @http.route('/api/register_investment_package', type='json', auth='public')
    def api_register_investment_package(self, user_id, product_id, price_unit, **kw):
        user = http.request.env['res.users'].sudo().search([('id', '=', user_id)])
        data = []
        if user:
            vals = {}
            vals['partner_id'] = user.partner_id.id
            products = http.request.env['product.product'].sudo().search([('id', '=', product_id)])
            if products:
                sale_order = http.request.env['sale.order'].sudo().browse()
                sale_order_line = http.request.env['sale.order.line'].sudo().browse()

                sale_order.sudo().create(vals)
                orders = http.request.env['sale.order'].sudo().search([('partner_id', '=', user.partner_id.id)])
                for order in orders:
                    order_lines = http.request.env['sale.order.line'].sudo().search([('order_id', '=', order.id)])
                    if not order_lines:
                        items = [{
                            'order_id': order.id,
                            'product_id': products.id,
                            'price_unit': price_unit
                        }]
                        sale_order_line.sudo().create(items)
                return {
                    "code": 200,
                    "messages": "Tạo đơn hàng thành công!",
                    "data": data
                }
            return{
                "code": 400,
                "messages": "Không có sản phẩm/dịch vụ trong hệ thống!",
                "data": data
            }
        return {
            "code": 400,
            "messages": "Không có thông tin người dùng trong hệ thống",
            "data": data
        }
