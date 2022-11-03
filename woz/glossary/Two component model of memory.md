# 记忆的双组分模型

原文：[Two component model of memory - supermemo.guru](https://supermemo.guru/wiki/Two_component_model_of_memory)

## 模型概述

长期记忆的双组分模型断言，两个相互独立的变量足以描述人类大脑中[原子记忆](https://supermemo.guru/wiki/Atomic_memory)的状态。

- [稳定性](https://supermemo.guru/wiki/Stability)（S）决定了在未被干扰和未被提取的情况下，记忆可以保持多长时间

- [可提取性](https://supermemo.guru/wiki/Retrievability)（R）决定了在给定时刻，记忆可以被提取的概率

## 生物学功能

我们相信，该模型体现出为了阻止新皮质网络中灾难性[干扰](https://supermemo.guru/wiki/Interference)的进化。记忆[稳定性](https://supermemo.guru/wiki/Stability)将降低突触权重的变动，并阻止很有用的记忆被[遗忘](https://supermemo.guru/wiki/Forgetting)。另一方面，[间隔效应](https://supermemo.guru/wiki/Spacing_effect)保护记忆免于在频繁接触中达到过高的[稳定性](https://supermemo.guru/wiki/Stability)（参见：[间隔效应的结构与分子机理](https://supermemo.guru/wiki/Structural_and_molecular_mechanisms_of_the_spacing_effect)）。

记忆的双组分模型消除了可塑性-稳定性的两难问题

## 起源

在记忆研究文献中，「记忆强度」这一定义不明确的术语通常代表稳定性（S）或可提取性（R）。这导致了大量混淆，并延缓了记忆研究的进展。在 [1990](https://supermemo.guru/wiki/Optimization_of_learning) 和 [1995](https://supermemo.guru/wiki/ANE1995) 这两篇论文中，我们已经从理论上证明了这两个变量——[S](https://supermemo.guru/wiki/Stability) 和 [R](https://supermemo.guru/wiki/Retrievability)——足以描述记忆的状态。

[Bjork](https://supermemo.guru/wiki/Robert_Bjork) 的独立研究 *New Theory of Disuse*（1992）使用了类似的术语「储存强度」和「提取强度」。另见：[约斯特定律](https://supermemo.guru/wiki/Jost‘s_Law)。

要了解模型的发展历史，请参阅：[记忆的两个组成成分](https://supermemo.guru/wiki/Two_components_of_memory)

## 意义

该模型可用于[长期记忆的分子与结构性质分析](https://supermemo.guru/wiki/Modelling_molecular_and_structural_long-term_memory)。

[SuperMemo](https://supermemo.guru/wiki/SuperMemo) 的 [SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)的实现和实践结果证明了双组分模型的正确性。该模型和算法使人们可以定量研究记忆。例如：[人脑能容纳多少知识](https://supermemo.guru/wiki/How_much_knowledge_can_human_brain_hold)？

该模型提供了支持[祖母细胞](https://supermemo.guru/wiki/Grandmother_cell)理论的证据。参见： [祖母细胞的真相](https://supermemo.guru/wiki/The_truth_about_grandmother_cells)

本[术语表](https://supermemo.guru/wiki/Glossary)条目用于解释《[间隔重复的历史](https://supermemo.guru/wiki/Problem_of_Schooling)》（2017）作者：[彼得·沃兹尼亚克](https://supermemo.guru/wiki/Piotr_Wozniak)

[![SuperMemo: Changes in two variables of long-term memory: retrievability and stability](https://supermemo.guru/images/thumb/5/57/Memory_status.jpg/500px-Memory_status.jpg)](https://supermemo.guru/wiki/File:Memory_status.jpg)

> 图：示例[知识片段](https://supermemo.guru/wiki/Piece_of_knowledge)的记忆状态随时间的变化。横轴表示跨越整个[重复历史](https://supermemo.guru/wiki/Repetition_history)的时间。顶部面板展示了[可提取性](https://supermemo.guru/wiki/Retrievability)（为了便于分析，进行十次方变换，R^10）。灰色的可提取性网格标记了 R=99%, R=98% 等标签。中部面板用深蓝色展示了[最优间隔](https://supermemo.guru/wiki/Optimum_interval)。复习日期由蓝色垂线和浅蓝色标签标记。[最优间隔](https://supermemo.guru/wiki/Optimum_interval)的末端对应的 [R](https://supermemo.guru/wiki/Retrievability) 为 90% 左右，由红色垂线标记（仅当实际复习[间隔](https://supermemo.guru/wiki/Interval)大等于[最优间隔](https://supermemo.guru/wiki/Optimum_interval)时）。底部面板可视化了[稳定性](https://supermemo.guru/wiki/Stability)（为了便于分析，以 `ln(S)/ln(days)` 的形式展示）。该图表指出 ，[可提取性](https://supermemo.guru/wiki/Retrievability)在最初几次[稳定性](https://supermemo.guru/wiki/Stability)很低时的[复习](https://supermemo.guru/wiki/Repetition)中下降得很快（指数型）。然而在第 7 次复习后，经过十年时间，可提取性从 100% 只下降到了 94%。所有的数值都来自实际的复习历史和[记忆的三变量模型](https://supermemo.guru/wiki/Three_component_model_of_memory)。