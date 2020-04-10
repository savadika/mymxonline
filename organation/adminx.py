# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         adminx
# Description:
# Author:       ylf
# Date:         2020-04-10
# -------------------------------------------------------------------------------

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    """xadmin管理器"""
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    """课程机构管理器"""
    list_display = [
        'name',
        'desc',
        'tags',
        'category',
        'click_nums',
        'fav_nums',
        'images',
        'address',
        'city',
        'students',
        'course_nums',
        'add_time']
    search_fields = [
        'name',
        'desc',
        'tags',
        'category',
        'click_nums',
        'fav_nums',
        'images',
        'address',
        'city',
        'students',
        'course_nums',
        'add_time']


class TeacherAdmin(object):
    list_display = [
        'name',
        'org',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'click_nums',
        'fav_nums',
        'age',
        'images',
        'add_time']
    search_fields = [
        'name',
        'org',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'click_nums',
        'fav_nums',
        'age',
        'images',
        'add_time']


# 向xadmin这个后台注册该管理器
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
