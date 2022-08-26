# -*- coding: utf-8 -*-
from odoo import models, fields, _,api


class VssUser(models.Model):
    _inherit = 'res.users'

    message = fields.Char(string="Message")
    other_info = fields.Char(string="Other information")

class VssEmployees(models.Model):
    _inherit = 'hr.employee'

    pincode = fields.Char(string="Pincode")
    password = fields.Char(string="Password")

class VssCar(models.Model):
    _name = "vss.car"
    _description = "vss car"

    name = fields.Char(string="Name")
    refer = fields.Char(string="CAR", readonly=True,required=True,copy=False,default='New')
    horse_power = fields.Integer(sring="Horse Power")
    door_number = fields.Integer(string="Door number")
    driver_id = fields.Many2one('res.partner')
    parking_id = fields.Many2one('vss.parking')
    feature_ids = fields.Many2many('vss.car.feature',string="Feature Car")
    total_speed = fields.Integer(string='total speed',compute='_onchange_total')
    status = fields.Selection(
        [('new', 'New'),
         ('used', 'Used'),
         ('sold', 'Sold')],
        'Status', default="new")
    car_sequence = fields.Char(string="Sequence")

    image = fields.Binary(attachment=True,string= 'image')
    car_price = fields.Float(string='Car price')
    car_total = fields.Float()
    @api.model
    def create(self, vals):
        if vals.get('refer','New') =='New':
            vals['refer']=self.env['ir.sequence'].next_by_code('vss.car') or _('New')
        result = super(VssCar,self).create(vals)
        return result
    @api.depends('horse_power')
    def _onchange_total(self):
        for rec in self:
            rec.total_speed = rec.horse_power*5

    @api.onchange('car_total')
    def onchange_result(self):
        print('ok')
        for rec in self:
            rec.car_total = rec.car_price + rec.parking_id.parking_price
            print(rec.car_total)







