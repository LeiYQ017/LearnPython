# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

"""
demo04_detail:Numpy基本数据类型

bool、int8、int16、int32、int64、float16、float32、float64、uint8、
uint16、uint32、uint64、complex64、complex128、str
?、i1、i2、i4、i8、f2、f4、f8、u1、u2、u4、u8、c8、c16、U<字符数>
日期类型:M8[Y/M/D/h/m/s]
"""
import numpy as np

# 自定义数据类型
data = [
    ("张三", [90, 80, 85, 70], 20),
    ("李四", [92, 80, 75, 90], 19),
    ("王老五", [67, 70, 55, 83], 23),
]
# 定义组合数据类型：2Unicode字符、数组4int32、整数int32
"""
方法一：
ary = np.array(data, dtype='U3,4int32,int32')
print(ary)
print(ary[1][1])
=======================================
方法二：
ary = np.array(
    data, dtype=[
        ("name", "str_", 3),
        ("scores", "int32", 4),
        ("ages", "int32", 1)
    ])
print(ary)
print(ary[2]["ages"])
=======================================
# 方法三：
ary = np.array(
    data, dtype={
        "names": ["name", "score", "age"],
        "formats": ["U3", "4int32", "int32"]
    })
print(ary)
print(ary[2]["name"])
"""

# 方法四：
ary = np.array(
    data, dtype={
        "names": ("U3", 0,),
        "scores": ("4int32", 16),
        "ages": ("int32", 28),
    })
print(ary)
print(ary[2]["names"], ary.itemsize)

# 测试数组中存储日期数据类型：
datas = [
    "2021-01-01", "2020", "2008-11", "2019-06-18",
    "2017-08-24 10:39:52",
]
date = np.array(datas)
dates = date.astype("M8[s]")
print(dates, dates.dtype)
print(dates[1] - dates[2])
