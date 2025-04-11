from datetime import date, timedelta
from django import template

register = template.Library()

@register.filter
def is_urgent(deadline):
    if deadline:
        return date.today() >= (deadline - timedelta(days=1))
    return False
