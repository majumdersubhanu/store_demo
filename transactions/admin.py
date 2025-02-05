from django.contrib import admin

from transactions.models import Order, Transaction

# Register your models here.
admin.site.register(Order, options={"readonly_fields": ["total"]})
admin.site.register(Transaction)
