# Ye, J., Su, J., & Cao, Y. (2022). A Stochastic Shortest Path Algorithm for Optimizing Spaced Repetition Scheduling. Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 4381–4390

有关[优化间隔重复系统的调度算法](https://notes.andymatuschak.org/zYK41LaWjuWkRmv3ZGnNmoF)。来自 Jarrett Ye，一位赞助者。

我觉得这篇论文里最吸引我的是他们用「半衰期」来描述[间隔重复记忆系统](https://notes.andymatuschak.org/z2D1qPwddPktBjpNuwYFVva)卡片的状态。但问题是，你没法直接量出一张卡片的半衰期。你只能做一次观察，因为每次练习都会改变接下来的半衰期。同一个项目的半衰期序列当然是相互关联的，但这仍然相当棘手。

他们的方法是根据用户群体的初次回忆率将项目分为不同「难度组」。然后，他们可以使用汇总的用户组为后续事件拟合半衰期参数。可以想象，就像[项目反应理论](https://notes.andymatuschak.org/zFkZXm2t1D4FAGGrBUUHNz4)那样，为每位用户再加一个「能力」/「熟悉度」参数。

然后，作者引入了一个马尔可夫时序模型，用于描述给定反应的半衰期和难度的转移方程组。这个方法已经被做成了 Anki 插件：[GitHub - open-spaced-repetition/fsrs4anki: A modern Anki custom scheduling based on free spaced repetition scheduler algorithm](https://github.com/open-spaced-repetition/fsrs4anki)