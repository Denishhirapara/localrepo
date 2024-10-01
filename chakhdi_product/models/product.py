# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import fields,models,api,_
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _sql_constraints = [('unique_default_code','unique(default_code)',"Internal Reference must be unique !")]

    brand = fields.Many2one('product.brand',string="Brand")
    company_reference = fields.Char(string="Pos Name")
    size_range = fields.Selection([
        ('2-5', '2-5'),
        ('6-10', '6-10'),
        ('6-12', '6-12'),
    ], string='Size Range', default='6-12')

    size_list = [
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14')
    ]
    size_from = fields.Selection(size_list, string='Size From', default="6")
    size_to = fields.Selection(size_list, string="Size To", default="12")

    product_commission = fields.Float('Product Commission(%)', default=1.5)
    product_color = fields.Char(string="Product Color")
    product_style = fields.Char(string="Product Style")
    is_image_set = fields.Boolean(string="Is Image Set")
    # image_1920 = fields.Binary()
    promo_code = fields.Char(string="Promo Code")


    @api.model
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        if res.pos_categ_id.artical_code and not res.default_code:
            artical_code = res.pos_categ_id.artical_code
            res.default_code = artical_code + self.env['ir.sequence'].next_by_code('default.code')
        elif not res.default_code and not res.pos_categ_id.artical_code:
            res.default_code = self.env['ir.sequence'].next_by_code('default.code')
        return res

    @api.depends('product_variant_ids', 'product_variant_ids.default_code')
    def _compute_default_code(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.default_code = template.product_variant_ids.default_code

    @api.onchange('size_from', 'size_to')
    def onchange_size_range(self):
        attribute = self.env['product.attribute'].search([('auto_product_sku', '=', True)], limit=1)
        attribute_size = self.env['product.attribute.value']
        size_from = int(self.size_from)
        size_to = int(self.size_to)
        code_list = []
        for i in range(size_from, (size_to + 1)):
            code_list.append(str(i).zfill(2))
        if code_list:
            attribute_size = attribute_size.search([('code', 'in', code_list)])
            attribute_line_ids = [(5, 0, 0), (0, 0, {
                "attribute_id": attribute[0].id,
                "value_ids": [(6, 0, attribute_size.ids)]
            })]
            self.attribute_line_ids = attribute_line_ids

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.company_reference = self.name

class ProductProduct(models.Model):
    _inherit = "product.product"

    _sql_constraints = [('unique_default_code','unique(default_code)',"Internal Reference must be unique !")]

    company_reference = fields.Char(string="Pos Name",compute="_compute_product_variants",readonly=False,store=True)
    default_code = fields.Char('Internal Reference',index=True,compute="_compute_product_variants",readonly=False,store=True)
    barcode = fields.Char('Barcode', copy=False,compute="_compute_product_variants",
        help="International Article Number used for product identification.",readonly=False,store=True)

    @api.depends('product_template_attribute_value_ids','product_tmpl_id.default_code','company_reference')
    def _compute_product_variants(self):
        for rec in self:
            attribute_value = ''
            if rec.product_template_attribute_value_ids and rec.product_tmpl_id.default_code:
                for value in rec.product_template_attribute_value_ids:
                    if value.attribute_id.auto_product_sku == True:
                        attribute_value += value.product_attribute_value_id.code
                rec.default_code = rec.product_tmpl_id.default_code + '-' + attribute_value
                if not rec.barcode:
                    rec.barcode = rec.default_code
                if not rec.company_reference and attribute_value:
                    rec.company_reference = rec.product_tmpl_id.company_reference + ' ' + attribute_value
            

    @api.constrains('is_published')
    def _check_is_published(self):
        for rec in self:
            if rec.pos_categ_id.is_not_for_published:
                raise ValidationError(_("%s Category Product Are Not Allowed To Be Published On Website" % (rec.pos_categ_id.name)))


class PosCategory(models.Model):
    _inherit = "pos.category"

    artical_code = fields.Char(string="Article Code")
    is_not_for_published = fields.Boolean()
