from django.contrib import admin

# Register your models here.

from .models import CityDict, CourseOrg, Teacher

# 建立后台管理器
class CityDictAdmin(admin.ModelAdmin):
    pass


class CourseOrgAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


# 向后台注册该管理器，便于进行后台各种操作
admin.site.register(CityDict, CityDictAdmin)
admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(Teacher, TeacherAdmin)
