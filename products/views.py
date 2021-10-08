from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def products(request):
    """ A view to return the products page """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if request.GET:
            if 'category' in request.GET:
                category = request.GET['category'].split(',')
                products = products.filter(category__name__in=category)
                category = Category.objects.filter(name__in=category)

                if 'q' in request.GET:
                    print(request.GET['q'])

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('products'))

                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    context = {
        'products': products,
        'searchterm': query,
        'current_category': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return product page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
