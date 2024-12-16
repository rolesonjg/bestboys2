from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale


# class CustomWebsiteSale(WebsiteSale):
#
#     @http.route(['/shop/cart/update_json'], type='json', auth="public", website=True)
#     def cart_update_json(self, product_id, quantity=1, **kwargs):
#         # Add your custom logic for adding the product to the cart
#         response = super(CustomWebsiteSale, self).cart_update_json(product_id, quantity, **kwargs)
#
#         # Optionally return additional data like custom messages
#         return response
