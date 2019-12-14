## 第10节 机器学习算法（贝叶斯，k-means，SVM，随机森林，XGBoost 等）

这一节主要学习了：经典机器学习中的贝叶斯方法，K-means，SVM；集成学习中的随机森林，XGBoost

### 1. 贝叶斯方法

> Recap of probability theory:
>
> Independency Assumption:![](http://latex.codecogs.com/gif.latex?P(A\cap B)=P(A)\cdot P(B))
>
> Rule of Total Probability: ![](http://latex.codecogs.com/gif.latex?P(A)=\sum_i{P(A|B_i)\cdot P(B_i)})
>
> Bayes' Rule: ![](http://latex.codecogs.com/gif.latex?P(A|B)=\frac{P(A\cap B)}{P(B)}=\frac{P(B|A)\cdot P(A)}{P(B)})

先验概率：*指根据以往经验和分析得到的概率*

后验概率：*事情已经发生，要求这件事情发生的原因是由某个因素引起的可能性的大小*

![](http://latex.codecogs.com/gif.latex?P(A|B)=\frac{P(A\cap B)}{P(B)}=\frac{P(B|A)\cdot P(A)}{P(B)})

#### 1.1 Maximum a Posterior（极大后验概率）、Maximum Likelihood（极大似然估计）

![](http://latex.codecogs.com/gif.latex?h_{MAP}=\arg\max_{h\in H}P(h|D)=\arg\max_{h\in H}P(D|h)P(h))

![](http://latex.codecogs.com/gif.latex?h_{ML}=\arg\max_{h\in H}P(D|h))

where D is short for Data, H is the set of Hypothesises, h is a particular function in the hypothesises

简单解释：

- 在极大后验概率情况下，Data已经发生，我们需要求一个最佳h，它对数据的拟合情况最好（生成概率最大），则这个h就是最佳h
- 在极大似然的情况下，我们要求一个h，使得在这个h下，我们取得观测数据D的概率最大，则这个h是最佳h

#### 1.2 朴素贝叶斯 Naive Bayes

朴素贝叶斯分类器，是一个生成模型，对于每一种分类，它都可以生成一个后验概率

![](http://latex.codecogs.com/gif.latex?h_{y=y_0, MAP}\\=\arg\max_{h\in H}P(y=y_0|a_1,a_2,a_3,...)\\=\arg\max_{h\in H}\frac{P(a_1,a_2,a_3,...|y=y_0)\cdot P(y=y_0)}{P(a_1,a_2,...)}\\=\arg\max_{h\in H}{P(a_1,a_2,a_3,...|y=y_0)\cdot P(y=y_0)}\\=\arg\max_{h\in H}{P(a_1|y_0)\cdot P(a_2|y_0)\cdot P(a_3|y_0)\cdots P(y=y_0)}(According to "Naive"hypothesis))

然后我们同样可以求出![](http://latex.codecogs.com/gif.latex?h_{y=y_1}), ![](http://latex.codecogs.com/gif.latex?h_{y=y_2}), ...。最后y的估计值就是使h得到最大值所对于的y值。

例：文档分类

![](https://uricc.ga/images/2019/12/13/_20191213164304.png)

在用朴素贝叶斯进行文档分类的例子中，由于词库中某些词可能在句子中没有出现，产生条件概率为0的情况，因此对于所有词的初始词频默认为1（而不是0）（Add 1 smoothing）

##### 

### 2. K-means

> **Input:** dataset D, number of clusters K
>
> **Output:** partition of D into k clusters
>
> **Algorithm:** 
>
> ​		Choose k random seeds
>
> ​		Repeat until no changes:
>
> ​				Assign each instance to the cluster of its closest seed
>
> ​				Redefine seeds as cluster means
>
> ​		Return k clusters

如何提升聚类效果：k个点的选取尽可能互相远离

### 3. SVM

> 拉格朗日乘子法：
>
> f(x), h(x), 求 min f(x)  *subject to*  h(x)=0
>
> 令L = f(x) + λh(x), 