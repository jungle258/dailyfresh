from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=30, default='')
    consignee = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=6, default='')
    phone = models.CharField(max_length=11, default='')


