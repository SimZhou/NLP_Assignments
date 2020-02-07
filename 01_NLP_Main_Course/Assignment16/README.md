## 第16节 深度学习高阶知识——强化学习

这一节学了：强化学习。

目录：

- 概念
- Bellman等式
- 动态规划
- 蒙特卡洛
- TD
- Q-learning 和 SARSA
- Deep Q-Network 和 Policy gradient



### 1. 强化学习概念

强化学习是一个 Agent 与 Environment 相互交互的过程

​	   state s∈**S**

​      action a∈**A**

​     —————— 

​    |					 ↓

Agent		Environment

​	↑					 |

​     ——————

​	  Get reward **r**

​    New state s'∈**S**

其中重要的概念有如下：

- States状态空间：包含所有可能的状态

- Actions动作空间：包含所有可能的动作
- Rewards奖励：R（s, a）在不同的状态采取相同或不同的动作都有对应的一个奖励
- Values期望值：总奖励
- Policy：策略，代表在某个状态s的最佳动作action
- Episode：通过一系列动作经过一系列状态后，获得的一个序列，例如：S1 A1 R2 S2 A2 R3 S3 …… ST（终止）

**Model Transition（数学描述状态转移）**

![](http://latex.codecogs.com/gif.latex?P(S^{'},r|S,a)=P[S_{t+1}=s^{'},R_{t+1}=r|S_t=s,A_t=a]=\sum_{r\in{R}}P(s^{'},r|S,a))

期望Reward: ![](http://latex.codecogs.com/gif.latex?R(s,a)=E[R_{t+1}|S_t,A_t=a])

**Value Function and action-value(Q-value) （数学描述奖励函数）**

Rewards: ![](http://latex.codecogs.com/gif.latex?G_t=R_{t+1}+\gamma{R_{t+2}}+\gamma^{2}{R_{t+3}}+\gamma^{3}{R_{t+4}}+\cdots)

State values: ![](http://latex.codecogs.com/gif.latex?V_\pi(s)=E_\pi[G_t|S_t=s])，是在某个状态s下，Rewards的期望值。适用于路线不唯一且具有随机性的步骤。

Q-values：![](http://latex.codecogs.com/gif.latex?Q_\pi(s,a)=E_\pi[G_t|S_t=s,A_t=a])，是在某个状态s下，已经采取动作a后，Rewards的期望值。

A-values：![](http://latex.codecogs.com/gif.latex?Q_\pi(s,a)-V_\pi(s))，代表了采取步骤后，所获得的奖励与平均值的差值，如果它高于平均值（A-value＞0），那么该动作应该来讲是比较好的选择。



### 2. Bellman等式 - 奖励函数的计算方法

Bellman equation是求解每个状态s的V值的过程，只要求解出每个状态的V值后，我们就可以通过每次都选择最大V值来获得最优策略。

**Bellman equation (1):**

  ![](http://latex.codecogs.com/gif.latex?\begin{aligned}V(s)&=E[G_t|S_t=s]\\&=E[R_{t+1}+\gamma{R_{t+2}}+\gamma^{2}{R_{t+3}}+\cdots|S_t=s]\\&=E[R_{t+1}+\gamma({R_{t+2}}+\gamma{R_{t+3}}+\cdots)|S_t=s]\\&=E[R_{t+1}+\gamma{G_{t+1}|S_t=s}]\\&=E[R_{t+1}+\gamma{V(S_{t+1})}|S_t=s]\end{aligned})

可以看到，这是一个递归，所以要求解V(s)，只需要从末端反推就可以。

**Bellman equation (2):**

![](http://latex.codecogs.com/gif.latex?\begin{aligned}Q(s,a)&=E[R_{t+1}+\gamma{V(S_{t+1})}|S_t=s,A_t=a]\\&=E[R_{t+1}+\gamma{E_{a=\pi}[{Q(s_{t+1},a)]}}|S_t=s,A_t=a]\end{aligned})

通过求解max(Qa_1, Qa_2, Qa_3,...)来获得当前步最佳策略action。

 ![](http://uricc.ga/images/2020/02/06/_20200207001807.png)



### 3. Dynamic Programming - 奖励函数的求解方法

**Value iteration 值迭代**

具体做法是：先对所有状态初始化一个值，然后使用Bellman equation![](http://latex.codecogs.com/gif.latex?V(S_t)=r+\sum_{P}{P(S_{t+1}|S_t)}V(S_{t+1}))进行值的更新，然后不断迭代，直到收敛 |W_t+1 - W_t| ≤ δ：

![](http://uricc.ga/images/2020/02/07/Bellman-iteration.png)



其中有两种做法，一种是一次计算，同时更新，另一种是将更新后的值作为下一个格子的输入值进行更新。这两种做法都是可取的。

**Policy iteration 策略迭代**

具体做法是：先对所有状态初始化一个随机策略，然后使用第二种Bellman equation，进行最佳策略的更新，然后不断迭代，直到收敛。

![](http://uricc.ga/images/2020/02/07/Bellman-iteration2.png)



### 4. Monte-Carlo Method - 奖励函数的求解方法2

![](http://uricc.ga/images/2020/02/07/_20200207231312f43e8b578cd59838.png)

正常情况下一般来讲，各状态之间的Transition Probability是未知的。

蒙特卡洛是用随机模拟的方式，来估算每一个状态的V值的方法。

 ![](http://latex.codecogs.com/gif.latex?S_0\xrightarrow[r]{a_0}S_1\xrightarrow[r]{a_1}S_2\xrightarrow[r]{a_2}\cdots\xrightarrow[r]{a_{t-1}}S_T\;\textcircled{1})

 ![](http://latex.codecogs.com/gif.latex?S_0^{'}\xrightarrow[r]{a_0}S_1^{'}\xrightarrow[r]{a_1}S_2^{'}\xrightarrow[r]{a_2}\cdots\xrightarrow[r]{a_{t-1}}S_T^{'}\;\textcircled{2})

…… 

通过不同的模拟，我们可以得到不同的路线，而每次模拟都可以算出路线上每个状态点的![](http://latex.codecogs.com/gif.latex?G_t)值。

而真![](http://latex.codecogs.com/gif.latex?G_t)值的计算有2种方法：

**① First Visited - 每个状态在每条路径只计算第一次** 

![](http://latex.codecogs.com/gif.latex?V(S_1)=\frac{G_t^1+G_t^2+G_t^3+...+G_t^n}{n})

**② Every Visited - 每个状态碰见几次就是几次** 

![](http://latex.codecogs.com/gif.latex?V(S_1)=\frac{G_t^1{(S_1)}+G_t^2{(S_1)}+G_t^3{(S_1)}+...+G_t^n{(S_1)}}{n})



总体来讲，蒙特卡洛方法bias低（为0），variance高（由于随机采样）

DP法bias高（需要估计概率值），variance低（不需随机采样，直接计算）



### 5. Temporal-Difference Learning - 奖励函数的求解方法3

- Temporal-Difference Learning是DP与Monte-Carlo的结合。

即，一部分用蒙特卡洛采样解，一部分用Bellman Equation解。

![](http://latex.codecogs.com/gif.latex?\textcircled{\,}\longrightarrow\textcircled{\,}\longrightarrow\textcircled{\,}\longrightarrow{V(S_{t+2})})

例如，前面几步用蒙特卡洛，后面几步用DP。（圆圈表示采样）

TD相较于蒙特卡洛，bias升高（需要用概率估计值），variance降低（减少了随机采样）

TD相较于蒙特卡洛，计算更快；相较于DP，不需要知道Transition Probability。



### 6. Q-learning and SARSA

Q-learning: 计算出不同的Q后，Value取值按照max()取

SARSA (State-Action-Reward-State-Action): 计算出不同的Q后，Value取值按照policy取



### 7. Function Approximation (Deep Q-Network)

Deep Q-Network的思路是使用神经网络来拟合Q函数：f(S1) → Q值

该神经网络的输入就是State，输出就是Q-Value

![](http://uricc.ga/images/2020/02/07/Annotation-2020-02-08-020129.png)

（例如，Atari游戏中，输入的就是图片像素，使用CNN提取特征）



### 8. Policy Gradient

给一个函数，这个函数可以拟合出最佳move，即π的学习。

![](http://latex.codecogs.com/gif.latex?maximize\;J(\theta)=\sum_{a\in{A}}{\pi(a|s,\theta)}Q_\pi(s,a))

**AlphaGo**

先通过人类棋谱学习，再通过自己对弈学习。

**AlphaZero**

棋盘输入13层的CNN提取状态特征，并且加上一些额外信息（例如棋盘中可被吃掉的目，等）。

通过自己和自己下棋，更新policy gradient中的参数。其中使用了蒙特卡洛树搜索，剪枝等方法。