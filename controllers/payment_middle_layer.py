#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/5/10.
from argeweb import Controller, route_menu, route


class PaymentMiddleLayer(Controller):
    class Scaffold:
        display_in_list = ['title', 'name', 'image', 'is_enable', 'category']

    @route
    def admin_after_pay_for_test(self):
        return self.json(self.params.get_ndb_record('payment_record'))

    @route
    def taskqueue_after_install(self):
        from ..models.payment_status_model import PaymentStatusModel
        PaymentStatusModel.create_default_status()
        return 'done'
