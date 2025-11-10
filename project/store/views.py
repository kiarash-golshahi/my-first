from .models import Product
from django.shortcuts import render

def product_details(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    return render(request, template_name='store/product-details.html', context=context)
