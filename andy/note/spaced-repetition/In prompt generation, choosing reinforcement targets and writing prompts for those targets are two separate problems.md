# 卡片生成任务中，选择要强化的目标概念，和为这些目标概念编写卡片，是两个独立的问题

原文：[In prompt generation, choosing reinforcement targets and writing prompts for those targets are two separate problems (andymatuschak.org)](https://notes.andymatuschak.org/z62s1nNLEfhGbDmpb8Z7dZiYyi3kaSziuLVXd)

对于[使用机器学习从解释性文本中生成优质的间隔重复卡片](https://notes.andymatuschak.org/z2DY7qsP5iHsiA5hxUHheV8hu7Xe96vdGyYX)的问题，大多数人似乎是将语言模型对准一段文字或一个被高亮的短语，然后告诉它「就这些内容写一些卡片吧！」这很少会有可接受的结果，除非文本内容本身某种意义上可以完全决定卡片应该是关于什么的（比如「碳的原子序数是 6。」）

直觉告诉我，对语言模型而言，**选择什么内容来制卡**要比**编写强化某个具体细节的卡片**要难得多。见[将卡片生成任务定义为强化目标的过滤问题](https://notes.andymatuschak.org/zQ4E1DXZoZTTitsik89ZcvXMu8dQMkJzRUS)。

原因之一在于，模型**无法知道**—— 至少在没有大量其他外部信息的情况下 —— 你对什么感兴趣、你已经知道什么、什么对你阅读这个材料的目标来说很重要。在人类作者为一般读者写卡片，这已经是一个问题了（见[助记媒介应该让读者对他们收集的卡片进行控制](https://notes.andymatuschak.org/z3XqmAYKcD411jZgBik9oyXgcrarXycADWVeh)），但至少在那种情况下，作者心中有整本书的结构，也知道为了整体，学习哪些东西是最重要的。

另一个导致「选」比「制」更困难的原因是，我们可以给模型有效写卡的具体建议。如果我们给它一个《如何写出好卡片》中的原则，并要求以此为准验证输出的每一张卡片，它的表现要比简单地 「写一个关于 xxx（特定细节）的卡片」要好得多。相比之下，我们还没有一套关于目标选择的原则。我们只是告诉它例如「写出关于最重要的细节的卡片」。实际上，我们需要编码一些知识理论（给它）。这方面可能已经有一些进展，但我怀疑，用户的输入总是必不可少的，哪怕只为了优化模型选择。（小部分相关内容见：[对于卡片生成任务，大型语言模型（LLM）缺乏为复杂概念材料编写卡片的模式](https://notes.andymatuschak.org/zmrbnm683nVZi9ut63vsr8BwYKEtATA6e4B3)）

我觉得这种困难基本可以接受。阅读时，要是看到最重要或最有趣的部分，我们也会用荧光笔画线，这很自然（[间隔重复系统中选择去记忆某项内容的行为有如轻松的手势](https://notes.andymatuschak.org/z2vBgMKvhXq9yM4wMR3uuQVsqJRarfbfbEoWr)）。这基本上就完成了「选」。回过头来，**根据**这些高亮部分写卡片，是相当费力和耗时的（[写好间隔重复记忆卡片很难](https://notes.andymatuschak.org/z3ntJ7w9C3uapYp1m3gy2EK6PN788guzEoUNN)）；如果模型可以帮助解决这个问题，那就太好了。虽然光有高亮部分也一定不够：[对于卡片生成任务，大型语言模型（LLM）经常需要额外的提示，来确定从何种角度制卡](https://notes.andymatuschak.org/zomoPzCNzSi5GqtfTeVWgm7RjmiArjS8vvM5)。

------

过去的几年里，一些想法引导我产生如此思考。[Ozzie Kirkby](https://notes.andymatuschak.org/zn9igQGgecLncBSpKbgv5123mC5YEAP3hnfP) 和我注意到（[2021-06-10](https://notes.andymatuschak.org/zWLsqjDeYgCEERgoVeE8BjFbPrWSPsR5WhY)），模型从个人笔记生成的卡片更为优秀，这些笔记已经从较长的段落中提炼出了你关心的内容。同样，[GPT-3 可以将填空卡转换成问答卡](https://notes.andymatuschak.org/z4A7LCXBAkAUH2uZ21JnNrBhJHCjkobFMyn)，也是一个卡片生成任务，其中强化目标已经被非常准确地指定了。