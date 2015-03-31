# -*- coding: utf-8 -*-
"""
Basic rules for data validation

@author: Tomas Krizek
"""

from errors import *


def check_integer(val, min=float("-inf"), max=float("inf")):
    if not isinstance(val, int):
        try:
            val = int(val)      # string conversion: "3" -> 3
        except ValueError:
            raise TypeError("Expecting type Integer")

    if (val < min):
        raise ValueTooSmall(min)

    if (val > max):
        raise ValueTooBig(max)

    return True


def check_double(val, min=float("-inf"), max=float("inf")):
    if not isinstance(val, (int, float)):
        try:
            val = float(val)      # string conversion: "3.14" -> 3.14
        except ValueError:
            raise TypeError("Expecting type Double")

    if (val < min):
        raise ValueTooSmall(min)

    if (val > max):
        raise ValueTooBig(max)

    return True
