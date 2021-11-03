from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return format(float(price) * float(quantity), ".2f")


@register.filter(name='price_by_size')
def price_by_size(price, size):

    if size == "small":
        return price
    if size == "medium":
        return price + 12
    if size == "large":
        return price + 20
#return format(price, ".2f")
