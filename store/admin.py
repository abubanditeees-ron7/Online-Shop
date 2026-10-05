from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'created_at'
    )

    search_fields = (
        'name',
    )

    readonly_fields = (
        'created_at',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'old_price',
        'stock',
        'is_available',
        'is_featured'
    )

    list_filter = (
        'category',
        'is_available',
        'is_featured'
    )

    search_fields = (
        'name',
        'description'
    )

    readonly_fields = (
        'created_at',
        'updated_at'
    )