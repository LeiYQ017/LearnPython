# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo01_start:测试numpy
"""
import numpy as np

# 创建一维数组
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))

# 维度
print(ary.shape)

# 修改维度
ary.shape = (2, 3)
print(ary, ary.shape)
ary.shape = (6,)

# 数组的运算
print(ary)
print(ary * 3)
print(ary > 3)
print(ary + ary)
