from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    summary = models.TextField()
    avilable = models.BooleanField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def  __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Products'