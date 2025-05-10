from django.urls import path
from store.views import product_list, product_detail, cart_add, cart_remove, cart_detail

urlpatterns = [
    path('boutique', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', cart_remove, name='cart_remove'),
]
