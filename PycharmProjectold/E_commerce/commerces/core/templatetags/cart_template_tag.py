from django import template
from core.models import Order,OrderItem

register = template.Library()


@register.filter
def cart_item_count(user):
    result=0
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        order_item=OrderItem.objects.all()
        if qs.exists():
            for item in order_item:
                result+=item.quantity
            return result
    return 0
