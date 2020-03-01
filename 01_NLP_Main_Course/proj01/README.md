## 项目1 非监督文本自动摘要模型的构建

### 1. Introduction

自动摘要问题是NLP领域的一个经典问题，简单的说，就是**输入一段长文字**，**输出**对这段长文字的一个**总结概要**。在新闻，语音播报、文档信息提取、公司报表、上市公司分析等等领域具有很多的应用场景。



### 2. Method

#### 2.1 Data source

中文的数据来源有两个：

1. 维基百科中文语料库：[下载链接](https://dumps.wikimedia.org/zhwiki/20190720/zhwiki-20190720-pages-articles.xml.bz2)，使用提取工具 [wikiextractor](https://github.com/attardi/wikiextractor) 进行提取
2. 汉语新闻语料库：[下载链接]( https://github.com/Computing-Intelligence/datasource/blob/master/export_sql_1558435.zip )，下载后进行数据清洗和 Tokenization 的操作

其中，1+2 作为词向量训练的来源，2 作为主要处理的数据源

最后将Content专门放在一个单独文件夹中

**（技术点：数据清洗）**



#### 2.2 Training word2vec    *调参点：Skip-gram/CBoW、等*

使用2.1构建好的语料库，使用 Skip-gram / CBOW 模型训练词向量，直接使用Python的gensim库

**（技术点：语义相似性，负采样等细节的理解）**



#### 2.3 Testing & visualization word2vec

- 使用余弦相似度计算语义相似性
- 计算语义线性关系
- 词向量的可视化：使用 [t-sne]( https://www.kaggle.com/jeffd23/visualizing-word-vectors-with-t-sne ) 进行高维向量的可视化（可能需要减少单词量）

**（技术点：数学余弦相似度，语义线性关系，降维算法 t-sne）**



#### 2.4 Sentence-to-Vec      *调参点：暂时未知*

计算完词向量后，我们进一步使用普林斯顿大学提出的SIF方法对每个句子进行句子向量化，计算出 ![](http://latex.codecogs.com/gif.latex?V_{Sentence(i)})

[A SIMPLE BUT TOUGH-TO-BEAT BASELINE FOR SENTENCE EMBEDDINGS](https://openreview.net/pdf?id=SyK00v5xx)

通过把整篇文章当成一个长句，计算 ![](http://latex.codecogs.com/gif.latex?V_{Doc})。(创新点：是否可以用句向量合成文向量，效果可能会更好？）

再计算出文章标题的句向量 ![](http://latex.codecogs.com/gif.latex?V_{Title})

**（技术点：SIF论文阅读，SIF实现，降维算法 PCA，）**



#### 2.5 Achieve the most similar N sentences

因为已经得到了句向量，标题句向量，文向量，我们构建一个函数![](http://latex.codecogs.com/gif.latex?f)，使得![](http://latex.codecogs.com/gif.latex?f(V_{Sentence(i)}, V_{Title}, V_{Doc})) = ![](http://latex.codecogs.com/gif.latex?C_i)

，![](http://latex.codecogs.com/gif.latex?C_i)为该句与全部内容的相似度，排序取出Top_N，就能获得语义上最相关的句子了（即摘要）



#### 2.6 KNN平滑（移动平均）     *调参点：权重，N-Neighborhoods的选取*

通过平滑使得相关句不会被单独提出来，导致它显得很突兀

n选取太小可能会导致平滑不够，依旧突兀，n选取太大可能会导致太平滑，摘要效果不够好（创新点：考虑将n做成一个前端可交互的控件滑块，通过调整它可以让模型生成的摘要不一样）



#### 2.7 获得End-to-end模型

summrize(content, title) = summary



#### 2.8 可视化

**（技术点：前端XXX，后端Flask）**



### 3. Optimization

#### 3.1 作业范围内优化

- 扩充语料库，以获得更精准的词向量

- 词向量优化：[Stanford cs224n Lecture2: Word vectors 2 and Word Senses](http://web.stanford.edu/class/cs224n/slides/cs224n-2019-lecture02-wordvecs2.pdf)，[cs224n中文笔记：词向量的计算与评价](http://www.mwhitelab.com/archives/813)，[词向量的内部评价、外部评价、再训练](http://kuaibao.qq.com/s/20180124G0DVUJ00?refer=cp_1026)，可以考虑尝试多种词向量例如GloVe等。

  [Skip-gram与CBoW的优缺点]( https://www.zhihu.com/question/68112508?sort=created )

- KNN平滑

- 作业要求内提到的：标点符号与特殊字符的处理

- ...

#### 3.2 作业范围外优化（可选）

- BERT word Embedding
- ...