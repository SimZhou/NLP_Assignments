# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:56:29 2019

@author: yihua
"""

import numpy as np
array = lambda n=100: list(np.random.randint(1,100,n))

'''
3. 快速排序 - Quicksort
    快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均
    比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

时间复杂度：O(nlogn)
空间复杂度：O(nlogn)
'''
def quick_sort(array):








