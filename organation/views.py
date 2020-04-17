# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from .models import CityDict, CourseOrg
# Create your views here.


class OrgView(View):
    """课程列表视图"""

    def get(self, request):
        # 获取所有城市信息
        all_citys = CityDict.objects.all()
        # 索取所有课程信息
        org_lists = CourseOrg.objects.all()
        # 获取所有课程的数量
        org_nums = org_lists.count()
        return render(request, 'org-list.html', {
            'all_citys': all_citys,
            'org_lists': org_lists,
            'org_nums': org_nums
        })
