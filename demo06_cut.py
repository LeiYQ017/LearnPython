# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo06_cut:数组切片操作
切片区间：[)
步长遵循：顺+逆-
"""
import numpy as np

# 一维数组
aray_a = np.arange(1, 9)
print("aray_a:\n", aray_a)  # [1 2 3 4 5 6 7 8]
print("aray_a[:3]:\n", aray_a[:3])  # [1 2 3]
print("aray_a[3:]:\n", aray_a[3:])  # [4 5 6 7 8]
print("aray_a[::-1]:\n", aray_a[::-1])  # [8 7 6 5 4 3 2 1]
print("aray_a[::3]:\n", aray_a[::3])  # [1 4 7]
print("aray_a[:]:\n", aray_a[:])  # [1 2 3 4 5 6 7 8]
print("aray_a[-3:-7:-1]:\n", aray_a[-3:-7:-1])  # [6 5 4 3]

# 二维数组
aray_a.shape = (2, 4)
print("aray_a:\n", aray_a)  # [[1 2 3 4],[5 6 7 8]]
print("aray_a[:2,:2]:\n", aray_a[:2, :2])  # [[1 2],[5 6]]
print("aray_a[:2][:1]:\n", aray_a[:2][:1])  # [[1 2 3 4]]
print("aray_a[::2,:]:\n", aray_a[::2, :])  # [[1 2 3 4]]

# 掩码操作
# 基于bool数组的掩码
aray_b = np.array([4, 2, 1, 0, 3])
print("aray_b:\n", aray_b)  # [4 2 1 0 3]
mask = [True, False, True, True, False]
print("aray_b[mask]:\n", aray_b[mask])  # [4 1 0]
print("aray_b[aray_b % 2 == 0]:\n", aray_b[aray_b % 2 == 0])  # [4 2 0]
# 基于索引的掩码
phones = np.array(["Apple", "小米", "OPPO", "Honor", "华为", "vivo"])
rank = [1, 2, 0, 5, 4, 3]  # 输出结果的顺序：1, 2, 0, 5, 4, 3
print("phones[rank]:\n", phones[rank])  # ['小米' 'OPPO' 'Apple' 'vivo' '华为' 'Honor']
