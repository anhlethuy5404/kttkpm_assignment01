from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        try:
            return int(value) * int(arg)
        except (ValueError, TypeError):
            return ''
