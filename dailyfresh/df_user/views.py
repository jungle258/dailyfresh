from django.shortcuts import render, redirect
from df_user.models import *
from df_goods.models import GoodsInfo
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect
from .user_decorator import login_decorator
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
               'current_page': 1,
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
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
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


def login_off(request):
    request.session.flush()
    red = HttpResponseRedirect('/')
    return red


@login_decorator
def info(request):
    user_name = request.session.get('user_name', '')
    uid = request.session.get('id')
    user = UserInfo.objects.filter(id=uid)
    # 获取最近浏览过的列表
    has_view_goods_id = request.COOKIES.get('goods_ids', '')
    if has_view_goods_id != '':
        ids = has_view_goods_id.split(',')
        has_view_list = GoodsInfo.objects.filter(pk__in=ids)
    else:
        has_view_list = []
    context = {'info': '个人信息', 'user_name': user_name,
               'phone': user[0].phone, 'address': user[0].address,
               'current_page': 1, 'has_view_list': has_view_list,
               'current_model': '用户中心',
               }
    return render(request, 'df_user/user_center_info.html', context)


@login_decorator
def order(request):
    user_name = request.session.get('user_name', '')
    context = {'info': '我的订单', 'user_name': user_name,
               'current_page': 1, 'current_model': '用户中心',
               }
    return render(request, 'df_user/user_center_order.html', context)


@login_decorator
def site(request):
    user_name = request.session.get('user_name', '')
    uid = request.session.get('id')
    user = UserInfo.objects.filter(id=uid)
    context = {'info': '收货地址', 'user_name': user_name,
               'phone': user[0].phone, 'address': user[0].address,
               'consignee': '('+user[0].consignee+'收)', 'postcode': user[0].postcode,
               'current_page': 1, 'current_model': '用户中心',
               }
    return render(request, 'df_user/user_center_site.html', context)


@login_decorator
def site_handle(request):
    user_name = request.session.get('user_name', '')
    uid = request.session.get('id')
    user = UserInfo.objects.get(id=uid)
    post = request.POST
    user.consignee = post.get('consignee', '')
    user.address = post.get('address', '')
    user.phone = post.get('phone', '')
    user.postcode = post.get('postcode', '')
    user.save()
    context = {'info': '收货地址', 'user_name': user_name,
               'phone': user.phone, 'address': user.address,
               'consignee': '('+user.consignee+'收)', 'postcode': user.postcode,
               'current_page': 1, 'current_model': '用户中心',
               }
    return render(request, 'df_user/user_center_site.html', context)


