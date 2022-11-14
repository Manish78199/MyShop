from django.contrib import admin

from MyShop.models import order,OrderUpdate,product
# Register your models here.
admin.site.register(product)
admin.site.register(order)
admin.site.register(OrderUpdate)