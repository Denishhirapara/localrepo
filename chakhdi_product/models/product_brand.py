# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import fields,models,api

class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string="Title")
    url = fields.Char(string="Url")
    description = fields.Html(string="Description")
    image = fields.Binary(string="Image")


