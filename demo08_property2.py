# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo08_property2:ndarray其他属性
"""
import numpy as np

aray = np.array([
    [1 + 2j, 2 + 4j, 4 + 8j],
    [4 + 2j, 6 + 3j, 2 + 1j],
    [5 + 5j, 6 + 6j, 1 + 1j],
])

print(aray.shape)  # (3, 3)
print(aray.dtype)  # complex128
print(aray.itemsize)  # 16
print(aray.size)  # 9
print(len(aray))  # 3
print(aray.nbytes)  # 144
print(aray.real)  # 实部：[[1. 2. 4.],[4. 6. 2.],[5. 6. 1.]]
print(aray.imag)  # 虚部：[[2. 4. 8.],[2. 3. 1.],[5. 6. 1.]]
print(aray.T)  # 转置：[[1.+2.j 4.+2.j 5.+5.j],[2.+4.j 6.+3.j 6.+6.j],[4.+8.j 2.+1.j 1.+1.j]]

print([i for i in aray.flat])
