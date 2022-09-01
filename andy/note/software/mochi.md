# Mochi

原文：[Mochi (andymatuschak.org)](https://notes.andymatuschak.org/zxAXSEQidXeYW2XFBj9ftGxz1kTNtV4fXjhZ)

[Mochi](https://mochi.cards/) 是网页端上的[笔记写作系统](https://notes.andymatuschak.org/z8XrKGDz49o6XxEx7tzGewzrXQnw6jSgv3Yyf), 主要使用 Markdown 语言, 集成了[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)。

尽管不是很完全，Mochi 试图实现[助记媒介可以扩展到个人笔记]((https://notes.andymatuschak.org/z5ARNXtS5VxteskEW91S1yYTgAcLABNXsZuJE) 中描述的想法：Mochi 的主要功能还是制作卡片，但它也支持在文章式的笔记中嵌入卡片；嵌入卡片这个操作并没有得到强调，这很奇怪：我估计是 Mochi 的预期用途还是语言学习的原因。

Mochi 的界面打磨得很不错，而且在逐步完善。2019 年 2 月Mochi 启动，截至 2021 年 5 月，开发势头很足，并且会规律发布新特性。

## 笔记内编写卡片

Mochi 的早期版本中，「笔记」和「牌组」泾渭分明，但最近这两者似乎融合了。现在笔记和牌组都是一件事——只是**查看方式**不同。

所以「牌组」可以像这样作为列表展现：

![img](https://notes.andymatuschak.org/BearImages/88E66810-9773-4C21-A2F4-7A9E46FED863-81997-00014D671A7B3EAC/7CD4E391-F87F-4015-B77A-EADD855259C1.png)

... 或者作为「笔记本」呈现，每张卡片内容展开，顺次显示：

![img](https://notes.andymatuschak.org/BearImages/72825D81-DBCD-439B-B71B-3DAC214AC82F-81997-00014D8458BCD383/34E2CFBA-7378-47CA-AF2D-143C9C973610.png)

Mochi 不像是用来编辑连续文本的：每个段落都看成「块」，鼠标不能在段落之间移动。但是打字时有个交互很不错：

1. 创建新段落。

2. 输入一些文字。

3. 输入 `---`。

4. 再输入一些文本。

5. 按两次回车键。

6. 一张卡片就做好了！

[file:08E15323-4727-445A-884D-F374B045D282-81997-00014DBA696FE38A/Screen Recording 2021-05-11 at 11.04.17 AM.mov](https://notes.andymatuschak.org/About_these_notes?stackedNotes=zUw5PuD8op9oq8kHvni6sug6eRTNtR9Wqma&stackedNotes=z5ARNXtS5VxteskEW91S1yYTgAcLABNXsZuJE&stackedNotes=zxAXSEQidXeYW2XFBj9ftGxz1kTNtV4fXjhZ)

对于编辑文章来说，Mochi 的交互方式很尴尬：所有操作都是针对单独某个段落的：只有「点中」某个段落才能打开编辑窗口；而且段落内容会动来动去，很难「对准」。不能用光标跨段落移动，也不能同时编辑多个段落。但这些交互从实现的角度很容易修改，所以我拭目以待。

对于把 Mochi 当作「个人助记媒介」使用的思路，还有一个明显的问题，就是如果你写了一篇很长的文章式笔记，里面嵌入了几张填空卡或者多面卡片，那么笔记里所有「段落」都会变成复习任务（也就是变成没有背面的卡片）。我觉得这样设计很奇怪！

## SRS 实现

使用经过修改的 SM-2 算法：简易度不会动态调整（虽然对每个牌组可以单独设置），如果忘记一张卡片，下一次的间隔会减半，而不会从零开始。

对于新卡片有「学习」的阶段，就像 Anki. 「新卡片」和「当日到期卡片」会区别对待。新卡片要回答正确了，**之后** 才加入到明天到期卡片中。

## 直接嵌入的卡片

2019 年 11 月 18 日，Mochi 添加了直接在笔记中嵌入 SRS 卡片的能力。卡片必须已经在牌组里，而且语法比较古怪。这种操作基本上是嵌入操作。

## 商业模式

Mochi 桌面版本免费使用。同步功能和 API 需要每月支付 5 美元。这样的商业模式很难盈利：需要有 1700 名活跃用户才能达到 10 万美元的年平均收益率(ARR)。

Mochi 开发者是{Matthew Steedman}。他主要在纽约活动，在各种机构中最为活跃（如 Code and Theory）。他有广告/图形设计的 partial 美术学士校历。