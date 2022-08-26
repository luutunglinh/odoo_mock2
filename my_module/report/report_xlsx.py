# -*- coding: utf-8 -*-

import datetime

from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.my_module.baocaochitietexcel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("HMMMMM",data['appointments'])
        print("name", data['name1'])
        sheet = workbook.add_worksheet('Báo cáo chi tiết phương tiện đo lường trong tập đoàn Excel')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#fffbed', 'border': True})
        # merge_format = workbook.add_format({'bold': True, 'align': 'center', 'border': True})
        row = 0
        col = 0
        sheet.set_column('A:Y', 20)
        sheet.write(row,col,'Reference',bold)
        sheet.write(row, col+1, 'Name', bold)
        sheet.write(row, col+2, 'Horse Power', bold)
        sheet.write(row, col+3, 'Door Number', bold)
        sheet.write(row, col+4, 'Driver', bold)
        sheet.write(row, col+5, 'Parking', bold)


        for appointment in data['appointments']:
            if data['name1'] <= appointment['horse_power']:
                row += 1
                sheet.write(row, col, appointment['refer'])
                sheet.write(row, col + 1, appointment['name'])
                sheet.write(row, col + 2, appointment['horse_power'])
                sheet.write(row, col + 3, appointment['door_number'])
                sheet.write(row, col + 4, appointment['driver_id'][1])
                sheet.write(row, col + 5, appointment['parking_id'][1])







        # sheet.set_column('A:Y', 20)