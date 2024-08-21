# 高效学习的间隔重复

通过间隔效应实现高效记忆：可以广泛使用的文献综述、使用技巧、适用范围及其裨益。

> 间隔重复是有数百年历史的心理学方法，常用于高效记忆以及技能练习。与尝试去死记硬背相反的，通过间隔性的复习，人复习时长的增加，软件的计划安排，使得记忆效率更高。间隔重复虽然节奏较慢，但更加稳扎稳打，所以实现了更高的效率，便可以扩展到记忆成百上千的内容（相比之下，死记硬背的内容几乎转瞬即忘），因此对于外语和医学学习尤为有用。

>

> 我回顾了这种方法的适用范围与相关的大型研究文献，以及测试效应（大部分材料截止到 2013 年），可用的软件工具和使用方式，以及关于它的各种想法和观察。

计算机技术最富有成效的领域之一就是弥补人类的弱点。计算机精通算数，因为这是人类力有未逮之处[1](https://www.gwern.net/Spaced-repetition#sn1)⁠。计算机要记住 TB 量级的数据，因为人类忘性大。计算机能制作最好的日程表，因为人类总要查看今天要做什么。不过即使我们记不清楚东西，记住哪里能参考到也够用了。从头到尾阅读一本手册或教科书的意义并不是记住里面的一切知识以备万一，而是之后能记住「什么在里面」以便检索（快速浏览之后，你便能掌握用于搜索某个主题的正确关键词，来应对深入了解此话题的需要）。

这样的[神经辅助工具](https://en.wikipedia.org/wiki/Neuroprosthetic)[2](https://www.gwern.net/Spaced-repetition#sn2)是有不少，但总有更多可以发掘出来。这些工具值得上下求索，因为它们价值连城：铲子比你的手要有效得多，但[电铲](https://en.wikipedia.org/wiki/Power_shovel) 比两者都要强上几个数量级——虽然它需要培训和专业知识才能使用。

# [间隔效应](https://www.gwern.net/Spaced-repetition#spacing-effect)

> 「练习能让你受益匪浅，

> 若其时机适当地分散。

> 你若想当个蠢驴笨蛋

> 那就**一口气**做完，

> 你能记住的少得可怜。」

>

> Ulrich Neisser[3](https://www.gwern.net/Spaced-repetition#sn3)

我目前最喜欢的神经辅助工具，是利用[间隔效应](https://en.wikipedia.org/wiki/Spacing_effect)⁠的软件。间隔效应在认知心理学中有数百年历史，这些软件借此在学习或记忆方面能比传统学习方法取得更好的效果；唉，但这种效应还不为人知[4](https://www.gwern.net/Spaced-repetition#sn4)⁠。

间隔效应实质上是说，如果你有一个问题「你学到的这个随机序列中的第五个字母是什么？」，而你只能学习它 5 次，那么如果你把 5 次机会分散到很长的一段时间——天、周、月，那么你对答案「e」的记忆将会最强。而集中在一两天内草草学习 5 次则是最不明智选择。你可以把「[遗忘曲线](https://en.wikipedia.org/wiki/Forgetting_curve)」想象成一张放射性[半衰期](https://en.wikipedia.org/wiki/Half-life)的图表：比方说，每次复习都会使你的记忆力提高 50%，但复习在早期并没有起到多大作用，因为记忆并没有衰退太多！（**为什么**生物学水平上间隔效应有效？在[动物模型](https://www.gwern.net/docs/www/downloads.hindawi.com/28f6fb747bb3f6c33a5eb1ea8b01e3ecb63d7122.pdf)中，集中学习和间隔学习存在明显的神经化学差异。间隔学习（间隔大于一小时）能助长神经元连接强度的[长期增益效应](https://en.wikipedia.org/wiki/Long-term_potentiation)，而集中学习没有此效果[5](https://www.gwern.net/Spaced-repetition#sn5)。但是这种差异的原因还是悬而未决的问题；请参阅[记忆痕迹](https://en.wikipedia.org/wiki/Engram_(neuropsychology))或者[睡眠学习](https://www.gwern.net/Spaced-repetition#when-to-review)的概念。）遗忘曲线的图形表示：

![Stahl et al 2010; CNS Spectrums](https://www.gwern.net/images/spacedrepetition/forgetting-curve-stahl.jpg)Stahl et al 2010; *CNS Spectrums*

更好的是，我们都知道[主动回忆](https://en.wikipedia.org/wiki/Active_recall)是一种种远胜于单纯被动接触信息的学习方法。[6](https://www.gwern.net/Spaced-repetition#sn6)间隔也可以扩展到海量信息；身为赌徒和金融家的 [Edward O.Thorp](https://en.wikipedia.org/wiki/Edward_O._Thorp) 在他还是一名物理研究生的时候就利用了「间隔学习」，「以便能更久且更努力地工作」[7](https://www.gwern.net/Spaced-repetition#sn7)⁠，还有 [Roger Craig](https://en.wikipedia.org/wiki/Roger_Craig_(Jeopardy！_contestant)) 在 2010-2011 年的智力竞赛节目「[Jeopardy！](https://en.wikipedia.org/wiki/Jeopardy！)」中创造了多项记录，归功于[使用 Anki](https://www.gwern.net/docs/spaced-repetition/2011-qs-rogercraigwinsjeopardy.html#comment-3004) 记忆了许多 [>200,000](http://www.j-archive.com/) 张关于以前问题的卡片[8](https://www.gwern.net/Spaced-repetition#sn8)⁠；后来的「Jeopardy！」获奖者 Arthur Chu 也使用了间隔重复[9](https://www.gwern.net/Spaced-repetition#sn9)⁠。医学院的学生 (由于他们在医学院期间需要记住大量的事实材料而成为 SRS 的主要人群) 通常拥有数千张卡片，特别是如果使用预制的牌组 (由于标准化课程和普遍缺乏制作自己卡片的时间，预制牌组更适合于医学)。外语学习者可以很容易地累积到 10-30,000 张卡片；[一个 Anki 用户](https://old.reddit.com/r/Anki/comments/a9s456/what_is_the_largest_anki_deck_you_have_read_about/)报告了一副超过 76.5 万张[自动生成](http://subs2srs.sourceforge.net/)卡片的牌组，里面装满了各种来源(「Youtube 视频、视频游戏、电视节目等」)的日语音频样本。

一图胜千言；假设这里有一个人有条件多次复习一条给定的信息 (假设他很忙碌)。通过观察我们所记内容的保留率可以看到，短期内的突击记忆非常有用，然而，未经锻炼的记忆衰退得非常快，倘若拉长该记忆的间隔，那么记忆效果要好得多：

![《连线》(出自 Wozniak?); 集中 VS 间隔(可代替的图表)](https://www.gwern.net/images/spaced repetition/forgetting-curve-wired-wozniak.jpg)《连线》（杂志）(出自 Wozniak?)；集中 VS 间隔([可代替的图表](https://web.archive.org/web/20130128115142/http://www.anewspring.com/storage/memotrainerrr.png))

如果我们观看一段可视化了记忆衰退的视频[《随机重复 VS 近期重复 VS 间隔重复》](https://www.youtube.com/watch?v=ai2K3qHpC7c#t=2m40s)⁠，结果会更加惊人。

## [如果你这么棒，你为什么没钱](https://www.gwern.net/Spaced-repetition#if-youre-so-good-why-arent-you-rich)

> 大多数人认为编程在概念上很好理解，但动手实践就难乎其难。[10](https://www.gwern.net/Spaced-repetition#sn10)

当然，学生们选择的正是后一种策略（死记硬背）。他们在考试前一晚临时抱佛脚，一个月后就什么都记不起来了。那么为什么要这么做呢？(我自己也不幸置身其中) 为什么间隔重复如此不受欢迎，甚至对于稍有尝试的人也是如此？[11](https://www.gwern.net/Spaced-repetition#sn11)

![Scumbag Brain 表情包：考试前一晚死记硬背的时候什么都知道/一个月后什么都忘了](https://www.gwern.net/images/spacedrepetition/scumbag-brain.png)Scumbag Brain 表情包：考试前一晚死记硬背的时候什么都知道/一个月后什么都忘了

因为死记硬背在某种程度上确实有它的功用。但有得必有失：你用现在的强记忆换取以后的弱记忆。(非常弱[12](https://www.gwern.net/Spaced-repetition#sn12)⁠。)考试通常全是新材料，虽偶尔会有旧问题，所以死记硬背是有回报的！这就是它的可恶之处——总的来说，虽然死记硬背的记忆寿命和质量都不如间隔重复的功效，但死记硬背能**立即**收效[13](https://www.gwern.net/Spaced-repetition#sn13)。因此，死记硬背虽说有些短视，但也算是理性的对策。甚至 SRS 软件也承认其功用，并提供一定程度的支持[14](https://www.gwern.net/Spaced-repetition#sn14)⁠。(但正如人们可能预期的，如果进行连续而渐进的测试，那么所学知识寿命也更长[15](https://www.gwern.net/Spaced-repetition#sn15)⁠；我不知道这是否因为这种测试是一种变相的、偶然间形成的间隔重复系统，还是学生或受试者只是为了应对小风险的考试而学习表现不同。)除了这种短期集中的优势之外，人们还常[忽略](https://www.gwern.net/docs/spaced-repetition/2011-mccabe.pdf)间隔重复的优势，以及有着认为短期记忆的成效会持续存在的主观“错觉”[16](https://www.gwern.net/Spaced-repetition#sn16)[17](https://www.gwern.net/Spaced-repetition#sn17)(参见：[Son & Simon 2012](https://www.gwern.net/docs/spaced-repetition/2012-son.pdf)[18](https://www.gwern.net/Spaced-repetition#sn18)⁠, [Mulligan & Peterson 2014](https://www.gwern.net/docs/spaced-repetition/2014-mulligan.pdf)⁠, [Bjork et al 2013](https://www.gwern.net/docs/spaced-repetition/2013-bjork.pdf)⁠, [Deslauriers et al 2019](https://www.pnas.org/content/early/2019/09/03/1821936116)); from [Kornell 2009](https://www.gwern.net/docs/www/sites.williams.edu/0b05297b47a1cfa08a95b83f49e8d254b1eefc84.pdf) 的对 GRE 词汇的研究(重点添加)：

> 在整个实验中，对于 90% 的参与者来说，**间隔**比集中更有效，然而在第一次学习之后，72% 的参与者认为**集中**比间隔更有效……当他们确实考虑间隔时，他们经常有这样的错觉：「集中学习比间隔学习更有效」，即使事实是相反的 ([Dunlosky & Nelson, 1994](https://www.gwern.net/docs/spaced-repetition/1994-dunlosky.pdf)⁠; Kornell & Bjork, 2008a; [Simon & Bjork 2001](https://www.gwern.net/docs/spaced-repetition/2001-simon.pdf)⁠; [Zechmeister & Shaughnessy, 1980](http://www.willatworklearning.com/2005/11/research_review.html))。

正如人们所预期的那样，如果测试效应和间隔效应真实存在，那么那些本就自我测试并在考试前用功学习的学生往往会有较高的 GPA。[19](https://www.gwern.net/Spaced-repetition#sn19) 如果我们将问题解释为测试，那么一对一辅导[显著优于](https://en.wikipedia.org/wiki/Bloom‘s_2_Sigma_Problem)常规教学，这不会令我们惊讶，而且受辅导学生回答的问题数量高要出几个数量级[20](https://www.gwern.net/Spaced-repetition#sn20)⁠。

当然，从长远来看，这种短视观点并不是一件好事。知识建立在知识的基础上，不是与学习无关的琐事。[Richard Hamming](https://en.wikipedia.org/wiki/Richard_Hamming) 在[《你和你的研究》](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html)一书中回忆到：

> 可以看到，大多数伟大的科学家都有澎湃的干劲。我在[贝尔实验室](https://en.wikipedia.org/wiki/Bell_Labs)与 [John Tukey](https://en.wikipedia.org/wiki/John_Tukey) 共事了十年。他便是干劲很足的人。我加入实验室约三四年后，有一天我发现 John Tukey 其实年龄竟比我小一点。John 是个天才，而我显然不是。我怒气攻心，冲进 [Bode](https://en.wikipedia.org/wiki/Hendrik_Wade_Bode) 的办公室说：「跟我差不多大的人怎么能像 John Tukey 那样知道这么多？」他靠在椅子上，把双手放在脑后，微微一笑，说道：「Hamming，如果你像他那样努力工作那么多年，你的知识也会多到让你惊讶的。」我羞愧至极，简直是马上溜出了办公室！

>

> Bode 的意思是：「知识和生产力就像[复利](https://en.wikipedia.org/wiki/Compound_interest)⁠。」如果两个人的能力大致相同，而其中一个人的工作量比另一个人多 10%，那么前者的产量将是后者的两倍多。知道的越多，学的越多；学的越多，能做的越多；能做的越多，机会越多——这很像复利。我不想给你一个利率，但这是一个非常高的利率。如果两个人拥有完全相同的能力，那么一个日复一日多花一个小时思考的人在一生中的工作效率将会大大提高。我把 Bode 的话放在心上；几年来，我花了更多的时间努力工作，并发现，事实上我可以完成更多的工作。

知识需要积累，而间隔重复搭配上抽认卡很适合辅助积累，即使有[数千张](https://www.gwern.net/Spaced-repetition#the-workload)⁠卡片和前置概念，所有知识仍然能稳定地复习。

间隔重复关注长远，这或许可以解释为什么显式的间隔重复很不普及：很久才能收获回报，而且这种回报很反直觉，却需要当即付出自律的代价，然而这个代价却很实在。(请参阅[双曲贴现](https://en.wikipedia.org/wiki/Hyperbolic_discounting)⁠。）而雪上加霜的是，确定何时进行下一次复习很困难——最好的时机是你即将忘记知识的时候，但这样就进退两难：如果即将忘记知识，又怎么能记住要复习它呢？你只记得去复习知道的知识，但知道了又不用去复习了！[21](https://www.gwern.net/Spaced-repetition#sn21)

这个悖论的破局之道是让计算机处理所有的计算。我们要感谢[赫尔曼·艾宾浩斯](https://en.wikisource.org/wiki/Memory:_A_Contribution_to_Experimental_Psychology)细致得令人发指的研究，不过现在我们可以给计算机编程来计算遗忘曲线以及最需要复习的卡片集合[22](https://www.gwern.net/Spaced-repetition#sn22)⁠。这就是[间隔重复](https://en.wikipedia.org/wiki/Spaced_repetition)软件背后的逻辑：一遍又一遍地问同样的问题，但每次询问之间间隔不断增加。一开始每隔几天问一次，使用者很快就会记得挺清楚。然后间隔扩展成几周，然后是几个月，然后是几年。一旦记忆形成并存储到长期记忆中，只需要偶尔复习一下就很硬朗[23](https://www.gwern.net/Spaced-repetition#sn23)——我很清楚地记得我四五岁生日时用纸板做过大恐龙，或者用盒子做隧道，尽管我最多就一年回忆一两次。