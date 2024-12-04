from django.contrib import messages, admin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.contrib.auth import logout as auth_logout


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 检查两次密码输入是否一致
        if password1 != password2:
            messages.error(request, '两次密码输入不一致，请重新输入。')
            return render(request, 'login.html')  # 返回注册页面

        user = CustomUser(username=username, phone_number=phone_number)
        user.set_password(password1)  # 设置用户密码
        user.is_active = False  # 设置为不活跃，等待管理员确认
        user.save()

        messages.success(request, '用户注册成功！请等待管理员确认！')
        return redirect('login')
    else:
        return render(request, 'login.html')  # 返回注册页面

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')  # 或者其他已登录后的页面
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # 重定向到首页或其他页面
            else:
                messages.error(request, '该账户尚未被激活，请联系管理员。')
        else:
            messages.error(request, '用户名或密码错误。')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  # 重定向到主页
