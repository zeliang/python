#!/usr/bin/python  
# -*- coding: utf-8 -*-

import numpy as np

class LearnNumpy:

    def get_np_version(self):
        ver=np.version.version
        return ver

    #用array产生一维数组，或者是多维数组，注意是用[]来实现
    def make_array(self):
        return np.array([[1,1,3,4,5],[1,1,1,1,1],[9,0,0,0,0],[10,1,1,1,7]])

print LearnNumpy().make_array()
# [[ 1  1  3  4  5]
#  [ 1  1  1  1  1]
#  [ 9  0  0  0  0]
#  [10  1  1  1  7]]


#dtype=np.string_是可以指定数据类型的，指定array的数据类型是什么东西，
# 那么就是说一切的基本数据类型都是可以组成多维矩阵
numeric_strings2 = np.array(['1.23','2.34','3.45'],dtype=np.string_)
print numeric_strings2
# ['1.23' '2.34' '3.45']

#astype是可以转换类型的
print numeric_strings2.astype(float)
# [ 1.23  2.34  3.45]

#其实也是可以用dtype指定为想要的数据类型，如下
numeric_boolean2 = np.array([[1,21,0],[1,21,0],[1,21,0]],dtype=np.string_)
print numeric_boolean2
# [['1' '21' '0']
#  ['1' '21' '0']
#  ['1' '21' '0']]

array=np.arange(10)
print 'origin:',array
# origin: [0 1 2 3 4 5 6 7 8 9]

#下标为2到下标为4的都改为90，一共修改的有两个值，左边闭合，右边开
# 并且对指定下标进行修改了，直接影响原始数据
array[2:4]=90
print '修改90后:',array
# 修改90后: [ 0  1 90 90  4  5  6  7  8  9]

#[:]表示数组的所有下标
array[:]=0
print '全部修改:',array
# 全部修改: [0 0 0 0 0 0 0 0 0 0]

#使用copy方法对数据进行拷贝后修改，不影响原来数组
array=np.arange(10)
print "origin:",array
copy1=array[2:5].copy()
copy1[:]=0
print "modify copy :",copy1
print "origin:",array
print 'get[i]:',array[2]
# origin: [0 1 2 3 4 5 6 7 8 9]
# modify copy : [0 0 0]
# origin: [0 1 2 3 4 5 6 7 8 9]
# get[i]: 2

a=np.arange(1,13)
print a
#reshape 是改变数组的形状，比如一维变为多维，不影响之前的数据，变为3行4列的矩阵
print a.reshape(3,4)
print a
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

#linspace表示在8和9之间生成10个数字，生成的都是固定的，注意是线性的，都是闭区间
print np.linspace(8,9,10)
# [ 8.          8.11111111  8.22222222  8.33333333  8.44444444  8.55555556
#   8.66666667  8.77777778  8.88888889  9.        ]

#产生3行6列的0矩阵
print np.zeros([3,6])
# [[ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.]]

#产生3行6列的1矩阵
print np.ones((3,6))
# [[ 1.  1.  1.  1.  1.  1.]
#  [ 1.  1.  1.  1.  1.  1.]
#  [ 1.  1.  1.  1.  1.  1.]]

#产生对称矩阵，3行3列，可以是一行一列等
print np.eye(3)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

print np.eye(2)
# [[ 1.  0.]
#  [ 0.  1.]]

print np.eye(1)
# [[ 1.]]

#获取数组的各种属性
eye=np.eye(3)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]

print eye.ndim #数组的维数
# 2，因为左上角有两个[[

print eye.shape #数组每一维的大小
# (3L, 3L) 2维，第一维有3个，第二维有3个

#----------------------切片
array=np.array([[1,2,4],[7,8,9],[90,89,77]])
print array
# [[ 1  2  4]
#  [ 7  8  9]
#  [90 89 77]]
#这里的0代表下标为0的数组[1,2,4]
print array[0]
# [1 2 4]

#获取下标为1，长度为2-1=1的数组
print array[1:]
# [[ 7  8  9]
#  [90 89 77]]