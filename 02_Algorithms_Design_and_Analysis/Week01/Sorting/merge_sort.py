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
4. Merge Sort - 归并排序
    归并排序具体工作原理如下（假设序列共有n个元素）：
    ① 将序列每相邻两个数字进行归并操作（Merge），形成floor(n/2+n%2)个序列，排序后每个序列包含两个元素
    ② 将上述序列再次归并，形成floor(n/4)个序列，每个序列包含四个元素
    ③ 重复步骤2，直到所有元素排序完毕
'''

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
    
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result

if __name__ == "__main__":
    print MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45])





