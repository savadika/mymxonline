# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class OrgView(View):
    """课程列表视图"""

    def get(self, request):
        print(dir(self))
        print(dir(request.session))
        return render(request, 'org-list.html', {})


