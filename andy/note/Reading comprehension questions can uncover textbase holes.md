# 阅读理解问题可以发现文本基础的漏洞

原文：[Reading comprehension questions can uncover textbase holes (andymatuschak.org)](https://notes.andymatuschak.org/zLZUS7KTrG4ABm3tRLGxMMj)

我有些尴尬地发现（[2023-09-11](https://notes.andymatuschak.org/z2ZU99Tadhs5MdtF8rTsSuw)），当我要求[大语言模型](https://notes.andymatuschak.org/zBe9vHWwqLoyaeA7eJfLnBA)生成阅读理解问题，以此来帮我评估我针对[《线性代数》- Hefferon](https://notes.andymatuschak.org/z4e951xY6fkjGgoHGwHHchi)某一章节所构建的文本基础（参见[构建-整合模型](https://notes.andymatuschak.org/zHTLU2rAxAo8i1xBGVQPPcr)）时，有几个问题揭示出了文本中我完全未曾理解的部分。尽管我已经努力仔细阅读。

[阅读理解问题令人不快](https://notes.andymatuschak.org/zVKwVczp4nEAKPWqfS1BqMi)，这些也不例外。关于这次我注意到的问题，我在这里加了一些笔记：

> 不幸的是，当遇到与我未能充分理解的内容相关的问题时，这种感觉**尤为**明显。这些问题对我来说似乎毫无意义。我能感觉到它们在要求我给出某种特定的答案，但我无法确定具体需要回答什么（因为我之前并未真正理解过需要的信息）。因此，这些问题就像让我盲目地追寻一样，我不得不翻来覆去地检查章节，试图找到与问题中词汇相匹配的段落。然后我才意识到，我原来根本没有真正理解过那部分内容，虽然我可能最终弄清楚了问题的意图……但这是一种不优雅的达成方式。

有趣的是，这里的机制是间接的：当阅读理解问题暴露出我理解上的失败时，我通常并不完全明白这个问题到底在问什么。但这种困惑引导我重新阅读，寻找可能有帮助的信息，这个过程最终帮助我弥补了理解上的空缺。

我假设阅读理解问题同样能揭示出我在情境模型（参见[构建-整合模型](https://notes.andymatuschak.org/zHTLU2rAxAo8i1xBGVQPPcr)）中的漏洞，尽管我对此没有太多直接体验。对我而言，通过需要推理（即[迁移学习](https://notes.andymatuschak.org/z7ffiDfqTR9pPcEEUUbCL7C)）的复杂任务来发现这些漏洞更为常见。当我无法完成这些任务，而我的文本基础又看起来很扎实时，要确定情境模型的具体崩溃点似乎颇有难度。

另见，在[助记媒介](https://notes.andymatuschak.org/zKPv6qkSErdRGqyryvgS2wS)的背景下：[助记媒介中穿插的卡片有时会不太愉快地揭示出阅读理解上的疏漏](https://notes.andymatuschak.org/z58xEZ2ojjRjm1sMcih4bfQ)。