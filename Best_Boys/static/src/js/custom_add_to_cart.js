odoo.define('Best_Boys.custom_add_to_cart', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    // Override the add to cart button
    $(document).on('click', '.btn_add_to_cart', function (e) {
        var $this = $(this);
        var product_id = $this.data('product_id');
        var quantity = 1;  // You can modify this as needed

        // Add product to cart using Ajax
        ajax.jsonRpc('/shop/cart/update_json', 'call', {
            'product_id': product_id,
            'quantity': quantity,  // Pass quantity to the server-side method
        }).then(function (data) {
            // After adding the product, redirect directly to the checkout page (payment page)
            window.location.href = '/shop/checkout';
        });

        // Prevent the default action (redirection to the cart page)
        e.preventDefault();
    });
});
