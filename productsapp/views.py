from django.http import HttpResponse
from django.shortcuts import render, redirect

from productsapp.models import Product

from .forms import PriceForm
# Create your views here.


def index(request):
    #return HttpResponse("PKO")
    return render(request, "index (copy).html")


def get_products(request):
    lista = Product.objects.all()
    return render(request, "products.html", {"productos": lista})


def get_product(request, id):
    producto = Product.objects.get(id=id)
    return render(request, "product.html", {"producto": producto, "form": PriceForm()})

def create_price(request, id):
    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            form.precio = request.precio
            form.producto = Product.objects.get(id=id)
            form.save()
            
        return redirect('product', id=id)
    else:
        return redirect('product', id=id)