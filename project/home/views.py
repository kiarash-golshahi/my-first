from django.shortcuts import render
from store.models import Category, Product

def categories():
    """A function to send categories to index view"""
    return Category.objects.all().values()

def newest_products():
    """A function to get 20 newest products"""
    return Product.objects.order_by('-registration_date')[:20]

def index(request):
    """Return and render the homepage"""
    context = {
        'title': 'کالاهای مورد نیازتان را در فروشگاه ما پیدا کنید!',
        'products': newest_products(),
        'categories': categories(),
    }
    return render(request, template_name='home/index.html', context=context)
