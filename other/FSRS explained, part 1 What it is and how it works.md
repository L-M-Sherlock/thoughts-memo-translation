# 解释 FSRS（上篇）：算法描述与运作原理

原文：[FSRS explained, part 1: What it is and how it works : Anki (reddit.com)](https://www.reddit.com/r/Anki/comments/15mab3r/fsrs_explained_part_1_what_it_is_and_how_it_works/)

如果你正在使用 Anki 但还没听说过 [FSRS](https://github.com/open-spaced-repetition/fsrs4anki)，那我来简单地给你介绍一下：它是一个新的调度算法，比 Anki 的默认算法更加灵活、准确。最近，FSRS 的新版本已经发布，它比之前更加精确，因此我决定写两篇关于 FSRS 的文章。

注：我并不是 FSRS 的开发者。我只是一个在 GitHub 上经常提交错误报告和功能请求的普通人。但我对 FSRS 非常了解，特别是 v4 版本的很多改动，都是我一手提议的。

## 等级 1：小白版

FSRS 采用了一个叫做 DSR 的记忆模型，全称是「难度（**D**ifficulty）、稳定性（**S**tability）和回忆概率（Probability of **R**ecall）」。如果你是 Piotr Wozniak 的话，可能会说成是「保留率（**R**etention）」或「可提取性（**R**etrievability）」。不过在他的术语中，「保留率」和「可提取性」又不是一回事……唉，要给这些概念起个好名字真不容易。

**R** 代表着用户根据某卡片的复习历史，在某一天回忆起这张卡片的概率。这个概率取决于自上次复习过去了多少天，以及 **S**。重要的是，任何**诚实**的间隔重复算法都得能预测 R，无论用什么方式（即使它不使用记忆稳定性）。否则，它不可能确定哪些间隔是最优的。 

**S** 代表记忆稳定性，定义为 **R** 从 100% 降到 90% 所需的天数。越高越好。比如，S=365 意味着整整一年后，回忆某张卡片的概率才会降到 90%。估计 **S** 是最难的部分，这正是 FSRS 的核心所在。

**D** 代表难度。不同于其他两个变量，难度没有明确的定义，而是基于一堆与人类记忆理解不太相关的启发式方法来计算的。简单说，如果你按下「简单」，难度就下降；如果你按「困难」或「重来」，难度就上升。

这个模型最初是由 SuperMemo 的缔造者 Piotr Wozniak 提出的。几年前，[u/LMSherlock](https://www.reddit.com/u/LMSherlock/)（译注：正是在下）发表了一篇论文，也用到了这个模型。

## 等级 2：完整描述，但不涉及数学

对于任何给定的卡片，FSRS 都会进行以下操作：

如果这是首次复习：

1. 根据评分——「重来」、「困难」、「良好」和「简单」，设置初始的记忆稳定性 S。这些初始值是经过特定方法优化后得到的，并作为参数传递给调度器。

2. 计算初始难度 D。这个难度完全基于评分。

3. 根据 S 和期望的回忆概率 R（由用户设置）来安排下一次复习。

若不是第一次复习该卡片：

1. 计算复习时的理论（预测）回忆概率 R。它基于两个变量：从上次复习到现在过去的天数 Δt，以及复习时的记忆稳定性 S。

2. 计算难度 D，但与第一次复习时的公式不同。D 基于两个变量：其先前的值和此次的评分。

3. 根据 D、S 和 R 来获取复习**后**的**新**稳定性估计。每次成功的复习后（用户按下「困难」、「良好」或「简单」），稳定性都会提高或至少保持不变，但在失败后（用户按下「重来」）会降低。新的稳定性估值取决于四个变量：D、S、R 和评分。如果用户按「重来」，公式会有所不同。

4. 根据 S 的新估值和期望的回忆概率 R（由用户设置）来安排下一次的复习。

## 等级 3：完整描述，包括数学

[阅读这个 wiki 即可 ¯\_(ツ)_/¯](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm)

## FSRS v4 的强项

1. 得益于通用记忆公式与机器学习的结合，FSRS 能够适应任何用户的记忆和复习习惯，例如只使用「重来」和「良好」。所以你不需要改变自己的复习习惯。

2. FSRS 让你能够自己设置期望的回忆概率 R，这使得你可以在复习压力和长期记忆保留之间权衡。

3. FSRS 允许你提前或推迟复习，同时最小化对长期学习的影响。当你积压了大量的复习时，可以选择推迟；考试前，可以选择提前复习。但**过于**频繁的推迟/提前仍然可能造成伤害。如果你选择某天不学习，如周日，FSRS 也允许你有「休息日」。所有这些都得益于 FSRS 能够准确预测 S 和 R，即使复习太晚或太早。

4. FSRS 能帮助你准确估算目前大脑中掌握的知识量。这是任何其他插件都做不到的，因为它依赖于准确预测所有卡片的 R。

5. 从标准的 Anki 调度器转到 FSRS 并不需要花上数月或数周——只需轻触按钮，卡片就可以被重新安排。不过，重新安排后的初始复习量通常较大。顺便说一下，这个辅助插件同时支持 v3 和 v4 版本。

6. 如果你一直在为「学习步伐」、「毕业间隔」、「简单奖励」等参数的最佳值而烦恼，那么现在不需要再折腾了。优化器会为你找到最佳参数，再也不用手动调整了。

## FSRS v4 的弱项

1. 对于最简单的卡片（D=1）和最困难的卡片（D=10），理论上预测的 R 与实测的 R 存在较大偏差。这表明我们计算 D 的公式有待改进。尽管我们注意到了公式中的其他一些问题，但修正尝试都未能取得成功。

2. FSRS 要求很多复习数据（至少一千条，最好更多）才能准确优化其参数。如果你是新用户，还没有做过几千次的复习，优化器只会给你默认参数，这些参数可能适合也可能不适合你。

3. FSRS 的用户友好度不高。目前，它有三个模块：优化器（在 Google Colab 中为你找到最佳参数的部分）、调度器（你粘贴到 Anki 的代码）和助手插件，而目前还无法将它们合并成一个模块。除非 Anki 的开发者决定直接将 FSRS 整合到 Anki 中，否则这种情况不太可能改变。我敢赌 100 块，就算太阳成为红巨星并吞噬地球，也比这来得快。

4. 虽然我说你不再需要手动调整任何参数，但如果你目前的学习步伐超过有超过 1 天的话，唯一需要更改的是**将你的学习（和重新学习）步伐设置改为不超过 1 天**。否则，你可能会遇到「困难」的间隔比「良好」或「简单」的间隔长的情况，这会导致辅助插件和调度器出现奇怪的行为。不幸的是，Anki 的数据库有些古怪，所以处于「学习」（和「重新学习」）阶段的卡片与处于「复习」阶段的卡片的处理方式不同，FSRS 调度器只能影响处于「复习」阶段的卡片。这也意味着「休息日」功能并不如名字所述，它只是让你选择的日子不再有「复习」卡片，但你仍然需要处理「学习」和「重新学习」的卡片。

---

在[下篇](https://www.reddit.com/r/Anki/comments/15mab6e/fsrs_explained_part_2_accuracy/)，我将解释如何评估间隔重复算法的准确性。剧透一下：尽管这个 Reddit 版块上的人都在说需要随机对照试验，但实际上并不需要。真正需要的是大量的复习数据。

PS：如果你目前正在使用 FSRS v3，我建议你切换到 v4 版本。如何安装，请在[此处](https://github.com/open-spaced-repetition/fsrs4anki#2-advanced-usage)查阅。