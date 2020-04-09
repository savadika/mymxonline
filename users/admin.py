from django.contrib import admin

# Register your models here.
from .models import UserProfile

# 注册一个后台管理器
class UserProfileAdmin(admin.ModelAdmin):
    pass

# 添加该后台管理器
admin.site.register(UserProfile, UserProfileAdmin)