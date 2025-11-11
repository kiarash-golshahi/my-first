from .forms import OrderForm
from .models import Order
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product

def delete_order(request, id):
    next_url = request.GET.get('next', 'order:orders-history')
    order = get_object_or_404(Order, id=id, orderer_user=request.user)
    order.delete()
    messages.success(request, 'سفارش با موفقیت حذف شد')
    return redirect(next_url)

def orders_history(request):
    orders = Order.objects.filter(orderer_user=request.user).order_by('-registration_date')
    context = {
        'orders': orders,
    }
    return render(request, template_name='order/orders-history.html', context=context)

def order_placing(request, id):
    product = get_object_or_404(Product, id=id)
    # 'get_object_or_404' gets the product based on the id. If the id isn't valid, it will redirect the user to 404 page.
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.orderer_user = request.user
            order.ordered_product = product
            order.save()
            messages.success(request, 'سفارش شما با موفقیت ثبت شد')
            return redirect('store:product-details', id=id)
    else:
        form = OrderForm()
    context = {
        'product': product,
        'order_form': form,
    }
    return render(request, template_name='order/order-placing.html', context=context)
