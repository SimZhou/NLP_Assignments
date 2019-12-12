## 第4节 神经网络及其训练算法介绍

**补充知识：Lazy Learning and Eager Learning，Outliers, **

**Lazy Learning**

​		特点： 简单地把训练样本存储起来，直到需要分类新的实例时才分析其与所存储样例的关系，据此确定新实例的目标函数值。也就是说这种学习方式只有到了需要决策时才会利用已有数据进行决策，而在这之前不会经历 Eager Learning所拥有的训练过程。 

​        例子：KNN，Naive Bayers

**Eager Learning**

​		特点： 在进行某种判断（例如，确定一个点的分类或者回归中确定某个点对应的函数值）之前，先利用训练数据进行训练得到一个目标函数，待需要时就只利用训练好的函数进行决策，显然这是一种一劳永逸的方法。

​        例子：SVM、LR、Decision Tree、Neural Networks、……

**Outliers：异常点**

简单方法：用Percentiles剔除比如20%以外的数据



这一节主要学习了：

神经网络

逻辑回归

Logistic Loss 与 交叉熵的原理与应用（LogitLoss适用于01分布，交叉熵适用于多分类，本质上是一样的）

反向传播、链式法则……



[返回目录]( https://github.com/SimZhou/NLP_Assignments )

