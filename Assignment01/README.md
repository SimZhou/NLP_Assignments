## 第1节 基于语法树和概率的AI模型

这一节主要学习了：

### 1. 基于语法树规则的短句生成器

> 基于语法树的短句生成器基本思路是通过预先构建的语法树，以及词库，对一个固定语法不断递归查找最终生成一句符合该语法的短句

  ![语法树例子](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571823712&di=a36fecb9108f453546fb3aca53cd450c&imgtype=jpg&er=1&src=http%3A%2F%2Fimg3.coin163.com%2F50%2F84%2FJfInei.gif) 



*基于语法树的句子生成器，**优点**在于速度快，需要数据量少，开发快，可以迅速开发出适用于某个领域的生成器，而**缺点**在于依赖预先制定的规则所以通用性差，可扩展性也较差。*

### 2. 基于概率（语言）模型的句子判断器

> 基于语言模型的句子判断器可以运用概率模型计算一句短句在某个语料库的基础下产生的可能性，其中包括1-gram，2-gram，n-gram模型	

#### 2.1 1-gram模型

1-gram模型假设一句句子的每个词的出现都是独立的，因此一句话产生的概率即为所有词在语料库中出现概率之积：

 ![](http://latex.codecogs.com/gif.latex?\\P(sentence)=P(w_1\cdotw_2\cdotsw_n)=\prod_{i=1}^{n}\frac{count(w_i)}{\sum_{\forallk}count(w_k)}) 

其中k为语料库中的Token数目

#### 2.2 2-gram模型

2-gram模型假设一句句子中的每一个词的出现依赖且仅依赖于上一个词，因此有：

![](http://latex.codecogs.com/gif.latex?\\P(sentence)\\=P(w_1 \cdot w_2 \cdots w_n) \\= P(w_n|w_1 \cdots w_{n-1})\cdot P(w_1\cdots w_{n-1})\\=P(w_n|w_1 \cdots w_{n-1})\cdot P(w_{n-1}|w_1\cdots w_{n-2})\cdot P(w_1\cdots w_{n-2})\\= P(w_{n}|w_1 \cdots w_{n-1})\cdot P(w_{n-1}|w_{1}\cdots w_{n-2})\cdot P(w_{n-2}|w_1\cdots w_{n-1})\cdots P(w_2|w_1)\cdot P(w_1)\\=P(w_1)\cdot P(w_2|w_1)\cdot P(w_3|w_2)\cdot P(w_4|w_3)\cdots P(w_{n-1}|w_{n}))

又根据贝叶斯公式：

![](http://latex.codecogs.com/gif.latex?\\P(w_{i+1}|w_{i})= \frac{P(w_{i+1}\cdot w_{i})}{P(w_{i})})

所以上式可以简化为：

![](http://latex.codecogs.com/gif.latex?\\P(sentence) = P(w_1 \cdot w_2 \cdots w_n) = \prod_{i=1}^{n-1} \frac{count(w_i, w_{i+1})}{count(w_i)}\times P(w_1))

其中，![](http://latex.codecogs.com/gif.latex?\\count(w_i, w_{i+1})) 即为前后两个词同时出现的次数，对应的token就是将语料库中所有1-gram token前后两两结合，比如[“我”，“喜欢”，“游泳”]就变成了[“我喜欢”，“喜欢游泳”]。

具体实现方式为：

1. 将语料库进行数据清洗并分词/split
2. 调用collections.Counter直接对分词完的1-gram数组计数，产生words_count_1_gram
3. 对分词完的数组进行前后两两相加，产生新的2-gram数组，并调用Counter产生words_count_2_gram
4. 给定一句话，套用公式计算句子生成概率



*基于语言模型的句子判断器，优点在于模型简单开发速度快，缺点在于对于长句有先天性劣势（长句因为概率相乘，几乎总是比短句的概率要低）*

### 3. 附加题：基于模式匹配的对话机器人

主要思路为模式匹配：

1. 根据字典里的模式（pattern）对saying进行匹配，看是否有匹配的pattern
2. 找到匹配的问句，提取匹配的字符
3. 从待选的回答里面随机选取一个，用匹配字符替换
4. join成回答输出

匹配规则的样例：

>rules = {
>    "?*X hello ?*Y": ["Hi, how do you do?"],
>    "I was ?*X": ["Were you really ?X ?", "I already knew you were ?X ."]
>}

根据这样的样例，?X, ?Y, ?*X处可以匹配任意词语或短句实体，并且将匹配的实体替换到任一回答中，然后输出。

其中的一些关键函数有：

① 判断一个token是否是匹配符

② pat_match函数，输入一个pattern和一个saying，返回其中的(匹配符+匹配词)组合

③ pat_match_with_seg函数，使pat_match函数可以匹配(多变量匹配符+多个匹配词)

④ substitute函数，根据匹配组合，将response中的匹配符替换掉，变成回答

⑤ get_response函数，根据rules list和saying，返回response的最终函数 





[返回目录]( https://github.com/SimZhou/NLP_Assignments )
