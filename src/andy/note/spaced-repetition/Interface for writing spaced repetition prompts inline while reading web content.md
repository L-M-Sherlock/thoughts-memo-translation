# 为阅读网页内容时在行内撰写间隔重复卡片而设计界面

原文：[Interface for writing spaced repetition prompts inline while reading web content (andymatuschak.org)](https://notes.andymatuschak.org/z6NAUU151tRAwC9JCEbi5aW7PVU2BFiwmsFWt)

[助记媒介可以扩展到个人笔记](https://notes.andymatuschak.org/z5ARNXtS5VxteskEW91S1yYTgAcLABNXsZuJE)；这种方式为我的卡片提供了结构，并让我更流畅、更自信地编写卡片。但是在阅读材料和笔记之间来回切换仍然是不流畅的。而且，在阅读笔记中的卡片时，我有时仍然会感到迷惑，因为[文章笔记中关于源材料的卡片缺乏上下文](https://notes.andymatuschak.org/z39cc5AFaeVExHJkKKEEjAohRNZxz7iuZWSTX)。我的直觉是，某种行内交互会在这里起作用。

在 [2022-12-22](https://notes.andymatuschak.org/2022-12-22) 我做了一个类似的工作流原型。

- 我使用 [Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 来编写内置卡片（它使用的格式与 [我的个人助记媒介实现](https://notes.andymatuschak.org/z4mAF1uBV96r72e4NjLcDaujEyTPGiUQJEj8C) 中所述的格式相同）

- 使用 [Obsidian](https://notes.andymatuschak.org/z3aPTeVY2CVJqs61k26bHCvTZnniAK3hMEk3B) 的 [插件](https://github.com/weichenw/obsidian-hypothesis-plugin) 将这些内置卡片导入到我的 Markdown 笔记中（模板字符串：[20211227122651 ](https://notes.andymatuschak.org/20211227122651)）

- 使用[Orbit](https://notes.andymatuschak.org/z72ioKyd4X48WndtAsfkhnKwsD8o5PaaT384o) 的‘笔记同步’功能导入这些卡片。

## 日志

[2022-12-30(https://notes.andymatuschak.org/z6WvCc6W6ikmyPRRzxD1PCZ2ntTw7txyg9rCZ)：[Ozzie Kirkby](https://notes.andymatuschak.org/zn9igQGgecLncBSpKbgv5123mC5YEAP3hnfP)尝试将机器生成的卡片与我的卡片相匹配！[他的笔记](https://gist.github.com/kirkbyo/3530442c3bcdfc3cd5a5b95cafde9d0e)。

- Ozzie 提了个很有深度的问题，这个问题让我注意到：“在大多数情况下，我阅读时是在实时编写卡片。我注意到，与平时阅读时相比，这样做的阻力要小很多。我认为降低阻力的话，一气完成阅读和制卡是更容易的。

------

[2022-12-27](https://notes.andymatuschak.org/zgTBe9eLWVyAosrskDqtgd1RRoQn-WXPitXut)：迄今为止得到的观察结果。

- 与将这些卡片写在我的笔记中相比，将它们文内写入的感觉要好得多，这让我感到惊讶。

- 我注意到上下文切换感觉更加轻松。每次在笔记和文章之间切换，我都需要定位一下：我在哪里？下一张卡片写在哪里？当切换回之后：我在当前页面的什么位置？

- 标重点功能让我对“内容范围”有一些非常粗略的印象。当我在文章笔记中写卡片时，我认为我正在做一些心理簿记，以追踪我写了什么卡片，我没有写什么。

  - 有时，我需要“找到”我写的关于某个概念的卡片，我可以通过滚动到文本中介绍该概念的位置，然后单击合适的标重点轻松地做到这一点。

- 当我查看我已经编写的卡片时，[Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 界面能实现上述功能，我几乎总是在上下文中查看它 —— 我同时看到“邻近”的文本。这太棒了！

- 原则上，在这里极大的优点*应该是*空间性——即卡片位置和文本位置之间的物理关联。不幸的是，这种效果在我目前的原型中减弱了，因为 [Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 的注释并没有像谷歌文档的注释一样空间化：它们位于侧边栏中的线性列表中。

  - 这意味着我不能简单地滚动到我感兴趣的页面部分，并查看“邻近”卡片。相反，我必须先滚动到页面的一部分，接着点击随机的标重点，以将侧边栏滚动到右侧“附近”，然后从那里浏览，但哪里没有明确标明附近的“边缘”。

  - 我很惊讶他们没有在空间上分布注解，因为他们努力在侧边栏的槽中构建非常精细的“提示”，这些“提示”确实是空间化的。

很遗憾，那些提示并不能解决我的问题：它们需要点击多次，容易出错。而且它们的交互受到 [上下文中的细节问题](https://notes.andymatuschak.org/z6zGpscnGJpsV4brsMmuVrMvhYq6EUASYNTY4) 的妨碍。

- 编辑界面使得添加同一段落的多个卡片变得笨拙。这还没有那么困扰我。

  - 应该能在单个 Hypothesis 注释中编写多个卡片，但是有时在我复杂的导入操作中，用于分隔卡片的新行的格式会丢失。也许我努力一下可以解决这个问题。

- 我不喜欢 [Readwise](https://notes.andymatuschak.org/z2ewMN8Hzd8gt4qyfQV1ognJ5PQs3CXxDfCJ) 每天仅从 [Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 导入一次。这使得在编写内置提示和编写开放式文章笔记之间流畅地切换变得困难，因为正在考虑的网页笔记可能尚不存在。

  - 小阻力：网络书籍各个章节的卡片将被分成不同的笔记，如果我手写笔记，我可能会将它们放在同一个笔记中。

  - 有一个 [Obsidian](https://notes.andymatuschak.org/z3aPTeVY2CVJqs61k26bHCvTZnniAK3hMEk3B) 的插件，可以直接从 [Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 导入卡片；我会尝试切换到它。

  - 此外， [Readwise](https://notes.andymatuschak.org/z2ewMN8Hzd8gt4qyfQV1ognJ5PQs3CXxDfCJ) 似乎没法导入 [Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 的文档位置元数据，所以我不能轻易地从笔记摘录跳回到页面位置。

- ……做完了——我已经切换到直接从 Obsidian 导入标重点了。现在等待时间很短，我已经从循环中剪掉了工作流程的一个环节。此外，看来我现在可以成功地在单个 Hypothesis 的高亮中编写多个卡片！太棒了！

- [Obsidian](https://notes.andymatuschak.org/z3aPTeVY2CVJqs61k26bHCvTZnniAK3hMEk3B) 仍然很粗糙，我发现自己不想用它来实际写作......但我可以使用它来运行导入的插件。也许已经有人编写了能够直接运行的一些能替代它的命令行脚本？