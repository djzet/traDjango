from .models import Product, Category
from django.contrib import admin


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
