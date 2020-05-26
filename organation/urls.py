# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         urls
# Description:  urls分发
# Author:       ylf
# Date:         2020-05-25
#-------------------------------------------------------------------------------

from django.conf.urls import url, include
from .views import OrgView, UserAskView

urlpatterns = [
    # 课程机构列表页urls
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    # 添加用户咨询
    url(r'^add_ask/$', UserAskView.as_view(), name='add_ask'),
]