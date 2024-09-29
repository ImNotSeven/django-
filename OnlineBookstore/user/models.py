from django.contrib.auth.models import User
from django.db import models

class user_extend(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    姓名=models.CharField(blank=False,null=False,max_length=15)
    昵称=models.CharField(blank=False,null=False,max_length=15)
    手机号=models.CharField(blank=False,null=False,max_length=11)

    class Meta:
        verbose_name_plural="user_extend"

