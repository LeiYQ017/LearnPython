# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo03_property:ndarray属性
"""
import numpy as np

# 创建一维数组
ary_a = np.array([[1, 2, 3], [4, 5, 6]])

# 对象类型操作
print(type(ary_a))
print(ary_a.dtype)
# 正确的修改数据类型操作
print(ary_a.astype(float))
print("size:", ary_a.size)
print(ary_a.shape)
print("len:", len(ary_a))

# 创建三维数组
c = np.arange(1, 19)
c.shape = (3, 2, 3)
print(c)
print("三维数组索引数字9：", c[1][0][2])
print("三维数组索引数字9：", c[1, 0, 2])

for i in c:
    for j in i:
        for k in j:
            print(k)
