from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default="", verbose_name="昵称")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=6, choices=(
        ("male", u"男"), ("female", "女")), verbose_name="性别")
    address = models.CharField(max_length=200, default=u"", verbose_name="地址")
    mobile = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name="手机号码")
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100,
        verbose_name="头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVertifyRecord(models.Model):
    """存储邮箱激活码的表"""
    active_code = models.CharField(max_length=20, verbose_name=u"激活码")
    email = models.EmailField(max_length=30, verbose_name=u"邮箱")
    send_type = models.CharField(
        choices=(
            ("register",
             u"注册"),
            ("forget",
             u"找回密码"),
            ("update_email",
             u"修改邮箱")),
        verbose_name="类型", max_length=20)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)


    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.active_code, self.email)
