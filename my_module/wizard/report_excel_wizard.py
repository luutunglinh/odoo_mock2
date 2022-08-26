# -*- coding: utf-8 -*-
from odoo import models, fields, _,api

class ReportExcellWizarad(models.TransientModel):
    _name = 'vss.report.car.wizard'
    _description = "Excell Wizard Car"

    name = fields.Integer(string="Max of horse power")

    def print_report_excel(self):
        appointments = self.env['vss.car'].search_read([])
        print(appointments)
        data={
            'appointments':appointments,
            'form_data':self.read()[0],
            'name1':self.name
        }
        return self.env.ref('my_module.print_report_ptd_xls').report_action(self, data=data)
