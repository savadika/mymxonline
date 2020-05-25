# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from .models import CityDict, CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class OrgView(View):
    """课程列表视图"""
    def get(self, request):
        # 获取所有城市信息
        all_citys = CityDict.objects.all()
        # 索取所有课程信息
        org_lists = CourseOrg.objects.all()
        # 获取所有课程的数量


        # 进行城市筛选
        cityid = request.GET.get('city', '')
        print(cityid)
        if cityid:
            org_lists = org_lists.filter(city_id = int(cityid))

        # 进行机构的筛选
        category = request.GET.get('ct','')
        if category:
            org_lists = org_lists.filter(category = category)


        # 进行分页
        #1 设置page变量，默认为从url中获取，没有的话设置为1
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        #2  生成分页器,并对数据进行分页化,每页展示3条数据
        p = Paginator(org_lists, 2, request=request)
        page_orgs = p.page(page)

        org_nums = org_lists.count()
        return render(request, 'org-list.html', {
            'all_citys': all_citys,
            'org_lists': page_orgs,
            'org_nums': org_nums,
            'cityid':cityid,
            'category':category
        })
