# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         forms
# Description:  对比两种不同的表单验证类，form.Form 和 forms.ModelForm
# Author:       ylf
# Date:         2020-05-25
#-------------------------------------------------------------------------------

from django import forms
from .models import UserAsk


class TraditionUserAskForm(forms.Form):
    """传统的表单验证器"""
    name = forms.CharField(max_length=50, min_length=2, required=True)
    mobile = forms.CharField(max_length=11, min_length=11, required=True)
    course_name = forms.CharField(max_length=50, min_length=2 ,required=True)


class UserAskForm(forms.ModelForm):
    """定义modelform"""
    """
    优点：
    1  方便快捷
    2  可自主添加需要验证的字段，并可以增添新的字段
    3  可以直接进行save
    """

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
