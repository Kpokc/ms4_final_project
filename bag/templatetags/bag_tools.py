from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return format(float(price) * float(quantity), ".2f")


@register.filter(name='price_by_size')
def calc_size_price(price, size):

    if size == "small":
        return format(float(price * 1), ".2f")
    if size == "medium":
        price = float(price) * 1.25
        return format(price, ".2f")
    if size == "large":
        price = float(price) * 1.35
        return format(price, ".2f")
