# 应用程序无法很好地记录滚动条的历史位置

原文：[Applications don’t reliably maintain scroll positions (andymatuschak.org)](https://notes.andymatuschak.org/z2aEsmuNMnFH15r8LstXK3SpX3uuHGoP4HLN)

具有长可滚动区域的界面（例如长文本，消息历史）会让人感到麻烦和不可靠，部分原因是应用开发人员没把记录阅读位置当作应用的重要组成部分。

如果用户收藏一条消息，或者打开了按条件搜索，这通常是一个持续型行为；取消操作之后数据可能会丢失。相比之下，界面中的常见操作都会丢失滚动位置。

这里的一个关键点是，虽然滚动行为通常通过一个共同的系统级组件来实现，但滚动位置的**语义**解析在应用程序状态却是由界面决定的。例如，同一个视窗可能用于显示多个不同的话题聊天记录。在某些情况下，保留并恢复最近浏览的聊天记录的滚动位置更合理；在其他情况下，为每个聊天记录独立保留滚动位置更合理。因此，保留这种状态不能通常在其本应所在的层上进行。

相关笔记：

- [连续滚动式的电子阅读扰乱了物体恒存性，令人不适](https://notes.andymatuschak.org/z6cxCDMXRWBritiSgzs4cdKd737H5U9XLBaFr) 

- [数据电子化不意味着井井有条](https://notes.andymatuschak.org/ztR58jhZh7eCJLm7Yc51wAqJVLENXNL4JDi)

------

问：为什么应用程序不能可靠地保留界面视图的滚动位置？

答：开发人员并不认为滚动位置是界面状态的重要组成部分。

问：记录滚动位置的应用程序状态有哪些难点？

答：（例如，通常 UI 框架想要成为“模型”，视窗标识的语义解释有微妙的变化，等等）

------

## 参考文献

推特用户 Omar Rizwan：「我对滚动条害怕又反感（例如，向上滚动很长时间以查看聊天记录）,因为我知道应用程序开发人员并不认真对待它们。比如我会在中途点击另一个聊天，之后又回到我曾向上滚动的聊天，然后发现原来的滚动位置已经丢失了。」