# 人类的信道容量随着每个组块的比特量的增加而增加

原文：[Human channel capacity increases with bits-per-chunk (andymatuschak.org)](https://notes.andymatuschak.org/z6ZFtY8UGPaF9uofckBB7HwK62pssJAUg8C91)

如果把人类作为信息处理器，那在[人作为信息处理器时的信道容量](https://notes.andymatuschak.org/z8iJEzmLdBMoWYtQHkDohDgeWz6UBGm74qEiW)的问题上，一个常见的变通方法，是进行一系列更小的观察，而不是做单个、复杂、绝对的判断。这仅在你头脑 hold 得住如此一序列的东西时有效，所以它受限于你的记忆[工作记忆的容量界限](https://notes.andymatuschak.org/z4omDTWHCLoqW7PLpN2tiW63QzoYN5tqxPT9B)，好消息是，[工作记忆与单元复杂度无关](https://notes.andymatuschak.org/z6Pe8LaXhDBjjiiVX1Y2WJquaZyRQPTJB3y2K)。所以你可以通过在每个组块中，增加可察觉 bit 数，来提升你的「有效信道容量」（[认知中的「组块」](https://notes.andymatuschak.org/z75gWU7QuiB5L3x6zFGLGQk3fVkuVJ6eKuEwP)）。

在这个描述 Pollack（1953）数据的图中，信道容量随着每组块比特量的增加而几近线性扩展（Miller, 1956, p.92）。

![img](https://notes.andymatuschak.org/BearImages/8C535948-19D5-4CB7-91D7-6279BC04B55F-84615-0002BE396DE9900C/D1D6C134-0ADF-461B-A6CB-3207BCE86933.png)

这种效果仍然受到[绝对判断的容量界限](https://notes.andymatuschak.org/ziwhFzgTbrS2uxWEkCvoJzQrDzRz5EAWWZFy)的限制，所以要把每个数据块的比特量扩大到 5 以上，就要把数据块变成多维的（[人类的信道容量随激活维度增长](https://notes.andymatuschak.org/z7LQGcrQpYKed1qdC1nS7Dg8Ad6gdi1apWyuZ)）。

------

问：元素序列中，元素 bits 数变化时，人的信道容量如何变化？

答：它大致呈线性增长。

问：工作记忆的容量界限不受绝对判断的容量界限的影响，这点为什么很重要？

答：它表明，我们可以通增加记忆单元的「组块」大小，往工作记忆中保存更多信息。

------

## 参考文献

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97. https://doi.org/10.1037/h0043158 [Miller - The magical number seven, plus or minus two](https://notes.andymatuschak.org/zjfsd9pyxWQAF3HU5k7RAXhRjJBqtMEGKK27)

Pollack, I. (1953). Assimilation of Sequentially Encoded Information. The American Journal of Psychology, 66(3), 421–435. JSTOR. https://doi.org/10.2307/1418237