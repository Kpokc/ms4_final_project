from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return format(float(price) * float(quantity), ".2f")


@register.filter(name='price_by_size')
def price_by_size(price, size):

    if (size == "small") or (size == "SM"):
        return price
    if (size == "medium") or (size == "MD"):
        return price + 12
    if (size == "large") or (size == "LG"):
        return price + 20
