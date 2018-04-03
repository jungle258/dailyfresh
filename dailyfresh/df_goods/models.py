from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Classify(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class GoodsInfo(models.Model):
    goods_title = models.CharField(max_length=30)
    goods_pic = models.ImageField(upload_to='df_goods')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    goods_unit = models.CharField(max_length=20, default='500g')
    goods_click = models.IntegerField()
    summary = models.CharField(max_length=200)
    stock = models.IntegerField()
    goods_content = HTMLField()
    goods_classify = models.ForeignKey('Classify')

