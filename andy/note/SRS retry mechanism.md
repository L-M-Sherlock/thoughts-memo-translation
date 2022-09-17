# SRS 重试机制

原文：[SRS retry mechanism (andymatuschak.org)](https://notes.andymatuschak.org/z2GB3wDnERaJr2337zGJdb5Gnr7tURrfmoxu)

在[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)中通常会有各种类型的「重试」机制。通常这些工作方式是，如果你答不上来一个问题，几分钟后，或在复习结束时，它将再次呈现。换句话说，这张卡片被暂时分配一个很短的间隔时间，在它被成功记住之后，它就会得到新的「遗忘后」间隔，通常是更长的间隔时间。

## 在助记媒介中

从 2019 年底开始，[量子国度](https://notes.andymatuschak.org/z2fBHADWa93EZTuNzuww7V3Vi587ZyZ4FHTHm)实现了以下行为；[Orbit](https://notes.andymatuschak.org/z72ioKyd4X48WndtAsfkhnKwsD8o5PaaT384o) 一直都在实现这一行为。如果你在阅读文章时忘记了问题的答案，该问题会在文章的下一个复习区重新出现（除非是最后一个复习区，在这种情况下，一旦你回答了当前复习区的所有问题，它就会重新出现）。如果你在复习阶段忘记了问题的答案，它将在复习阶段结束时重新出现。

到目前为止的研究结果：[重试干预使量子国度的早期准确率大幅提高](https://notes.andymatuschak.org/z26sYZAf3H5ohZTM2eaAosMRNwLkXiRKDsAJ)。

这个功能的灵感大致来自 Anki 的「学习」队列。如果我忘记了一张卡片的答案，然后提前结束我的复习（即在再次复习该卡片之前），我觉得我对它的记忆就不那么可靠了。提取练习文献中可能有关于这方面的经验数据。我没有去找它，也没有在我的背景阅读中偶然发现它。

有趣的是，[间隔效应](https://notes.andymatuschak.org/z5oCe7JTrkYfmb6SHE4n5HxisE7PdwS6nmXEw)表明，这种快速重试不太可能像简单地在下一次复习环节上重新呈现卡片那样有效。但我的直觉（以及我们越来越多的证据）表明，重试干预确实有帮助。我还没有读到任何关于间隔效应的文献，这些文献根据最初的反应成功率来区分表现（尽管我再次想象，这样的研究确实存在）。

在[助记媒介](https://notes.andymatuschak.org/z4rRX3qwSSJRsEkdXKwH2shamgHNeRthrMLiF)中对这种机制有更多的说明：

- [重试结果可能会给出额外的可提取性信号](https://notes.andymatuschak.org/zq2kRQRbZ5ykqy6TWtece3NscvMdjYRUZFr)