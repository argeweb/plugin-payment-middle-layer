#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/5/10.
import random
from argeweb import Controller, scaffold, route_menu, Fields, route_with, route
from argeweb.components.pagination import Pagination
from argeweb.components.search import Search


class PaymentMiddleLayer(Controller):
    class Meta:
        components = (scaffold.Scaffolding, Pagination, Search)

    class Scaffold:
        display_in_list = ('title', 'name', 'image', 'is_enable', 'category')

    @route
    def gen_payment_record(self):
        from ..models.payment_record_model import PaymentRecordModel
        from ..models.payment_type_model import PaymentTypeModel
        payment_record_name = self.params.get_string('payment_record')
        PaymentRecordModel.find_by_name(payment_record_name)

    @route
    def taskqueue_after_install(self):
        from ..models.payment_status_model import PaymentStatusModel
        PaymentStatusModel.create_default_status()
        self.logging.info('done')
        return 'done'
