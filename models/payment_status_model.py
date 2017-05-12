#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/1.

from argeweb import BasicModel
from argeweb import Fields


payment_status = {
    'unconfirmed': u'未確認',
    'pending_payment': u'待付款',
    'already_paid': u'已付款',
    'refunding': u'退款中',
    'refunded': u'已退款',
    'full_payment_with_point': u'購物金全額付款',
    'part_payment_with_point': u'購物金部分付款'
}


class PaymentStatusModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(default=u'未命名', verbose_name=u'付款狀態名稱')
    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'啟用')

    @classmethod
    def get_or_create(cls, name, title=None):
        r = cls.find_by_name(name)
        if r is None:
            r = cls()
            r.name = name
            r.title = title
            r.put()
        return r

    @classmethod
    def create_default_status(cls):
        for name, title in payment_status.items():
            cls.get_or_create(name, title)