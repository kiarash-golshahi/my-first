from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    # Signup page URL
    path('signup/', views.signup, name='signup'),
    # Login page URL
    path('login/', views.login_view, name='login'),
    # Logout URL
    path('logout/', views.logout_view, name='logout'),
]
