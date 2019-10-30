## 第2节 BFS和DFS、以及机器学习初步

这一节主要学习了：图算法中的**深度优先算法**和**广度优先算法**，以及线性回归的实现

### 1. BFS和DFS

> Breadth-First Search 和 Depth-Frist Search 是图搜索算法中的两种基本算法。都是用来寻找从一个node到另一个node的某条路径的。

 在进行这两个算法之前的第一步，就是先把图通过无循环遍历转换成树的形式：

![GraphToTree](http://chuantu.xyz/t6/702/1572356286x1033347913.png)

#### 1.1 BFS(Breadth-First Search)

广度优先算法，通常使用**队列**的数据结构实现。从第一层开始，以广度优先的方式，遍历它的下一层所有子节点。

![](http://chuantu.xyz/t6/702/1572372528x1031866013.png)

**复杂度**：![](http://latex.codecogs.com/gif.latex?b^0+b^1+b^2+b^3+\dots+b^d=\frac{1-b^{d+1}}{1-b}\stackrel{b,d\to\infty}{\approx}O(b^d))，其中b为宽度，d为深度

**最优路径问题**：当，

- 所有节点之间的 Cost 都非负（例如距离）

- 每次迭代后，都对数组依照总Cost排序（比如距离、节点个数，对应找最短路径和最少换乘次数）

时，BFS一定可以获得最优路径。



#### 1.2 DFS(Depth-First Search)

深度优先算法，通常使用**堆**的数据结构实现。从一个节点开始，以深度优先的方式，遍历下面的子节点。

![](http://chuantu.xyz/t6/702/1572372575x1033347913.png)

**复杂度**：最坏情况同样是遍历每个节点，同样是![](http://latex.codecogs.com/gif.latex?O(b^d))

**最优路径**：很少给出最优路径



#### 1.3 BFS与DFS的区别

![BfsDfsDifference](http://chuantu.xyz/t6/702/1572355914x1031866013.png)

| 算法         | BFS                                             | DFS                                             |
| ------------ | ----------------------------------------------- | ----------------------------------------------- |
| 实现方式     | 队列                                            | 堆                                              |
| 时间复杂度   | ![](http://latex.codecogs.com/gif.latex?O(b^d)) | ![](http://latex.codecogs.com/gif.latex?O(b^d)) |
| 空间复杂度   | ![](http://latex.codecogs.com/gif.latex?O(b^d)) | ![](http://latex.codecogs.com/gif.latex?O(b*d)) |
| 是否最优路径 | 在某些条件下                                    | 很少给出最优                                    |



#### 1.4 A* Search

（待补充）

### 2. Machine Learning

（待补充）



### 参考资料

[1] [基本算法——深度优先搜索（DFS）和广度优先搜索（BFS）](https://www.jianshu.com/p/bff70b786bb6)

[2] [完美二叉树, 完全二叉树和完满二叉树]( https://blog.csdn.net/qq_22642239/article/details/80774013 )

[3] [队列、堆思想]( https://blog.csdn.net/qq_40981899/article/details/85869971 )



[返回目录]( https://github.com/SimZhou/NLP_Assignments )

