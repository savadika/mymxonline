# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         urls
# Description:  urls分发
# Author:       ylf
# Date:         2020-05-25
#-------------------------------------------------------------------------------

from django.conf.urls import url, include
from .views import OrgView


urlpatterns = [
    # 课程机构列表页urls
    url(r'^list/$', OrgView.as_view(), name='org_list'),
]