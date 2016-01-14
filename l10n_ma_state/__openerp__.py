# -*- coding: utf-8 -*-
##############################################################################
#
#    l10n MOROCCO States module for OpenERP
#    Copyright (C) 2015-2016 AGORA DEVELOPPEMENT
#    (http://www.agoradeveloppement.com)
#    @author Mohamed HABOU
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
    'name': 'Morocco States (Régions)',
    'summary': 'Populate Database with the 12 Moroccan States (Régions)',
    'version': '9.0.0.1.0',
    'category': 'Morocco Localization',
    'author': "Agora Developpement, Odoo Community Association (OCA)",
    'website': 'http://www.agoradeveloppement.com',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'data/res_country_state_data.yml',
    ],
    'installable': True,
    'images': [
        'static/src/img/screenshots/1.png'
    ],
}
