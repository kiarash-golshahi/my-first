from django.shortcuts import render

def index(request):
    """Return and render the homepage"""
    context = {
        'title': 'کالاهای مورد نیازتان را در فروشگاه ما پیدا کنید!',
    }
    return render(request, template_name='home/index.html', context=context)
