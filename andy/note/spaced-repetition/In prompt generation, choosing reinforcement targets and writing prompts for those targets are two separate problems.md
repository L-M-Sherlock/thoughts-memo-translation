# 卡片生成任务中，选择要强化的目标概念，和为这些目标概念编写卡片，是两个独立的问题

原文：[In prompt generation, choosing reinforcement targets and writing prompts for those targets are two separate problems (andymatuschak.org)](https://notes.andymatuschak.org/z62s1nNLEfhGbDmpb8Z7dZiYyi3kaSziuLVXd)

对于[使用机器学习从说明文中生成优质的间隔重复卡片](https://notes.andymatuschak.org/z2DY7qsP5iHsiA5hxUHheV8hu7Xe96vdGyYX)的问题，大多数人似乎是将语言模型对准一段文字或一个被高亮的短语，然后告诉它「就这些写一些卡片吧！」这很少会有很好的结果，除非输入的文本基本上可以完全决定卡片应该是关于什么的（比如「碳的原子序数是 6。」）

我个人的印象，仅凭直觉，是选择为什么内容写卡片比为强化一个具体的细节而写卡片要难得多。更多的信息可以在[将卡片生成任务定义为强化目标的过滤问题](https://notes.andymatuschak.org/zQ4E1DXZoZTTitsik89ZcvXMu8dQMkJzRUS)中找到。

原因之一在于，模型**无法知道**——至少在没有大量其他外部信息的情况下——你对什么感兴趣，你已经知道什么，什么对你阅读这个材料的目标来说很重要。当一位作者为普通读者写卡片时，这已经是一个问题了（参见[助记媒介应该让读者对他们收集的卡片进行控制](https://notes.andymatuschak.org/z3XqmAYKcD411jZgBik9oyXgcrarXycADWVeh)），但至少在那种情况下，作者心中有整本书的结构，并且对学习这个主题最重要的东西有强烈的观点。

另一个导致这个相对困难的原因是，我们可以给模型很多关于如何写出有效卡片的具体建议。例如，如果我们给它一个我在《如何写出好卡片》中的原则，并要求它验证它写的每一张卡片是否符合这些原则，它的表现要比简单地被要求写一个关于特定细节的卡片要好得多。相反，我们还没有一套关于目标选择的原则。我们只是告诉它例如「写出关于最重要的细节的卡片」。实际上，我们需要编码一些知识理论。在这里可能有一些进展，但我怀疑我们总是需要用户的输入，即使只是为了优化模型的选择。（在更小的范围内相关：[对于卡片生成任务，大型语言模型（LLM）缺乏为复杂概念材料编写卡片的模式](https://notes.andymatuschak.org/zmrbnm683nVZi9ut63vsr8BwYKEtATA6e4B3)）

我觉得这种困难基本上可以接受。阅读时使用荧光笔指出看起来最重要或最有趣的部分是很自然的事情（[间隔重复系统中选择去记忆某项内容的行为有如轻松的手势](https://notes.andymatuschak.org/z2vBgMKvhXq9yM4wMR3uuQVsqJRarfbfbEoWr)）。这基本上就完成了任务。回过头来，根据这些高亮部分写卡片，是相当费力和耗时的（[写好间隔重复记忆卡片很难](https://notes.andymatuschak.org/z3ntJ7w9C3uapYp1m3gy2EK6PN788guzEoUNN)）；如果模型可以帮助解决这个问题，那就太好了。即使是高亮部分也不够：[对于卡片生成任务，大型语言模型（LLM）经常需要额外的提示来确定需要强化何种角度](https://notes.andymatuschak.org/zomoPzCNzSi5GqtfTeVWgm7RjmiArjS8vvM5)。

------

过去的几年里，我有几个想法引导了我走到这里。[Ozzie Kirkby](https://notes.andymatuschak.org/zn9igQGgecLncBSpKbgv5123mC5YEAP3hnfP) 和我注意到（[2021-06-10](https://notes.andymatuschak.org/zWLsqjDeYgCEERgoVeE8BjFbPrWSPsR5WhY)），模型从已经精炼出你关心的内容的个人笔记中生成的卡片要好得多。同样，[GPT-3 可以将填空卡转换成问答卡](https://notes.andymatuschak.org/z4A7LCXBAkAUH2uZ21JnNrBhJHCjkobFMyn)，也是一个卡片生成任务，其中强化目标已经被非常准确地指定了。