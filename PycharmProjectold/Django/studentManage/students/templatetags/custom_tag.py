import datetime
from django import template
from django.utils import timezone

register = template.Library()
@register.filter(name='cal_age')
def cal_age(value):
    current_date=timezone.now().year
    return current_date-value.year