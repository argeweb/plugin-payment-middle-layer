#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/5/10.

from argeweb import ViewDatastore
from models.payment_middle_layer_model import PaymentMiddleLayerModel

ViewDatastore.register('payment_middle_layer', PaymentMiddleLayerModel.find_by_name)

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
    },
    'install_uri': 'payment_middle_layer:payment_middle_layer:after_install'
}
