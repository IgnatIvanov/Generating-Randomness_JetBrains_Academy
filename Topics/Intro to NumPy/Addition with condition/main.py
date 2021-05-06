import numpy as np


def custom_sum(arg1, arg2):
    l1 = type(list()) == type(arg1)
    l2 = type(list()) == type(arg2)
    if l1 and l2:
        return 'Both arguments are lists, not arrays'
    elif l1 or l2:
        return 'One argument is a list'
    else:
        return arg1 + arg2
