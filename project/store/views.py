from .models import Category, Product
from django.shortcuts import get_object_or_404, render

def search(request):
    search_term = request.GET.get('search', '').strip()
    products = Product.objects.filter(title__icontains=search_term) if search_term else []
    context = {
        'search': search_term,
        'products': products,
    }
    return render(request, template_name='store/search-results.html', context=context)

def category_page(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, template_name='store/category.html', context=context)

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, template_name='store/product-details.html', context=context)
