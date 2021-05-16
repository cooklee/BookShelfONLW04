from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from accounts.forms import LoginForm, CreateUserForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('index')
            return render(request, 'form.html', {'form': form, 'message':'wrong login data'})
        return render(request, 'form.html', {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        url = reverse('index')+"?message=Wylogowano"
        return redirect(url)


class CreateUserView(View):

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # u2 = User()
            # username = form.cleaned_data['username']
            # passwoed = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # u2.username = username
            # u2.first_name=first_name
            # u2.last_name = last_name
            # u2.set_password(password)
            # u2.save()
            return redirect('login')
        return render(request, 'form.html', {'form': form})

