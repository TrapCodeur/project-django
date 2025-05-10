from django.contrib import admin
from store.models import Product_store, Cart, CartItem
# Register your models here.
admin.site.register(Product_store)
admin.site.register(Cart)
admin.site.register(CartItem)