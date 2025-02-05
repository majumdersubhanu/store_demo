from django.db import models


class ProductImage(models.Model):
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=2083)

    def __str__(self):
        return self.image_url

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class QR(models.Model):
    url = models.URLField(max_length=2083)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "QR Code"
        verbose_name_plural = "QR Codes"


class Product(models.Model):
    # Basic product info
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(default=0)
    discount_percentage = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    # Physical details
    weight = models.FloatField(null=True, blank=True)
    dimension_width = models.FloatField(null=True, blank=True)
    dimension_height = models.FloatField(null=True, blank=True)
    dimension_depth = models.FloatField(null=True, blank=True)

    # Additional information
    warranty_information = models.CharField(max_length=255, blank=True, null=True)
    shipping_information = models.CharField(max_length=255, blank=True, null=True)
    availability_status = models.CharField(max_length=50, blank=True, null=True)
    return_policy = models.CharField(max_length=255, blank=True, null=True)
    minimum_order_quantity = models.IntegerField(null=True, blank=True)

    # Meta data
    meta_created_at = models.DateTimeField(null=True, blank=True)
    meta_updated_at = models.DateTimeField(null=True, blank=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    qr_code = models.ForeignKey(QR, on_delete=models.SET_NULL, blank=True, null=True)

    # Images and relationships
    thumbnail = models.URLField(max_length=2083, blank=True, null=True)
    featured_image = models.ForeignKey(
        ProductImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="featured_image",
    )
    images = models.ManyToManyField(ProductImage, related_name="product_images")
    categories = models.ManyToManyField(Category, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(
        auto_now_add=True
    )  # you can also use auto_now_add=True if appropriate
    reviewer_name = models.CharField(max_length=255)
    reviewer_email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Review for {self.product.title} by {self.reviewer_name}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
