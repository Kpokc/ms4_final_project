from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JjkOhGTC1vx7XHrTAAdvk0iEn3pMIbBVdWzQlFN98EpjCSNs1zUckaZwK753yvgjvLgGYOh2xr0bpDdbjVdd95P00y48vCXow',
        'client_secret': 'client_secret_test',
    }

    return render(request, template, context)
