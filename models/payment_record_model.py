#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/5/10.

from argeweb import BasicModel
from argeweb import Fields
from plugins.application_user import ApplicationUserModel
from payment_type_model import PaymentTypeModel


class PaymentRecordModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'付款記錄摘要')
    detail = Fields.RichTextProperty(verbose_name=u'付款記錄細節')
    amount = Fields.FloatProperty(verbose_name=u'應付款金額')
    user_object = Fields.KeyProperty(verbose_name=u'付款人', kind=ApplicationUserModel)
    user = Fields.SearchingHelperProperty(verbose_name=u'付款人', target=u'user_object', target_field_name=u'name')
    user_email = Fields.SearchingHelperProperty(verbose_name=u'付款人', target=u'user_object', target_field_name=u'email')

    source_uri = Fields.HiddenProperty(verbose_name=u'來源 URI')
    source_params = Fields.HiddenProperty(verbose_name=u'來源參數')
    source_ndb_key = Fields.HiddenProperty(verbose_name=u'來源物件 Key')

    payment_type = Fields.KeyProperty(verbose_name=u'付款方式', kind=PaymentTypeModel)

    is_enable = Fields.BooleanProperty(default=True, verbose_name=u'顯示於前台')

    def get_pay_url(self, controller, payment_type=None):
        if controller is None:
            raise Exception('need Controller')
        if payment_type is None:
            payment_type = self.payment_type.get()
        return '%s?payment_record=%s' % (controller.uri(payment_type.pay_uri), controller.util.encode_key(self))
