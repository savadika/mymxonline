# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         forms
# Description:
# Author:       ylf
# Date:         2019-05-29
# -------------------------------------------------------------------------------

from django import forms


class LoginForm(forms.Form):
    """登录验证器"""
    username = forms.CharField(error_messages={'required': '请输入用户名'})
    password = forms.CharField(
        min_length=6,
        error_messages={
            'required': '请输入密码',
            'min_length': '密码不少于6个字符'}
    )
