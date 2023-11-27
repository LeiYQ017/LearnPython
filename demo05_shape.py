# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo05_shape:数组变维
"""
import numpy as np

aray_a = np.arange(1, 9)
print("aray_a:\n", aray_a)  # [1 2 3 4 5 6 7 8]
aray_a[0] = 0

# 视图变维
aray_b = aray_a.reshape(2, 4)  # 视图变维：二行四列二维数组
print("aray_b:\n", aray_b)  # [[1 2 3 4],[5 6 7 8]]
aray_c = aray_b.reshape(2, 2, 2)  # 视图变维：二页二行二列三维数组
print("aray_c:\n", aray_c)  # [[[1 2],[3 4]],[[5 6],[7 8]]]
aray_d = aray_c.ravel()  # 视图变维：一维数组
print("aray_d:\n", aray_d)  # [1 2 3 4 5 6 7 8]

# 复制变维
aray_e = aray_c.flatten()
print("aray_e:\n", aray_e)  # [1 2 3 4 5 6 7 8]

# 就地变维
aray_e.shape = (4, 2)
print("aray_e:\n", aray_e)  # [[0 2],[3 4],[5 6],[7 8]]
aray_e.resize((8,))
print("aray_e:\n", aray_e)  # [1 2 3 4 5 6 7 8]
