from django.shortcuts import render
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ResetPasswordForm, ConfigPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVertifyRecord
from django.db.models import Q  # 使用Q来实现并集查询
from django.contrib.auth.hashers import make_password
from untils.send_my_emails import send_mxonline_mail

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
        :return
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
                    return render(request, "login.html", {"msg": "用户尚未激活！"})
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
        return render(request, "login.html")


class UserRegisterView(View):
    """用户注册操作"""

    def get(self, request):
        register_form = RegisterForm(request.POST)
        return render(
            request, "register.html", {
                'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email')
            pass_word = request.POST.get('password')
            # 1 保存用户信息到数据库
            if UserProfile.objects.filter(email=user_name):
                return render(
                    request, 'register.html', {
                        'msg': '用户已经注册', 'register_form': register_form})
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()
            # 2 发送激活邮件给用户
            send_status = send_mxonline_mail(user_name, 'register')
            if send_status:
                return render(request, 'login.html', {})
            else:
                return render(request, 'register.html')
        else:
            return render(
                request, 'register.html', {
                    'register_form': register_form})


class UserActiveView(View):
    """用户激活操作"""

    def get(self, request, code):
        if code:
            # fiter用来取多条数据，返回的是一个列表[]
            email_record = EmailVertifyRecord.objects.filter(active_code=code)
            if email_record:
                for record in email_record:
                    user_email = record.email
                    # get用来去单条数据
                    user = UserProfile.objects.get(email=user_email)
                    user.is_active = True
                    user.save()
                    return render(request, 'login.html', {})
            else:
                return render(request, 'register_failed.html', {})
        else:
            return render(request, 'register_failed.html', {})


class ForgetPwdView(View):
    """重置密码操作"""

    def get(self, request):
        """显示重置页面"""
        reset_pwd_form = ResetPasswordForm(request.POST)
        return render(
            request, 'forgetpwd.html', {
                'reset_pwd_form': reset_pwd_form})

    def post(self, request):
        """向用户发送一封邮件，并告知成功发送"""
        reset_pwd_form = ResetPasswordForm(request.POST)
        if reset_pwd_form.is_valid():
            email = request.POST.get('email')
            # 1 邮箱是否存在
            # 2 向这个用户发送一封重置邮件
            # 3 跳向重置成功界面
            users = UserProfile.objects.filter(email=email)
            for user in users:
                if user:
                    send_status = send_mxonline_mail(user.email, 'reset')
                    if send_status:
                        return render(request, 'reset_success.html', {})
                    else:
                        return render(request, 'register_failed.html', {})
        else:
            return render(request, 'forgetpwd.html', {'msg': '用户名或验证码错误'})


class PassWordReserView(View):
    """重置密码操作"""
    """注意需要传回userid"""

    def get(self, request, code):
        verfity_code = EmailVertifyRecord.objects.get(active_code=code)
        return render(
            request, 'password_reset.html', {
                'user_id': verfity_code.email})


class ModifyPwdView(View):
    def post(self, request):
        config_password = ConfigPasswordForm(request.POST)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if config_password.is_valid():
            if password1 != password2:
                return render(
                    request, 'password_reset.html', {
                        'user_id': email, 'msg': '两次密码不一致'})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(password1)
                user.save()
        return render(request, 'login.html', {})
