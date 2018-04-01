from django.shortcuts import render, redirect
from df_user.models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.


def register(request):
    context = {'info': '用户注册'}
    return render(request, 'df_user/register.html', context)


def register_handle(request):
    post = request.POST
    user_name = post.get('user_name')
    password = post.get('pwd')
    c_password = post.get('cpwd')
    email = post.get('email')

    if password != c_password:
        return redirect('/user/register')
# 密码加密
    else:
        s1 = sha1()
        s1.update(password.encode('utf-8'))
        password = s1.hexdigest()

        user = UserInfo()
        user.user_name = user_name
        user.password = password
        user.email = email
        user.save()
        return render(request, 'df_user/login.html')


def register_exist(request):
    flag = request.GET.get('flag')
    if flag == '0':
        user_name = request.GET.get('p')
        count = UserInfo.objects.filter(user_name=user_name).count()
    else:
        email = request.GET.get('p')
        count = UserInfo.objects.filter(email=email).count()
    return JsonResponse({'count': count})


def login(request):
    user_name = request.COOKIES.get('user_name', '')
    context = {'info': '用户登录', 'error_user_name': 0,
               'error_password': 0, 'user_name': user_name,
               }
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    post = request.POST
    user_name = post.get('user_name')
    password = post.get('pwd')
    remember = post.get('remember', 0)
    # 判断用户名是否存在，密码是否正确
    user = UserInfo.objects.filter(user_name=user_name)
    if len(user) == 1:
        s1 = sha1()
        s1.update(password.encode('utf8'))
        if s1.hexdigest() == user[0].password:
            red = HttpResponseRedirect('/user/info')
            if remember != 0:
                red.set_cookie('user_name', user_name)
            else:
                red.set_cookie('user_name', '', max_age=-1)
            request.session['user_name'] = user_name
            request.session['id'] = user[0].id
            return red
        else:
            context = {'info': '用户登录', 'error_user_name': 0,
                       'error_password': 1, 'user_name': user_name,
                       'password': password,
                       }
            return render(request, 'df_user/login.html', context)
    else:
        context = {'info': '用户登录', 'error_user_name': 1,
                   'error_password': 0, 'user_name': user_name,
                   'password': password,
                   }
        return render(request, 'df_user/login.html', context)


def info(request):
    user_name = request.session.get('user_name', '')
    if user_name == '':
        return redirect('/user/login')
    context = {}
    return render(request, 'df_user/user_center_info.html', context)


def order(request):
    user_name = request.session.get('user_name', '')
    if user_name == '':
        return redirect('/user/login')
    context = {'current_page': 'active'}
    return render(request, 'df_user/user_center_order.html', context)


def site(request):
    user_name = request.session.get('user_name', '')
    if user_name == '':
        return redirect('/user/login')
    context = {'current_page': 'active'}
    return render(request, 'df_user/user_center_site.html', context)

