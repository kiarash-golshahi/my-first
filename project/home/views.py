from django.shortcuts import render
from store.models import Product

def newest_products():
    """A function to get 20 newest products"""
    return Product.objects.order_by('-registration_date')[:20]

def index(request):
    """Return and render the homepage"""
    context = {
        'title': 'کالاهای مورد نیازتان را در فروشگاه ما پیدا کنید!',
    }
    return render(request, template_name='home/index.html', context=context)
