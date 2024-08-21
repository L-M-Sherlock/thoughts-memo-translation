# 自主评分的间隔重复记忆系统可避免假阴性

原文：[Self-graded spaced repetition memory systems avoid false negatives (andymatuschak.org)](https://notes.andymatuschak.org/z7NmYGQd6wLQr3zQcDEPMizghkD9thEhhfg2E)

在[间隔重复记忆系统](https://notes.andymatuschak.org/z4eXdSMJFv2qVGXSUEKH4vdcHBrLHcFY1ZGfC)的复习环节中，如果我因为记错了一个函数的名字而在 SQL 表达式中打错了字，那就不好了，我可能应该再复习一遍。但是，如果我因为手指打滑而打错了字，我仍然自认为是「正确的」。在机器评分的系统中，假阴性是非常令人恼火的。当然，假阴性也是低效的，因为卡片会更快地重新出现。但激怒用户才是更严重的问题。

机器分级系统引入了各种机制来避免这个问题——例如，允许用户输入与答案之间有一定的较小的编辑距离，或者为的拼写变体准备字典。这些措施必然是相当片面的。（译注：编辑距离是针对二个字符串的差异程度的量化量测，量测方式是看至少需要多少次的处理才能将一个字符串变成另一个字符串。）

更多内容请参见《为非常好奇的人提供的量子计算》中的[如何使用（或不使用！）问题](https://quantum.country/qcvc#how-to-use-or-not-use-the-questions)一节；例如：

> 你可能已经注意到这些问题是自我评估的。如果你有时即使是在你不正确的时候，但也想评为「正确」，尽可大胆去做！你认为这对你的学习会有什么影响？你喜欢这种略带背德的感觉吗？我必须承认，我喜欢。如果是的话，不要感到尴尬：这应该是，首先是乐趣。或者试着在你正确的时候给自己评分为「错误」，或者干脆跳过这些问题。这些行为对你的学习有什么影响？关键是要弄清楚如何与这些问题尽力较量，从而尽可能快地学习。这意味着要对你的学习方式进行有趣的试验，找到适合你的方法。

------

## 参考文献

Matuschak, A., & Nielsen, M. (2019, March). Quantum computing for the very curious. Quantum Country. https://quantum.country/qcvc