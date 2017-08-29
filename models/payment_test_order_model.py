#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/1.
import time

from argeweb import BasicModel
from argeweb import Fields
from plugins.application_user.models.application_user_model import ApplicationUserModel
from ..models.payment_type_model import PaymentTypeModel
from ..models.payment_status_model import PaymentStatusModel
from ..models.payment_record_model import PaymentRecordModel


class PaymentTestOrderModel(BasicModel):
    order_no = Fields.StringProperty(verbose_name=u'訂單編號', default=u'')
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    user = Fields.KeyProperty(verbose_name=u'使用者', kind=ApplicationUserModel)

    payment_type_object = Fields.CategoryProperty(verbose_name=u'付款方式', kind=PaymentTypeModel, tab_page=1)
    payment_type = Fields.SearchingHelperProperty(verbose_name=u'付款方式', target='payment_type_object', target_field_name='title', tab_page=1)
    payment_status_object = Fields.CategoryProperty(verbose_name=u'付款狀態', kind=PaymentStatusModel, tab_page=1)
    payment_status = Fields.SearchingHelperProperty(verbose_name=u'付款狀態', target='payment_status_object', target_field_name='title', tab_page=1)
    payment_record_object = Fields.KeyProperty(verbose_name=u'付款記錄', kind=PaymentRecordModel, tab_page=1)
    payment_record = Fields.SearchingHelperProperty(verbose_name=u'付款記錄', target='payment_record_object', target_field_name='title', tab_page=1)

    need_pay_amount = Fields.FloatProperty(verbose_name=u'應付金額', tab_page=1, default=0.0)

    @classmethod
    def gen_test_order(cls, name, payment_type):
        order = cls.get_or_create_by_name(name)
        order.order_no = str(int(time.time()))
        order.need_pay_amount = 100
        order.payment_status_object = PaymentStatusModel.get_or_create_by_name('pending_payment').key
        if isinstance(payment_type, str):
            payment_type = PaymentTypeModel.get_by_name(payment_type)
        order.payment_type_object = payment_type.key
        return order
