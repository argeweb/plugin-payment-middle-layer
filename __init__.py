#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/5/10.

from argeweb import ViewDatastore
from argeweb.core.events import on
from models.payment_type_model import PaymentTypeModel


@on('create_payment')
def create_payment(controller, title, detail, amount, source, source_params, source_callback_uri, payment_type, user, status):
    from models.payment_record_model import PaymentRecordModel
    from argeweb.core.json_util import stringify
    try:
        r = source.payment_record.get()
    except:
        r = None
    if r is None:
        r = PaymentRecordModel()
        # 先儲存一次，產生 key
        r.put()

    r.source_ndb_key = source.key
    r.source_params = stringify(source_params)
    r.source_callback_uri = source_callback_uri
    r.payment_type = payment_type.key
    r.user_object = user.key
    r.title = title
    r.detail = detail
    r.amount = float(amount)
    r.set_state(status)
    r.set_source_record(source)
    r.put()
    r.process_url(controller.uri, payment_type=payment_type)
    r.put()
    return r

ViewDatastore.register('payment_type', PaymentTypeModel.find_all_by_properties)
ViewDatastore.register('payment_type_list', PaymentTypeModel.all_enable)

plugins_helper = {
    'title': u'付款中間層',
    'desc': u'用來聯繫各種付款請求與付款方式的中間層。',
    'controllers': {
        'payment_middle_layer': {
            'group': u'付款中間層',
            'actions': [
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        },
        'payment_status': {
            'group': u'付款狀態',
            'actions': [
                {'action': 'list', 'name': u'付款狀態'},
                {'action': 'add', 'name': u'新增付款狀態'},
                {'action': 'edit', 'name': u'編輯付款狀態'},
                {'action': 'view', 'name': u'檢視付款狀態'},
                {'action': 'delete', 'name': u'刪除付款狀態'},
            ]
        },
        'payment_type': {
            'group': u'付款方式',
            'actions': [
                {'action': 'list', 'name': u'付款方式'},
                {'action': 'add', 'name': u'新增付款方式'},
                {'action': 'edit', 'name': u'編輯付款方式'},
                {'action': 'view', 'name': u'檢視付款方式'},
                {'action': 'delete', 'name': u'刪除付款方式'},
            ]
        },
        'payment_record': {
            'group': u'付款記錄',
            'actions': [
                {'action': 'list', 'name': u'付款記錄'},
                {'action': 'add', 'name': u'新增付款記錄'},
                {'action': 'edit', 'name': u'編輯付款記錄'},
                {'action': 'view', 'name': u'檢視付款記錄'},
                {'action': 'delete', 'name': u'刪除付款記錄'},
            ]
        },
    },
    'install_uri': 'payment_middle_layer:payment_middle_layer:after_install'
}
