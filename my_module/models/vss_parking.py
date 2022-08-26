# -*- coding: utf-8 -*-
from odoo import models, fields, _

# Tạo model câu 6
class VssParking(models.Model):
    _name = "vss.parking"
    _description = "vss parking car"

    name = fields.Char(string="Parking name")
    cars_id = fields.One2many('vss.car','parking_id')
    parking_price=fields.Float(string="Parking Price")


