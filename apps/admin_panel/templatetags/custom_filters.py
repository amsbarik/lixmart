from django import template
import datetime
from django.utils.safestring import mark_safe

register = template.Library()

# template filter for date filter
@register.filter
def abbreviate_month(date):
    if isinstance(date, datetime.date):
        return date.strftime('%d %b %Y')
    return date


# template filter to access dictionary values by key
@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)



@register.filter
def index(sequence, position):
    try:
        return sequence[position]
    except IndexError:
        return None
    

# model fields active or inactive 
# @register.filter(name='active_inactive')
# def active_inactive(value):
#     return "Active" if value else "Inactive"


@register.filter(name='active_inactive')
def active_inactive(value):
    if value:
        return mark_safe('<span class="badge bg-success ">Active</span>')
    else:
        return mark_safe('<span class="badge bg-danger ">Inactive</span>')