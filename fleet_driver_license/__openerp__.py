# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 HESATEC (<http://www.hesatecnica.com>).
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

{   
    "name"        : "Gestion des permis de conduire",
    "version"     : "1.0",
    "category"    : "Vertical",
    'complexity'  : "normal",
    "author"      : "Inovativ Developpement",
    "website"     : "http://www.inovativdeveloppement.ma",
    "depends"     : ["fleet_management"],
    "summary"     : "Gestion des permis",
    "description" : """
Gestion des permis
==========================

This application allows you to manage driving licenses.

""",

    "data" : [

        'view/license_view.xml',
        'data/driver_license_category_data.xml',
        'data/license_cron.xml',

        ],
    "application": True,
    "installable": True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
