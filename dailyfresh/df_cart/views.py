from django.shortcuts import render, redirect
from df_user.user_decorator import login_decorator
from .models import CartInfo
from django.http import JsonResponse
# Create your views here.


@login_decorator
def cart(request):
    uid = request.session["id"]
    user_name = request.session.get("user_name")
    carts = CartInfo.objects.filter(user_id=uid)

    context = {'info': '购物车', 'current_model': '购物车',
               'current_page': 1, 'carts': carts,
               'user_name': user_name,
               }
    return render(request, 'df_cart/cart.html', context)


@login_decorator
def add(request, gid, num):
    uid = request.session['id']
    gid = int(gid)
    num = int(num)
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)

    if len(carts) >= 1:
        cart = carts[0]
        cart.count += num
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = num
    cart.save()
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=uid).count()
        return JsonResponse({'count': count})
    else:
        return redirect('/cart')


@login_decorator
def delete(request, gid):
    try:
        uid = request.session['id']
        c = CartInfo.objects.get(user_id=uid, goods_id=gid)
        c.delete()
        data = {'ok': 1}
        print(gid)
    except Exception as e:
        data = {'ok': 0}
        print(e)
    return JsonResponse(data)


@login_decorator
def edit(request, gid, count):
    try:
        uid = request.session['id']
        c = CartInfo.objects.get(user_id=uid, goods_id=gid)
        c.count = count
        c.save()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': count}

    return JsonResponse(data)
