# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo02_operate:操作ndarray数组
"""
import numpy as np

# 创建一维数组
ary_a = np.array([1, 2, 3, 4, 5, 6])

# 打印数组
print(ary_a)

# np.arange(起始值,终止值,步长)
ary_b = np.arange(0, 10, 3)
print(ary_b)

# np.zeros(数组元素个数,dtype='类型')
ary_c = np.zeros(10)
print(ary_c)

# np.ones(数组元素个数,dtype='类型')
ary_d = np.ones((2, 3), dtype="float")
print(ary_d)

# 构造5个1/5
print((np.ones(5, dtype="int32") / 5))
