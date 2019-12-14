# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:56:29 2019

@author: yihua
"""

'''
各种排序算法
'''
import numpy as np
array = lambda n=100: list(np.random.randint(1,100,n))

'''
1. 选择排序 - Selection Sort
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



'''
2. 冒泡排序 - Bubble Sort
    冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的
    顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列
    已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

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


'''
3. 快速排序 - Quicksort
    快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均
    比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

时间复杂度：O(nlogn)
空间复杂度：O(nlogn)
'''
def quick_sort(array):

'''
Merge Sort - 归并排序
'''








