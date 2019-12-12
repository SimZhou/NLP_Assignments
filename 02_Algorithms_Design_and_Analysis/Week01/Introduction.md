# Algorithms: Design and Analysis

Notes from Stanford Open-Course: 

Algorithms: Design and Analysis, [Course Link](https://lagunita.stanford.edu/courses/course-v1:Engineering+Algorithms1+SelfPaced/course/)

### Introduction

Algorithms are: 

- Important for all branches of CS
- Key to Tech Innovation: e.g. PageRank
- Challenging and fun

### Intuition from Integer Multiplication

**Input:** 2 n-digit numbers **x** and **y**

**Output:** the product x·y

Tim gave an simple analysis on the 3rd-grade integer multiplication:

​		  5678

​		x1234

Let n be the length of input number x&y. Normally if we calculate the partial products and add them up, 

5678 × 4 has at most **2n** operations, 

5678 × 3 has at most **2n** operations, 

...

(The process is repeated for n times)

**Upshot:** #operations overall ≤ ![](https://latex.codecogs.com/gif.latex?Constant\cdot n^{2}) and the constant would likely to be 4

**Can we do better？ -  This is important for algorithm designers, to refuse to be content**

### New algo for Integer Multiplication: Karatsuba Multiplication

