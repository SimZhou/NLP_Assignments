## 第1节 基于语法树和概率的AI模型

这一节主要学习了：

### 1. 基于语法树规则的短句生成器

> 基于语法树的短句生成器基本思路是通过预先构建的语法树，以及词库，对一个固定语法不断递归查找最终生成一句符合该语法的短句

  ![语法树例子](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAT4AAACeCAMAAACcjZZYAAABDlBMVEX///+tyclsmZnv9vbO3t7l7u48fn77/f32+voAPIFci4tolpb2+vj0+fmxzMza4uvf7+fm6/EAaWkAJHTF1tYAMHq52McAP4Hx8/YARYUASYgAFW9ti7Dp8fFFgoLu9vIAKnYAYWEITorG0uDc5+cmdHSSup8AIHKwwdRqqILN2OTa7OPCyddJbJsAN3yWtLSDqqqqz7oAAGnF4NKPnbiCuZrL4tadu7sAVVV9oqJQonZap355k7SnsscACmxksYqNw6efwapXeqRVbpoqWZAAcx4vl2Jtg6c6ZJaEupw8nWxksouKmbaos8cLj1NPdqJylbhionpFmWpSmW2azrR4uZd7rIsAAGsAikqcp78fPIo8AAAQN0lEQVR4nO1dC3uiyBItXzQqEfCBaBSiiA/QqPHB+MjEGK8abzK5ycbs+v//yG3M7E52ghEUJc54duN8MUAXx6qutqqrADjiiF8ZvNMCHDKUm9G07LQQBws06rPNc6elOFiQ2RQNtNNSHC6USqGQclqIgwWpANB/Sk6Lcaggs0OleHG03k1BDyuVotNCHDJIpwU44rcFQr4cclqIw8RJVOsQYZnIyMFqyOe0NAcE0uuqEZlwQHtlzRPV3HJG7mjRI4kfg/RGq0I4HKi5cj//KR2qBuWwXAt5005I9smBcl6sY3IA6xi50tsiMueqBQlZqEW9nn1K94mBvUOoJghCsBbyecz4CU/aqwUDguDWcrmTnYv3eYE8vmg1GCAEtyvns7rAS+eitYBOuivn+e0Wh9gMtU6AkANadCsN8nlDbmzM7mrIQ/4mKxyfqxqQw0Q15LXL9HJRLRgOC/q8adMVPyXS+hLkC9FxRXcxZ3lD1UA4I+CP5ZfTwzReyuG1m1sL7XrZgQcK4KVPNfprfF1BObyUkwl9ikf7uiFERqsdfVBX9NAXiR63W/OmHVhg6H69FtT2P/CvhAO2YB4B4oHked6Jm+B5TB6P8OiHmSumL/qgXPCp08jp1IE7WGRJmDxIhUjBf5DZEvbsjFYifL8C5KkDEXc6wUJckvwkDCv7H3170P7UlMb0TWnp1InPv7KgCyD5y0pl4sDoW4OO0aP/xfj+ecLvSK728mExAek8EZ+yTgy/LTB9SuwMax/pzNzNZrNlrH00f5jf5OhTGoZ/8qmpUwLc4HlPOjtI1cPgJR74MqIVpwRgFV2IA175HXGEo/B6HR39oGMGpEsWBCLkjOtLR93hQEcmqgca//PVZHcOkNct1/adoUU5TSDcrjQCMlcNEMGDSxEjb5D4mzVfjQjuUQXS3pog1N6kMrEeCoFa7nBym2RIIFxvxD0JCYK2DxtGaS1IBN5n2UlvFatjyFQm1Gl4qnLgncfwusO1nUfqa0K4E12lZVgJZaHqqCszgZw7YzzXeaoZIbqzYUlXMENo79TuJ3g1IuMOfd7sekiWXastJCpkqjvJslXDmY7JjwaFOmG5urvPcXOktfB7q/03fLWM21778YUC4cBatfvpHA2fE7J2zq6RwysUExKReE1hl/ngZQlBdEKb+FQy2hGI2mfZaoSiAqGZdA1vFzVbYLkeqW6xHjnJaQEh6PI57o6RJghRK1LkqnJwKxtOawEiYMNqGH8GRKDmsDv2dCwLQLq2ysGGal7b1pE5rWbXpY444mDAxs8Kye/xZL5pKqlxOgE+sV2V7jAFcNPf6hJvpGET5eJZpOBERon1l6Gf5EEp81D2m0rnRs4knT66rAAq02VWsR5PL8fxPduTBHiVpujn2aw9n4clsH4J2DP6bjrMQtNvSoDCcMomy8r5MNEk/6yMsjcJy3KjAl0e2bPcKAwrWJqin+WnTtF3fpldSIUimzSl/l+Lw/6onOpDMcsWWCmJ+tZzccNF6s7ySSukeehny8VYNjFyoHST9SugxKRsf9FU6KQpAU6LdNJfrixAidMRXspuQl95am4sc9KcY+1TFCcymmxs0vQPyemdNGLp+L2ZUy6K0P9avowXK0Pygi8n0QaZ4JPY1KZV36s0xZg9V7MK/nKxwA6D7Q8lIO9MGdSCBhL/LIZNHi1I9h6VN9hAVLRr18xSGpa+tOlyRxxxaLBcFAR6DnaLpQdpZ+osHXXlHN1HtC5I+h6kmxCEzQMdOffGp/4kxzJoVROE1TmS3cMyfa5w7QRCcmdTkXOBDU/8F06iHeJ7yDQXCsiBqkOhP4v05QhiaXyomnFtNmBO2DpenVsG7N9MAshbleVOyAEGLdF34g7/k6hJC/JGFpwTtpqsyFAnIxvlLNMhM/k6u2GFPi1TffsBR8PBDSzYE9icPq8mh90fpAO9VSLs3nn12FuYp88rB35ymkgLW487e4TNZk1f1C0Hamvr3U5CeFLc394is/T53LJBgtUXJKxasIewvnI5yVUFwfRGjZNcbW97i8zRhzS5ZmxzUdltzVis0of0tJxgNS3nCy1zeTvflGCKPi8RWDknk1XZmgX/PAV8BH2TmhyMbuQQSO9rJnmndmyCPs8bf2sEX8CSDxbM0oedrCxrW01jvlAwjDV3iyuswXr6tC/VdYd4w0Hz7lQ2dTeeqr4jyI6vE9hd4yvZcCHDi6+V0NRCwIL9mmtb4LNVZ0IbrvGP2CFE8eO/6/UxOmiWVwx1Rq+coc0F31XDd5n3EigYfw+2bY8SBcu2o1g+mgNX//iQxcVrFHpyxw4NhZicSjC8MTXc2PDdwXsJkslKsvKdtoctez9n4yxkm9tdYwW4bxw3vx1Q8FzijI9A02kWAd+fDJvsnWEivR8fQeoGpMlEgmZz0iwOjcL3TKslwuz5pQ2Nl5aInud4PO4FE9e6nb8fOrsAOl6Gu8klSPEtC3qn8RSMFlCcpGiYLCaXi4lthWbMTOS6zLxdHzDdtuERdIQtKDCplM+aeomyAfrDSjE15GOLRYy8mRYLqWbc4LinBteDvxqNRzQT68/cnOmhxpyZ12+f1W8G9DUBVZrNipQsbp0AH6VG0nQhnRdTCShMFpFmKrvdBX+A6urGyzUeW/nSreERd1ll1OezCgybtHEmuP/Axh8mxThArHhzCX5F8b8/Tn3Bg8EMqBdQr7sDZpxXYV7Kv3THhsar0zdtTqeT5BBGWxazj5rFbGXRnwB5SkdoNskW/dtd8Ade6as3StQKF8KPsqNRls4WYbqSvgr0IxMpBiii6PRJhvSVsK1i+sQXdSaqAxHUJ7WlAqVi+loG9C30/HOlyRel7em7g4fIYlEB9pSPKGyCvbePvjHDPWP6Gl1ubEhfucACXygvYtPYHZ01dh1T4OM3MB1lKzBdQEFSIgZ++Cqfn2PXIZaYcbtb4rrcE6M+cU8q161/e09fIhKL9aGceEgqMEpud4+JPtAXTTY5TaTgQqFj9GVkuwu+gaoiCigEKme8fln2AcEvisIjyVj79EPwDykp2MWQwCNk5GFQA8+tom7BKkc1UJtj8Myrv7Qb1Pv10PcGJHQZv7Jbet7v8vGSsuyuojdX2e6CG6LiREeSXwfskb3NgEx99/TZnSu0twzQW/0gxL9T+GQzNxK0+zt5wL4LRjthQgt+CTiRiQMfYYY+t930BW0KMXlrGUFb3kHI/UVw7T2hfsj0eWvhgPYmYI/1UNhrIu5w6dNT54F31VKkXtrq2mOF+kHSh3I1QqimDSc7j16NtDcGD48+5KsKxIfBak9UL1zfixUfGn2YO9lEoP8kGgwHXLvf3HZQ9Hk0Imy6ShBF3V8Crh2ngg+HPp8mZ6wmmKKdDLHT1cyB0OdzEfJm1alevKrenSdxiD5rmVmvvldy4y8VyNuRiV21SDDloGx/9oG1C3q37Xl/Ev3sbU6OWAU9SLr6UTEbwMK1/g6A8hs9Ehjxrz+Oov8nC/a16qyTYs/80YnCMg7Of2XZmPUsZPniEopfLZ+2Ftx1G1C7cS2Ceq2qYptriMAY5zMB7mJTPd1rD8Rxnfkvd00Bc70i//wWdCx5CcAuiucsWbSuRuVYgsf0ofuFBErx/p5e2NKoul5qdxnqL+65xcwa3evGmGvMYd5YcXT/YVTu20bfjBO/cYM8022U1uyCwLibLCrA+1M3BZ4930D7RsOU9BUq07uYdB+5S2TvCnbU3KE2N2OoGYj56wbWxMYz4F+M91mAnq9URib3apjAlSheAZO/brW5lSP+g8SiGGeLcWDPWH6DMvVykh79r8Ce0TDp3z/gFzBXWL8G+ZY6Z6gupm/QfqUPbuf5VUf3pzA5t52+urhytvgHUmQ0OscMAr0hfdh2z8+W9KXuh7bRV+LUcRsrHPPCdJnekr72f5hVR09GQNtIXxu7Diav9pjbtcY7mfJ8f8TGUw9fN6PvnIXpBQyn/XPlsqJ3qjizgz5xUG9woALFYN0bYD3A9rzakvR9aoptm2/adWo5cHuw3nXou894iaSbkoTYuHUR9O7QbBlOigtF7xZN0yDZu59N1TcF4H+p3vp53Fn0Y5/xcdTi6yYEapXb/TSwT//3Dq+jDW7R1l9YUbXqZEM72/O8lpCWt7yAK1yrhTXn2tnZHrCyBD681emvVT++oFHZ2X7gLH2ebbTvB21eYYcNbj+Es/SdEBufqteU/YjvhOSgI5O4w/RtbLyhnyoakZapOTAFOkxfZrPzfPL7nhao9mX/Dyh0lj5yI+1LBzOGU106GN5VCdwqOEzfBq4DVcMrSx1zgT07Yafps5zsDsmdj3Jg0Q8qmHcAp+mz6C9zwrpCXOT6mF970dn3bPEvkIK1O9XMTG6e2v4s+MTZ/t0WbddkjwPfIT8u6XdAe01F8A6ArvUKm9dIKrUyoKoa1w/D946N5CUqrym5uS8DKu44gni7MoC/M3AD+Ie3ZUKYmRscVR8Ynowip0tG+FO+uCYqf+6nUXLHvSnz824LxKtuHVCr1xPbrTm12wEBdcfiYI7ZqXdbA2o277YH3xpo3sVvDHotgOfuFaJ6vatrw7OL2WlTf4Dy8Ixf13A0m52g0a7pe6bm9VYDdRn1GQYcV9q9MdefYdZgujAWuT+osdi4Va/wyKjUntfRGBotVL9t1ameMX3DZnGElJiyKJCpNQ/PjTenxZ3Tx0D76jGfL3FQv+1y66r77QAeoyeKvUYemBKlZzTFOXRv8y/1lgqPMCjl8/MxJtmQPj6W6sfoyxGwkfX0XZazO6evgeeiEgUNqn4L9X3Sx5RAfaT0jCae+7DSt0VMXw+uORDbXQZuDem7Px8Os33pnJRMaN8ChhFTDZk3R36WH1PcUx5bzdNgVtoHffU6dEXfE9a47iPVBeZFnKnqOD9GcxW6IM5ux/jXl5kRfUhvz36ZYKfx7Fd+HX1nC6BPd97WeJnE1F9EBvbphhEnqt9drigC+rFOYdB3gT6Anst9cOTB4Z8Grf92t/m4lKQte6kOF9R2XxQP88HnnwA+k6EAZ5PXnxYhwdxxtc/4QELn4TXZOrrmaBTu0yJtVvvWNi78LeEzmRY+0mcIs1tiXEf6jGCavuMjCI3gMWm8oeBu5ThQmN1RdKTPEB6TmxJyR/qMYFb77Hm0yC+HE5PrvpzJ44444ohdo8VctxlADFybqrJgWm9+UY37u/5OKKmMOGPULspzwBjFWpH+LmJEEYmAREoFEUPvdcksO7D+5igx+cF48PytkW/Uez0DdWpddTmYX109iWPMF3MF4159Nqf0t4/06fS1r5B4Bfn6E4I/3ukf9aRSKvOI/9Xpe/H14Bu056B28Ttto70MvxcwfY0epdP3/Mf1df19Sp9pfeMaeUCPf9M3g/YAGo/X19yRPnjU6VtqHzejqN67XIk4B2qM/1O/iX8BV1rS1xgA5pKZq1dOSPypUBc5ZjAQS1xDVUuPBrXW9d6jCtzj/EnMXw04sQ4DYPQG+48lRvzsBaV7Alr+//3l3R/1dxHVFf/9Z2c3fx4aUH3X+8SOOOIIJ/B/PIjU3IcKWPQAAAAASUVORK5CYII=) 



*基于语法树的句子生成器，**优点**在于速度快，需要数据量少，开发快，可以迅速开发出适用于某个领域的生成器，而**缺点**在于依赖预先制定的规则所以通用性差，可扩展性也较差。*

### 2. 基于概率（语言）模型的句子判断器

> 基于语言模型的句子判断器可以运用概率模型计算一句短句在某个语料库的基础下产生的可能性，其中包括1-gram，2-gram，n-gram模型	

#### 2.1 1-gram模型

1-gram模型假设一句句子的每个词的出现都是独立的，因此一句话产生的概率即为所有词在语料库中出现概率之积：

 ![](http://latex.codecogs.com/gif.latex?\\P(sentence) = P(w_1 \cdot w_2 \cdots w_n) = \prod_{i=1}^{n} \frac{count(w_i)}{\sum_{\forall k}count(w_k)}) 

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