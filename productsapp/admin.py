from django.contrib import admin

from productsapp.models import Product, Price

# Register your models here.
admin.site.register(Product)
admin.site.register(Price)
