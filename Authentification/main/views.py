from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('WelcomePage')
    context = {}
    return render(request, "main/LoginPage.html", context) 


def Logoutpage(request):
    logout(request)
    return redirect('LoginPage')



def RegisterPage(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginPage')
    context = {'form':form}
    return render(request, "main/RegisterPage.html", context)


@login_required(login_url = "LoginPage")
def WelcomePage(request):
    context = {}
    return render(request, "main/WelcomePage.html", context) 
   