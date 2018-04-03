from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['goods_title', 'goods_classify']
    search_fields = ['goods_title']


@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ['title']


