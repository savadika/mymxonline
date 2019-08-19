# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         forms
# Description:
# Author:       ylf
# Date:         2019-05-29
# -------------------------------------------------------------------------------

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """登录验证器"""
    username = forms.CharField(error_messages={'required': '请输入用户名'})
    password = forms.CharField(
        min_length=6,
        error_messages={
            'required': '请输入密码',
            'min_length': '密码不少于6个字符'}
    )


class RegisterForm(forms.Form):
    """注册验证器"""
    email = forms.EmailField(required=True)
    password = forms.CharField(
        min_length=6,
        error_messages={
            'required': '请输入密码',
            'min_length': '密码不少于6个字符'}
    )
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})
