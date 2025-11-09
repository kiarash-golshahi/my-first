from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def logout_view(request):
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد')
    return redirect('home:index')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "ورود با موفقیت انجام شد")
            return redirect('home:index')
        else:
            messages.error(request, 'نام کاربری یا گذرواژه نادرست است')
    else:
        form = LoginForm()
    context = {
        'login_form': form,
    }
    return render(request, template_name='users/login.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username, password)
            login(request, user)
            return redirect('home:index')
    else:
        form = SignUpForm()
    context = {
        'signup_form': form,
    }
    return render(request, template_name='users/signup.html', context=context)
