#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/5/10.

from argeweb import BasicModel
from argeweb import Fields
from plugins.application_user import ApplicationUserModel


class PaymentRecordModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'付款記錄摘要')
    pay_user = Fields.KeyProperty(verbose_name=u'付款人', kind=ApplicationUserModel)
    user = Fields.SearchingHelperProperty(verbose_name=u'付款人', target=u'pay_user', target_field_name=u'name')
    user_email = Fields.SearchingHelperProperty(verbose_name=u'付款人', target=u'pay_user', target_field_name=u'email')
    content = Fields.RichTextProperty(verbose_name=u'內容')
    image = Fields.ImageProperty(verbose_name=u'圖片')
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'顯示於前台')


