from django.shortcuts import render, get_object_or_404
from soccer.models import Product, PlayerImage

## Create your views here.
def index(request):
    products = Product.objects.all()
    extra_images = PlayerImage.objects.all()
    return render(request, "soccer\\index.html", {'products': products,'extra_images': extra_images})

def player_detail(request, slug):
    products = get_object_or_404(Product, slug=slug)
    extra_images = products.extra_images.all()
    return render(request, 'soccer\\player_detail.html', {'products': products, 'extra_images': extra_images})

