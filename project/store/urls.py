from . import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    # Product details page URL
    path('details/<int:id>', views.product_details, name='product-details'),
]
