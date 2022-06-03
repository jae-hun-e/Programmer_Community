from django.shortcuts import render, redirect
from django.contrib import auth


def login(req):
    if req.method =="POST":
        username = req.POST['username']
        pwd = req.POST['password']
        user = auth.authenticate(req, username=username, password=pwd)  # user 객체 || none
        if user is not None:
            auth.login(req, user)
            return redirect('home')
        else:
            return render(req, 'bad_login.html')
    else:
        return render(req, 'login.html')


def logout(req):
    auth.logout(req)
    return redirect('home')
