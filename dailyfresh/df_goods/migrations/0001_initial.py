# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('goods_title', models.CharField(max_length=30)),
                ('goods_pic', models.ImageField(upload_to='df_goods')),
                ('goods_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('goods_unit', models.CharField(default='500g', max_length=20)),
                ('goods_click', models.IntegerField()),
                ('summary', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('goods_content', tinymce.models.HTMLField()),
                ('goods_classify', models.ForeignKey(to='df_goods.Classify')),
            ],
        ),
    ]
