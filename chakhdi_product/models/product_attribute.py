# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import fields,models,api

class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    auto_product_sku = fields.Boolean(string="Auto Product Sku")

class ProductAttributeValue(models.Model):
	_inherit = "product.attribute.value"

	code = fields.Char(string="Code")
