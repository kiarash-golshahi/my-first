from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('order-placing/<int:id>', views.order_placing, name='order-placing'),
]
