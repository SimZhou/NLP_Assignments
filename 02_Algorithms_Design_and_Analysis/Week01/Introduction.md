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

(Not really understanding what's happening here, just some kind of magical operations...)

recursive programing



### About the Course

Tim introduced about the course topics, which includes:

- Vocabulary for algorithms, e.g. Big-Oh, ...
- Algorithm design paradigms, Divide-and-Conquer
  - IM, sorting, matrix multi
  - Master method...
- Randomization
- Primitives for reasoning about graphs
- Data structure
  - Heaps, balanced binary search trees, hashing and some variants(e.g. bloom filters)

Sequel Courses: 

- Greedy algorithms
- Dynamic programming
- NP-complete problems
- ...

Skill: 

- better programmer
- better mathematical/analytical skills
- think algorithmically

No required books but recommended ones are: 

- Kleinberg/Tardos, *Algorithm Design*, 2005. 
- Dasgupta/Papadimitriou/Vazirani, Algorithms, 2006. 
- Cormen/Leiserson/Rivest/Stein, *Introduction to Algorithms*, 2009 (3rd ed). 
- Mehlhorn/Sanders, *Data Structures and Algorithms: The Basic Toolboox*, 2008. 



### Merge Sort

![](https://uricc.ga/images/2019/12/13/_20191214094220.png)

