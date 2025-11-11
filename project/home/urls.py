from . import views
from django.urls import path

# Define the namespace
app_name = 'home'

urlpatterns = [
    # Index (homepage) URL
    path('', views.index, name='index'),
]
