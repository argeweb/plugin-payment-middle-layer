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
        'about': {
            'group': u'付款中間層',
            'actions': [
                {'action': 'list', 'name': u'付款中間層'},
                {'action': 'add', 'name': u'新增付款中間層'},
                {'action': 'edit', 'name': u'編輯付款中間層'},
                {'action': 'view', 'name': u'檢視付款中間層'},
                {'action': 'delete', 'name': u'刪除付款中間層'},
                {'action': 'plugins_check', 'name': u'啟用停用模組'},
            ]
        }
    }
}