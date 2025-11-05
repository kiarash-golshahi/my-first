from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

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
