from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import SingUpForm, LogInForm


def sign_up(request):
    if request.method == "POST":
        form = SingUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(new_user.password)
            new_user.save()
            login(request, new_user)
            return redirect('home')
        else:
            return HttpResponse('잘못된 정보입니다. 다시 확인해 주세요')
    else:
        form = SingUpForm()
        return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LogInForm()
        return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')
