from django.contrib import admin
from .models import Category, Product, ProductOrder, OrderStatus, UserOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(OrderStatus)
admin.site.register(UserOrder)