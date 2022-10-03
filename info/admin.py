from django.contrib import admin

from .models import Firm, Stock, Product, Category, Brand

# Register your models here.
admin.site.register(Firm)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Stock)

