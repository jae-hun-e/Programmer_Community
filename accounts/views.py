from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


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


def signup(request):
    if request.method=="POST":
        if request.POST["password"] == request.POST["repeat"]:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')
