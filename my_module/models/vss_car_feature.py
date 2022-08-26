# -*- coding: utf-8 -*-
from odoo import models, fields, _

class VssCarFeature(models.Model):
    _name = "vss.car.feature"
    _description = "vss car feature"

    name = fields.Char(string="Feature")
    note = fields.Text(string="Note")
