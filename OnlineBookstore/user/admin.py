# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import user_extend
# # Register your models here.
# from . import models
# class user_extendInline(admin.TabularInline):
#     models=user_extend
#     can_delete = False
#     verbose_name_plural = 'user_extend'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (user_extendInline,)
#
# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)
