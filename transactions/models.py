from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from carts.models import CartItem


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=100, decimal_places=2)
    items = models.ManyToManyField(CartItem, related_name="order_items")
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} [Rs {self.total}] on {self.datetime}"

    def save(self, *args, **kwargs):
        self.total = sum([item.product.price for item in self.items.all()])
        super().save(*args, **kwargs)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=120)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.username} - {self.transaction_id}"
