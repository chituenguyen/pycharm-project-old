from django.contrib import admin
from .models import OrderItem, Order, Item, BillingAddress, Coupon,refund


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ordered','refund')


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item)
admin.site.register(BillingAddress)
admin.site.register(Coupon)
admin.site.register(refund)
