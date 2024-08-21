# 2005：稳定性增长函数

## 为什么简单的想法不一定容易落地？

对长期记忆的完美的数学描述即将完成。断断续续研究长达三十年，一个足够好的模型才得以脱颖而出，这在今天看来简直不可思议，特别是模型本身并不复杂。在人类事业中，科学往往是人类好奇心的副产品，而其他更紧急的项目往往得到优先处理。科学和发明有个问题，就是它们没有方向，而且难以预测。真相在发现多年后才显现其力量和价值。这个故事的一个道理就是，所有政府和公司都应该不遗余力地推进良好的科学发展。科学有点像 [SuperMemo](https://supermemo.guru/wiki/SuperMemo)，今天看来没什么甜头，但久久为功，收益会很惊人。

现在利用[SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17) 中的工具集，我们可以近乎完美地描述记忆。在理解记忆方面取得进一步进展的唯一限制是想象力、可用时间和提出正确问题的能力。我们工具齐全，数据充沛。我们还有不少数据是和睡眠记录相结合的，可用于为模型添加新的维度：[稳态](https://supermemo.guru/wiki/Homeostatic)学习意愿，[稳态](https://supermemo.guru/wiki/Homeostatic)疲劳，甚至还有[昼夜节律](https://supermemo.guru/wiki/Circadian)因素。

SuperMemo 的故事表明，如果你有一个想法，你应该将它实现（除非你有另一个更好的想法）。很多想法表面上灰头土脸，实则颇具魅力。我早在 [1984 年](https://supermemo.guru/wiki/Hermann_Ebbinghaus_(1885)_and_spaced_repetition_(1985))就绘制了第一条[遗忘曲线](https://supermemo.guru/wiki/Forgetting_curve)，但在几个月内就把它忘了。直到 34 年后我才想起来，那时候我的整个生活都围绕着遗忘曲线打转。想象一下这种惊喜吧！当我实现了第一个[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)算法时，我等了两年才决定招募第一个用户。如果没有 [Tomasz Kuehn](https://supermemo.guru/wiki/Tomasz_Kuehn)，SuperMemo for Windows 可能晚个两三年才能出世。如果没有 [Janusz Murakowski](https://supermemo.guru/wiki/Janusz_Murakowski)，SuperMemo 中重要的大数据：SuperMemo 重复历史记录可能会延迟 1-2 年。当[渐进阅读](https://supermemo.guru/wiki/Incremental_reading)在 2000 年落地时，只有我知道它是里程碑式的创举。但我蹉跎良久才得以纵观这丰碑之伟。今天，我知道[神经创造力](https://supermemo.guru/wiki/Neural_creativity)是突破性的工具，但我仍然半信半疑地使用它，而且不像使用[筛选集合进行复习](https://supermemo.guru/wiki/Subset_review)那样频繁。

### 1990：第一个提示

[SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17) 酝酿了近四分之一个世纪。在为这篇文章准备材料时，我在我的档案中发现了一张图片，里面是名为「新强度」的矩阵，行为「强度」，列为「耐久性」。这两个词是[稳定性](https://supermemo.guru/wiki/Stability)和[可提取性](https://supermemo.guru/wiki/Retrievability)的原始名称，在 1988-1990 年使用。这篇论文就像是古老的化石，说明 SM-17 算法的想法一定是在 1990 年左右诞生的。

[![A "new strength" matrix with rows marked as "strength" (stability) and columns marked as "durability" (retrievability)](https://supermemo.guru/images/thumb/f/f5/New_strength_matrix.jpg/300px-New_strength_matrix.jpg)](https://supermemo.guru/wiki/File:New_strength_matrix.jpg)

> 图：一张名为「新强度」的矩阵图片，行为「强度」，列为「耐久性」。这两个词是[稳定性](https://supermemo.guru/wiki/Stability)和[可提取性](https://supermemo.guru/wiki/Retrievability)的原始名称，在 1988-1990 年使用。这篇论文说明 SM-17 算法的想法一定是在 1990 年左右诞生的。

从创建[记忆的双组分模型](https://supermemo.guru/wiki/Two_components_of_memory)之初，我想基于这个模型写一个算法，但我的动力总是不太够。这套理论虽好，但[SuperMemo](https://supermemo.guru/wiki/SuperMemo) 那时已经够用了，似乎无需再实现新算法。但今天看来，我认为那时的算法的角色，是为这套模型提供数据，而这套模型能够回答很多关于记忆的问题，其中一些问题实际上从未被提出过（例如，关于[稳定性](https://supermemo.guru/wiki/Stability)的组分）。这也类似于 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 本身，它不温不火，是因为它的价值很难单纯从理论上被认可，实际效果才最容易让优秀的学生认可。

### 1993：干扰

1993 年，我自己的想法阻碍了进展。我认为进一步探索算法没有那么重要。用户很难受益。记忆建模是毫无实用价值的研究。参见：[微调算法的徒劳](https://supermemo.guru/wiki/Neural_networks_in_spaced_repetition#Futility_of_the_fine-tuning_the_spaced_repetition_algorithm)。那时，是 [Murakowski](https://supermemo.guru/wiki/Janusz_Murakowski) 努力地推动进展。他一直抱怨「SuperMemo 在流失诺贝尔奖级别的数据」。他有次对我吼道：「把历史重复数据功能给我实现了！」，简直是破口大骂。这是一场优先次序的争斗。我们迎来了 [SuperMemo 的新 Windows 版本](https://supermemo.guru/wiki/SuperMemo_7)，音频数据，CD-ROM 技术，也迎来了真切的竞争，比如 Young Digital Poland, 他们先我们一个月获得了波兰第一个 CD-ROM 软件的称号。我们仍然珍视波兰第一个 CD-ROM 上的 Windows 软件的宝座。第一张 [SuperMemo 7](https://supermemo.guru/wiki/SuperMemo_7) CD-ROM 实际上还是在美国生产的，但其内容完全是在波兰制作的。CD 里面的是 100% 纯波兰的 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 。

### 1996：风险投资

1996 年 2 月，所有的障碍都扫清了，[SuperMemo](https://supermemo.guru/wiki/SuperMemo) 终于开始收集完整的项目重复历史数据（当时，它仍然只是作为一个选项加入，以防止堵塞较少的系统少量的未使用数据）。我自己的项目重复历史数据现在基本上可以追溯到 1992-1993 年。这是可能的，因为 1996 年 2 月的所有[项目](https://supermemo.guru/wiki/Item)的最后一次重复仍然很容易从当时的间隔得出。我甚至有相当多的历史可以追溯到 1987 年。在我的数据强迫症中，我手动记录了一些具体的[项目](https://supermemo.guru/wiki/Item)的进展，后来通过手动编辑完成了重复的历史记录。因此，我自己的数据现在是现存的[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)中跨度最长的重复历史数据。30 年的数据，大量覆盖了 22-25 年的学习。这是个宝库。

1996 年 9 月 29 日，星期天，晚上，我花了两个小时来勾画基于[记忆的双组分模型](https://supermemo.guru/wiki/Two_component_model_of_memory)的新算法。这一切看起来都非常简单，而且需要的工作也不多。SuperMemo 刚刚开始收集重复历史，所以我应该有大量的数据在手。我们的重点从多媒体课程，如《越野》，转向更容易的项目，如[高级英语](https://supermemo.guru/wiki/Advanced_English)。这是个好时机，似乎。不幸的是，第二天，我们接到了 Antek Szepieniec 的电话，他与美国的投资者交谈，梦想让 [SuperMemo World](https://supermemo.guru/wiki/SuperMemo_World) 成为纳斯达克的第一家波兰公司。他兴奋地预言，他相信有很大的机会从风险投资中为我们的努力注入几百万美元。这一下子就把我抛到了新的角色和新的工作中。在坏事方面，这使[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 推迟了 20 年。好事方面，超媒体 SuperMemo 的概念，又称[知识机器](https://supermemo.guru/wiki/Knowledge_Machine)，又称[渐进阅读](https://supermemo.guru/wiki/Incremental_reading)，在理论和设计方面获得了很大的发展势头。实践再次战胜了科学。

### 2005：理论方法

随着 2000 年[渐进阅读](https://supermemo.guru/wiki/Incremental_reading)以及 2006 年[优先队列](https://supermemo.guru/wiki/Priority_queue)的出现，对延迟重复的需求，以及对提早复习的需求激增。这就要求大大偏离[最优间隔](https://supermemo.guru/wiki/Spaced_repetition)。旧的[算法 SM-8](https://supermemo.guru/wiki/Algorithm_SM-8) 无法有效地应对这种情况。[最优间隔](https://supermemo.guru/wiki/Optimum_interval)的功能必须扩展到时间维度（即[可提取性](https://supermemo.guru/wiki/Retrievability)）。我们需要一个[稳定性增长](https://supermemo.guru/wiki/Stability_increase)函数。

科学进步的一个非常有趣的动态是，对现实的树状探索往往需要临界的大脑质量（*译注：指量变引起质变的知识积累量）来推动一个新的想法。2005 年，[Biedalak](https://supermemo.guru/wiki/Krzysztof_Biedalak) 和其他人基本上不在圈子里，忙着把 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 作为一项业务来推广。我当时正处在[渐进阅读](https://supermemo.guru/wiki/Incremental_reading)的重大突破的路上：处理过载。随着维基百科的出现，人们突然意识到，导入成吨的知识不需要什么努力，但低优先级的知识较为庞大，会掩盖高优先级的知识。因此，知识富裕后破坏了知识的质量。我对这个问题的解决方案是采用[优先级队列](https://supermemo.guru/wiki/Priority_queue)。它在 2006 年才开始被实现。在此期间，[Gorzelanczyk](https://supermemo.guru/wiki/Edward_Gorzelanczyk) 和 [Murakowski](https://supermemo.guru/wiki/Janusz_Murakowski) 正忙于他们自己的科学项目。

Gorzelanczyk 曾经在克拉科夫参加过一个控制论会议，这个会议由 Ryszard Tadeusiewicz 教授 提供支持，他是我早期的灵感源泉。在 2005 年的演讲中，Gorzelanczyk 建议我们更新记忆模型。那时距上次制定模型已有十年，而分子生物学的新数据汹涌而来，势必有巨大影响。我认为自己那些寻找记忆稳定性公式的想法会成为很好的补充。与穆拉科夫斯基的交流后，这点星星之火很快获得了动力。如果没有这三个人（即 Wozniak, Gorzelanczyk 与 Murakowski）的协同工作，如果没有激起人们的兴趣，下一个大幅的进步会很难获得。利用在 1990 年间歇学习模型中首次采用的工具，我决定找出稳定性增长的函数。一旦我的电脑开始计算数据，有趣的信息开始连续不断地浮现。这项工作花了半个冬天的时间，本来只是预计只消几个晚上。

### 2013：大局观的重新觉醒

2013 年的情况和 2005 年一样，在新的解决方案落实前，我们必须确立大脑的临界质量。然而，我必须把最大的功劳归于 [Biedalak](https://supermemo.guru/wiki/Krzysztof_Biedalak)，是他倾斜了资源。那时为了给 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 的领导地位和开创性正名，我们承受无休止的斗争。是他要求我们继续进行这个项目，并派我去休一个短期的创造性假期来完成它。这本来只是一个冬季项目，结果花了两年，而且到今天仍然占用了我很多时间。

2014 年 11 月 09 日，我们进行了 26 公里的步行，讨论新的算法。散步是我们[最佳形式的头脑风暴](https://supermemo.guru/wiki/How_to_solve_any_problem%3F)，并且总能带来甜美耳的果实。第二天，我们在一个游泳池与 Leszek Lewoc 会面，他是大数据的死忠，总是有大量的奇妙想法（我第一次见到 Lewoc 是在 1996 年，而他的妻子可能早在 1992 年就在写一篇关于语言学习的论文，包括 SuperMemo）。那次头脑风暴总结了一些简单的结论：使用[记忆的双组分模型](https://supermemo.guru/wiki/Two_component_model_of_memory)来简化算法的方法，简化术语，并使其更加人性化（不再有 [A-系数](https://supermemo.guru/wiki/A-Factor)、[U-系数](https://supermemo.guru/wiki/U-Factor)、[R-系数](https://supermemo.guru/wiki/R-Factor)，等等）。

## 通过复述提高记忆稳定性

了解用于计算[记忆稳定性增长](https://supermemo.guru/wiki/Stability_increase)的公式有助于理解[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17)。在 2005 年，我们的目标是找到任何有效的 [R](https://supermemo.guru/wiki/Retrievability) 和 [S](https://supermemo.guru/wiki/Stability) 水平的稳定性增长的函数：*SInc*=*f*(R,S)。这些目标和工具与寻求建立[间歇学习模型](https://supermemo.guru/wiki/Search_for_a_universal_memory_formula)（1990）时所用的相当相似。

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

直到 2005 年，我们还无法制定一个通用的公式，将重复与[记忆稳定性增长](https://supermemo.guru/wiki/Stability_increase)联系起来。那时用来确定[重复间隔时间](https://supermemo.guru/wiki/Spaced_repetition)的算法，是基于对所谓最佳重复间隔的理解（定义为产生通常超过 90% 的已知回忆率的间隔），考虑了最佳重复间隔下，记忆稳定性的增强情况 —— 术语「最优间隔」用来描述学习中间隔时间的适用性。而这套间隔时间算法允许以矩阵形式，给出最优间隔所对应的准确稳定性增长函数。然而，对于可提取性水平较低（即当间隔不是**最优**的时候）时的稳定性增长，我们所知甚少。在 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 收集的数据的帮助下，我们现在可以尝试填补这一空白。尽管 SuperMemo 的设计是为了在学习中应用最佳的间隔时间，但在现实生活中，用户经常因为各种原因（如假期、疾病等）被迫推迟重复学习。这样一来，对于几乎所有材料体，在[可提取性](https://supermemo.guru/wiki/Retrievability)较低时都会给人大量重复。此外，在 2002 年，SuperMemo 引入了中位重复间隔的概念，使得重复间隔可以缩短。尽管在任何数据体中，中位间隔只占很小的一部分，但样本量足够大的话，可提取性极高或极低的样本数量，应可以将之前的发现推广 —— 原理论中记忆稳定性的增量和可提取性之间的关系仅在「可提取性=0.9」时有结论，现在可以推广到完整的作用域上了。

为了通过学习的方式最佳地建立记忆稳定性，我们需要知道**最优间隔的函数**，或者说，**稳定性增长函数**（*SInc*）。它们考虑三个参数：[记忆稳定性（S）](https://supermemo.guru/wiki/Stability), [记忆可提取性（R）](https://supermemo.guru/wiki/Retrievability)和[知识难度（D）](https://supermemo.guru/wiki/Difficulty)。在 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 的传统上，我们一直专注于 S 和 D 这两个维度，因为保持高水平的可提取性，是程序在做复习间隔优化时参照的主要优化准则。对 S 和 D 的关注取决于稳定性增长函数的实际应用。文本则聚焦于 S 和 R，不讨论 D ，因为我们现在试着分析「纯知识」，以消去维度 D 的影响。也就是说，讨论那些由非复合的记忆痕迹刻画的知识，它们易于学习。消除 D 维度使我们在理论上做划分更为容易，而且以后结论可以扩展到复合记忆痕迹，和看起来难以学习的知识。换句话说，当我们从实践到理论讨论时，我们的兴趣从 ( S, D ) 对转移到 ( S, R ) 对。出于这种逻辑，所有实验数据集都按难度进行了过滤。同时，我们会寻找最大的数据集，其中的项目由于排期的延迟（违反了最优的重复间隔），低 R 值的项目会有足够大的代表性

我们开发了一个两步算法，用来提出一个符号公式，来表示在**[难度](https://supermemo.guru/wiki/Difficulty低而统一的数据集)**（所谓表述良好、容易记忆的知识数据集）中，不同[可提取性](https://supermemo.guru/wiki/Retrievability)水平的稳定性增长。表述良好和统一的学习材料使我们很容易通过排练提炼出一个纯粹的长期记忆巩固过程。正如本文其他地方所讨论的那样，表述不清的知识会导致独立巩固过程的叠加，不适合于所提出的分析。

### 两步计算法

在 SuperMemo 17 中，可以遍历重复历史的全部记录来收集[稳定性增长](https://supermemo.guru/wiki/Stability_increase)数据。这使得绘制 *SInc[]* 矩阵的图形表示成为可能。然后可以用这个矩阵来找出[稳定性增长](https://supermemo.guru/wiki/Stability_increase)函数的符号近似函数。同样的推理也用在了 2005 年。不过程序要简单得多。这个推理可以用来更好地理解[SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

确定记忆稳定性增长 *SInc* 函数的两步程序：

- **第 1 步**：使用 *SInc* 的矩阵表示和一个迭代程序来最小化真实学习过程（数据）中的成绩和 *SInc* 预测的成绩之间的[偏差](https://supermemo.guru/wiki/Deviation) *Dev*。*Dev* 被定义为 *R-Pass* 在给定知识的重复序列上的总和，其中 *R* 是可提取性，*Pass* 为 1 表示合格成绩，0 表示不合格成绩

- **第 2 步**：使用爬山算法（Hill Climbing ）解决最小二乘法问题，以计算出 *SInc* 的符号式可能选择，找出一种最能拟合步骤 1 中得出的 *SInc* 矩阵

### 计算稳定性增长

[稳定性增长](https://supermemo.guru/wiki/Stability_increase)（*SInc[]*）的矩阵是在**第 1 步**计算的。在 2005 年， *SInc* 初值只要合理即可。今天，由于我们知道这个函数本质是近似的，我们可以加快这个过程，使之成为非迭代过程（见[SM-17 算法](https://supermemo.guru/wiki/Algorithm_SM-17)）。

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

让我们定义一套流程来计算给定的复习模式下记忆的稳定性。这套流程用于计算稳定性时，可以基于学习过程中已知的评分（实际变体），也可以仅仅基于重复时间（理论变体）。两种方法的唯一区别是，实际变体允许对稳定性进行修正，因为随机遗忘反映在不及格的评分上。

在下面的段落中，我们将使用以下符号：

- S(t) - 时刻 t 的记忆稳定性

- S[r] - 第 r 次重复后的记忆稳定性（例如，S[1] 代表学习新知识后的记忆稳定性）

- R(S,t) - 稳定性 S 和时刻 t 下的记忆可提取性（已知 R=exp-k*t/S，k=ln(10/9)）

- *SInc*(R,S) - 作为可提取性 R 和稳定性 S 下复习结果的稳定性增长（Stability INCrease），其中 *SInc*(R(S,t),S(t))=S(t)/S(t')=S[r]/S[r-1]（其中：t' 和 t 代表记忆巩固前后的排练时间，t-t' 与零不可区分）

我们的目标是找到对任何有效范围内的 R 和 S 都可用的稳定性增长函数：*SInc*=*f*(R,S)。

如果我们采取任何合理的 *SInc*(R,S) 的初始值，并使用 S[1]=S1，其中 S1 是第一次接触复习后利用记忆衰减函数得出的稳定性（对于最优重复间隔），那么对于每个重复历史，我们可以使用以下迭代来计算 S：

```

r:=1;

S[r]:=S1

repeat

  t:=Interval[r]; // 其中：Interval[r] 取自学习过程（实践性变体）或被调查的复习模式（理论性变体）

  Pass:=(Grade[r]>=3); // 其中：Grade[r] 是第 r 个间隔后的评分（实践变体）或 4（理论变体）

  R:=Ret(S[r],t);

  if Pass then

     S[r+1]:=S[r]*SInc[R,S[r]]

     r:=r+1;

 else begin

    r:=1;

    S[r]:=S1;

    end;

 until (r 是最后一次重复)

```

在[SM-8 算法](https://supermemo.guru/wiki/Algorithm_SM-8) 中，我们可以使用首次间隔图来确定 S1，每次评分为失败后，S1 都会逐渐变短。

我们以矩阵 *SInc[R,S]* 的假设初始值开始迭代过程，例如，像[算法 SM-2](https://supermemo.guru/wiki/Algorithm_SM-2) 中那样，选择将所有项设置为 [E-系数](https://supermemo.guru/wiki/E-Factor) 。

然后，我们可以在现有的重复历史数据上继续使用上述程序，计算出 *SInc[R,S]* 的新值，该值与实际学习过程中的评分有较小的[偏差](https://supermemo.guru/wiki/Deviation)（我们为此使用差值 *R-Pass* ）。

以下观察有助于实现渐进式的改进：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

- 如果 Pass=true 并且 S[r]<Interval[r]，那么*SInc[R,S[r-1]]* 元素的估计值过小（并且可以朝着 Interval[r]/S[r]*SInc[R,S[r-1]] 的方向修正）

- 如果 Pass=false 并且 S[r]>Interval[r]，那么*SInc[R,S[r-1]]* 元素的估计值过大

我们可以对 *SInc[]* 进行迭代，使其数值与学习过程中的评分越来越接近，达到一致。

这种方法使得有可能得出相同的最终 *SInc[R,S]*，与初始化时设定的 *SInc[R,S]* 的原始值无关

在[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 中，我们使用实际的[遗忘曲线](https://supermemo.guru/wiki/Forgetting_curve)来对[可提取性](https://supermemo.guru/wiki/Retrievability)进行更好的估计，然后可以用来修正估计的[稳定性](https://supermemo.guru/wiki/Stability)，而不是上述开关递进方法。最终的稳定性估计结合了[可提取性](https://supermemo.guru/wiki/Retrievability)的理论预测、从[遗忘曲线](https://supermemo.guru/wiki/Forgetting_curve)中获取的实际[保留](https://supermemo.guru/wiki/Recall)（根据数据的可用性进行加权），以及与上述推理中的间隔相结合的实际评分。通过结合这三个信息来源，[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 可以提供稳定性/间隔估计，而不需要反复迭代 *SInc[]* 矩阵。

### 稳定性增长的符号公式

经过多次迭代，我们得到一个 *[SInc](https://supermemo.guru/wiki/Stability_increase)* 的值，该值使误差最小。这个过程是可收敛的。有了[稳定性增长](https://supermemo.guru/wiki/Stability_increase)的矩阵，我们可以寻找一个符号公式来表达稳定性增长。

#### 稳定性增长与 S 的关系

可以预见的是，*[SInc](https://supermemo.guru/wiki/Stability_increase)* 随着 *[S](https://supermemo.guru/wiki/Stability)* 的增加而减少。这种现象被命名为[稳定化衰减](https://supermemo.guru/wiki/Stabilization_decay)，现在可以在 [SuperMemo for Windows](https://supermemo.guru/wiki/SuperMemo_for_Windows) 中检视。以下是 2005 年的原始发现：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

在第 2 步中，我们将使用这里得到的 *SInc[R,S]* 矩阵来获得 *SInc* 的符号公式。

**第 2 步** - 找到 *SInc* 的一个符号公式

现在我们可以使用任何梯度下降算法，为最佳拟合上面得出的矩阵 SInc 而求出 SInc 的符号候选公式，

查看 SInc 矩阵时，我们立即看到当 R 取为常数时， SInc 是 S 的函数，并且可以完美地用负幂函数刻画，如下面的示例性数据集所示：

[![SInc as a function of S for constant R is excellently described with a negative power function](https://supermemo.guru/images/0/0e/SInc-vs-S.gif)](https://supermemo.guru/wiki/File:SInc-vs-S.gif)

这在同一图表的对数版中更加清楚：

[![Log(SInc)-vs-log(S).gif](https://supermemo.guru/images/4/4e/Log%28SInc%29-vs-log%28S%29.gif)](https://supermemo.guru/wiki/File:Log(SInc)-vs-log(S).gif)

上面关于 [*SInc* 对 *S* 幂律相关](https://supermemo.guru/wiki/Stabilization_decay)的结论证实了以前的发现。特别是，在 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 中，[R-系数](https://supermemo.guru/wiki/R-Factor)沿着[重复类别](https://supermemo.guru/wiki/Repetition_category)的下降总是用幂函数近似最佳。

#### 稳定性增长与 R 的关系

正如[间隔效应](https://supermemo.guru/wiki/Spacing_effect)所预测的那样，*[SInc](https://supermemo.guru/wiki/Stability_increase)* 对于较低水平的 *[R](https://supermemo.guru/wiki/Retrievability)* 来说更大。然而，请注意，2005 年使用的程序可能引入了一个假象：记忆痕迹随着时间的推移而存续，将线性地贡献于新的稳定性估计。但根据[遗忘](https://supermemo.guru/wiki/Forgetting)的随机性质，这是有问题的。这样一来，较长的记忆存续期可能是一个偶然的问题。在[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 中，更多的证据被用来估计稳定性，并且**存续间隔**与所有其他证据一起被权衡。

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

当我们寻找反映常数 S 下 *SInc* 和 R 关系的函数时，我们看到数据中的噪音更多，这是因为 SuperMemo 在低 R 下提供的点击率要少得多（其算法通常试图达到 R > 0.9）。尽管如此，在检查了多个数据集后，我们得出结论，有点令人惊讶的是，当 R 降低时，*SInc* 会呈指数级增长（见后面的内容，说明这种增长导致 *SInc* 和时间之间几乎呈线性关系）。这一增长的幅度高于预期，应该为[间隔效应](https://supermemo.guru/wiki/Spacing_effect)的力量提供进一步证据。这一结论应该对学习策略产生重大影响。

这里有一组取 S 为常数的 SInc 对 R 的函数的示例数据。我们可以看到 SInc=f(R) 可以很好地用一个负指数函数进行近似：

[![SInc as a function of R for constant S can be quite well approximated with a negative exponential function](https://supermemo.guru/images/2/29/SInc-vs-R.gif)](https://supermemo.guru/wiki/File:SInc-vs-R.gif)

还有同一图表的半对数版本，其线性近似的趋势线截距设置为 1：

[![SInc-vs-log(R).gif](https://supermemo.guru/images/b/b2/SInc-vs-log%28R%29.gif)](https://supermemo.guru/wiki/File:SInc-vs-log(R).gif)

有趣的是，可提取性为 100% 时，稳定性增长可能小于 1。一些分子生物学的研究表明，复习时记忆的不稳定性会增加。这个发现又佐证了死记硬背的伤害不仅限于枉费时间。

#### 稳定性增长与可提取性的关系（2018）

尽管有种种算法上的差异和伪命题，[稳定性增长](https://supermemo.guru/wiki/Stability_increase)对[可提取性](https://supermemo.guru/wiki/Retrievability)的函数关系于[表述良好的知识](https://supermemo.guru/wiki/20_rules)与[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 13 年后产生的数据的函数关系几乎完全一样。

记得在 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 中，我们使用[遗忘曲线](https://supermemo.guru/wiki/Forgetting_curve)来提供对[可提取性](https://supermemo.guru/wiki/Retrievability)的更好估计。然后，这被用来修正估计的[稳定性](https://supermemo.guru/wiki/Stability)。通过结合几个信息来源，[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 可以提供更准确的[稳定性](https://supermemo.guru/wiki/Stability)估计。但算法仍然有一个历史遗留问题，那就是记忆痕迹的存续，记忆痕迹将线性地贡献数值给新的稳定性。这个问题可以通过调参数来改掉，然而每次 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 试图这样做的时候，它的性能指标都会下降。

尽管已经改进了这么多，数据集（尤其是 R 低的数据）也更大了，但对于简单的项目，[稳定性增长](https://supermemo.guru/wiki/Stability_increase)与[可提取性](https://supermemo.guru/wiki/Retrievability)的相关性仍然不变。

一旦考虑[困难](https://supermemo.guru/wiki/Difficulty)的知识，这样美妙的关联就崩溃了。部分原因是减少了上面提到的**长时间存续**假象的问题。出于这个原因，新的 SuperMemos 并不依赖这个看似被证实的记忆公式。

[![Stability increase for easy knowledge at different retrievability levels](https://supermemo.guru/images/thumb/d/dc/Stability_increase_as_a_function_of_memory_retrievability_for_easy_knowledge.png/600px-Stability_increase_as_a_function_of_memory_retrievability_for_easy_knowledge.png)](https://supermemo.guru/wiki/File:Stability_increase_as_a_function_of_memory_retrievability_for_easy_knowledge.png)

> 图：长期记忆的[强度](https://supermemo.guru/wiki/Stability)取决于[回顾](https://supermemo.guru/wiki/Repetition)的时间。对于[精心表述的知识](https://supermemo.guru/wiki/20_rules)，长时间的复习延迟会使[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)大大增加。最佳的复习应该平衡这种增长与[遗忘的概率](https://supermemo.guru/wiki/Retrievability)。在所展示的图表中，[稳定性增长](https://supermemo.guru/wiki/Stability_increase)和[可提取性](https://supermemo.guru/wiki/Retrievability)的对数（log(R)）之间的关系是线性的。log(R) 表示的是时间。近 27,000 次[重复](https://supermemo.guru/wiki/Repetition)被用来绘制这个图表。复习前观察到的[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)从 2 天到 110 天不等。在最低的[可提取性](https://supermemo.guru/wiki/Retrievability)水平下，[稳定性](https://supermemo.guru/wiki/Stability)的最大增幅接近 10 倍。[稳定性增长](https://supermemo.guru/wiki/Stability_increase)矩阵是用 SuperMemo 17 的[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 生成的

### 记忆稳定性增长公式

有了[稳定性增长](https://supermemo.guru/wiki/Stabilization)的矩阵在手，我们可以寻找稳定性增长的符号表达式。2005 年找到的方程之后将被称为 *Eqn. SInc2005*。请注意，[算法 SM-17](https://supermemo.guru/wiki/Algorithm_SM-17) 中使用的公式有所不同：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

对于恒定的知识难度，我们应用二维表面拟合法来获得 *SInc* 的符号公式。我们使用了改良的 Levenberg-Marquardt 算法，其中有许多可能的符号函数候选，这些函数可能准确地描述 *SInc* 作为 S 和 R 的函数。该算法通过一个持续的随机重启循环得到加强，以确保找到全局最大值。我们用以下公式获得了最佳结果（公式：SInc2005）：

> *SInc*=*a*S*^-b*\*e^*c*R+*d*

>

> 其中：

>

> - *SInc* - 成功复习后的记忆稳定性增长倍数（重复前和重复后的稳定性 S 之比）

> - R - 复习时记忆的可提取性，以百分比表示回忆的概率

> - S - 复习前的记忆稳定性，以产生 R=0.9 的间隔表示

> - *a*, *b*, *c*, *d* - 不同数据集的参数可能略有不同

> - e - 自然对数的底

对于不同的数据集，参数 *a*、*b*、*c*、*d* 会略有不同，这可能反映了用户-知识互动的可变性（即不同的学习材料集呈现给不同的用户，可能导致不同的难度分布，以及具有不同的评分标准，这些都可能影响最终的测量结果）。

为了说明问题，从几组数据中提取的 *a*、*b*、*c*、*d* 的平均值为：*a=76*，*b=0.023*，*c=-0.031*，*d:=-2*，其中 *c* 在不同的数据集中变化不大，而 *a* 和 *d* 的变化相对较大。请看例子：[如何使用计算记忆稳定性的公式？](http://supermemopedia.com/wiki/How_to_use_the_formula_for_computing_me mory_stability?)

## 从稳定性增长公式中得出的结论

上述[稳定性增长](https://supermemo.guru/wiki/Stability_increase)的公式与后来的发现略有不同。例如，它似乎低估了[稳定性增长](https://supermemo.guru/wiki/Stability_increase)随 S 的下降（低 *b*）。然而，它可以用来推导出大量有趣的结论。

### 随着时间的推移，复习的价值线性增长

由于[间隔效应](https://supermemo.guru/wiki/Spacing_effect)，[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)的增长潜力随着时间的推移几乎以线性方式不断增长：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

上述公式产生的 *SInc* 值与同质数据集\*上的 *SInc* 矩阵形式的数据平均相差 15%（\* 即复习历史来自于：同一学生、同一知识类型、低难度和小范围的 [A-系数](https://supermemo.guru/wiki/A-Factor)）。

随着重复间隔的增加，尽管随着时间的推移进行了双重指数化，*SInc* 沿着近乎线性的 sigmoid 曲线增长（两个负指数化操作相互抵消）：

[![The graph of changes of SInc in time. This graph was generated for S=240 using Eqn. SInc2005](https://supermemo.guru/images/d/d0/SInc-vs-time.gif)](https://supermemo.guru/wiki/File:SInc-vs-time.gif)

> 图：SInc 随着时间变化的图像。该图是用公式 [SInc2005](https://supermemo.guru/wiki/SuperMemo_Algorithm:_30-year-long_labor#SInc2005) 对 S=240 产生的。

*SInc* 对时间的近乎线性相关反映在 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 中，通过用 [O-Factor](https://supermemo.guru/wiki/O-Factor) 乘以实际使用的重复间隔，而不是之前计算的[最优间隔](https://supermemo.guru/wiki/Optimum_interval)来计算新的最优间隔（在 SuperMemo 中，O-Factor 是一个二维矩阵 OF[S,D] 的卡片，代表 R=0.9 的 *SInc*）。

### 稳定性增长期望

学习的优化可以使用各种标准。我们可以对特定的[回忆](https://supermemo.guru/wiki/Recall)水平进行优化，也可以对[记忆稳定性增长](https://supermemo.guru/wiki/Stability_increase)进行最大化。在这两种情况下，了解[稳定性增长](https://supermemo.guru/wiki/Stability_increase)的期望水平是有帮助的。

让我们把记忆稳定性增长的期望值定义为：

> E(*SInc*)=*SInc*\*R

>

> 其中：

>

> - R - 可提取性

> - *SInc* - 稳定性增长

> - E(*SInc*) - 稳定性增长的概率期望（即由 *SInc* 定义的增长，被遗忘的可能性所减弱）

2005 年得出的[稳定性增长](https://supermemo.guru/wiki/Stability_increase)公式产生了一个重大的惊喜。我们曾经声称，最好的学习速度可以在[遗忘指数](https://supermemo.guru/wiki/Forgetting_index)为 30-40% 时实现。公式 [SInc2005](https://supermemo.guru/wiki/History_of_spaced_repetition_(print)#SInc2005) 似乎表明，非常低的[保留](https://supermemo.guru/wiki/Retention)可以带来相当好的记忆效果。由于 2005 年时低保留率数据的稀缺性，这些结论需要慎重对待：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

从公式 [SInc2005](https://supermemo.guru/wiki/History_of_spaced_repetition_(print)#SInc2005) 我们可以得到 E(*SInc*)=(*a*S*-b*\*e^*c*R+*d*)\*R。通过找到导数 d*ESInc*/dR，并将其等同于零，我们可以找到在不同的稳定性水平下，最大化期望稳定性增长的可提取性：

[![Expected increase in memory stability E(SInc) as a function of retrievability R for stability S](https://supermemo.guru/images/c/ca/Consolidation_curve_E%28Sinc%29%3Df%28R%29_%282005%29.gif)](https://supermemo.guru/wiki/File:Consolidation_curve_E(Sinc)%3Df(R)_(2005).gif)

> 图：巩固曲线：[记忆稳定性增长](https://supermemo.guru/wiki/Stabilization)期望 E(SInc) 为[稳定性 S](https://supermemo.guru/wiki/Stability)的函数，由公式（[SInc2005](https://supermemo.guru/wiki/SuperMemo_Algorithm:_30-year-long_labor#SInc2005)）得出。使用 [SuperMemo](https://supermemo.guru/wiki/SuperMemo) 用户所知道的术语，短间隔记忆稳定性的最大期望增长发生在[遗忘指数](https://supermemo.guru/wiki/Forgetting_index)等于 60% 的时候！这也意味着，SuperMemo 中允许的最大遗忘指数（20%）导致的稳定性预期增长比可能的最大值少了近 80%（如果我们只准备牺牲高[保留](https://supermemo.guru/wiki/Retention)）

[![Expected increase in memory stability E(SInc) as a function of retrievability R and S based on Eqn SInc2005](https://supermemo.guru/images/thumb/2/27/E%28SInc%29_as_function_of_R_for_S.jpg/600px-E%28SInc%29_as_function_of_R_for_S.jpg)](https://supermemo.guru/wiki/File:E(SInc)_as_function_of_R_for_S.jpg)

> 图：[记忆稳定性增长](https://supermemo.guru/wiki/Stability_increase)期望 E(SInc) 是[可提取性](https://supermemo.guru/wiki/Retrievability) R 和[稳定性](https://supermemo.guru/wiki/Stability) S 的函数，由公式 [SInc2005](https://supermemo.guru/wiki/SuperMemo_Algorithm:_30-year-long_labor#SInc2005) 得出

### 间隔重复中的记忆复杂性

在[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)中，记忆的[稳定性](https://supermemo.guru/wiki/Stability)取决于[复习](https://supermemo.guru/wiki/Review)的质量，而复习又取决于[记忆的复杂性](https://supermemo.guru/wiki/Memory_complexity)。早在 1984 年，我就在自己的学习中使用了这个原则，即后来被称为**[最小信息原则](https://supermemo.guru/wiki/Minimum_information_principle)**。为了有效地复习，知识关联需要简单（即使知识本身很复杂）。[项目](https://supermemo.guru/wiki/Item)可以建立一个复杂的知识结构，但受复习的个别记忆应该是[原子性的](https://supermemo.guru/wiki/Atomic_memory)。

[![Memory complexity: simple and complex memories](https://supermemo.guru/images/thumb/f/f5/Memory_complexity.png/450px-Memory_complexity.png)](https://supermemo.guru/wiki/File:Memory_complexity.png)

> 图：**[记忆复杂性](https://supermemo.guru/wiki/Memory_complexity)**说明了[最小信息原则](https://supermemo.guru/wiki/Minimum_information_principle)的重要性。在记忆简单的问题和答案时，我们可以依靠简单的记忆连接，并在复习时统一刷新这种连接。复杂的记忆可能会以不完整的方式激活其概念，或以不同的顺序，取决于上下文。因此，在复习时很难产生[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)的统一增长。复杂的项目是很难记住的。一个简单项目的例子可能是一个词对，例如「苹果=pomo」（世界语）。而要认识一个苹果可能需要一个复杂的联系网。「苹果」和「pomo」之间的联系是不可简化的（即最大限度的简化）

在复杂项目的稳定性公式中，[稳定性](https://supermemo.guru/wiki/Stability)就像电路中的电阻：许多并联的电阻使更多电流漏过

顺便说一句，在[渐进阅读](https://supermemo.guru/wiki/Incremental_reading)的早期，Zonnios 独立地得出了[渐进写作](https://supermemo.guru/wiki/Incremental_writing)的概念，这在今天看来是将[渐进阅读](https://supermemo.guru/wiki/Incremental_reading)的工具运用于[创造](https://supermemo.guru/wiki/Creativity)的一个明显步骤。这篇文章也是通过[渐进写作](https://supermemo.guru/wiki/Incremental_writing)的方式写的。

2005 年，人们就是这样描述和分析对复杂项目的记忆：

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

学习的[难度](https://supermemo.guru/wiki/Difficulty)是由所记信息的[复杂性](https://supermemo.guru/wiki/Complexity)决定的。复杂的知识会产生两种效果：

- 对其他信息的[干扰](https://supermemo.guru/wiki/Interference)增加

- 在复习时难以统一刺激记忆痕迹的子成分

这两种影响都可以通过在学习过程中应用[合适的知识表述](https://supermemo.guru/wiki/20_rules)来解决。

让我们看看知识的[复杂性](https://supermemo.guru/wiki/Complexity)如何影响[记忆稳定性](https://supermemo.guru/wiki/Memory_stability)的建立。

想象一下，我们想学习以下内容：「玛丽-斯克洛多夫斯卡-居里是 1911 年诺贝尔化学奖的唯一得主。」我们可以采取两种方法：一种是保持知识的复杂性，另一种是采用简单的表述方式。在选择保持知识复杂性的情况下，为了学习玛丽-居里的名字和她获得诺贝尔奖的年份，我们可能会制定一个双[挖空](https://supermemo.guru/wiki/Cloze)。

> 「问：[...]是[...]诺贝尔化学奖的唯一得主」

> 「答：玛丽-斯克洛多夫斯卡-居里，1911」

如果采用简单的表述方式，这个双挖空将被拆开，而波兰人的婚前姓氏将成为可有可无的，并被用来创造第三个挖空：

> 「问：[...]是 1911 年诺贝尔化学奖的唯一得主」

> 「答：玛丽（斯克洛多夫斯卡）居里」

>

> 「问：玛丽-斯克洛多夫斯卡-居里是[...]（年份）诺贝尔化学奖的唯一得主」

> 「答：1911」

>

> 「问：玛丽-[...]-居里是 1911 年诺贝尔化学奖的唯一得主」

> 「答：斯克洛多夫斯卡」

此外，在简单的表述方式中，一个完整的学习方法需要形成两个挖空，因为玛丽-居里也是 1903 年诺贝尔物理学奖的得主（以及其他奖项）：

> 「问：玛丽-斯克洛多夫斯卡-居里是 1911 年诺贝尔[...]奖的唯一得主」

> 「答：化学」

>

> 「问：玛丽-斯克洛多夫斯卡-居里是 1911 年[...]的唯一获奖者」

> 「答: 诺贝尔（化学）奖」

现在让我们考虑一下一开始的那个复合双[挖空](https://supermemo.guru/wiki/Cloze)版本。为了便于讨论，让我们假设记住 1911 年和「居里」这个名字同样困难。复合记忆痕迹（即整个双挖空）的[可提取性](https://supermemo.guru/wiki/Retrievability)将是其子痕迹的可提取性的乘积。这来自于一个一般的规则，即在大多数情况下，记忆痕迹基本上是独立的。尽管[遗忘](https://supermemo.guru/wiki/Forgetting)一个痕迹可能会增加遗忘另一个痕迹的概率，但在绝大多数情况下，正如经验所证明的那样，与同一主题有关的独立的不同问题可以承载一个完全独立的学习过程，其中的回忆和遗忘是完全不可预知的。让我们看看把回忆的概率当作独立的事件是如何影响复合记忆痕迹的[稳定性](https://supermemo.guru/wiki/Stability)的：

> (9.1) R=Ra*Rb

>

> 其中：

>

> - R - 二元复合记忆痕迹的[可提取性](https://supermemo.guru/wiki/Retrievability)

> - Ra 和 Rb - 两个独立的记忆痕迹子组分（子痕迹）的[可提取性](https://supermemo.guru/wiki/Retrievability)：a 和 b

>

> (9.2) R=exp^-kt/Sa*exp^-kt/Sb=exp^-kt/S

>

> 其中：

>

> - t - 时间

> - k - ln(10/9)

> - S - 复合记忆痕迹的[稳定性](https://supermemo.guru/wiki/Stability)

> - Sa 和 Sb - 记忆子痕迹 a 和 b 的稳定性

>

> (9.3) -kt/S=-kt/Sa-kt/Sb=-kt(1/Sa+1/Sb)

>

> (9.4) S=Sa*Sb/(Sa+Sb)

我们使用公式 (9.4) 来进一步分析复合记忆痕迹。我们预计，如果最初，记忆子痕迹 Sa 和 Sb 的[稳定性](https://supermemo.guru/wiki/Stability)差别很大，随后的[重复](https://supermemo.guru/wiki/Repetition)，为最大化 S 而优化（即标准 R=0.9），可能会由于次优的复习时机而削弱子组分的[稳定性](https://supermemo.guru/wiki/Stability)。我们表明情况并非如此。在学习过程中，子稳定性倾向于收敛！

[![Value of keeping memories simple](https://supermemo.guru/images/thumb/5/5a/Memory_stability_for_complex_memories_and_memory_subtraces.png/400px-Memory_stability_for_complex_memories_and_memory_subtraces.png)](https://supermemo.guru/wiki/File:Memory_stability_for_complex_memories_and_memory_subtraces.png)

> 图：在学习中保持简单的记忆是至关重要的（见：[最小信息原则](https://supermemo.guru/wiki/Minimum_information_principle)）。复杂的知识模型可以由简单的记忆来表示。从长远来看，简单性可以提高记忆的保持力。简单性对记忆的[稳定性](https://supermemo.guru/wiki/Stability)的影响是[记忆的双组分模型](https://supermemo.guru/wiki/Two_component_model_of_memory)的一个重要贡献，证明了[祖母细胞](https://supermemo.guru/wiki/Grandmother_cell)存在的必要性。人类的智慧依赖于一个概念图系统，而概念图的[稳定性](https://supermemo.guru/wiki/Stability)又归功于个体记忆的简单性

[复杂](https://supermemo.guru/wiki/Stability)记忆的[稳定性](https://supermemo.guru/wiki/Complexity)可以从[原子记忆](https://supermemo.guru/wiki/Atomic_memory)的子稳定性中得出

复杂记忆的记忆痕迹促成了长期保留知识的困难，这一事实暗示了新皮层不可能使用连接主义方法来储存记忆。这是一个重要的新论据，证明了被称为[祖母细胞](https://supermemo.guru/wiki/Grandmother_cell)的神经元的存在（更多信息见：[关于祖母细胞的真相](https://supermemo.guru/wiki/The_truth_about_grandmother_cells)）。下面的图片有助于理解记忆[概念化](https://supermemo.guru/wiki/Conceptualization)是如何随时间推移而进行的：

[![Uncertain course of stabilization in complex memories](https://supermemo.guru/images/thumb/0/0d/Uncertain_course_of_the_stabilization_of_complex_memories.png/450px-Uncertain_course_of_the_stabilization_of_complex_memories.png)](https://supermemo.guru/wiki/File:Uncertain_course_of_the_stabilization_of_complex_memories.png)

> 图：**复杂记忆的稳定化的不确定过程**。图中显示了以单个[概念细胞](https://supermemo.guru/wiki/Stabilization)的单一树突输入模式为例的[稳定化](https://supermemo.guru/wiki/Stabilization)、[遗忘](https://supermemo.guru/wiki/Forgetting)、[泛化](https://supermemo.guru/wiki/Generalization)和[干扰](https://supermemo.guru/wiki/Interference)的假想过程。神经元、树突和树突丝以橙色显示。图片没有显示树突丝转化为树突棘的过程，树突棘的形态随着时间的推移会发生变化[稳定化](https://supermemo.guru/wiki/Stabilization)。方块代表参与识别输入模式的突触。每个方块显示了突触在[长期记忆的双组分模型](https://supermemo.guru/wiki/Two_component_model_of_long-term_memory)方面的状态。红色的强度代表[可提取性](https://supermemo.guru/wiki/Retrievability)。蓝色区域的大小代表[稳定性](https://supermemo.guru/wiki/Stability)。在记住一个复杂的记忆模式后，[概念细胞](https://supermemo.guru/wiki/Concept_cell)在收到来自红色方块的信号总和后能够识别该模式，这些信号代表高[可提取性](https://supermemo.guru/wiki/Retrievability)和极低[稳定性](https://supermemo.guru/wiki/Stability)的新记忆。每次细胞被重新激活，活跃的输入将经历[稳定化](https://supermemo.guru/wiki/Stabilization)，这表现在输入方块中蓝色区域的增加。每次当概念细胞活跃时，信号没有到达输入端，其稳定性就会下降（泛化）。每次源轴突活跃而目标神经元未能发射，稳定性也会下降（竞争性干扰）。由于输入到概念细胞的信号模式不均匀，一些突触将被稳定下来，而另一些则会丢失。当一个突触失去其稳定性和可提取性，以及相关的树突棘被收回时，[遗忘](https://supermemo.guru/wiki/Forgetting)就会发生。当同一个[概念细胞](https://supermemo.guru/wiki/Concept_cell)可以用一个更小但更稳定的输入模式重新激活时，[泛化](https://supermemo.guru/wiki/Generalization)就会发生。当一个新的输入模式有助于忘记一些识别旧输入模式所必需的冗余输入时，就会发生追溯性[干扰](https://supermemo.guru/wiki/Interference)。旧模式的[稳定化](https://supermemo.guru/wiki/Stabilization)导致树突丝的流动性降低，从而防止新模式接管[概念](https://supermemo.guru/wiki/Concept)（主动的[干扰](https://supermemo.guru/wiki/Interference)）。在这个过程的每一端，一个稳定的、泛化性强的输入模式是激活[概念细胞](https://supermemo.guru/wiki/Concept_cell)的充要条件。同一个细胞可以对不同的模式作出反应，只要它们是一致的、[稳定的](https://supermemo.guru/wiki/Stabilization)。在[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)中，对[知识表征](https://supermemo.guru/wiki/Knowledge_representation)的选择不当将导致激活模式的可重复性差，突触的[稳定化](https://supermemo.guru/wiki/Stabilization)不均匀，以及[遗忘](https://supermemo.guru/wiki/Forgetting)。当输入模式无法激活足够多的突触，从而无法重新激活[概念细胞](https://supermemo.guru/wiki/Concept_cell)时，就会发生对[项目](https://supermemo.guru/wiki/Item)的遗忘。在[重复](https://supermemo.guru/wiki/Repetition)时，根据上下文和[思路](https://supermemo.guru/wiki/Conceptual_computation)，一个[项目](https://supermemo.guru/wiki/Item)可能被提取或遗忘。[复习](https://supermemo.guru/wiki/Repetition)的结果是不确定的

### 复合记忆痕迹的子稳定性收敛情况

在[间隔重复](https://supermemo.guru/wiki/Spaced_repetition)中模拟复杂记忆的行为很容易。复杂记忆的子稳定性趋于收敛，使得复习很低效，稳定性增长缓慢。现在我们可以证明，项目复杂到一定程度后，提升其记忆稳定性来实现长期[保留](https://supermemo.guru/wiki/Retention)的目标，是不可能的。简而言之，要记住一本书，只能是循环往复地读这本书，别无他法。这是一个徒劳的过程。

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

如果一个项目挖了两个空，分别对应不同的知识点，以及两个记忆痕迹，那么很难确定单次重复能够均匀地激活这两个记忆痕迹。不妨假设只有第一次重复对两个记忆痕迹是不同的，其他的学习过程遵循上述公式进行。

为了研究在以 R=0.9 为标准的复合稳定性优化的复习模式下，记忆子痕迹的稳定性行为，让我们采取以下手段：

- Sa=1

- Sb=30

- S=Sa*Sb/(Sa+Sb) （来自公式 9.4）

- *SInc*=*a*S*-b*\*e^*c*R+*d* （来自公式 [SInc2005](https://supermemo.guru/wiki/History_of_spaced_repetition_(print)#SInc2005)）

- 通过 R=0.9 的复习巩固复合记忆痕迹，使两个子痕迹都得到同样好的再巩固（即对复合痕迹的复习不会忽略子痕迹）

从下图中可以看出，复合痕迹的记忆稳定性总是小于单个子痕迹的稳定性；但是，子痕迹的稳定性会收敛。

[![Convergence of stability for memory sub-traces rehearsed with the same review pattern optimized for the entire composite memory trace (i.e. review occurs when the composite retrievability reaches 0.9)](https://supermemo.guru/images/a/a0/Stabil4.gif)](https://supermemo.guru/wiki/File:Stabil4.gif)

> 图：用相同的复习模式对整个复合记忆痕迹进行优化后，记忆子轨迹的稳定性趋于一致（即当复合可提取性达到 0.9 时，进行复习）。横轴表示复习次数，纵轴表示[稳定性](https://supermemo.guru/wiki/Stability)的对数。蓝线和红线对应的是两个子痕迹的稳定性，这两个子痕迹在原始学习后的稳定性差距很大。黑线对应的是复合稳定性（S=Sa\*Sb/(Sa+Sb)）。如果每次复习的结果都是对基础突触结构的统一激活，那么 Sa 和 Sb 之间的差异会自我纠正。

### 复合稳定性增长

存档警告：[为什么使用文字档案？](https://supermemo.guru/wiki/Why_use_literal_archives%3F)

现在让我们弄清楚 *[SInc](https://supermemo.guru/wiki/Stability)* 对于复合稳定性 S 和子痕迹稳定性 Sa 和 Sb 的差异有多大？如果我们假设记忆子痕迹的刺激相同，并将 SInca 和 SIncb 记为 *i*，那么对于重复次数 r，我们有：

> SInca=SIncb=*i*

>

> Sa[r]=Sa[r-1]\**i*

> Sb[r]=Sb[r-1]\**i*

>

> S[r]=Sa[r]\*Sb[r]/(Sa[r]+Sb[r])=

> =Sa[r-1]\*Sb[r-1]**i*2/(Sa[r-1]\**i*+Sb[r-1]**i*)=

> =*i*\*(Sa[r-1]\*Sb[r-1])/(Sa[r-1]+Sb[r-1)=*i*\*S[r-1])

换句话说：

> (11.1) SInc=*i*=SInca=SIncb

以上表明，在所提出的模型中，假设记忆子痕迹的再巩固程度相同，记忆稳定性的增长与知识的复杂性无关

**复合稳定性增长与子痕迹的稳定性增长是一样的**