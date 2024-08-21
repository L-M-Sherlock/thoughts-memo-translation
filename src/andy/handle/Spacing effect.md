# 间隔效应

原文：[Spacing effect](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)

如果学习材料的时间错开来，比起花同样的时间一晚上死记硬背，材料会记得更牢。

换句话说，接连的记忆强化可以让[遗忘曲线](https://notes.andymatuschak.org/zHdKY3GwoUW9xG6wQtKFqjz9jcrxdM3mxram)更平，因此可以让复习间隔拉得越来越长。如果间隔时间安排得当，曲线可以被压到一个极平的角度。（译者注：遗忘得越快，遗忘曲线就随时间下坠得越厉害，抬平这个曲线就代表不容易遗忘）

[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)的算法利用了这一点来实现高效的学习系统。

## 最优间隔

复习之间的时间间隔不应该无限制地拉长，否则复习时材料更难回忆起来，进而削弱了对记忆的强化作用。最优的 ISI 取决于「保留间隔」(RI, retention interval )—— 最后一次学习和学习之后第一次测试的间隔时间。

Mozer 和 Lindsey (2016) 利用各种实证数据，推导出个人学习存在幂律关系：

最优 ISI = 0.097 * RI ^ 0.812

画成曲线形状如下：

![img](https://notes.andymatuschak.org/BearImages/A393B526-968E-4EBD-83EA-6359A5CD262F-65195-00020D8E87454AE0/16CD74F1-BD28-485D-9BAE-A4C240829927.png)

在我看来，它大致就是线性的。他们的数据集中所有的 RI 都没超过一年 ，所以这个函数在这个范围之外都不可靠。

另外，这个函数不太能拟合 Cepeda 等人 2008 年论文的数据：

![img](https://notes.andymatuschak.org/BearImages/FCDAD728-37AA-4974-B538-666C246B8AD5-65195-00020DA83A9E95B9/9966CFC2-C6BF-4A9E-A7C2-6282AADB8EA7.png)

例如，他们发现 RI=35 时，OISI~=5，但幂律拟合算出的是 OISI=1.8，从经验上讲，这个OISI在该研究中表现得更差。

## 收集的经验证据

Kornel (2009)，在一个涉及 GRE 词汇的实验中：

> 综合这三个实验，90% 的参与者在间隔条件下比集中条件下学到的更多，而只有 6% 的参与者正好相反。

## 解释间隔效应的可能理论

1. 「编码的可变性」：练习有间隔后改变了情景，记忆编码受这些情景影响，也更加丰富而多样

2. 与集中学习相比，间隔不那么需要全神贯注，耗费精力更少。

3. [较难提取的记忆经回忆得到更多强化](https://notes.andymatuschak.org/z4JH6dnUaSv1TcxgSpaBofAaFXxUmC4M3APqQ)，这可能通过[记忆的双组分模型](https://notes.andymatuschak.org/z4dAUBxVn79XSWRxGZHnKRXCP5XHeX2P9sw3y)来加强学习

4. 「预测效用」：如果一条信息通常在很短的间隔内被提取，你的大脑就会认为这个间隔过后就不再需要它了；提取间隔较长，所需实践也变长。

------

问：在间隔效应研究中，什么术语指代两次复习环节之间的时间？

答：环节间间隔 (ISI)

问：ISI 在间隔效应文献中代表什么？

答：环节间间隔。

问：在间隔效应研究中，什么术语指最后一次学习环节和测试之间的时间？

答：保留时间间隔（RI）

问：区分间隔效应研究中的「环节间间隔」和「保留间隔」。

答：前者指的是学习环节之间的时间，后者指的是最后一次学习环节和测试之间的时间。

问：间隔效应的相关文献中，「间隔函数」指什么？

答：回忆准确率与间隔时间的函数关系

问：间隔函数的形状特征是什么？

答：一个小山丘：最初的准确性相对较快增加，随后缓慢下降。

问：相对于间隔效应，「最优 ISI」指的是什么？

答：间隔函数的峰值点：能产生最高回忆准确率的 ISI。

问：很大程度上，「最优ISI」 取决于什么间隔指标？

答：保留时间间隔（Cepeda 等人，2006；通过 Mozer 等人，2009）

问：「编码变异理论」对「间隔效应」的核心主张是什么？

答：间隔能产生更优质的回忆，因为它用更多样的「心理情景*」来编码「记忆痕迹*」( memory trace )，这样与回忆背景重合的可能性更大。（注：「心理情景」指记忆时你的情绪、环境、反应等上下文；「记忆痕迹」是一个花里胡哨的术语，你可以自己查一下）

问：为什么在更广泛的心理情景下留下记忆痕迹后，回忆会更加牢靠？

答：编码特异性原则

问：在编码变异理论中，为什么不无限制地增加 ISI 来最大限度提升背景变异性？

答：随着 ISI 的增加，提取愈发不准确，因为每个学习背景之间相同成分更少。

问：预测效用理论对间隔效应的核心主张是什么？

答：大脑依据记忆被访问的规律来判断记忆还需要留存多长时间；学习之间间隔长，则留存时间更长。

------

## 参考文献

Branwen, G. (2009). 高效学习的间隔重复。2019 年 12 月 16 日检索，来自 https://www.gwern.net/Spaced-repetition

Kornell, N. (2009). Optimising learning using flashcards: Spacing is more effective than cramming. Applied Cognitive Psychology, 23(9), 1297–1317. https://doi.org/10.1002/acp.1537

[Psychological Theory Matters in the Big Data Era. In M. N. Jones (Ed.), Big data in cognitive science (pp. 34–64).](https://notes.andymatuschak.org/Mozer%2C_M._C.%2C_%26_Lindsey%2C_R._V._(2016)._Predicting_and_Improving_Memory_Retention)

## 反向链接

- 间隔重复记忆系统

    - 间隔重复记忆系统结合了[测试效应](https://notes.andymatuschak.org/z45mhbpabsigFceeSiRyDXZdvcRqvE2A1xMsn)和[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)，能够高效记忆成千上万条事实（[间隔重复记忆系统非常高效](https://notes.andymatuschak.org/z5rVJfPsyCU3pHBbhwef9DNR5fohTHCQFJWir)）。有些人还将这套系统用于更大范围的任务（见下文）。[间隔重复记忆系统使记忆成为一种选择](https://notes.andymatuschak.org/z4bR1HVvDUhMXDm5SJB4Tiw4xGbrm9AfXWgbc)，但它们不仅能用于背诵事实。[间隔重复记忆系统可用于发展概念性理解](https://notes.andymatuschak.org/z6UZP7P4sRNgRKSvNj7tMV5uW6dDhwwbdZCy9)。

- 间隔重复记忆系统是非常高效的

    - 使用[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)，你可以在每天投入短短的几分钟，就能记住成千上万的问题的答案。看上去很不直观，但正是[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)中的指数效果发挥作用：[间隔重复产生指数级的回报，而投入精力只需要增加一点点](https://notes.andymatuschak.org/z7AeS1H6h8GRAaZ9ZuqumphVu1LNM323rdS6u)。

- 记忆的双组分模型

    - 稳定性随着每次复习而增加，因此，可提取性随着每次重复而下降得更慢（见[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)）。当可提取性较低时，提取似乎会更多地增加稳定性：也就是说，[较难获得的记忆通过提取得到强化更多](https://notes.andymatuschak.org/z4JH6dnUaSv1TcxgSpaBofAaFXxUmC4M3APqQ)（另见 [Bjork 提出的理想困难](https://notes.andymatuschak.org/z49u8mtc9wZoY7siV7nz4V3PG2oMkNBn7AgUk)）。[Supermemo](https://notes.andymatuschak.org/z6Bub13H3u5SKX7Yzbt8GBuK86HPTXSU1TdAK) [试图用指数曲线来描述这种关系](https://supermemo.guru/wiki/Spacing_effect_gain)，但 Supermemo 使用的模型非常复杂，我有些怀疑。

- 赫尔曼-艾宾浩斯

    - 发现了[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)，是实验心理学的创始人之一，实验心理学也是[认知心理学](https://notes.andymatuschak.org/zLQzZhPX1oCXyCAt6fL1J2Hf6vWnEw91jhz)出现之前主导的方法论；更多请参见[A Contribution to Experimental Psychology (H. A. Ruger & C. E. Bussenius, Trans. ) 。(原作发表于1885年)](https://notes.andymatuschak.org/Ebbinghaus%2C_H._(1913)._Memory)。

- 大众传媒大多缺乏一个超过一天的自创时间维度

    - 书籍往往需要几周或几个月的时间来阅读。但书籍几乎从来没有有**作者制定**的时间线，像电影或戏剧那样。作者一般不安排读者在哪天、哪周、哪月怎么读书，相比之下，电影制作人会精心编排每一分钟的内容。然而很多想法需要时间来沉淀：[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)。不仅如此，只有在很多地方都遇到这些想法并加以琢磨，这些想法的真实含义才会变得清晰。

- 概念性知识的「最优间隔」的安排节奏可能更慢

    - 几乎所有关于[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)和[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)应用落地的文献，都只聚焦于陈述性信息，像是词对、术语定义或简单属性的值之类。我猜测这是因为概念类的信息非常依赖先验知识、背景知识的缘故，因此其记忆效果与陈述类会表现得截然不同。

- 「重试干预」使《量子国度》的早期准确率大幅提高

    - 实质上，当你相对更能回忆起答案时（也就是刚刷过答案不久时），该机制让你得做额外的[提取练习](https://notes.andymatuschak.org/zFGWCfLsZMkwKPYG2F3k9mnpwWM9D6cEJXS)。根据[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)，晚点重试可能会更好——像推迟半天或一天。但这样一来，下一次复习环节对于有效的[提取练习](https://notes.andymatuschak.org/zFGWCfLsZMkwKPYG2F3k9mnpwWM9D6cEJXS)来说就太晚了，因为你可能已经忘记了正确的答案，而且一旦没想起来，提取练习的效果（似乎）就会降低。

- 助记媒介中简单的应用卡片可以和回忆卡片以一样的方式呈现

    - 这两种卡片都受益于[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)（尽管时间安排有所不同）。

- Nate Kornell

    - 是威廉姆斯学院的认知心理学教授，[Robert A. Bjork](https://notes.andymatuschak.org/zcHyJy8EutFjUfJcEUw7sYLJ4UVTmR3NDsYS)的学生。围绕[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)和[测试效应](https://notes.andymatuschak.org/z45mhbpabsigFceeSiRyDXZdvcRqvE2A1xMsn)进行了大量研究。

- §认真对待知识工作（Stripe 上的融合讲座，2019-12-12）

    - [间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)

- 笔记类型命名法

    - 对艺术术语的简单定义，我自己加了一点；例如，[绝对判断的跨度](https://notes.andymatuschak.org/ziwhFzgTbrS2uxWEkCvoJzQrDzRz5EAWWZFy)，[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)

- 助记媒介实现了对被遗忘卡片的重试机制

    - 有趣的是，[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)表明，这种快速重试不太可能像简单地在下一次复习环节上重新呈现卡片那样有效。但我的直觉（以及我们越来越多的证据）表明，重试干预确实有帮助。我还没有读到任何关于间隔效应的文献，这些文献根据最初的反应成功率来区分表现 (再次，尽管我希望这样的研究确实存在)。

- 助记媒介的功效在不同的平台-知识-风格主题中是如何变化的？

    - 有充分的实验数据表明[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)对许多主题都适用，也有个人经验说明[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)可以有效地编码许多主题的材料。为了构建将不同主题的知识编码成卡片的方法，我们需要特定领域的问题解决办法。

- 提取强度下降可能是记忆干扰的函数，而不是时间的函数

    - [间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)通常表述成「记忆随着时间的推移而消退，所以我们应该研究它何时消退」。但这种随时间推移的衰退可能不是随时间推移自然发生的，而更应归因于干扰——学习其他材料的结果。

- 2021-02-28 - 2021-03-06

    - [间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)是存在的，但很难观察清楚。

- 2021-03-07 - 2021-03-13

    - 很高兴能更深入地理解[遗忘曲线](https://notes.andymatuschak.org/zHdKY3GwoUW9xG6wQtKFqjz9jcrxdM3mxram)和[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)的一些正式模型，尽管我对这类模型仍持怀疑态度。

- 2019-12-16

    - 9:12：写了[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)和[间隔重复记忆系统效率极高](https://notes.andymatuschak.org/z5rVJfPsyCU3pHBbhwef9DNR5fohTHCQFJWir)

- A Contribution to Experimental Psychology (H. A. Ruger & C. E. Bussenius, Trans. ) 。(原作 1885 年出版)

    - 在这一章的结尾，他提出了一个关于间隔练习和集中练习的关键观察。在第六章中，他发现一个用 68 次重所习得的 12 音节串，需要在第二天重复 7 次才能重新记起。但在这个实验中，他发现在三天内重复 38 次，在第四天也产生了同样的结果。7 次重复后重新记起。这是一个非常令人兴奋的结果，它表明时间安排不同，耗费的力气差异非常大（即[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)）。

- 筹备 2020 年 FOO 营会谈（Foo 营是由出版商 O'Reilly Media 主办的年度黑客活动。）

    - [间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)

- 对量子国度的分析

    -量子国度没有显著的[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)。

    - [2021-03-08](https://notes.andymatuschak.org/z3Ret6vAj4qcgbx2XjsFLLcFP4oNyvAGwhc2e)

- Marr 的水平分析

    - 从**算法**角度分析便会发现，间隔学习计划是良好的学习流程，因为该计划基于[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)和[提取练习](https://notes.andymatuschak.org/zFGWCfLsZMkwKPYG2F3k9mnpwWM9D6cEJXS)的计算理论

- A Multiscale Context Model of Memory. In Y. Bengio, D. Schuurmans, J. Lafferty, C. K. I. Williams, & A. Culotta (Eds.), Advances in Neural Information Processing Systems 22 (pp. 1321-1329).

    - 本文提出了一个模型，可以用来拟合实证学习数据（例如来自[间隔重复记忆系统](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)的数据）的间隔函数（即[间隔效应](https://notes.andymatuschak.org/zHdKY3GwoUW9xG6wQtKFqjz9jcrxdM3mxram)）和[遗忘曲线](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)。

    - 它的灵感来自于之前两个试图捕捉和解释[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)的模型：联想记忆的搜索（SAM）模型，其前提是编码-变异理论；以及多重时间尺度（MTS）模型，其前提是预测-效用理论。

- [[Roediger, H. L., & Karpicke, J. D. (2006).The Power of Testing Memory: Basic Research and Implications for Educational Practice. Perspectives on Psychological Science, 1(3), 181-210. https://doi.org/10.1111/j.1745-6916.2006.00012.x]]\* 关于[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw):

- [[Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. Journal of Educational Psychology, 112(1), 40–52. https://doi.org/10.1037/edu0000367]]\* 交错练习是[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)和[测试效应](https://notes.andymatuschak.org/z45mhbpabsigFceeSiRyDXZdvcRqvE2A1xMsn)的天然温床: