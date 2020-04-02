"""mymxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users.views import IndexShowView, UserLoginView, UserLogoutView, UserRegisterView, UserActiveView, ForgetPwdView, PassWordReserView, ModifyPwdView
from django.conf import settings
from django.views.static import serve
from organation.views import OrgView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', IndexShowView.as_view(), name='index'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^login/$', UserLoginView.as_view(), name='login'),
    url(r'^logout/$', UserLogoutView.as_view(), name='logout'),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    # 将任意active后面的值取出，复制给code，传递给后端
    url(r'^active/(?P<code>.*)$', UserActiveView.as_view(), name='active'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^reset/(?P<code>.*)$', PassWordReserView.as_view(), name='resetpwd'),
    url(r'^modify/$', ModifyPwdView.as_view(), name='modify_pwd'),
    #课程机构
    url(r'^org_list/$', OrgView.as_view(), name='org_list')
]
