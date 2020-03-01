# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:56:29 2019

@author: yihua
"""

import numpy as np
array = lambda n=100: list(np.random.randint(1,100,n))

'''
1. 冒泡排序 - Bubble Sort
    冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的
    顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列
    已经排序完成。这个算法的名字由来是因为越小/大的元素会经由交换慢慢“浮”到数列的顶端。

时间复杂度：O(n^2)
空间复杂度：O(1)
'''
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort(array(100)))
%timeit bubble_sort(array(1000))







