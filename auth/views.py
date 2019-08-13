from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate ,logout
from django.shortcuts import render, redirect
from auth.forms import SignUpForm


class Login(LoginView):
    template_name = 'auth/login.html'

def Logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.field_order)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/signup.html', {'form': form})
    else:
        form = SignUpForm()
        print(form.as_table())
    return render(request, 'auth/signup.html', {'form': form})