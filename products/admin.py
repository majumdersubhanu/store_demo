from django.contrib import admin

from products.models import QR, Category, Product, ProductImage, Review, Tag


# Register your models here.
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(QR)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "rating", "reviewer_name", "date")
    search_fields = ("product__title", "reviewer_name")
    list_filter = ("rating", "date")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "brand",
        "price",
        "stock",
        "discount_percentage",
        "rating",
    )
    search_fields = ("title", "brand", "sku")
    list_filter = ("brand", "categories")
    filter_horizontal = (
        "categories",
        "images",
    )
