# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         forms
# Description:  对比两种不同的表单验证类，form.Form 和 forms.ModelForm
# Author:       ylf
# Date:         2020-05-25
#-------------------------------------------------------------------------------

from django import forms
from .models import UserAsk
import re


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

    def clean_mobile(self):
        """自定义手机号码验证"""
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1([38]\d|5[0-35-9]|7[3678])\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="invalid_mobile")
