# 基于机器学习的卡片生成可以被有效的重定义为过滤问题吗？

原文：[Can ML-based prompt generation be helpfully recast as a filtering problem? (andymatuschak.org)](https://notes.andymatuschak.org/zQ4E1DXZoZTTitsik89ZcvXMu8dQMkJzRUS)

当我开始专注 [使用机器学习模型来生成高质量的间隔重复卡片](https://notes.andymatuschak.org/z2DY7qsP5iHsiA5hxUHheV8hu7Xe96vdGyYX)，我认为这个问题主要在于如何让系统产生我想要的输出。但在体验过一些模型后，我注意到

生成卡片的问题，跟让模型生成可接受的输出的问题完全不一样。或许可以开发一些过滤器，在模型生成问题之后筛选，以找出我们需要的问题。此外，我们也可以开发一个界面来辅助这个筛选问题。

什么是「不合理」的问题？我发现这些问题并不是胡言乱语，而是非常规矩的问题，也都能说得通。但这些问题中读不出对文章的有趣理解。这种「有趣」有主观因素——有些人对人物时间事件等具体细节感兴趣，有人对关键定义感兴趣，而有人对大局影响感兴趣。但我想知道的是这种有趣是否能客观评价。

比如，假设我们围绕一篇关于跑步者的文章生成问题，文章里有句话是「他绑紧了他的鞋带」，而如果有个问题是「他跑步前绑紧了什么？」，那么这个问题可以认为是客观上低质量的，其中一个因素是当代故事里的其他跑步者都会这么干（也就是说，这条信息是低熵的）。另一个更为微妙的因素是，这个细节对这个故事**并不重要**。跑步者的鞋子是无关紧要的；文章之后也没有提起。我觉得量化第一个因素是可行的，但我不确定如何量化第二个因素。有个笨想法：如果你移除文章的某处细节，文章的自编码向量会移动多少？我们能在这里使用模型的熵吗？

## 参考文献

我在 [2021年 9 月 6日](https://notes.andymatuschak.org/zYhPmghQMv93jZsGwPfLcZx7E4npiQc87xX) 与[Yuval Milo](https://notes.andymatuschak.org/zJ55L18u5sagXqnMWh5szwfZ388oGQbyfW3)的电话会谈里意识到了这点。