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
from argeweb.core.ndb import encode_key


class PaymentRecordModel(BasicModel):
    title = Fields.StringProperty(verbose_name=u'付款記錄摘要')
    detail = Fields.RichTextProperty(verbose_name=u'付款記錄細節')
    amount = Fields.FloatProperty(verbose_name=u'應付款金額')
    user_object = Fields.KeyProperty(verbose_name=u'付款人', kind=ApplicationUserModel)
    user = Fields.SearchingHelperProperty(verbose_name=u'付款人名稱', target=u'user_object', target_field_name=u'name')
    user_email = Fields.SearchingHelperProperty(verbose_name=u'付款人信箱', target=u'user_object', target_field_name=u'email')

    source_ndb_key = Fields.KeyProperty(verbose_name=u'來源物件 Key')
    source_params = Fields.HiddenProperty(verbose_name=u'來源參數')
    source_callback_uri = Fields.HiddenProperty(verbose_name=u'來源 Callback URI')

    target_ndb_key = Fields.KeyProperty(verbose_name=u'組件物件 Key')

    payment_type = Fields.KeyProperty(verbose_name=u'付款方式', kind=PaymentTypeModel)
    payment_status = Fields.CategoryProperty(verbose_name=u'付款狀態', kind=PaymentStatusModel)

    pay_url = Fields.HiddenProperty(verbose_name=u'付款網址')
    return_rul = Fields.HiddenProperty(verbose_name=u'回傳網址')

    def process_url(self, uri, payment_type=None):
        if uri is None:
            raise Exception('need URI')
        if payment_type is None:
            payment_type = self.payment_type.get()
        try:
            self.pay_url = uri(payment_type.pay_uri, payment_record=encode_key(self))
        except:
            self.pay_url = '%s?payment_record=%s' % (uri(payment_type.pay_uri), encode_key(self))
        try:
            self.return_rul = uri(self.source_callback_uri, payment_record=encode_key(self))
        except:
            self.return_rul = '%s?payment_record=%s' % (uri(self.source_callback_uri), encode_key(self))

    def set_state(self, payment_status):
        if payment_status is None:
            return
        if isinstance(payment_status, basestring):
            self.payment_status = PaymentStatusModel.get_by_name(payment_status).key
            return
        self.payment_status = payment_status

    def set_source_record(self, source):
        try:
            if hasattr(source, 'payment_record_object'):
                setattr(source, 'payment_record_object', self.key)
                source.put()
            elif hasattr(source, 'payment_record'):
                setattr(source, 'payment_record', self.key)
                source.put()
        except:
            pass

    def get_source_params(self):
        from argeweb.core.json_util import parse
        try:
            return parse(self.source_params)
        except:
            return {}

    @property
    def order_no(self):
        params = self.get_source_params()
        order_no = 'order_no' in params and params['order_no'] or self.name
        return order_no

    @property
    def source(self):
        return self.source_ndb_key.get()
