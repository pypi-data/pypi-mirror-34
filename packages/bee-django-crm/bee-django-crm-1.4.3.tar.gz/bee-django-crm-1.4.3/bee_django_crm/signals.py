# -*- coding:utf-8 -*-
from django.dispatch import Signal

# 费用审核后的信号
contract_checked = Signal(providing_args=["preuser_contract","user"])
