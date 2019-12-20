## 项目2 情感细粒度分类

### 1. Introduction

在自然语言处理中，有一个常见的问题就是**对客户的评价进行分析**。 这些用户评论中，包含了大量的有用信息，例如**情感分析**，或者**相关事实描述**。 例如: 

 “味道不错的面馆，性价比也相当之高，分量很足～女生吃小份，胃口 小的，可能吃不完呢。环境在面馆来说算是好的，至少看上去堂子很 亮，也比较干净，一般苍蝇馆子还是比不上这个卫生状况的。中午饭 点的时候，人很多，人行道上也是要坐满的，隔壁的冒菜馆子，据说 是一家，有时候也会开放出来坐吃面的人。“

首先情感是正向的，除此之外我们还能够进行知道这个的几个事实描述：1. 性价比比较高； 2. 装修比较好； 3. 分量足。

### 2. Method

#### 2.1 Data source 

AI Challenger 2019 中情感细粒度分类任务数据集

竞赛数据，描述，参考资料（包括第一名的思路和代码）：[AI Challenger 2018情感分析赛道资料汇总](https://blog.csdn.net/lrt366/article/details/89244735)

#### 2.2 Model

本次的任务，**输出端**本质上是一个**多分类的多分类问题**（有20个输出信息，每个信息有4个类别，分别是1（正面），0（中性），-1（负面），-2（未提及））

而**输入端**是一篇短评，因此少不了自然语言的预处理，分词分句清洗等，然后做词嵌入进行输入。



输入和输出都是确定的，因此**本次项目2的重点**就在于**模型部分的构建和优化**。另外，前端和后端的构建也是比较重要的。

#### 2.3 模型的评价指标

Precision, Recall, AUC. 竞赛官方好像使用的是F1值作为评价指标

### 3. 任务分配

#### 3.1 前端

前端的设计，需要包含如下内容：

1. 一个输入框，用来输入短评

2. “分析”按钮，用来把文本发送到后端并激活分析函数

3. 一个把分析结果可视化出来的组件：

   - 根据项目指导ppt，建议用[D3.js](https://github.com/d3/d3/wiki/Gallery)中的这三个组件中的一个：[Bullet Charts](https://bl.ocks.org/mbostock/4061961)，[Cluster Dendrogram](https://observablehq.com/@d3/cluster-dendrogram)，[Radial Boxplot](https://bl.ocks.org/davidwclin/ad5d13db260caeffe9b3)

   - [Echarts](https://www.echartsjs.com/examples/zh/index.html)是备选，其中：[单轴散点图](https://www.echartsjs.com/examples/zh/editor.html?c=scatter-single-axis)，[树图](https://www.echartsjs.com/examples/zh/editor.html?c=tree-basic)，[雷达图](https://www.echartsjs.com/examples/zh/editor.html?c=radar) 可以作为上面D3中三个组件的替代品。



可选内容：“随便试试”功能，点一下，就会在数据库中的已有数据中随机选择一条，展示出来。

#### 3.2 后端

后端的end_to_end：输入一篇评论，输出各个标签的分类值。

#### 3.3 模型

模型的优化可以是一个持续的过程，但在这次项目中我们至少要有一个高于Baseline的模型，作为作业上交。

资料：[AI Challenger 2018情感分析赛道资料汇总](https://blog.csdn.net/lrt366/article/details/89244735)

#### 3.4 总结及重要性优先级

根据项目指导，我们的项目计划和优先级应该是：

1. 复现前人的Baseline（优先级：**高**）
2. 完成end-to-end（优先级：**高**）
3. 模型调优（至少需要调出一个比Baseline好的模型，再网上的调优根据精力来做，保证其它步骤先完成）
   - 模型调优时可以多个人分别尝试不同开源模型或优化手段，然后选取效果最好的
4. 完成前后端交互及展示（优先级：**高**）