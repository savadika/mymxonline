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
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


