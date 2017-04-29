from django import template


register = template.Library()


@register.filter(name='times')
def times(number):
    return range(1, number+1)


@register.filter(name='to_int')
def to_int(number):
    return round(number)
