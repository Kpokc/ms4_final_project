from django.shortcuts import render

# Create your views here.

def contact(request):
    """ A view that renders the bag contents page """

    return render(request, 'contact/contact.html')