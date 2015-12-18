# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from datetime import datetime
from openerp.osv import fields, osv
import time


class fleet_vehicle(osv.osv):
    _inherit = "fleet.vehicle"
    _columns = {
        'driver_license_category_ids': fields.many2many('driver.license.category', 'vehicle_license_category_rel', 'vehicle_id','license_category_id', "Driver's License categories"),
    }

    #Driver must have an appropriate license to be affected to a car
    def _check_driver_license_categ(self,cr,uid,ids):

        for vehicle in self.browse(cr, uid, ids):
            driver_license_category_ids = vehicle.driver_license_category_ids.ids
            driver_permis= [i.category.id for i in vehicle.employee_id.driver_license_ids]
            intersect =[i for i in driver_license_category_ids if i in driver_permis]
            if intersect or not vehicle.employee_id or not driver_license_category_ids:
                return True
            else:
                return False


    _constraints = [(_check_driver_license_categ, "This driver hasn't an appropriate license", ['employee_id','driver_license_category_ids'])]

class driver_license_category(osv.osv):
    _name = 'driver.license.category'
    _columns = {
        'name':fields.char('Catégorie du permis', size=128),
        }

class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    _columns = {
        'driver_license_ids': fields.one2many('driver.license', 'driver_id', string="Driver's Licenses"),
        }

    def name_search(self,cr, uid, name='',args=None, operator='ilike', context={}, limit=80):

        if not context.get('driver_license_category_ids') and not context.get('kit_id') and not context.get('unit_id') and not context.get('trailer1_id'):
            return super(hr_employee,self).name_search(cr, uid, name=name, args=args, operator=operator, context=context, limit=limit)
        else:
            #driver_license_category_ids: Table des cagterories de permis autorisé => chercher seulement les chauffeurs disposants de ces permis
            if context.get('driver_license_category_ids'):
                driver_license_category_ids = context.get('driver_license_category_ids')[0][2]
                driver_license_category_ids2 = driver_license_category_ids
            else:
                driver_license_category_ids = []
                driver_license_category_ids2 = []
                if context.get('unit_id'):
                    print '----------unit---------------'
                    unit = self.pool.get('fleet.vehicle').browse(cr, uid, context.get('unit_id'), context)
                    driver_license_category_ids = unit.driver_license_category_ids.ids
                if context.get('trailer1_id'):
                    print '----------trailer---------------'
                    trailer1 = self.pool.get('fleet.vehicle').browse(cr, uid, context.get('trailer1_id'), context)
                    print trailer1.id, trailer1.driver_license_category_ids.ids
                    driver_license_category_ids2 = trailer1.driver_license_category_ids.ids
            
            drivers = self.search(cr, uid, args, context = context)
            tab=[] #table qui va accueillir les chauufeurs disposant des permis spécifiés dans le véhicule
            for dr in drivers:
                driver = self.pool.get('hr.employee').browse(cr, uid, dr, context=context)
                categories=[i.category.id for i in driver.driver_license_ids if datetime.strptime(i.date_out,'%Y-%m-%d')>= datetime.now()]
                intersect =[i for i in  driver_license_category_ids if i in categories]
                intersect2 =[i for i in  driver_license_category_ids2 if i in categories]
                print '----------------intersect---------'
                print categories, driver_license_category_ids, intersect, driver_license_category_ids, intersect2
                if (intersect and not context.get('trailer1_id')) or (intersect and context.get('trailer1_id') and intersect2):
                    tab.append(driver.id)
            args.append(('id', 'in' , tab))
            return super(hr_employee,self).name_search(cr, uid, name=name, args=args, operator=operator, context=context, limit=limit)

class driver_license(osv.osv):
    _name = 'driver.license'
    _columns = {
        'name':fields.char('Num', size=128, required=True),
        'driver_id':fields.many2one('hr.employee','Driver', required=True),
        'category': fields.many2one('driver.license.category', string='Catégorie', required=True),
        'date_in':fields.date('Date de délivrance', required=True),
        'date_out':fields.date('Date de fin de validité', required=True),
        }

    #check drivers licenses
    def check_driver_licenses(self, cr, uid, context=None):
        print '..................checking........................'
        tab=[]
        for l in self.search(cr, uid, [], context=context):
            license = self.browse(cr, uid, l, context=context)
            if datetime.strptime(license.date_out,'%Y-%m-%d') <= datetime.now():
                print '--------------------alert--------------------'
                tab.append(license)
            if tab:
                #Send Alert
                list_dest=[]
                admin = self.pool.get('res.users').browse(cr, uid, [1], context=context)
                list_dest.append(admin.partner_id.id)
                body = "These driver's licenses must be renewed:"
                for i in tab:
                    body += i.name +'-'+i.driver_id.name+', '

                nom_permis=license.name
                post_vars = {
                        'subject': "Licenses expired",
                        'body': body,
                        'partner_ids': list_dest,
                    } 

                thread_pool = self.pool.get('mail.thread')
                thread_pool.message_post(
                        cr, uid, False,
                        type="notification",
                        subtype="mt_license_expired",
                        context=context,
                        **post_vars)

class tms_unit_kit(osv.osv):
    _inherit = "tms.unit.kit"

    #Driver must have an appropriate license to be affected to a kit
    def _check_driver_license_categ(self,cr,uid,ids):

        for kit in self.browse(cr, uid, ids):
            driver_license_category_ids = []
            driver_license_category_ids2 = []

            if kit.unit_id:
                driver_license_category_ids = kit.unit_id.driver_license_category_ids.ids
            if kit.trailer1_id:
                driver_license_category_ids2 = kit.trailer1_id.driver_license_category_ids.ids

            driver_permis= [i.category.id for i in kit.employee_id.driver_license_ids]

            intersect =[i for i in driver_license_category_ids if i in driver_permis]
            intersect2 =[i for i in driver_license_category_ids2 if i in driver_permis]

            if (intersect and not kit.trailer1_id) or (intersect and kit.trailer1_id and intersect2) or not kit.employee_id or not kit.unit_id.driver_license_category_ids:
                return True
            else:
                return False

    _constraints = [(_check_driver_license_categ, "This driver hasn't an appropriate license", ['employee_id','unit_id','trailer1_id'])]

class tms_travel(osv.osv):
    _inherit = "tms.travel"

    #Driver must have an appropriate license to be affected to a travel
    def _check_driver_license_categ(self,cr,uid,ids):

        for travel in self.browse(cr, uid, ids):
            driver_license_category_ids = []
            driver_license_category_ids2 = []
            #if travel.kit_id:
            #    driver_license_category_ids = travel.kit_id.driver_license_category_ids.ids
            if travel.unit_id:
                driver_license_category_ids = travel.unit_id.driver_license_category_ids.ids
            if travel.trailer1_id:
                driver_license_category_ids2 = travel.trailer1_id.driver_license_category_ids.ids

            driver_permis= [i.category.id for i in travel.employee_id.driver_license_ids]

            intersect =[i for i in driver_license_category_ids if i in driver_permis]
            intersect2 =[i for i in driver_license_category_ids2 if i in driver_permis]

            if (intersect and not travel.trailer1_id) or (intersect and travel.trailer1_id and intersect2) or not travel.employee_id or not travel.unit_id.driver_license_category_ids:
                return True
            else:
                return False


    _constraints = [(_check_driver_license_categ, "This driver hasn't an appropriate license", ['employee_id','unit_id','trailer1_id'])]

