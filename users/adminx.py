# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         adminx
# Description:
# Author:       ylf
# Date:         2020-04-10
# -------------------------------------------------------------------------------

import xadmin
from .models import EmailVertifyRecord


class EmailVertifyRecordAdmin(object):
    """email确认管理器"""
    list_diplay = ['active_code', 'email', 'send_type', 'send_time']
    search_fields = ['active_code', 'email', 'send_type', 'send_time']
    pass


xadmin.site.register(EmailVertifyRecord, EmailVertifyRecordAdmin)
