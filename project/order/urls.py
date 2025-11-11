from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
    # Order placing page URL
    path('order-placing/<int:id>', views.order_placing, name='order-placing'),
    # Orders history page URL
    path('orders-history/', views.orders_history, name='orders-history'),
    # Delete orders URL
    path('delete-order/<int:id>', views.delete_order, name='delete-order'),
]
