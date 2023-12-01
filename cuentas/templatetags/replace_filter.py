from django import template

register = template.Library()

@register.filter
def replace_hyphen(value):
    return value.replace("_", " ").title()