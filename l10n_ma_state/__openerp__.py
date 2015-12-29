# -*- encoding: utf-8 -*-
##############################################################################
#
#    l10n FR States module for OpenERP
#    Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
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
    'description': """
Populate Database with Moroccan States (Région)
=============================================

Feature:
--------
    * Populate the table res_country_state with the Moroccan states """
    """(named 'Région').

Technical information:
----------------------
    * Use 3166-2:MA codifications without country prefix (more detail """
    """http://fr.wikipedia.org/wiki/ISO_3166-2:MA); 
    * Mise à jour des régions @ https://fr.wikipedia.org/wiki/R%C3%A9gions_du_Maroc

Copyright, Authors and Licence:
-------------------------------
    * Copyright: 2015-2016, Agora Developpement;
    * Author: Mohamed HABOU;
    * Licence: AGPL-3 (http://www.gnu.org/licenses/);""",
    'author': "Agora Developpement,Odoo Community Association (OCA)",
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
