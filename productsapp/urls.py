from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path("products", views.get_products, name="get_products"),

    path("product/<int:id>", views.get_product, name="get_product")
]
