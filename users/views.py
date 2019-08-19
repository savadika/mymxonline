from django.shortcuts import render
from django.views.generic.base import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q  # 使用Q来实现并集查询

# Create your views here.


class IndexShowView(View):
    def get(self, request):
        """
        展示首页
        :param request:
        :return:
        """
        return render(request, 'index.html')


class MyBackend(ModelBackend):
    """自定义用户登录的方式，可以实现多种字段作为用户名登录，实际上就是重载了authenticate方法"""
    """自定义的时候需要把这个类添加到setting的配置中"""

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username))  # 根据用户名或者email查询出用户
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None


class UserLoginView(View):
    """用户登录相关操作"""

    def get(self, request):
        """
        用户登录页面展示
        :param request:
        :return:
        """
        return render(request, 'login.html')

    def post(self, request):
        """
        用户登录操作
        :param request:
        :return:
        """
        # 对数据进行校验，构建一个校验器对request传过来的数据进行校验
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            """如果校验通过[ylf,99@linux]"""
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                """如果存在用户"""
                if user.is_active:
                    """用户处于激活状态"""
                    login(request, user)
                    return render(request, "index.html", {"msg": '登录成功'})
            else:
                return render(request, "login.html", {"msg": "用户名或者密码不正确"})
        else:
            """如果校验不通过,将表单的错误信息传回"""
            return render(request, "login.html", {"login_form": login_form})


class UserLogoutView(View):
    """用户登出操作"""

    def get(self, request):
        """退出页面展示"""
        logout(request)
        return  render(request, "login.html")
