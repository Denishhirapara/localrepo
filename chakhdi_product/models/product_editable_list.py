# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.addons.http_routing.models.ir_http import slug, slugify


class ProductEditableList(models.Model):
    _name = 'product.editable.list'

    name = fields.Char('Name')
    default_code = fields.Char('Internal Reference')
    list_price = fields.Float('Sales Price')
    categ_id = fields.Many2one('product.category', 'Product Category')
    pos_categ_id = fields.Many2one('pos.category', 'Point of Sale Category')
    vendor = fields.Many2one('res.partner', 'Vendor')
    vendor_price = fields.Float('Vendor Price')
    public_categ_ids = fields.Many2many('product.public.category', string='eCommerce Category')
    is_product = fields.Boolean(string='Is Product')
    unique_id = fields.Integer('Unique Id')
    brand = fields.Many2one('product.brand', 'Brand')
    product_commission = fields.Float('Commission(%)', default='1.25')
    product_color = fields.Char("Product Color")
    product_style = fields.Char('Product Style')
    l10n_in_hsn_code = fields.Char('HSN/SAC Code', default='6403')

    size_range = fields.Selection([
        ('2-5', '2-5'),
        ('6-10', '6-10'),
        ('6-12', '6-12'),
    ], string='Size Range', default='6-12')
    size_list = [
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14')
    ]
    size_from = fields.Selection(size_list, string='From', default="6")
    size_to = fields.Selection(size_list, string="To", default="12")

    # unique_website_url = fields.Char('Unique Website URL')

    def _set_tax(self):
        if self.list_price > 999:
            model, res_id = self.env['ir.model.data'].get_object_reference('l10n_in', '1_sgst_sale_18')
            if self.env[model].search([('id', '=', res_id)]):
                return self.env['account.tax'].browse(res_id)
        else:
            model, res_id = self.env['ir.model.data'].get_object_reference('l10n_in', '1_sgst_sale_12')
            if self.env[model].search([('id', '=', res_id)]):
                return self.env['account.tax'].browse(res_id)

    def _set_supplier_tax(self):
        if self.vendor_price > 999:
            model, res_id = self.env['ir.model.data'].get_object_reference('l10n_in', '1_sgst_purchase_18')
            if self.env[model].search([('id', '=', res_id)]):
                return self.env['account.tax'].browse(res_id)
        else:
            model, res_id = self.env['ir.model.data'].get_object_reference('l10n_in', '1_sgst_purchase_12')
            if self.env[model].search([('id', '=', res_id)]):
                return self.env['account.tax'].browse(res_id)

    def create_product(self):
        un_website_url = slugify(self.name or '').strip().strip('-')
        # match_url = self.env['product.template'].search([('unique_website_url', '=', un_website_url)], limit=1)
        # if not match_url:
        #     self.unique_website_url = slugify(self.name or '').strip().strip('-')
        # else:
        #     url = self.name + " " + str(self.id)
        #     self.unique_website_url = slugify(url or '').strip().strip('-')
        product = self.env['product.template'].create({
            'name': self.name,
            'default_code': self.default_code,
            'list_price': self.list_price,
            'categ_id': self.categ_id.id,
            'pos_categ_id': self.pos_categ_id.id,
            'type': 'product',
            'available_in_pos': True,
            'company_reference': self.name,
            'l10n_in_hsn_code': self.l10n_in_hsn_code,
            'taxes_id': self._set_tax(),
            'supplier_taxes_id': self._set_supplier_tax(),
            'public_categ_ids': self.public_categ_ids,
            'size_range': self.size_range,
            'size_from': self.size_from,
            'size_to': self.size_to,
            'seller_ids': [(0, 0, {
                'name': self.vendor.id,
                'price': self.vendor_price
            })],
            'brand': self.brand.id,
            'product_commission': self.product_commission,
            'product_color': self.product_color,
            'product_style': self.product_style
        })
        # 'unique_website_url': self.unique_website_url,
        product.onchange_size_range()
        self.is_product = True
        self.unique_id = product.id
        product_variants_cost = self.env['product.product'].search([('name', '=', self.name)])
        if product_variants_cost:
            product_variants_cost.standard_price = self.vendor_price
        return product

    def show_product(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'product.template',
            'view_ids': self.env.ref('product.product_template_only_form_view').id,
            'target': 'current',
            'res_id': self.unique_id
        }
