# 统计数据

原文：[统计数据 - SuperMemo 帮助](https://help.supermemo.org/wiki/Statistics)

## 介绍

**统计**窗口允许你检查当前打开的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的主要学习过程的统计数据。按**F5**（**[Window](https://help.supermemo.org/wiki/Window_menu)：[Layout](https://help.supermemo.org/wiki/Layouts)：Warrior布局**）可以最方便地查看它。

[![SuperMemo: 插图: 统计窗口，可以随时检查当前打开的集合的主要学习过程的统计数据](https://help.supermemo.org/images/thumb/d/de/Statistics.jpg/186px-Statistics.jpg)](https://help.supermemo.org/wiki/File:Statistics.jpg)

> ***图：**统计**窗口（**[Toolkit](https://help.supermemo.org/wiki/Toolkit_menu)：[Statistics](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：统计**），可以随时检查当前打开的[集合](https://help.supermemo.org/wiki/Glossary:Collection)的主要学习过程统计。*。

## 标题

标题在方括号中显示[集合](https://help.supermemo.org/wiki/Glossary:Collection)的名称。*当前[集合](https://help.supermemo.org/wiki/Glossary:Collection)的名称是 all.*。

## 工具栏

- [日历](https://help.supermemo.org/wiki/Calendar)

    每日和每月的复习日历

- 统计菜单

    可通过右键菜单打开统计内容菜单，也可以在窗口上点击右键

- [分析](https://help.supermemo.org/wiki/Analysis)

    与学习过程和[SuperMemo算法]有关的各种统计数据(https://supermemo.guru/wiki/SuperMemo_Algorithm)

- [记忆图谱](https://help.supermemo.org/wiki/Memory_graphs_(4D))

    记忆函数的可视化展示，基于[SM-18 算法](https://supermemo.guru/wiki/Algorithm_SM-18)的近似估计，以及基于[复习历史](https://help.supermemo.org/wiki/Repetition_history)重置和重新计算的一些选项。

- 勇士布局

    以最适合[渐进阅读](https://help.supermemo.org/wiki/Glossary:Incremental_reading)的方式排列窗口，其中**统计**窗口被方便地排列在[元素窗口](https://help.supermemo.org/wiki/Element_window)的左边。

- 帮助

    查看此帮助文章

## 学习参数

为了方便地比较示范性字段和其相应的描述：

1.按住 Shift 后点击上面的图片，在一个新的浏览器窗口以其完整分辨率打开。

2. 将图片窗口的标题栏拖到屏幕的左边或右边，直到出现一个扩大的窗口的轮廓

3. 松开鼠标，扩大窗口

4. 用这个窗口重复步骤2和3，将窗口并排排列

### 日期

当前的日期和星期。如果这个值前面有*Night*，意味着新的日历日已经开始，但旧的重复日要到**[工具包:Toolkit](https://help.supermemo.org/wiki/Toolkit_menu)：[Options:选项](https://help.supermemo.org/wiki/Options)：[Learning:学习](https://help.supermemo.org/wiki/Learning_tab_in_Options)：[Midnight shift:午夜交替](https://help.supermemo.org/wiki/Learning_tab_in_Options#Midnight_clock_shift)**中定义的时间才会开始。当过了午夜交替的时间，这个字段会显示一个红色的警告*关闭时间到:Alt+F4*。如果你看到这个信息，请关闭/重新启动你的[集合:collection](https://help.supermemo.org/wiki/Glossary:Collection)，以防止收集到重复时间未定的学习数据。**在上面的例子中，图片是在2019年4月1日（星期一）午夜后截取的*。

### 第一天

学习过程开始的日期（即记住第一个[元素:element](https://help.supermemo.org/wiki/Glossary:Element)的日子）。*图片中呈现的典范[集合:Collection](https://help.supermemo.org/wiki/Glossary:Collection)自1987年12月15日开始使用(即[DOS 版本的SuperMemo诞生时间](https://supermemo.guru/wiki/SuperMemo_1.0_for_DOS_(1987))的后两天)*。

### 周期

学习过程中的天数（即**[日期:Date](https://help.supermemo.org/wiki/Statistics#Date)**和**[第一天:First day](https://help.supermemo.org/wiki/Statistics#First_day)**之间的天数）。

> ```

> 周期=日期-第一天

> ```

*当前展示的[收集箱:collection](https://help.supermemo.org/wiki/Glossary:Collection)已经使用了31年3个月17天*。

### 已记忆

在学习过程中引入的[元素:Element](https://help.supermemo.org/wiki/Glossary:Element)的总数，选项包括**[学习:Learn](https://help.supermemo.org/wiki/Learn)**或**[记忆:Remember](https://help.supermemo.org/wiki/Glossary:Remember)**。如果一个[条目:item](https://help.supermemo.org/wiki/Glossary:Item)参加了[重复:Repetition](https://help.supermemo.org/wiki/Glossary:Repetition)，它就是一个[已记忆:Memorized](https://help.supermemo.org/wiki/Glossary:Memorized_element)[条目:Item](https://help.supermemo.org/wiki/Glossary:Item)。这并不意味着它是一个记住的[条目:item](https://help.supermemo.org/wiki/Glossary:Item)。一部分[已记忆_元素:Memorized_element](https://help.supermemo.org/wiki/Glossary:Memorized_element)[条目:item](https://help.supermemo.org/wiki/Glossary:Item)总是被遗忘。*呈现的[集合 Collection](https://help.supermemo.org/wiki/Glossary:Collection)有 635,699 个[元素 Element](https://help.supermemo.org/wiki/Glossary:Element)在学习过程中，这些元素占所有注定要进入学习过程的元素的100.0%，即`记忆的/（记忆的+待定的）=100.0`。这表明推迟=0（见[推迟Pending]（https://help.supermemo.org/wiki/Statistics#Pending））*。

### 已记忆项目

在[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的[已记忆元素](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量和记忆的[元素](https://help.supermemo.org/wiki/Glossary:Element)中记忆的[项目](https://help.supermemo.org/wiki/Glossary:Item)的比例。*在上面的例子中，203,827个[项目](https://help.supermemo.org/wiki/Glossary:Item)参与了重复。这些[项目](https://help.supermemo.org/wiki/Glossary:Item)占参加学习过程的所有[元素](https://help.supermemo.org/wiki/Glossary:Element)的32.1%（其余67.9%的[元素](https://help.supermemo.org/wiki/Glossary:Element)是[已记忆元素](https://help.supermemo.org/wiki/Glossary:Memorized_element)[主题](https://help.supermemo.org/wiki/Glossary:Topic)、记忆的[概念](https://help.supermemo.org/wiki/Glossary:Concept)或记忆的[任务](https://help.supermemo.org/wiki/Glossary:Task)）。**[保留率](https://help.supermemo.org/wiki/Statistics#Retention)**字段表明，这些[项目](https://help.supermemo.org/wiki/Glossary:Item)的92.4937%在任何时候都应该被记住*。

### 已记忆的主题

[已记忆元素](https://help.supermemo.org/wiki/Glossary:Memorized_element)[主题](https://help.supermemo.org/wiki/Glossary:Topic)、[概念](https://help.supermemo.org/wiki/Glossary:Concept)和[任务](https://help.supermemo.org/wiki/Glossary:Task)的数量以及它们在所有记忆的[元素](https://help.supermemo.org/wiki/Glossary:Element)中的累积比例。在一个均衡的[增量阅读](https://help.supermemo.org/wiki/Glossary:Incremental_reading)过程中，[主题](https://help.supermemo.org/wiki/Glossary:Topic)应该使少数[元素](https://help.supermemo.org/wiki/Glossary:Element)用于[回顾](https://help.supermemo.org/wiki/Glossary:Review)。如果[话题](https://help.supermemo.org/wiki/Glossary:Topic)的比例增加，[保持率](https://help.supermemo.org/wiki/Glossary:Retention)就会下降，学习过程可能逐渐开始类似于传统的学习，无效的[被动复习](https://help.supermemo.org/wiki/Glossary:Passive_review)占主导。你可以在你的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中放置尽可能多的[主题](https://help.supermemo.org/wiki/Glossary:Topic)，只要你确保通过设置适当的[卡片排序标准](https://help.supermemo.org/wiki/Priority_queue#Sorting_repetitions)来限制它们的[复习](https://help.supermemo.org/wiki/Glossary:Review)（**[Learn_menu](https://help.supermemo.org/wiki/Learn_menu) : [排序](https://help.supermemo.org/wiki/Learn_menu#Sorting) : 排序标准 **）。*在图片中，431,872 个[主题](https://help.supermemo.org/wiki/Glossary:Topic)使67.9%的材料参加了学习过程*。

### 已记忆/天

每天记忆的[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量。`（记忆的项目）/日`。*在这个例子中，在过去31年多的时间里，平均每天有 17.8311个[项目](https://help.supermemo.org/wiki/Glossary:Item)在当前展示的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中被记忆。只要每天执行定期复习，这就是普通学生的典型情况*。

### 总计

在[集合](https://help.supermemo.org/wiki/Glossary:Item)中的[项目](https://help.supermemo.org/wiki/Glossary:Item)、[主题](https://help.supermemo.org/wiki/Glossary:Topic)、[概念](https://help.supermemo.org/wiki/Glossary:Concept)和[任务](https://help.supermemo.org/wiki/Glossary:Task)数量。有这样两种关系:

> ```

> 总计=已记忆的+待定的+丢弃的

> ```

> `总计=主题+条目`（[概念](https://help.supermemo.org/wiki/Glossary:Concept)和[任务](https://help.supermemo.org/wiki/Glossary:Task)用**主题**统计法计算）

被删除的[元素](https://help.supermemo.org/wiki/Glossary:Element)不会对[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的元素总数有所贡献。*在图片中，所展示的集合由727,259个[元素](https://help.supermemo.org/wiki/Glossary:Element)组成（目前用户报告的最大[集合](https://help.supermemo.org/wiki/Glossary:Collection)数量高达到50万元素以上）*。

### 条目

[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的[条目](https://help.supermemo.org/wiki/Glossary:Item)的数量。*在这个例子中，集合包括 207,443个条目**。

### 主题

[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的[主题](https://help.supermemo.org/wiki/Glossary:Topic)、[概念](https://help.supermemo.org/wiki/Glossary:Concept)和[任务](https://help.supermemo.org/wiki/Glossary:Task)的数量。*当前展示的集合包括519,816个主题（与概念和任务一起计算）*。

#＃＃ 优秀

计划在这一天进行[重复](https://help.supermemo.org/wiki/Glossary:Repetition)的[未决](https://help.supermemo.org/wiki/Glossary:Outstanding_material)[项目](https://help.supermemo.org/wiki/Glossary:Item)、未决[主题](https://help.supermemo.org/wiki/Glossary:Topic)和[最后演练](https://help.supermemo.org/wiki/Glossary:Final_drill)项目的数量。第一个数字(加号之前)表示这一天安排的、尚未处理的[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量。第二个数字(+号后)表示这一天安排[复习](https://help.supermemo.org/wiki/Glossary:Review)的[题目](https://help.supermemo.org/wiki/Glossary:Topic)的数量。第三个数字（在第二个 "+"后面），如果有的话，表示今天已经重复过的[题目](https://help.supermemo.org/wiki/Glossary:Item)的数量，但得分低于**好（4）**。这些是组成[最终演练队列](https://help.supermemo.org/wiki/Glossary:Final_drill_queue)的[项目](https://help.supermemo.org/wiki/Glossary:Item)。只有在**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[选项](https://help.supermemo.org/wiki/Options)：[学习](https://help.supermemo.org/wiki/Learning_tab_in_Options)**中未勾选**Skip final drill**时，才会建立最终演练队列。*在提出的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，仍有3521个[项目](https://help.supermemo.org/wiki/Glossary:Item)计划在2019年4月1日进行[重复](https://help.supermemo.org/wiki/Glossary:Repetition)。还有1297个[主题](https://help.supermemo.org/wiki/Glossary:Topic)计划在这一天进行[复习](https://help.supermemo.org/wiki/Glossary:Review)，作为[增量阅读](https://help.supermemo.org/wiki/Glossary:Incremental_reading)过程的一部分。在[最终演练队列](https://help.supermemo.org/wiki/Glossary:Final_drill_queue)中没有[元素](https://help.supermemo.org/wiki/Glossary:Element)（**Outstanding**参数的第三个组成部分缺失）*。

### 评论

为[子集复习](https://help.supermemo.org/wiki/Subset_learning)安排的[元素](https://help.supermemo.org/wiki/Glossary:Element)的数量（例如，**[学习](https://help.supermemo.org/wiki/Learn_menu)中的[神经复习](https://help.supermemo.org/wiki/Subset_learning#Neural_review)中的元素：[去神经](https://help.supermemo.org/wiki/Learn_menu#Go_neural)**，**[内容](https://help.supermemo.org/wiki/Contents)中的[分支重复](https://help.supermemo.org/wiki/Subset_review#Branch_review)的[元素](https://help.supermemo.org/wiki/Glossary:Element)**[学习](https://help.supermemo.org/wiki/Subset_learning）**，[浏览器](https://help.supermemo.org/wiki/Browser)的**[学习](https://help.supermemo.org/wiki/Subset_learning)**中[浏览器子集重复](https://help.supermemo.org/wiki/Subset_review#Search_and_review)中的[元素](https://help.supermemo.org/wiki/Glossary:Element)，**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[随机测试](https://help.supermemo.org/wiki/Toolkit_menu#Random_test)**中的[随机测试]（https://help.supermemo.org/wiki/Toolkit#Random_test）队列中的[元素]（https://help.supermemo.org/wiki/Glossary:Element）等等）。显示的形式可能是*神经=<[元素](https://help.supermemo.org/wiki/Glossary:Element)要做>*在[神经审查](https://help.supermemo.org/wiki/Neural_creativity)中，或*<[项目](https://help.supermemo.org/wiki/Glossary:Item)要做>+<[主题](https://help.supermemo.org/wiki/Glossary:Topic)要做>+<[待处理](https://help.supermemo.org/wiki/Glossary:Pending_element)要做>+（<子集描述>）*在[子集审查](https://help.supermemo.org/wiki/Subset_learning)中，或*<[元素](https://help.supermemo.org/wiki/Glossary:Element)未处理>/<测试中的所有<元素>(https://help.supermemo.org/wiki/Glossary:Element)>*在随机测试。*这里有16个[项目](https://help.supermemo.org/wiki/Glossary:Item)留在[子集审查](https://help.supermemo.org/wiki/Subset_learning)中*。

### 保护

当天的最优先材料的处理程度。**重要的是**。由于统计是取自[未完成](https://help.supermemo.org/wiki/Glossary:Outstanding_material)[项目](https://help.supermemo.org/wiki/Glossary:Item)或[主题](https://help.supermemo.org/wiki/Glossary:Topic)队列的顶端（而不是[未完成队列](https://help.supermemo.org/wiki/Glossary:Outstanding_queue)的顶端，后者是两者的随机混合），如果你改变了顶端[项目](https://help.supermemo.org/wiki/Glossary:Priority），你会在**统计中看到一个错误的值，直到你审查那个改变了[优先级](https://help.supermemo.org/wiki/Glossary:Priority)的[项目](https://help.supermemo.org/wiki/Glossary:Item)（这种行为的设计是为了防止每次更新统计时需要扫描整个队列）。*在这个例子中，只有0.031%的最高优先级[项目](https://help.supermemo.org/wiki/Glossary:Item)，以及0%的最高优先级[主题](https://help.supermemo.org/wiki/Glossary:Topic)被处理过。0.031%的保护并不意味着要通过0.031%的未决项目队列。它意味着队列中最高[优先级](https://help.supermemo.org/wiki/Glossary:Priority)的未处理[议题](https://help.supermemo.org/wiki/Glossary:Item)是0.031%*。

### 留任

估计[收藏](https://help.supermemo.org/wiki/Glossary:Collection)中的平均知识[保留](https://help.supermemo.org/wiki/Glossary:Retention)。高[优先级](https://help.supermemo.org/wiki/Glossary:Priority)[项目](https://help.supermemo.org/wiki/Glossary:Item)的[保留率](https://help.supermemo.org/wiki/Glossary:Retention)应该高于所列的。低[优先级](https://help.supermemo.org/wiki/Glossary:Priority)[项目](https://help.supermemo.org/wiki/Glossary:Item)的[保留率](https://help.supermemo.org/wiki/Glossary:Retention)可能会低得多，导致平均数下降。要判断最高优先级材料的[保留率](https://help.supermemo.org/wiki/Glossary:Retention)，请参见**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：[分析](https://help.supermemo.org/wiki/Analysis)：[图表](https://help.supermemo.org/wiki/Analysis#Graphs)：[遗忘指数与优先级](https://help.supermemo.org/wiki/Analysis#Forgetting_Index_vs._Priority) **。*在这个例子中，在任何时候对[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的所有[元素](https://help.supermemo.org/wiki/Glossary:Element)进行随机测试，92.4937%的材料都应该被召回。你可以用[随机测试](https://help.supermemo.org/wiki/Toolkit#Random_test)来测试你的[保留](https://help.supermemo.org/wiki/Glossary:Retention)，看看SuperMemo的估计是否准确。如果你最近滥用了诸如**[Postpone](https://help.supermemo.org/wiki/Postpone)**或**[Mercy](https://help.supermemo.org/wiki/Mercy)**等重新安排时间的工具，这个统计数字可能过于乐观。**。**

### 测量的 FI

在[重复次数](https://help.supermemo.org/wiki/Glossary:Repetition)中记录的[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)的值。括号内的数字表示当天的**测量的FI**。在有大量[项目](https://help.supermemo.org/wiki/Glossary:Item)[超载](https://help.supermemo.org/wiki/Glossary:Overload)的[文集](https://help.supermemo.org/wiki/Glossary:Collection)中，[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)可能比整个[文集](https://help.supermemo.org/wiki/Glossary:Collection)的整体[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)低很多，这是因为重复的内容主要包括高[优先](https://help.supermemo.org/wiki/Glossary:Priority)材料。当从更随机的排序过渡到更优先的排序（由[排序标准](https://help.supermemo.org/wiki/Priority_queue#Sorting_repetitions)决定），或者当[知识形成和记忆技能](http://www.super-memory.com/articles/20rules.htm)提高时，它也可能低于[要求的遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index)，而这一事实可以反映在[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)上。**测量的 FI**高于**[平均FI](https://help.supermemo.org/wiki/Statistics#Average_FI)**的情况也不少见。这是由三个因素造成的。

1.每个用户都会时不时地遇到重复的延迟（例如，由于使用**[Postpone](https://help.supermemo.org/wiki/Postpone)**）。

2.超负荷的[增量阅读](https://help.supermemo.org/wiki/Incremental_reading)过程中的低[优先级](https://help.supermemo.org/wiki/Glossary:Priority)材料被安排在比[最佳间隔](https://help.supermemo.org/wiki/Glossary:Optimum_interval)更长的[间隔](https://help.supermemo.org/wiki/Glossary:Interval)中，并且

3.SuperMemo 对[间隔](https://help.supermemo.org/wiki/Glossary:Interval)的长度施加了一些限制，在某些情况下，使得它安排的重复次数比[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)所暗示的要晚。例如，计算[间隔](https://help.supermemo.org/wiki/Glossary:Interval)中的约束，阻止了新的间隔比旧的间隔短（假设[项目](https://help.supermemo.org/wiki/Glossary:Item)没有被遗忘）。对于[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)的低值和困难的[项目](https://help.supermemo.org/wiki/Glossary:Item)，新的[最佳区间](https://help.supermemo.org/wiki/Glossary:Optimum_interval)可能经常比旧的短!**测量的FI**可以通过**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：重置参数：遗忘指数记录**来重置。

*在提出的例子中，平均有 14.63% 的[项目](https://help.supermemo.org/wiki/Glossary:Item)[重复](https://help.supermemo.org/wiki/Glossary:Repetition)以低于**通过(3)**的[成绩](https://help.supermemo.org/wiki/Glossary:Grade)结束（因为[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)记录最后被重置）。2019年4月1日，到目前为止，没有任何一次重复以失败告终（即成绩低于**Pass**）*。

### R-Metric

两种[间隔重复](https://help.supermemo.org/wiki/Glossary:Spaced_repetition)算法在[成绩](https://help.supermemo.org/wiki/Glossary:Grade)打分之前，根据其预测回忆的能力，对性能的绝对衡量。在[SuperMemo 18](https://help.supermemo.org/wiki/What's_new_in_SuperMemo_18%3F)中，**R-Metric**仅用于比较[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)（从SuperMemo 16中得知）和新的[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18) 。它在**统计**和**[工具包](https://help.supermemo.org/wiki/Toolkit_menu) : [统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics) : [分析](https://help.supermemo.org/wiki/Analysis) : [使用](https://help.supermemo.org/wiki/Analysis#Use) : 效率 : [R-计量](https://help.supermemo.org/wiki/Analysis#Use_:_Efficiency_:_R-Metric) **中以百分比显示。**R-Metric**是两种算法性能的差异：`R-Metric=LSRM(Alg-15)-LSRM(Alg-18)`，其中`LSRM`是给定算法的最小二乘法预测召回措施。**R-Metric**大于零表明[算法SM-18]（https://supermemo.guru/wiki/Algorithm_SM-18）的优越性。**R-Metric**小于零表示新算法的表现不佳。`LSRM`是召回率预测的平方绝对差异的平均值的平方根。`abs(Recall-PredictedRecall)`，其中`Recall`对于不及格的[成绩](https://help.supermemo.org/wiki/Glossary:Grade)为 0，`Recall`对于合格的成绩为1。`PredictedRecall`是算法在[重复]之前发出的预测(https://help.supermemo.org/wiki/Glossary:Repetition)。在[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)中，预测是取自[Recall[\]矩阵](https://help.supermemo.org/wiki/Glossary:Recall_matrix)的值和从[S(稳定性)](https://help.supermemo.org/wiki/Glossary:Stability)和使用的[区间](https://help.supermemo.org/wiki/Glossary:Interval)计算的[R(可检索性)](https://help.supermemo.org/wiki/Glossary:Retrievability)的加权平均。使用的权重是基于先前的重复案例，这些案例告知了Recall[]矩阵预测的重要性（预测随着先前重复数据的增加而变得更有意义）。

- `R-Metric=LSRM（Alg-15）-LSRM（Alg-18）`

- `LSRM(Alg)=sqrt(sum(sqr(ARD)))'

- `ARD=abs(Recall-PredictedRecall)`

- 等级>=3时，"记忆 "为1，等级<3时，"记忆 "为0

- ```

    预测召回

    ```

    在

    超级备忘录18

    :

    - ```

        权重*召回[]+（1-权重）**R

        ```

        - 权重（0...1）"取决于之前的重复案例的数量

        - `R=exp(-kt/s)`

*在这种情况下，18.0899%的 R-Metric 显示出[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)在那一天（2019年4月1日）比[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)有巨大优势*。

### 警报

距离下一次闹钟的时间和闹钟响起的时间（要了解更多关于闹钟的信息，请看。[计划](https://help.supermemo.org/wiki/Plan)）。这个字段是可编辑的。要改变报警设置，请点击该字段并输入新的时间（以分钟为单位）（例如21.5将设置报警在21分30秒后响起）。要结束编辑，请按**Enter**。*在这个例子中，警报将在20分21秒后的00:52:13（即午夜后52分钟）响起*。

### 负担

对每天重复的[项目](https://help.supermemo.org/wiki/Glossary:Item)和[主题](https://help.supermemo.org/wiki/Glossary:Topic)的平均数量的估计。这个数值等于[所有区间倒数之和](https://help.supermemo.org/wiki/Glossary:Burden)（即1/[区间](https://help.supermemo.org/wiki/Glossary:Interval)）。这个数字的解释如下：每个[项目](https://help.supermemo.org/wiki/Glossary:Item)的[间隔](https://help.supermemo.org/wiki/Glossary:Interval)为100天，平均每天重复1/100次。因此，间隔的倒数之和是[收藏](https://help.supermemo.org/wiki/Glossary:Collection)中总的[重复工作量](https://help.supermemo.org/wiki/Calendar)的良好指标。*所介绍的文集每天需要153个[项目](https://help.supermemo.org/wiki/Glossary:Item)[重复](https://help.supermemo.org/wiki/Glossary:Repetition)，每天需要758个[主题](https://help.supermemo.org/wiki/Glossary:Topic)[回顾](https://help.supermemo.org/wiki/Glossary:Review)。在[增量阅读](https://help.supermemo.org/wiki/Incremental_reading)中，在这个过程中出现许多超出自己能力的[元素](https://help.supermemo.org/wiki/Glossary:Element)是很平常的。**[自动延期](https://help.supermemo.org/wiki/Glossary:Auto-postpone)**可以用来卸载多余的[主题](https://help.supermemo.org/wiki/Glossary:Topic)，以及减少低[优先级](https://help.supermemo.org/wiki/Glossary:Priority)[项目](https://help.supermemo.org/wiki/Glossary:Item)的负载。**[推迟](https://help.supermemo.org/wiki/Postpone)**使**负担**的统计数字出现偏差。[主题](https://help.supermemo.org/wiki/Glossary:Topic)经常挤在较低的[间隔](https://help.supermemo.org/wiki/Glossary:Interval)，并定期用**[推迟](https://help.supermemo.org/wiki/Postpone)**或**[自动推迟](https://help.supermemo.org/wiki/Glossary:Auto-postpone)***进行重新洗牌。

### 负担 +/-

上述**[负担](https://help.supermemo.org/wiki/Statistics#Burden)**参数在某一天的变化。*在这里，2019年4月1日，平均每天预期的[重复次数](https://help.supermemo.org/wiki/Glossary:Repetition)略有减少（即减少1.5[项](https://help.supermemo.org/wiki/Glossary:Item)）。主题](https://help.supermemo.org/wiki/Glossary:Topic)的负担也减少了（即减少了近166个[主题](https://help.supermemo.org/wiki/Glossary:Topic)）。负担变化的典范解释。比方说，**负担**减少了39（负担变化为-39）。为了减少39个负担，我们需要审查78个[元素](https://help.supermemo.org/wiki/Glossary:Element)，[间隔](https://help.supermemo.org/wiki/Glossary:Interval)从1天增加到2天（78/0.5=39）。然而，我们同样可以对2344个[元素](https://help.supermemo.org/wiki/Glossary:Element)执行**[推迟](https://help.supermemo.org/wiki/Postpone)**，[间隔](https://help.supermemo.org/wiki/Glossary:Interval)从10天增加到12天（2344\*(1/10-1/12)=39）*。

### 平均工作量

平均每天花在回答问题上的时间（从学习的第一天开始）。*对于所提出的[集合](https://help.supermemo.org/wiki/Glossary:Collection)，从2019年4月1日到1987年12月15日最开始的[重复](https://help.supermemo.org/wiki/Glossary:Repetition)这段时间内，学生平均每天花16分钟59秒回答[项目](https://help.supermemo.org/wiki/Glossary:Item)。

### Exp Workload

对某一[集合]中用于回答问题的平均每日时间的估计(https://help.supermemo.org/wiki/Glossary:Collection)。

> ```

> Exp Workload=（项目负担）*Avg time

> ```

*在提出的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，每天153个[项目](https://help.supermemo.org/wiki/Glossary:Item)[重复](https://help.supermemo.org/wiki/Glossary:Repetition)（[**负担+/-**](https://help.supermemo.org/wiki/Statistics#Burden_.2B.2F-)），每个需要10.241秒（[**平均时间**](https://help.supermemo.org/wiki/Statistics#Avg_time)），因此每天重复时间估计为26分钟10秒。由于评分、编辑、审查[文集](https://help.supermemo.org/wiki/Glossary:Collection)和各种干扰，真正的学习时间可能要长一倍。在[增量阅读](https://help.supermemo.org/wiki/Incremental_reading)中，由于[题目](https://help.supermemo.org/wiki/Glossary:Topic)[复习](https://help.supermemo.org/wiki/Glossary:Review)没有考虑到**Exp Workload**参数，学习时间将进一步增加。如果经常使用**[推迟](https://help.supermemo.org/wiki/Postpone)**，实际学习时间也可能被削减*。

### 时间

某一天的总问题回复时间和总会议时间（括号内）。*在这里，2019年4月1日回应问题所需的总时间是 2 分 11 秒。在同一天，SuperMemo已经运行了2小时9分47秒（即使你只是保持SuperMemo运行，这个值也会增加）*。

### 平均时间

平均响应时间（秒）。这是显示问题（或类似问题）和选择**显示答案**（或类似答案）之间的时间。如果你在按下**显示答案**前开始编辑问题，则计时器不会停止。*在提出的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，回答一个问题的平均时间约为10.241秒。如果这个数字增长超过15-20秒，你可能需要分析你的学习材料，如果它不是过于困难或[结构不好](http://super-memory.com/articles/20rules.htm)*。

### 总时间

在[集合]中回答问题所花费的总时间(https://help.supermemo.org/wiki/Glossary:Collection)。对于用SuperMemo 98或更早创建的集合来说，这个时间是无法准确测量的（只有在SuperMemo 99中才可以测量）。如果你升级了旧的[集合](https://help.supermemo.org/wiki/Glossary:Collection)，这个数字将大致为你所猜测。SuperMemo将从[项目]的总数(https://help.supermemo.org/wiki/Glossary:Item)、[重复]的平均数(https://help.supermemo.org/wiki/Glossary:Repetition)、[失效]的平均数(https://help.supermemo.org/wiki/Glossary:Lapse)和平均重复时间得出这个时间。*在所介绍的例子中，在 31 年的学习中，在重复过程中回答问题总共花了134天以上*。

### 遗忘次数

个别[项目](https://help.supermemo.org/wiki/Glossary:Item)在[集合](https://help.supermemo.org/wiki/Glossary:Collection)中被遗忘的平均次数（只有[记忆的元素](https://help.supermemo.org/wiki/Glossary:Memorized_element)是平均的）。括号里的数字表示某一天的[遗忘](https://help.supermemo.org/wiki/Glossary:Lapse)次数。*这里平均一个[项目](https://help.supermemo.org/wiki/Glossary:Item)被遗忘了0.49800次。在 2019 年 4 月 1 日，到目前为止，没有一个[项目](https://help.supermemo.org/wiki/Glossary:Item)的评分低于**通过(3)**。

### 速度

[平均知识获取率](https://help.supermemo.org/wiki/Glossary:Acquisition_rate)，即每日工作每分钟每年记忆的[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量（只计算回答项目问题）。最初，这个值可能高达100,000条/年/分钟（特别是如果你在真正衡量程序的局限性以及人类记忆的局限性之前就热情地开始使用该程序）。这个参数后来应该稳定在 40 到 400 条/年/分钟之间。

> ```

> 速度=（记忆的项目/天）/（重复时间）**365

> ```

*在提出的[收集](https://help.supermemo.org/wiki/Glossary:Collection)中，每天每分钟的工作都会导致每年有 354 个新的[项目](https://help.supermemo.org/wiki/Glossary:Item)被记住*。

### 平均成本

记忆一个[项目](https://help.supermemo.org/wiki/Glossary:Item)的时间成本，即总的学习时间除以[记忆的](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量。

> ```

> 平均成本=总时间/记忆的项目

> ```

*在所提出的例子中，每个单一[项目](https://help.supermemo.org/wiki/Glossary:Item)的总重复时间是 1 分 1 秒，这是它对不间断的近135天重复的总时间的贡献。编辑、馆藏重组、[渐进阅读](https://help.supermemo.org/wiki/Glossary:Incremental_reading)等的成本不包括在**平均成本**参数中。

### 期望成本

假设没有推迟，每个新[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的每日重复时间。

> ```

> Exp Cost=Exp Workload/(Memorized items/Day)

> ```

*在所介绍的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，每天新[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)的18个[项目](https://help.supermemo.org/wiki/Glossary:Item)中的每一个都贡献了 2 分11秒的重复次数，每天的总工作量超过26分钟。由于这个数值是由**[负担](https://help.supermemo.org/wiki/Statistics#Burden)**得出的，如果你经常使用**[推迟](https://help.supermemo.org/wiki/Postpone)**，它可能被高度高估（例如在[增量阅读](https://help.supermemo.org/wiki/Glossary:Incremental_reading)中）*。

### 间隔 (I)

在[收藏](https://help.supermemo.org/wiki/Glossary:Collection)中，[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的平均[间隔](https://help.supermemo.org/wiki/Glossary:Interval)。*在这里，一个平均记忆的项目已经达到了 9 年10个月18天的[重复](https://help.supermemo.org/wiki/Glossary:Repetition)[间隔](https://help.supermemo.org/wiki/Glossary:Interval)*。

### 间隔 (T)

在[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，[记忆的](https://help.supermemo.org/wiki/Glossary:Memorized_element)[主题](https://help.supermemo.org/wiki/Glossary:Topic)的平均[间隔](https://help.supermemo.org/wiki/Glossary:Interval)。*在这里，一个平均记忆的主题已经达到了 6 年 10 个月 13 天的[重复](https://help.supermemo.org/wiki/Glossary:Repetition)[间隔](https://help.supermemo.org/wiki/Glossary:Interval)*。

### 重复次数

在[文集](https://help.supermemo.org/wiki/Glossary:Collection)中，每个[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)(I)和[主题](https://help.supermemo.org/wiki/Glossary:Topic)(T)的平均[重复次数](https://help.supermemo.org/wiki/Glossary:Repetition)/[评论](https://help.supermemo.org/wiki/Glossary:Review)。*在这里，平均[项目](https://help.supermemo.org/wiki/Glossary:Item)被重复了 3.197 次，而平均[主题](https://help.supermemo.org/wiki/Glossary:Topic)被评论了2.369次*。

### 代表数

在[藏品](https://help.supermemo.org/wiki/Glossary:Item)中的[项目](https://help.supermemo.org/wiki/Glossary:Repetition)的总计数。*在所介绍的藏品中，有 957 个以上的项目被重复了。这几乎是每个[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的5次重复。这包括被重置、遗忘、[驳回](https://help.supermemo.org/wiki/Glossary:Dismissed_element)、删除等的[重复](https://help.supermemo.org/wiki/Glossary:Repetition)[项目](https://help.supermemo.org/wiki/Glossary:Item)*。

### 最后一次代表(I)

在[收藏](https://help.supermemo.org/wiki/Glossary:Collection)中的[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)中，最后一次[重复]的平均日期(https://help.supermemo.org/wiki/Glossary:Repetition)。*这里，最后一次重复的平均日期是 2009 年7月17日*。

### 最后一次代表 (T)

最后一次[复习](https://help.supermemo.org/wiki/Glossary:Review)的平均日期在[收藏](https://help.supermemo.org/wiki/Glossary:Memorized_element)[专题](https://help.supermemo.org/wiki/Glossary:Topic)中。*这里的最后一次复习的平均日期是2012年8月 15 日*。

### 下一个代表(I)

在[收集](https://help.supermemo.org/wiki/Glossary:Collection)的[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)中，下一次[重复]的平均日期(https://help.supermemo.org/wiki/Glossary:Repetition)。

> ```

> 下一个报告(I)=最后一个报告(I)+间隔(I)

> ```

*这里，下一次重复的平均日期是 2019 年 6 月 3 日或2009年7月17日之后的3,609天*。

### 下一次重复 (T)

在[文集](https://help.supermemo.org/wiki/Glossary:Collection)的[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[主题](https://help.supermemo.org/wiki/Glossary:Topic)中，下一次[复习](https://help.supermemo.org/wiki/Glossary:Review)的平均日期。

> ```

> 下一个报告(T)=最后一个报告(T)+间隔(T)

> ```

*这里，下一次审查的平均日期是2019年6月29日或2012年8月15日之后的2510天*。

### 等待

尚未被引入学习过程并等待记忆的[元素](https://help.supermemo.org/wiki/Glossary:Element)（[主题](https://help.supermemo.org/wiki/Glossary:Topic)或[项目](https://help.supermemo.org/wiki/Glossary:Item)）的数量（通过**[学习](https://help.supermemo.org/wiki/Learn)**、**[记忆](https://help.supermemo.org/wiki/Glossary:Remember)**、**计划**等操作）。所有的[待定元素](https://help.supermemo.org/wiki/Glossary:Pending_element)都被保存在所谓的[待定队列](https://help.supermemo.org/wiki/Glossary:Pending_queue)中，它决定了学习新[元素](https://help.supermemo.org/wiki/Glossary:Element)的顺序。[解除的元素](https://help.supermemo.org/wiki/Glossary:Dismissed_element)不保留在[待定队列](https://help.supermemo.org/wiki/Glossary:Pending_queue)中。**在这个例子中，[集合](https://help.supermemo.org/wiki/Glossary:Collection)不包含[待定元素](https://help.supermemo.org/wiki/Glossary:Pending_element)。有了[增量阅读](https://help.supermemo.org/wiki/Glossary:Incremental_reading)，[待定队列](https://help.supermemo.org/wiki/Glossary:Pending_queue)在SuperMemo中的作用正在减弱*。

### 搁置

被排除在学习过程之外，只作为参考材料、[知识树](https://help.supermemo.org/wiki/Glossary:Knowledge_tree)中的文件夹或[任务清单](https://help.supermemo.org/wiki/Glossary:Tasklist)的[元素](https://help.supermemo.org/wiki/Glossary:Element)的数量。[解散的](https://help.supermemo.org/wiki/Glossary:Dismissed_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)既不是[待定的](https://help.supermemo.org/wiki/Glossary:Pending_element)也不是[记忆的](https://help.supermemo.org/wiki/Glossary:Memorized_element)。所有的[任务](https://help.supermemo.org/wiki/Glossary:Task)默认为[驳回](https://help.supermemo.org/wiki/Glossary:Dismiss)，也就是说，它们通常不参与[重复](https://help.supermemo.org/wiki/Glossary:Repetition)。*在这个例子中，超过91,000个[元素](https://help.supermemo.org/wiki/Glossary:Element)已经被[驳回](https://help.supermemo.org/wiki/Glossary:Dismiss)*。

### 平均遗忘指数

整个[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的平均[请求遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index)（括号中的数字是[默认遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo#default_forgetting_index)）。如果个别[元素](https://help.supermemo.org/wiki/Glossary:Element)的[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)没有被手动改变，**平均FI**等于**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[选项](https://help.supermemo.org/wiki/Options)：[学习](https://help.supermemo.org/wiki/Learning_tab_in_Options)：遗忘指数（默认）**中设定的[默认遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo#default_forgetting_index)。默认的遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo#default_forgetting_index)是给所有添加到[集合](https://help.supermemo.org/wiki/Glossary:Collection)的新[项目](https://help.supermemo.org/wiki/Glossary:Item)的[要求的遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index)。[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)，一般来说，是指在重复过程中没有被记住的[项目](https://help.supermemo.org/wiki/Glossary:Item)的比例。遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)的值越低，对[元素](https://help.supermemo.org/wiki/Glossary:Element)的记忆就越好，但需要更多的[重复次数](https://help.supermemo.org/wiki/Glossary:Repetition)来保持它的记忆。最佳的[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)值是在7%到13%之间。太低的[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)会使学习变得太累，因为[重复](https://help.supermemo.org/wiki/Glossary:Repetition)的数量大得令人望而却步。所有的[元素](https://help.supermemo.org/wiki/Glossary:Element)都可以单独设置其[期望的遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index)。改变大量[元素](https://help.supermemo.org/wiki/Glossary:Element)的[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)的最简单方法是在[子集操作](https://help.supermemo.org/wiki/Subset_operations)中使用**[遗忘指数](https://help.supermemo.org/wiki/Subset_operations#Forgetting_index) **选项。*在提出的例子中，平均[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)为10.00%，而[默认遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo#default_forgetting_index)为10%*。见。[使用遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo)

### 完成

假设目前学习新[项目](https://help.supermemo.org/wiki/Glossary:Item)的速度，[待定队列](https://help.supermemo.org/wiki/Glossary:Pending_queue)中所有[元素](https://help.supermemo.org/wiki/Glossary:Element)将被[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)的预期日期。如果你正在记忆大型现成的[集合](https://help.supermemo.org/wiki/Glossary:Collection)，如[高级英语](https://supermemo.guru/wiki/Advanced_English)，这个参数就特别有用。对于**[待定](https://help.supermemo.org/wiki/Statistics#Pending)**=0，这个字段的值是*今天*。

> ```

> 完成=日期+(待定/(已记忆项目/日))

> ```

### A-Factor

在[集合](https://help.supermemo.org/wiki/Glossary:Collection)的[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)(I)和[主题](https://help.supermemo.org/wiki/Glossary:Topic)(T)中，[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)的平均值。对于项目，A-Factor是[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)中[难度](https://help.supermemo.org/wiki/Glossary:Difficulty)的一个衡量标准。A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)越高，[项目](https://help.supermemo.org/wiki/Glossary:Item)越容易。对于题目来说，A-Factor是**当前[间隔](https://help.supermemo.org/wiki/Glossary:Interval)**应乘以的数字，以获得**下一个间隔的值。*在提出的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，[项目](https://help.supermemo.org/wiki/Glossary:Item)的平均[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)是4.09。这表明[文集](https://help.supermemo.org/wiki/Glossary:Collection)的结构相当好，因此材料相对容易记忆。主题](https://help.supermemo.org/wiki/Glossary:Topic)的平均[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)为1.228*。

### 补充说明

- [条目](https://help.supermemo.org/wiki/Glossary:Item)不仅在标准重复期间被添加到[最终演练](https://help.supermemo.org/wiki/Glossary:Final_drill)，当你对一个[元素](https://help.supermemo.org/wiki/Glossary:Element)的评分低于**良好(4)**。诸如**记忆**（*Ctrl+M*）、**冻结**（*Alt+Z*）和**添加到钻头**（*Shift+Ctrl+D*）等操作也会添加到【最终钻头队列】(https://help.supermemo.org/wiki/Glossary:Final_drill_queue)。只有当你取消了**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[选项](https://help.supermemo.org/wiki/Options)：[学习](https://help.supermemo.org/wiki/Learning_tab_in_Options)：跳过最终演练**，才会自动创建[最终演练队列](https://help.supermemo.org/wiki/Glossary:Final_drill_queue)

- **统计**窗口的一些字段可以被编辑。比如说。**警报**，**总时间**，**报告数**，等等。要编辑一个条目，点击它，输入新的数值，然后按*Enter*。如果该条目不能被修改，SuperMemo会警告你（例如："*保留率条目不能被修改*"）。

- 参见[1994 年调查](http://super-memory.com/articles/survey1994.htm)和[1999年调查](http://super-memory.com/articles/survey.htm)，了解一些关于使用SuperMemo达到的学习速度的有趣说明。

## 统计学上下文菜单

要打开上下文菜单：

- 右键点击窗口中的任何地方

- 点击[工具栏]中的第一个按钮（https://help.supermemo.org/wiki/Statistics#Toolbar）。

上下文菜单项目：

- **[工作量](https://help.supermemo.org/wiki/Calendar)**--每天和每月的重复工作日历

- **报告** - 将**统计**窗口的内容保存到一个文本文件中

- **恢复布局** (*Ctrl+F5*) - 恢复SuperMemo窗口的默认布局

- **元素窗口** (*Esc*) - 将焦点转移到[元素窗口](https://help.supermemo.org/wiki/Element_window)