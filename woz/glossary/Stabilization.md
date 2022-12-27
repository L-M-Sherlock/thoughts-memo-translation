# 稳定化

原文：[Stabilization - supermemo.guru](https://supermemo.guru/wiki/Stabilization)

**记忆稳定化**（缩写为 **SInc**，即 **stability increase**）是指由记忆提取（例如，[复习](https://supermemo.guru/wiki/Review)）引起的[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)增长。**稳定化**可能也是睡眠[记忆优化](https://supermemo.guru/wiki/Memory_optimization)的结果。

[稳定性](https://supermemo.guru/wiki/Stability)越高，[复习](https://supermemo.guru/wiki/Review)时的[稳定性增长](https://supermemo.guru/wiki/Stability_increase)越慢（参见：[稳定化衰减](https://supermemo.guru/wiki/Stabilization_decay)）。顾名思义，记忆会在长期贮存中趋于「稳定」。

此外，提取记忆时的稳定性增长取决于[可提取性](https://supermemo.guru/wiki/Retrievability)和[记忆复杂性](https://supermemo.guru/wiki/Memory_complexity)。可提取性越低，稳定性的平均增长就越高。稳定性的增长期望通过**巩固曲线**描述，受记忆[遗忘](https://supermemo.guru/wiki/Lapse)的概率调节，其在不同的[遗忘指数](https://supermemo.guru/wiki/Forgetting_index)水平达到峰值（通常是[可提取性](https://supermemo.guru/wiki/Retrievability)在 30-80% 之间）。

[复杂性](https://supermemo.guru/wiki/Complexity)是记忆研究中的混淆因素。对于原子记忆，稳定性可以建模（例如，在 [SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)中）。随着记忆复杂性不断提升，稳定性逐渐失去意义。例如，如果我们考虑记忆一本书，其稳定性增长是无法衡量的，因为一本书无法逐字逐句地被完整回忆。一本书的记忆印记是一组复杂的记忆组，其稳定性可能跨越从短期到**[永久存储](https://supermemo.guru/wiki/Permastore)**的范围。

在 [SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)中，稳定性增长矩阵（SInc[]）可视作 [O-系数](https://supermemo.guru/wiki/Optimum_factor)矩阵（源自老版本的 [SuperMemos](https://supermemo.guru/wiki/SuperMemo)）在[可提取性](https://supermemo.guru/wiki/Retrievability)维度的拓展。这一拓展让算法适用于各种重复规划至关重要（[复习](https://supermemo.guru/wiki/Review)中的延迟对应较低的[可提取性](https://supermemo.guru/wiki/Retrievability))）。

另见：

- [长期记忆的双组分模型](https://supermemo.guru/wiki/Two_component_model_of_long-term_memory)

- [寻找通用记忆公式](https://supermemo.guru/wiki/Search_for_a_universal_memory_formula)

- [稳定化曲线](https://supermemo.guru/wiki/Stabilization_curve)

- [稳定化衰减](https://supermemo.guru/wiki/Stabilization_decay)

- [间隔效应的结构和分子机理](https://supermemo.guru/wiki/Structural_and_molecular_mechanisms_of_the_spacing_effect)

- [SuperMemo 算法：长达 30 年的努力](https://supermemo.guru/wiki/SuperMemo_Algorithm:_30-year-long_labor)

- [算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17)

- [遗忘后的稳定](https://supermemo.guru/wiki/Post-lapse_stability)

本[词汇表](https://supermemo.guru/wiki/Glossary)条目用于解释 [SuperMemo](https://supermemo.guru/wiki/SuperMemo_Guru)，一位自 [1987](https://supermemo.guru/wiki/History_of_spaced_repetition_(print)) 年以来的[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)软件先驱。

[![img](https://supermemo.guru/images/thumb/2/2b/Stability_increase_function.png/500px-Stability_increase_function.png)](https://supermemo.guru/wiki/File:Stability_increase_function.png)

稳定性增长函数

> 图：[稳定性增长](https://supermemo.guru/wiki/Stability_increase)函数由 [SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)计算。该函数有三个参数：（1）复习时的[稳定性](https://supermemo.guru/wiki/Stability)，以天为单位表示（左边），（2）复习时的[可提取性](https://supermemo.guru/wiki/Retrievability)（右边）和（3）记忆[复杂性](https://supermemo.guru/wiki/Complexity)，以[条目](https://supermemo.guru/wiki/Item)[难度](https://supermemo.guru/wiki/Difficulty)表示（标签为 **Diff** 的滑块目前设置为 0.8）。图中，稳定性增长在 15 左右达到峰值（纵轴）。在一些[稳定性](https://supermemo.guru/wiki/Stability)和[可提取性](https://supermemo.guru/wiki/Retrievability)水平下，函数值低于 1.0，代表[稳定性](https://supermemo.guru/wiki/Stability)下降（例如，由于集中学习而过早复习引发的[间隔效应](https://supermemo.guru/wiki/Spacing_effect)）。相对较[难](https://supermemo.guru/wiki/Difficulty)[条目](https://supermemo.guru/wiki/Item)的 61,768 次重复被用于生成该曲线（Diff=0.8）。最长[间隔](https://supermemo.guru/wiki/Interval)达到了 14 年（[稳定性](https://supermemo.guru/wiki/Stability)为 5172）

[![img](https://supermemo.guru/images/thumb/9/97/Approximation_of_memory_stabilization.png/500px-Approximation_of_memory_stabilization.png)](https://supermemo.guru/wiki/File:Approximation_of_memory_stabilization.png)

根据复习的记忆稳定化近似

> 图：[SuperMemo](https://supermemo.guru/wiki/SuperMemo) 中的稳定化函数近似。数据点、绿色和红色圆点，对应了在选定[难度](https://supermemo.guru/wiki/Difficulty)分位（Diff=0.5）下所有[稳定性](https://supermemo.guru/wiki/Stability)和[可提取性](https://supermemo.guru/wiki/Retrievability)对应的[记忆稳定化](https://supermemo.guru/wiki/Memory_stabilization)（SInc）。蓝-红曲线表示由 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 使用[稳定化曲线](https://supermemo.guru/wiki/Stabilization_curve)、[稳定化衰减](https://supermemo.guru/wiki/Stabilization_decay)和根据[条目](https://supermemo.guru/wiki/Item)[难度](https://supermemo.guru/wiki/Difficulty)更改这些函数的参数所找到的最佳拟合。生成该图使用了 54,449 个复习样本。右侧的绿色离群点表示来自新[条目](https://supermemo.guru/wiki/Item)的「污染」，因为它们的[稳定性](https://supermemo.guru/wiki/Stability)还未被准确估计。

[![img](https://supermemo.guru/images/thumb/c/c6/Stability_increase_function_approximation.jpg/500px-Stability_increase_function_approximation.jpg)](https://supermemo.guru/wiki/File:Stability_increase_function_approximation.jpg)

记忆巩固（期望稳定化）近似

> 图：由 [SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)近似的期望稳定性。该函数接受三个参数：（1）复习时的[稳定性](https://supermemo.guru/wiki/Stability)，以天为单位（在左侧），（2）复习时的[可提取性](https://supermemo.guru/wiki/Retrievability)（在右侧），和（3）记忆[复杂性](https://supermemo.guru/wiki/Complexity)，以条目难度表示（标签为 *Diff* 的滑块目前设置在 0.1 处，即简单条目）。在图中，巩固（期望稳定性增长）的峰值为 5（纵轴）。不同于实际数据，该近似被设置为永不小于 1.0。这意味着该近似函数永远不会让复习时的[稳定性](https://supermemo.guru/wiki/Stability)下降。10,130 次简单条目的重复被用于生成该图（Diff=0.1）。其中一个数据点展示了间隔达到 14 年的一组重复样本（[稳定性](https://supermemo.guru/wiki/Stability)为 5172）。

[![img](https://supermemo.guru/images/thumb/d/d7/Memory_stabilization_curve.png/500px-Memory_stabilization_curve.png)](https://supermemo.guru/wiki/File:Memory_stabilization_curve.png)

SuperMemo 中的记忆稳定化曲线

> 图：[SuperMemo](https://supermemo.guru/wiki/SuperMemo) 计算的**[稳定化曲线](https://supermemo.guru/wiki/Stabilization_curve)**。横轴以[记忆可提取性](https://supermemo.guru/wiki/Memory_retrievability)表示时间。纵轴表示稳定化，即记忆持久度的增长，以[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)增长表示。蓝色圆圈表示在给定[可提取性](https://supermemo.guru/wiki/Retrievability)下复习的[稳定性](https://supermemo.guru/wiki/Stability)增长程度。蓝色圆圈的大小取决于收集到的数据点数量。该图使用了 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 中[难度](https://supermemo.guru/wiki/Difficulty)=0.53 且 [稳定性](https://supermemo.guru/wiki/Stability)=26 [天]的 31,721 条复习记录。稳定性增长从[可提取性](https://supermemo.guru/wiki/Retrievability)=100% 对应的 1.36（SIncMin=1.36）到 R=0% 对应的 26.31（SIncMax=26.31）。[SuperMemo](https://supermemo.guru/wiki/SuperMemo) 中 R=90% 对应的最佳复习的稳定性增长为 1.86（Stab90 等价于旧版 SuperMemo 中的 [O-系数](https://supermemo.guru/wiki/O-Factor)）。表示[间隔效应(https://supermemo.guru/wiki/Spacing_effect)的增益系数等于 2.96，即相对较高，适应低[稳定性](https://supermemo.guru/wiki/Stability)。使用公式可以准确计算此数据集中的稳定化（黄色曲线）： 26\*e-2.96\*R，[偏差](https://supermemo.guru/wiki/Deviation)为 0.5069。巩固曲线以紫色展示，表明[遗忘指数](https://supermemo.guru/wiki/Forgetting_index)是所提供数据集的合理学习标准。当 R 接近 100% 时，本图的实际稳定化为 0.879，与 2074 次测量结果一致。这在图片中看不清楚，但可以通过 SuperMemo 中输出的稳定化矩阵进行调查。这意味着在[可提取性](https://supermemo.guru/wiki/Retrievability)接近 100% 和 0% 的极端情况下，稳定化曲线公式可能不准确。这可以解释为没有任何记忆是可以完美提取或可验证的完全忘却（见：[我们永远不会忘记](https://supermemo.guru/wiki/We_never_forget)）

[![img](https://supermemo.guru/images/thumb/4/4f/Stabilization_decay.png/500px-Stabilization_decay.png)](https://supermemo.guru/wiki/File:Stabilization_decay.png)

SuperMemo 中的稳定化衰减

> 图：**[稳定化衰减](https://supermemo.guru/wiki/Stabilization_decay)**是**[记忆稳定化](https://supermemo.guru/wiki/Memory_stabilization)**随着**[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)**提高而下降。取自 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 的图片展示了[稳定性](https://supermemo.guru/wiki/Stability)对[难度](https://supermemo.guru/wiki/Difficulty)估计为 0.37 的[条目](https://supermemo.guru/wiki/Item)的稳定化影响。绘制该图表使用了 25,686 条[复习](https://supermemo.guru/wiki/repetition)记录。稳定化的**衰减率**为 -0.529。稳定性可能的最大增长（SIncMax）是 3.102（当[稳定性](https://supermemo.guru/wiki/Stability) =1 时）。蓝色圆圈表示数据点（S:SInc)，圆圈越大，[复习](https://supermemo.guru/wiki/Repetition)记录的样本量越大。黄线是幂函数拟合，公式为：SInc=(3.102-1)\*[S](https://supermemo.guru/wiki/Stability)-0.529+1。该拟合的[偏差](https://supermemo.guru/wiki/Deviation)为 0.4235。

[![Uncertain course of stabilization in complex memories](https://supermemo.guru/images/thumb/0/0d/Uncertain_course_of_the_stabilization_of_complex_memories.png/400px-Uncertain_course_of_the_stabilization_of_complex_memories.png)](https://supermemo.guru/wiki/File:Uncertain_course_of_the_stabilization_of_complex_memories.png)

> 图：**复杂记忆的稳定化的不确定过程**。图中显示了以单个[概念细胞](https://supermemo.guru/wiki/Stabilization)的单一树突输入模式为例的[稳定化](https://supermemo.guru/wiki/Stabilization)、[遗忘](https://supermemo.guru/wiki/Forgetting)、[泛化](https://supermemo.guru/wiki/Generalization)和[干扰](https://supermemo.guru/wiki/Interference)的假想过程。神经元、树突和树突丝以橙色显示。图片没有显示树突丝转化为树突棘的过程，树突棘的形态随着时间的推移会发生变化[稳定化](https://supermemo.guru/wiki/Stabilization)。方块代表参与识别输入模式的突触。每个方块显示了突触在[长期记忆的双组分模型](https://supermemo.guru/wiki/Two_component_model_of_long-term_memory)方面的状态。红色的强度代表[可提取性](https://supermemo.guru/wiki/Retrievability)。蓝色区域的大小代表[稳定性](https://supermemo.guru/wiki/Stability)。在记住一个复杂的记忆模式后，[概念细胞](https://supermemo.guru/wiki/Concept_cell)在收到来自红色方块的信号总和后能够识别该模式，这些信号代表高[可提取性](https://supermemo.guru/wiki/Retrievability)和极低[稳定性](https://supermemo.guru/wiki/Stability)的新记忆。每次细胞被重新激活，活跃的输入将经历[稳定化](https://supermemo.guru/wiki/Stabilization)，这表现在输入方块中蓝色区域的增加。每次当概念细胞活跃时，信号没有到达输入端，其稳定性就会下降（泛化）。每次源轴突活跃而目标神经元未能发射，稳定性也会下降（竞争性干扰）。由于输入到概念细胞的信号模式不均匀，一些突触将被稳定下来，而另一些则会丢失。当一个突触失去其稳定性和可提取性，以及相关的树突棘被收回时，[遗忘](https://supermemo.guru/wiki/Forgetting)就会发生。当同一个[概念细胞](https://supermemo.guru/wiki/Concept_cell)可以用一个更小但更稳定的输入模式重新激活时，[泛化](https://supermemo.guru/wiki/Generalization)就会发生。当一个新的输入模式有助于忘记一些识别旧输入模式所必需的冗余输入时，就会发生追溯性[干扰](https://supermemo.guru/wiki/Interference)。旧模式的[稳定化](https://supermemo.guru/wiki/Stabilization)导致树突丝的流动性降低，从而防止新模式接管[概念](https://supermemo.guru/wiki/Concept)（主动的[干扰](https://supermemo.guru/wiki/Interference)）。在这个过程的每一端，一个稳定的、泛化性强的输入模式是激活[概念细胞](https://supermemo.guru/wiki/Concept_cell)的充要条件。同一个细胞可以对不同的模式作出反应，只要它们是一致的、[稳定的](https://supermemo.guru/wiki/Stabilization)。在[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)中，对[知识表征](https://supermemo.guru/wiki/Knowledge_representation)的选择不当将导致激活模式的可重复性差，突触的[稳定化](https://supermemo.guru/wiki/Stabilization)不均匀，以及[遗忘](https://supermemo.guru/wiki/Forgetting)。当输入模式无法激活足够多的突触，从而无法重新激活[概念细胞](https://supermemo.guru/wiki/Concept_cell)时，就会发生对[项目](https://supermemo.guru/wiki/Item)的遗忘。在[重复](https://supermemo.guru/wiki/Repetition)时，根据上下文和[思路](https://supermemo.guru/wiki/Conceptual_computation)，一个[项目](https://supermemo.guru/wiki/Item)可能被提取或遗忘。[复习](https://supermemo.guru/wiki/Repetition)的结果是不确定的