# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo07_split:多维数组的组合与拆分
分类：水平方向组合与拆分、垂直方向组合与拆分、深度方向组合与拆分
"""
import numpy as np

aray_a = np.arange(1, 7).reshape(2, 3)
aray_b = np.arange(7, 13).reshape(2, 3)
print("aray_a:\n", aray_a)
print("aray_b:\n", aray_b)

# 垂直方向
aray_c = np.vstack((aray_a, aray_b))
print("aray_c:\n", aray_c)
aray_d, aray_e = np.vsplit(aray_c, 2)
print("aray_d:\n", aray_d)
print("aray_e:\n", aray_e)

# 水平方向
aray_f = np.hstack((aray_a, aray_b))
print("aray_f:\n", aray_f)
aray_g, aray_h = np.hsplit(aray_f, 2)
print("aray_g:\n", aray_g)
print("aray_h:\n", aray_h)

# 深度方向
aray_i = np.dstack((aray_a, aray_b))
print("aray_i:\n", aray_i)
aray_j, aray_k = np.dsplit(aray_i, 2)
print("aray_j:\n", aray_j)
print("aray_k:\n", aray_k)

# 垂直：0、水平：1、深度：2
aray_l = np.concatenate((aray_a, aray_b), axis=0)
print("aray_l:\n", aray_l)
m, n = np.split(aray_l, 2, axis=0)
print("c:\n", m)
print("d:\n", n)

# 长度不相等数组组合拆分
a = np.array([1, 3, 5, 7])
b = np.array([0, 2, 9])
# 填充b数组,使其与a数组长度相同:头部补0个常量,尾部补1个常量,补充值为-1
b = np.pad(b, pad_width=(0, 1), mode="constant", constant_values=-1)
print("b:\n", b)

# 一维数组的组合
d = np.array([2, 6, 78, 9, 1])
e = np.array([7, 0, 8, 2, 10])
f = np.row_stack((d, e))
print("f:\n", f)  # 垂直
g = np.column_stack((d, e))
print("g:\n", g)  # 水平
