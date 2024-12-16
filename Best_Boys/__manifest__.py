# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Mohammed Dilshad TK (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Best_Boys',
    'version': '17.0.1.0.0',
    "category": "Industries",
    'summary': """Best_Boys""",
    'description': """This module facilitates the booking of cleaning processes 
    and effectively manages the cleaning procedures.""",
    'author': '',
    'company': '',
    # 'maintainer': 'Cybrosys Techno Solutions',
    # 'website': "https://cybrosys.com/",
    'depends': ['base', 'website', 'sale'],
    'data': [
        'views/Homepage.xml',
        'views/Shop.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/productdetails.xml'
             ],
    'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [
"static/src/js/custom_add_to_cart.js"
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
