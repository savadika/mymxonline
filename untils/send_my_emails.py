# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         send_my_emails
# Description:  工具类：定义激活码
# Author:       ylf
# Date:         2019-08-20
# -------------------------------------------------------------------------------

from django.core.mail import send_mail
from users.models import EmailVertifyRecord
from random import Random
from mymxonline.settings import EMAIL_FROM


def send_mxonline_mail(email, type="register"):
    """定义本程序发送的邮件"""
    # 1 生成数据库中的激活码
    email_record = EmailVertifyRecord()
    active_code = get_my_random_code(16)  # 随机生成16位的一个字符串
    email_record.active_code = active_code
    email_record.email = email
    email_record.send_type = type
    email_record.save()
    # 2 配置发送邮件的基本信息，包括setting
    EMAIL_TITLE =''
    EMAIL_CONTENT = ''
    if type == 'register':
        EMAIL_TITLE = '来自慕学在线的激活邮件'
        EMAIL_CONTENT = '请点击以下链接激活你的mxonline账号，http://127.0.0.1:8000/active/{0}'.format(
            active_code)
    # 3 调用发送邮件方法进行发送激活码给用户
    if type == 'reset':
        EMAIL_TITLE = '请重置你的慕学在线密码'
        EMAIL_CONTENT = '请点击以下链接激活你的mxonline账号，http://127.0.0.1:8000/reset/{0}'.format(
            active_code)
    send_status = send_mail(EMAIL_TITLE, EMAIL_CONTENT, EMAIL_FROM, [EMAIL_FROM])
    return send_status


def get_my_random_code(code_length=8):
    """定义一个随机的激活码"""
    str = ''
    str_colletcions = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(str_colletcions) - 1
    # 根据需要的长度生成随机字符串
    random = Random()
    for i in range(code_length):
        # 随机生成小于某个整数的值，取出char,循环放到变量中
        str += str_colletcions[random.randint(0, length)]
    return str
