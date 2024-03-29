# 对于卡片生成任务，如果提供了充足的上下文，大型语言模型（LLM）可能会表现得更好

原文：[In prompt generation, LLMs may perform better with ample context (andymatuschak.org)](https://notes.andymatuschak.org/z5LQFLXHFLrb4nYAtLrB3JBzNyJng8fYHVJYN)

许多人试图创建系统，[使用机器学习从说明文中为简单的陈述性知识生成优质的间隔重复卡片](https://notes.andymatuschak.org/z2DY7qsP5iHsiA5hxUHheV8hu7Xe96vdGyYX)，这些系统往往会对高亮内容进行处理。你选择一段文字，然后让模型根据所选的内容生成卡片。但是，除非所选的内容是一个孤立的、明确的陈述，否则模型通常需要更多的上下文来理解如何生成优质卡片。比如，你如果从教科书中选择了一句话，模型就需要对教科书的层次、已经介绍过的内容，以及观点的框架等方面有所了解。为此，我发现在目标文本周围提供几千个上下文相关的词元往往会有所帮助。

从某种角度来看，这样的上下文信息就像是在告诉模型，什么样的卡片才符合用户的需求；这也和另一种观点相吻合[对于卡片生成任务，大型语言模型（LLM）经常需要额外的提示来确定需要强化何种角度](https://notes.andymatuschak.org/zomoPzCNzSi5GqtfTeVWgm7RjmiArjS8vvM5)。

## 实例

```

<context>设想一个质量为 $m$ 的粒子，被限定在 $x$ 轴上运动，同时受到某个特定的力 $F(x, t)$ 作用（参见图 1.1）。经典力学的主要任务，就是求出粒子在任何特定时间的位置：$x(t)$。一旦我们得知了这个，我们就能算出速度（$v=d x / d t$）、动量（$p=m v$）、动能（$T=(1 / 2) m v^2$）或者其它我们感兴趣的动力学变量。我们如何求出 $x(t)$ 呢？我们应用牛顿第二定律：$F=m a$。（对于保守系统——也就是我们只会考虑的那种，幸运的是，它们也是在微观层面上唯一存在的类型，力可以表达为势能函数的导数，也就是 ${ }^1 F=-\partial V / \partial x$，于是牛顿定律就变成了 $m d^2 x / d t^2=-\partial V / \partial x$。）这个结论，再配合适当的初始条件（通常是在 $t=0$ 时的位置和速度），就能确定 $x(t)$

而量子力学处理同一问题的方式截然不同。在这种情况下，我们要找的是粒子的波函数，$\Psi(x, t)$，我们通过求解薛定谔方程得到它：

$$

i \hbar \frac{\partial \Psi}{\partial t}=-\frac{\hbar^2}{2 m} \frac{\partial^2 \Psi}{\partial x^2}+V \Psi

$$

其中，$i$ 是 -1 的平方根，$\hbar$ 是普朗克常数，或者更确切地说，是他的原始常数（$h$）除以 $2 \pi$：

$$

\hbar=\frac{h}{2 \pi}=1.054573 \times 10^{-34} \mathrm{~J} \mathrm{~s}

$$

薛定谔方程在逻辑上与牛顿第二定律的作用相似：给定适当的初始条件（通常是 $\Psi(x, 0)$），薛定谔方程就能确定未来所有时间的 $\Psi(x, t)$，就像在经典力学中，牛顿定律决定了未来所有时间的 $x(t)$。$^2$</context>

<target>薛定谔方程在逻辑上与牛顿第二定律的作用相似</target>

<hint>怎样</hint>

```

有 <context>：「**问题**：薛定谔方程在力学中作用，和牛顿第二定律有何相似之处？**答案**：只要有合适的初始条件，两者都可以确定系统在任何时间点的状态。」

没有：「薛定谔方程如何与牛顿第二定律相似呢？**答案**：薛定谔方程描述了量子状态随环境的演变，就如同牛顿第二定律描述了物体受力后的加速度变化。」

前者更贴近原文的语境。