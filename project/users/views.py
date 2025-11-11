from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def logout_view(request):
    next_url = request.GET.get('next', 'home:index')
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد')
    return redirect(next_url)

def login_view(request):
    next_url = request.GET.get('next', 'home:index') # 'home:index' is the default next URL
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'ورود با موفقیت انجام شد')
            return redirect(request.POST.get('next', next_url)) # Redirects the user to the 'next' URL
        else:
            messages.error(request, 'نام کاربری یا گذرواژه نادرست است')
    else:
        form = LoginForm()
    context = {
        'next': next_url,
        'login_form': form,
    }
    return render(request, template_name='users/login.html', context=context)

def signup(request):
    next_url = request.GET.get('next', 'home:index')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(request.POST.get('next', next_url))
    else:
        form = SignUpForm()
    context = {
        'next': next_url,
        'signup_form': form,
    }
    return render(request, template_name='users/signup.html', context=context)
