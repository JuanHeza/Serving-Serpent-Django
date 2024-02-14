from django.http import HttpResponse
from django.shortcuts import render

from productsapp.models import Product

# Create your views here.


def index(request):
    #return HttpResponse("PKO")
    return render(request, "index (copy).html")


def get_products(request):
    lista = Product.objects.all()
    return render(request, "products.html", {"productos": lista})


def get_product(request, id):
    producto = Product.objects.get(id=id)
    return render(request, "product.html", {"producto": producto})
