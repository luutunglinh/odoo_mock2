# -*- coding: utf-8 -*-
import odoo.http
from odoo import http
from odoo.http import request
import json


class Main(http.Controller):
    @http.route('/car',type='http',auth='none')
    def car(self):
        return json.dumps({
            "content":'Welcome to API'
        })
    @odoo.http.route(['/car/<dbname>/<id>'],type='http', auth="none", sitemap=False, cors='*', csrf=False)
    def car_handeler(self,dbname,id,**kw):
        model_name="vss.car"
        try:
            # registry = odoo.modules.registry.Registry(dbname)
            # with odoo.api.Environment.manage(), registry.cursor() as cr:
            #     env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
            #     rec = env[model_name].search([('id', '=', int(id))], limit=1)
            #     response = {
            #         "status": "ok",
            #         "content": {
            #             "name": rec.name,
            #
            #         }
            #     }
            car = request.env['vss.car'].sudo().search([])
            print(car)
        except Exception:
            response = {
                "status": "error",
                "content": "not found"
            }
        return json.dumps(response)

    @http.route('/car01', type='http', auth='none')
    def car01(self):
        mylist = []
        models_ids = request.env['vss.car'].sudo().search([], order='horse_power desc', limit=3)
        print(models_ids.read([]))
        for models_id in models_ids:
            response = {
                "status": "ok",
                "content": {
                    "name": models_id.name,
                    'refer': models_id.refer,
                    'horse_power':models_id.horse_power,
                    'door_number':models_id.door_number,
                }
            }
        return json.dumps(response)
        # cars = models_ids.read([])
        # for key in cars:
        #     print(key)












