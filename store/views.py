from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product_store, Cart, CartItem


# Create your views here.


def product_list(request):
    products = Product_store.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product_store, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id', None))
    if created:
        request.session['cart_id'] = cart.id
    return render(request, 'shop/cart_detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id', None))
    if created:
        request.session['cart_id'] = cart.id
    product = get_object_or_404(Product_store, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_remove(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')
