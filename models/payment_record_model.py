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
from payment_status_model import PaymentStatusModel


class PaymentRecordModel(BasicModel):
    name = Fields.StringProperty(verbose_name=u'識別名稱')
    title = Fields.StringProperty(verbose_name=u'付款記錄摘要')
    order_no = Fields.StringProperty(verbose_name=u'訂單編號', default=u'')
    detail = Fields.RichTextProperty(verbose_name=u'付款記錄細節')
    amount = Fields.FloatProperty(verbose_name=u'應付款金額')
    user_object = Fields.KeyProperty(verbose_name=u'付款人', kind=ApplicationUserModel)
    user = Fields.SearchingHelperProperty(verbose_name=u'付款人', target=u'user_object', target_field_name=u'name')
    user_email = Fields.SearchingHelperProperty(verbose_name=u'付款人', target=u'user_object', target_field_name=u'email')

    source_uri = Fields.HiddenProperty(verbose_name=u'來源 URI')
    source_params = Fields.HiddenProperty(verbose_name=u'來源參數')
    source_ndb_key = Fields.HiddenProperty(verbose_name=u'來源物件 Key')

    payment_type = Fields.KeyProperty(verbose_name=u'付款方式', kind=PaymentTypeModel)
    payment_status = Fields.CategoryProperty(verbose_name=u'付款狀態', kind=PaymentStatusModel)

    def get_pay_url(self, controller, payment_type=None):
        if controller is None:
            raise Exception('need Controller')
        if payment_type is None:
            payment_type = self.payment_type.get()
        try:
            url = controller.uri(payment_type.pay_uri)
        except:
            url = payment_type.pay_uri

        return '%s?payment_record=%s' % (url, controller.util.encode_key(self))

    def gen_result_url(self, controller):
        if controller is None:
            raise Exception('need Controller')
        try:
            return controller.uri(
                self.source_uri, payment_record=controller.util.encode_key(self), source_record=self.source_ndb_key)
        except:
            return '%s?payment_record=%s&source_record=%s' % (
                self.source_uri, controller.util.encode_key(self), self.source_ndb_key)

    def set_state(self, payment_status_name):
        self.payment_status = PaymentStatusModel.find_by_name(payment_status_name).key
