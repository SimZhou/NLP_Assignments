# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:56:29 2019

@author: yihua
"""

import numpy as np
array = lambda n=100: list(np.random.randint(1,100,n))

'''
2. 选择排序 - Selection Sort
    选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中
    找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小
    （大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。 

时间复杂度：O(n^2)
空间复杂度：O(1)
'''
def select_sort(array):
    for i in range(len(array)-1):
        minIndex = i    # 初始化最小值的位置
        for j in range(i+1, len(array)):
            '''
            循环遍历i后面的元素，如果第j个元素小于最小值，则替换掉当前的最小值的大小和位置
            '''
            if array[j] < array[minIndex]: 
                minIndex = j
                
        array[i], array[minIndex] = array[minIndex], array[i]
    return array

print(select_sort(array(100)))
%timeit select_sort(array(1000))