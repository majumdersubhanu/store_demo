from django.contrib import admin

from carts.models import Cart, CartItem

# Register your models here.
admin.site.register(CartItem)
admin.site.register(Cart)
