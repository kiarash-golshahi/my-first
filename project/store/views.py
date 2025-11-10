from .models import Category, Product
from django.shortcuts import render

def category_page(request, id):
    category = Category.objects.get(id=id)
    products = category.products.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, template_name='store/category.html', context=context)

def product_details(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    return render(request, template_name='store/product-details.html', context=context)
