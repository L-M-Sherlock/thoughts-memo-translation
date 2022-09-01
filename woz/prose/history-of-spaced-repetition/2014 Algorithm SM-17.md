# 2014：SM-17 算法

最新的 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 算法，可基于它的设计，用来总结自己的系统发展史。它也可以用来编写[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)的反事实历史。如果没有恐龙，人类可能不会出现，或者可能会有不同的外观。然而，即便进化树上恐龙一脉全部消失，人类在哺乳动物这一脉上的演化并不受太大影响。

以类似的方式，我们可以在[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)和[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 的出现中展示一个看似决定性的关联事件链。这可以用来证明 [Biedalak](https://supermemo.guru/wiki/Biedalak) 或 [Murakowski](https://supermemo.guru/wiki/Murakowski) 对[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)的历史比 [Ebbinghaus](https://supermemo.guru/wiki/Ebbinghaus) 更重要。Anki 比 Pimsleur 更重要。[Gary Wolf](https://supermemo.guru/wiki/Gary_Wolf) 比 William James 的影响更大。

尽管如此，[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)的影响力尚未达到顶峰，仍处于早期阶段，且受到各种外力的左右。具体而言，不容小觑的竞争对手层出不穷，唯有锐意创新，[SuperMemo](https://supermemo.guru/wiki/SuperMemo)才能维持它在间隔重复的核心地位（比如[神经创造力](https://supermemo.guru/wiki/Neural_creativity)）

以下是我如何使用为这篇文章所写的历史构件来解释整个[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17)：

- 长期保留的关键是[计算最优间隔](https://supermemo.guru/wiki/The_birthday_of_spaced_repetition:_July_31,_1985) (1985)

- 由于间隔取决于[记忆复杂性](https://supermemo.guru/wiki/Memory_complexity)，我们首先需要将[项目](https://supermemo.guru/wiki/Item)分为不同[难度](https://supermemo.guru/wiki/SuperMemo_1.0_for_DOS_(1987))类别 (1987)

- 我们通过[绘制遗忘曲线](https://supermemo.guru/wiki/Employing_forgetting_curves_in_spaced_repetition_(1991))找到最优复习时间，并找出[保留率](https://supermemo.guru/wiki/Retention)下降到可接受水平以下(1991)的时刻

- 为了在稀疏的数据中找到最优时间，我们需要使用近似手段，有助于得出[遗忘的指数性质](https://supermemo.guru/wiki/Exponential_nature_of_forgetting) (1994)

- 由于[遗忘](https://supermemo.guru/wiki/Forgetting)的速度取决于[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)，整个算法的设计必须以[双组份记忆模型](https://supermemo.guru/wiki/Two_components_of_memory)为核心（1988）。缺乏对这一模型的考虑可能是竞争性[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)算法的开发者所犯的主要错误，例如一个利用[神经网络方法](https://supermemo.guru/wiki/Neural_networks_in_spaced_repetition)的间隔重复算法（1997）

- 双组分模型的关键力量是使[计算复习时的记忆稳定性增长](https://supermemo.guru/wiki/SuperMemo_Algorithm:_30-year-long_labor) (2005) 成为可能

- 该算法必须通过收集重复的数据来建立记忆模型。它必须能够[适应现有信息](https://supermemo.guru/wiki/First_adaptable_spaced_repetition_algorithm:_Algorithm_SM-4) (1989)

- 在有数据之前，从[通用记忆公式](https://supermemo.guru/wiki/Search_for_a_universal_memory_formula)开始是有帮助的（1990）

- 更多小调整和改进可以带来[天壤之别](https://supermemo.guru/wiki/First_data-driven_spaced_repetition_algorithm:_Algorithm_SM-8)（1995），例如，遗忘后间隔、[绝对难度](https://supermemo.guru/wiki/A-Factor)、快速多维回归，等等。

- 需要实现[通用度量](https://supermemo.guru/wiki/Universal_metric) 以在未来算法中微调优化参数（2018）

就这样，一步一步，[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 傲然矗立于[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)的进化树顶端。