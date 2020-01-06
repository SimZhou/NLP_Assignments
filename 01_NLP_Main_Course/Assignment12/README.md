## 第12节 关键词提取，NER，依存分析，NLP相关任务

这一节主要学了：关键词提取的方法，包括TF-IDF，Text-Rank，机器学习法（机器学习法讲了LDA隐狄利克雷分布，词向量方法）；实体命名识别(NER)；依存分析、语法树；以及各类NLP任务

> 一开始课上纠正了之前的一个错误：
>
> seq2seq中，由于最终生成句子的概率为每一条的条件概率相乘，因此越长的句子最终概率就会越小，最终导致模型更容易生成短句。
>
> 解决方法应该是：先对P(y|x)取log，然后再乘以一个归一化项 ![](http://latex.codecogs.com/gif.latex?\frac{1}{T^\alpha})（T和长度正相关，长度越长，项越小）。使得越负的值，缩减效应更大，限制其负的程度。



### 1. TF-IDF

先计算![](http://latex.codecogs.com/gif.latex?TermFrequency_{t,d}=\begin{cases}tf_{t,d}=count(t,d)\\tf_{t,d}=log_{10}{count(t,d)+1}\end{cases})

然后根据语料库计算![](http://latex.codecogs.com/gif.latex?InverseDocumentFrequency(IDF)_{t}=log_{10}{\frac{N}{n_{t}}})

最后![](http://latex.codecogs.com/gif.latex?w_{t,d} = TF_{t,d}\times{IDF_t})

**Note：**TF-IDF实际上也是句子/文章表征的一种形式，是一种词袋模型(Bag-of-Words)，即不考虑词语之间的顺序关系，而是简单粗暴地把它们装进一个袋子里面，作为句子/文章的特征。

TF-IDF的优点是效果其实还不错，缺点是语料库很大的话维度会非常大（语料库中token个数的维度）

### 2. Page-Rank & Text-Rank（Graph based extraction）

#### 2.1 Page rank

假设：一个网页如果连接的网页越多，那么这个网页越重要

![](http://uricc.ga/images/2019/12/31/_20191231214446.png)

**算法：**迭代

![](http://latex.codecogs.com/gif.latex?At\;t=0:PR(p_i,0) = \frac{1}{N})。意味着一开始用平均值初始化每个Page(i)的PageRank权重。

![](http://latex.codecogs.com/gif.latex?At\;each\;time\;step:\;PR(Pi,t+1)=(1-d)+d*\sum_{j\in{In(P_i)}}{\frac{1}{|Out(P_j)|}PR(P_j,t)})。在每个新的time step, 某个Page(i)的新的权重等于【所有进入Page(i)的那些其他Pages的1/|出度|乘以它们自己的当前PR值】。

#### 2.2 TextRank

TextRank是用PageRank的思想做文本特征提取的一种模型，具体方法是对文档取滑动窗口，默认滑动窗口内的词语互相两两连接。

![](http://latex.codecogs.com/gif.latex?WS(V_i)=(1-d)+d*\sum_{j\in{In(V_i)}}{\frac{w_{ji}}{\sum_{V_k\in{Out(V_j)}}{w_{jk}}}WS(V_j)})

其中**WS**是**Weighted Sum**的缩写，代表该词在句子/文章中的重要性。

TextRank与PageRank唯一的不同之处是多了edge之间的权重![](http://latex.codecogs.com/gif.latex?w)。

参考资料：[[TowardsDataScience] TextRank for Keyword Extraction](https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0)

### 3. LDA主题模型 (Latent Dirichlet Allocation隐含狄利克雷分布) 

假设：

1. 一个文本的主题服从某个分布
2. 每个主题下的词语服从另一个分布





### 分类和生成

1. 分类任务

   Text Representation

   Machine Learning

   Deep Learning

2. 生成任务

   机器翻译

   ​		Statistics + EM Algorithm (IBM 1)

   ​		RNN

   ​		RNN + Attention

   ​		Transformer

   问题回答

   ​		

