#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/1.

from argeweb import BasicModel
from argeweb import Fields


class PaymentTypeModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(default=u'未命名', verbose_name=u'付款方式名稱')
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'啟用')
    pay_uri = Fields.StringProperty(verbose_name=u'Pay URI')

    @classmethod
    def get_or_create(cls, name, title=None, pay_uri=None):
        item = cls.find_by_name(name)
        if item is None:
            item = cls()
            item.name = name
            item.title = title
            item.pay_uri = pay_uri
            item.put()
        return item