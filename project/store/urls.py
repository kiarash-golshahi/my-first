from . import views
from django.urls import path

app_name = 'store'

urlpatterns = [
    # Product details page URL
    path('details/<int:id>', views.product_details, name='product-details'),
    # Category page URL
    path('category/<int:id>', views.category_page, name='category'),
    # Search results page URL
    path('search/', views.search, name='search-results'),
]
