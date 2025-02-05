from django.db import models
from django.contrib.auth.models import User

from products.models import Product


# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, related_name="cart_items")

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
