#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created with YooLiang Technology (侑良科技).
# Author: Qi-Liang Wen (温啓良）
# Web: http://www.yooliang.com/
# Date: 2017/3/1.


from argeweb import Controller, scaffold, route_menu


class PaymentRecord(Controller):
    class Scaffold:
        display_in_list = ['created', 'title', 'detail', 'amount', 'user', 'payment_status']

    @route_menu(list_name=u'system', group=u'金流管理', text=u'付款記錄', sort=891)
    def admin_list(self):
        return scaffold.list(self)
