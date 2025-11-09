from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    # Signup page URL
    path('signup/', views.signup, name='signup'),
]
