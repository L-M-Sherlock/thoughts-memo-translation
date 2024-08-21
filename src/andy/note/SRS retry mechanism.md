# SRS 重试机制

原文：[SRS retry mechanism (andymatuschak.org)](https://notes.andymatuschak.org/z2GB3wDnERaJr2337zGJdb5Gnr7tURrfmoxu)

在[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)中，通常有各种各样的「重试」机制。通常情况下，这些机制的工作方式是，如果你答不上来一个问题，几分钟后，或在复习结束时，它将再次呈现。换句话说，这张卡片被暂时分配一个很短的间隔，在成功记住之后，它就会得到新的「遗忘后」间隔，通常会更长。

## 在助记媒介中

从 2019 年底开始，《[量子国度](https://notes.andymatuschak.org/z2fBHADWa93EZTuNzuww7V3Vi587ZyZ4FHTHm)》实现了以下行为；[Orbit](https://notes.andymatuschak.org/z72ioKyd4X48WndtAsfkhnKwsD8o5PaaT384o) 一直都在实施这一行为。如果你在阅读文章时忘记了问题的答案，该问题会在文章的下一个复习区重新出现（除非是最后一个复习区，在这种情况下，一旦你回答了当前复习区的所有问题，它就会重新出现）。如果你在复习阶段忘记了问题的答案，它将在复习阶段结束时重新出现。

到目前为止的研究结果：[重试干预使量子国度的早期准确率大幅提高](https://notes.andymatuschak.org/z26sYZAf3H5ohZTM2eaAosMRNwLkXiRKDsAJ)。

这个功能大致受到 Anki 的「学习」队列启发。如果我忘记了一张卡片的答案，然后提前结束复习（即在再次复习该卡片之前），我觉得对它的记忆会变得不那么可靠。提取练习文献中可能存在实证数据。我还没有查阅相关文献，也没有在我的背景阅读中偶然发现它。

有趣的是，[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)表明，这种快速重试可能不如在下一个复习会话中重新呈现卡片那样有效。但我的直觉（以及我们越来越多的证据）表明，重试干预确实有帮助。在我读过的有关间隔效应的文献中，没有一篇根据最初的反应成功率来区分表现（尽管我认为应该已经有这样的研究了）。

关于[助记媒介](https://notes.andymatuschak.org/z4rRX3qwSSJRsEkdXKwH2shamgHNeRthrMLiF)中这种机制的笔记：

- [重试结果可能会给出额外的可提取性信号](https://notes.andymatuschak.org/zq2kRQRbZ5ykqy6TWtece3NscvMdjYRUZFr)