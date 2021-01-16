from django.contrib import admin
from .models import Product, Order, OrderItem, Category, Tags

# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Tags)
admin.site.register(Category)
