from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    user_name = request.session.get('user_name', '')
    classify = Classify.objects.all()
    class0 = classify[0].goodsinfo_set.order_by('-id')[0:4]
    class01 = classify[0].goodsinfo_set.order_by('-goods_click')[0:4]
    class1 = classify[1].goodsinfo_set.order_by('-id')[0:4]
    class11 = classify[1].goodsinfo_set.order_by('-goods_click')[0:4]
    class2 = classify[2].goodsinfo_set.order_by('-id')[0:4]
    class21 = classify[2].goodsinfo_set.order_by('-goods_click')[0:4]
    class3 = classify[3].goodsinfo_set.order_by('-id')[0:4]
    class31 = classify[3].goodsinfo_set.order_by('-goods_click')[0:4]
    class4 = classify[4].goodsinfo_set.order_by('-id')[0:4]
    class41 = classify[4].goodsinfo_set.order_by('-goods_click')[0:4]
    class5 = classify[5].goodsinfo_set.order_by('-id')[0:4]
    class51 = classify[5].goodsinfo_set.order_by('-goods_click')[0:4]

    context = {'current_page': 0, 'info': '正品低价、品质保障、配送及时、轻松购物！',
               'user_name': user_name, 'class0': class0, 'class01': class01,
               'class1': class1, 'class11': class11, 'class2': class2, 'class21': class21,
               'class3': class3, 'class31': class31, 'class4': class4, 'class41': class41,
               'class5': class5, 'class51': class51,
               }
    return render(request, 'df_goods/index.html', context)


def detail(request, id):
    user_name = request.session.get('user_name', '')
    goods = GoodsInfo.objects.get(id=id)
    goods.goods_click +=1
    goods.save()
    order_goods = GoodsInfo.objects.all().order_by('-id')[0:4]
    context = {'current_page': 0, 'user_name': user_name,
               'goods': goods, 'order_goods': order_goods,
               'info': goods.goods_title,
               }
    res = render(request, 'df_goods/detail.html', context)
    #  记录最近用户浏览的商品
    goods_ids = request.COOKIES.get('goods_ids', '')
    if goods_ids != '':
        goods_id_list = goods_ids.split(',')
        if goods_id_list.count(id) >= 1:
            goods_id_list.remove(id)
        goods_id_list.insert(0, id)
        if len(goods_id_list) >= 6:
            del goods_id_list[5]
        goods_ids = ','.join(goods_id_list)
    else:
        goods_ids = id
    res.set_cookie('goods_ids', goods_ids)
    return res


def list(request, cid, pindex, sort):
    user_name = request.session.get('user_name', '')
    goods = GoodsInfo.objects.all()
    goods_list = goods.filter(goods_classify_id=cid)
    order_goods = goods.order_by('-id')[0:4]
    # 排序
    if sort == '':
        sort = '1'
    elif sort == '2':
        goods_list = goods_list.order_by('-goods_price')
    elif sort == '3':
        goods_list = goods_list.order_by('-goods_click')

    # 分页
    p = Paginator(goods_list, 10)
    if pindex == '':
        pindex = '1'
    listp = p.page(int(pindex))
    plist =p.page_range
    context = {'current_page': 0, 'user_name': user_name,
               'order_goods': order_goods,'plist': plist,
               'listp': listp, 'goods': listp[0], 'sort': sort,
               'info': listp[0].goods_classify.title, 'pindex': pindex
               }
    return render(request, 'df_goods/list.html', context)

