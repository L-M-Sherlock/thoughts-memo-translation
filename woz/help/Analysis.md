# 分析

原文：[Analysis - SuperMemo Help](https://help.supermemo.org/wiki/Analysis)

在SuperMemo菜单栏中点击**[工具](https://help.supermemo.org/wiki/Toolkit_menu)：[统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：分析**(*Shift+Alt+A*)，分析提供了图表，说明当前打开的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中学习进度。

除了**分析**之外，SuperMemo还提供了其他多种[分析工具](https://help.supermemo.org/wiki/Theory)。

## 使用

学习过程的统计数据随时间变化的图表。这些图表记录了每日统计数字的变化，如某一天的[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[卡片](https://help.supermemo.org/wiki/Glossary:Item)、[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)或[未完成](https://help.supermemo.org/wiki/Glossary:Outstanding_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量。当天的第一个非零值被记录下来。如果该值之后增加，则忽略该增加值（少数情况除外，如新[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的统计，等等）。如果你在学习中中断了，最后记录的非零值将在你没有使用SuperMemo的时期内增加（除了少数情况，如重复次数的统计等）。

要放大图表的一部分（如下面的图片），用鼠标扫过要删除的图表部分，即指向焦点日期，向左移动鼠标并释放鼠标按钮。这样就会在鼠标移动的方向上切掉部分图形。你也可以使用*Ctrl+Left*和*Ctrl+Right*按钮来放大（见[下文](https://help.supermemo.org/wiki/Analysis#Use_context_menu)）。

### 使用统计（statistics）

下面是SuperMemo每天记录的统计数据，显示在**Use**标签上。

1. 已完成的工作（Work done）

      - **使用时间（Use time）** - 你每天主动使用某个[学习集(collection)](https://help.supermemo.org/wiki/Glossary:Collection)的总时间。时间取自学习区块记录（**[工具箱(Toolkit)](https://help.supermemo.org/wiki/Toolkit_menu)：[睡眠图（Sleep Chart）](https://help.supermemo.org/wiki/Sleep_Chart)**为红色）。天数从午夜算起（即不考虑午夜班）。

      - **回忆时间（Recall time）** - 你每天花在试图回忆问题答案上的总时间

      - **重复项目(Repetitions)** - 你每天记录的[卡片(item)）](https://help.supermemo.org/wiki/Glossary:Item)和[文本(topic)](https://help.supermemo.org/wiki/Glossary:Topic)的复习数量

      - **卡片重复（Item repetitions）** - 你每天记录的[卡片（item）](https://help.supermemo.org/wiki/Glossary:Item)重复次数

      - **文本复习(topic reviews)** - 你每天的[文本(topic)](https://help.supermemo.org/wiki/Glossary:Topic)fuxi记录

2. 待办队列

      \- 数目

      杰出因素

      预定在某一天

      - **未决** - 所有[未决元素]的数量(https://help.supermemo.org/wiki/Glossary:Outstanding_element)，安排在某一天。

      - **未完成的项目** - 计划在某一天进行的[未完成](https://help.supermemo.org/wiki/Glossary:Outstanding_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)的数量

      - **未完成的课题** - 在某一天安排的[未完成](https://help.supermemo.org/wiki/Glossary:Outstanding_element)[课题](https://help.supermemo.org/wiki/Glossary:Topic)的数量

3. 负载（burden）

      - **Burden** - 当前[*Burden*参数](https://help.supermemo.org/wiki/Glossary:Burden)记录。[Burden](https://help.supermemo.org/wiki/Glossary:Burden)估计每天安排[重复](https://help.supermemo.org/wiki/Glossary:Repetition)的[元素](https://help.supermemo.org/wiki/Glossary:Element)的数量，假设学习过程中没有延迟。[负担](https://help.supermemo.org/wiki/Glossary:Burden)是[间隔](https://help.supermemo.org/wiki/Glossary:Interval)的倒数之和。**[负担](https://help.supermemo.org/wiki/Glossary:Burden) = [项目](https://help.supermemo.org/wiki/Glossary:Item) [负担](https://help.supermemo.org/wiki/Glossary:Burden) + [主题](https://help.supermemo.org/wiki/Glossary:Topic) [负担](https://help.supermemo.org/wiki/Glossary:Burden)**

      - **项目负担** - 当前**[负担](https://help.supermemo.org/wiki/Glossary:Burden)**为[项目](https://help.supermemo.org/wiki/Glossary:Item)

      - **主题负担** - 当前**[负担](https://help.supermemo.org/wiki/Glossary:Burden)**为[主题](https://help.supermemo.org/wiki/Glossary:Topic)。

4.元素计数

      - **Elements** - 某天记录的[元素](https://help.supermemo.org/wiki/Glossary:Element)的总数(即[主题](https://help.supermemo.org/wiki/Glossary:Topic)+[概念](https://help.supermemo.org/wiki/Glossary:Concept)+[项目](https://help.supermemo.org/wiki/Glossary:Item)+[任务](https://help.supermemo.org/wiki/Glossary:Task)

      - **项目** - 某天记录的[收藏品](https://help.supermemo.org/wiki/Glossary:Item)的数量(https://help.supermemo.org/wiki/Glossary:Collection)

      - **主题和任务** - 某一天记录的[主题](https://help.supermemo.org/wiki/Glossary:Topic)和[任务](https://help.supermemo.org/wiki/Glossary:Task)的数量(见[下面的示范图](https://help.supermemo.org/wiki/Analysis#Use.C2.A0:_Element_count.C2.A0:_Topics_and_tasks))

      - **任务列表(*当前选择的任务列表名称/*)** - 当前使用的[任务列表](https://help.supermemo.org/wiki/Glossary:Task)上的[任务]数量(其名称显示在括号中)。使用[任务列表管理器](https://help.supermemo.org/wiki/Tasklist_manager)中的**设置**按钮来改变当前选择的[任务列表](https://help.supermemo.org/wiki/Glossary:Tasklist)。

5.记住了

      - **记忆** - 参加学习过程的[元素](https://help.supermemo.org/wiki/Glossary:Element)的数量（即没有[被解雇](https://help.supermemo.org/wiki/Glossary:Dismissed_element)和没有[待定](https://help.supermemo.org/wiki/Glossary:Pending_element)）。

      - **记忆的项目** - 参加学习过程的[项目]数量(https://help.supermemo.org/wiki/Glossary:Item)

      - **记忆中的主题** - 参加学习过程的[主题]数量(https://help.supermemo.org/wiki/Glossary:Topic)

6.新背的

      - **新记忆的** - 在某一天新记忆的[元素](https://help.supermemo.org/wiki/Glossary:Element)(见[下面的示范图](https://help.supermemo.org/wiki/Analysis#Use.C2.A0:_Newly_memorized))

      - **新项目** - 在某一天记住的新[项目](https://help.supermemo.org/wiki/Glossary:Item)

      - **新题目** - 在某一天记住的新[题目](https://help.supermemo.org/wiki/Glossary:Topic)

7. 效率

      - **遗忘指数** - [测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)(存储的数据有一定程度的平滑，以可视化的趋势)

      - **保留率** - [保留率](https://help.supermemo.org/wiki/Glossary:Retention)，每天测量。这张图是经过平滑处理的，以便更好地阅读长期趋势。要想获得更精确的读数，请看下一个标签。**回忆**。**Retention**标签现在可以容纳超过十年的数据，并保留了兼容性。**回忆**选项卡包含未经处理的原始数据，你可以随时用**光滑**进行打磨，使趋势可视化

      - **回忆** - 每天正确答案的比例（由[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)登记）。这是未经处理的原始数据，你可以将其导出到Excel中，供你自己分析。与**[保留率](https://help.supermemo.org/wiki/Glossary:Retention)**标签进行比较。它也应该与**遗忘指数**标签上显示的数据大致对应（回忆率是100%减去遗忘指数）。

      - **SM16中的R**--由[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)估计的[可检索性(R)](https://help.supermemo.org/wiki/Glossary:Retrievability)(R是[保留](https://help.supermemo.org/wiki/Glossary:Retention)的预测值，而召回率是[保留](https://help.supermemo.org/wiki/Glossary:Retention)的测量值)

      - **SM18中的R** - [可检索性（R）](https://help.supermemo.org/wiki/Glossary:Retrievability)由[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)估计。

      - **SM16/SM18 Diff**--SuperMemo算法的召回估计偏差的百分点差异`(abs(R16-Recall)-abs(R18-Recall))`。差值越大，新的[算法SM-18]（https://supermemo.guru/wiki/Algorithm_SM-18）的性能越好。正是该算法准确预测遗忘概率的能力，使得它在[间隔重复](https://help.supermemo.org/wiki/Glossary:Spaced_repetition)中的优势。这个标签显示了[超级备忘录18](https://help.supermemo.org/wiki/What's_new_in_SuperMemo_18%3F)在准确预测回忆方面的接近程度（与旧的算法相比）。

      - **SM16指标** - [算法SM-15]（https://supermemo.guru/wiki/Algorithm_SM-15）的性能指标。它是预测差异平方的平均数的平方根，以百分点表示（数字越小，说明召回的预测精度越高）。

      - **SM18公制** - [算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)的性能公制。它的计算方法与 **SM16 Metric** 标签上的类似参数相同。理想情况下，这个选项卡上的数字应该更低，表明[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)的优越性。

      - **R-Metric** - [算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)的最终性能指标。它与旧的[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)进行了比较。它是以前标签中两个指标之间的性能指标差异。**SM16指标**减去**SM18指标**。数字越大，算法SM-18对于给定的[集合](https://help.supermemo.org/wiki/Glossary:Collection)的优越性就越大。在指标为负数的日子里，旧的算法会比算法SM-18表现更好。由于遗忘是随机的，一天的实际度量结果是一种抽奖。只有每天有更多的重复次数才能提供一致的结果。对于一个基于8800个数据点的示范图，见。[下面的例子](https://help.supermemo.org/wiki/Analysis#Use_:_Efficiency_:_R-Metric)。

      - **主题负荷** - 在某一天安排[审查](https://help.supermemo.org/wiki/Glossary:Review)的[主题](https://help.supermemo.org/wiki/Glossary:Topic)在所有[元素](https://help.supermemo.org/wiki/Glossary:Element)中的比例。*[主题](https://help.supermemo.org/wiki/Glossary:Topic)负荷=[未决](https://help.supermemo.org/wiki/Glossary:Outstanding_element)[主题](https://help.supermemo.org/wiki/Glossary:Topic)/[未决要素](https://help.supermemo.org/wiki/Glossary:Outstanding_element)*。[主题](https://help.supermemo.org/wiki/Glossary:Topic)负荷是以任何一天的百分比表示。[主题](https://help.supermemo.org/wiki/Glossary:Topic)的负荷不应与**[排序标准](https://help.supermemo.org/wiki/Priority_queue#Sorting_repetitions)中[主题](https://help.supermemo.org/wiki/Glossary:Topic)的比例**混淆。如果可能的话，[主题](https://help.supermemo.org/wiki/Glossary:Topic)的比例与[主题](https://help.supermemo.org/wiki/Glossary:Topic)的负荷无关（例如，对于零[主题](https://help.supermemo.org/wiki/Glossary:Topic)负荷，你不能实现大于零的比例，等等）。如果你不使用[自动排序](https://help.supermemo.org/wiki/Glossary:Auto-sort)，[主题](https://help.supermemo.org/wiki/Glossary:Topic)负载告诉你，你的重复的比例是由[主题](https://help.supermemo.org/wiki/Glossary:Topic)组成的。

8.超负荷工作

      \- 已执行的重复次数除以未执行的重复次数（即实际执行的重复次数的百分比）。

      - **要素** - 所有未完成的重复执行的百分比

      - **项目** - [未完成](https://help.supermemo.org/wiki/Glossary:Outstanding_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)重复执行的百分比

      - **主题** - 已完成的[杰出](https://help.supermemo.org/wiki/Glossary:Outstanding_element)[主题](https://help.supermemo.org/wiki/Glossary:Topic)评论的百分比

9.优先保护

      \- 在某一天，你对高优先级材料的处理能力。如果你的图表在以下范围内震荡

      优先权

      3%，你就会知道，只有前3%的学习材料能保证及时重复。你可以通过做更多的工作，减少新材料的流入，降低不那么重要的元素的优先级，或降低随机化程度来增加这个数字。

      未完成的队列

      分选标准

      .阅读有关这一重要参数的文章

      [优先权规则手册](https://help.supermemo.org/wiki/Priority_queue#Prioritization_rulebook)

      - **项目** - 在重复中被遗漏的最高优先级的[项目](https://help.supermemo.org/wiki/Glossary:Item)（具有最低的百分比）。([未决队列](https://help.supermemo.org/wiki/Glossary:Outstanding_queue)中的实际百分比可能要高得多(因为你主要是审查高[优先级](https://help.supermemo.org/wiki/Glossary:Priority))

      - **主题** - 在重复中被遗漏的最优先的[主题](https://help.supermemo.org/wiki/Glossary:Topic)（百分比最低）。(见：[下面的示范图](https://help.supermemo.org/wiki/Analysis#Use.C2.A0:_Priority_protection.C2.A0:_Topics))

###使用上下文菜单

- **下一个**（*Ctrl+Tab*）--切换到下一个主要的使用统计表

- **上一个**（*Shift+Ctrl+Tab*）--切换回上一个主要的使用统计表

- **下一个二级**（*标签*）--切换到二级行的下一个标签

- **上一个二级**（*Shift+Tab*）--切换到二级行的上一个标签。

- **切掉左边**（*Ctrl+右箭头*）--切掉图形的左边部分以放大其余部分

- **切掉右边**（*Ctrl+左箭头*）--切掉图形的右边部分以放大其余部分。

- **切掉顶部**（*Ctrl+向下箭头*）--切掉图形的顶部部分以放大其余部分。

- **导出** - 将当前显示的统计数据导出为CSV文件（该文件可以在[集合](https://help.supermemo.org/wiki/Glossary:Collection)的[STATS]子文件夹中找到

- **导入** - 为当前显示的统计数字导入数据

- **关闭**（*Esc*）--关闭**分析**窗口

# # # 例子

#### 使用 : 效率 : R-Metric

[![SuperMemo: Algorithm SM-18 performance metric](https://help.supermemo.org/images/thumb/0/04/Recall_metric.jpg/800px-Recall_metric.jpg)](https://help.supermemo.org/wiki/File:Recall_metric.jpg)

> ***图：**[R-Metric](https://help.supermemo.org/wiki/Glossary:R-Metric)**图显示了[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)比旧的[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)在提出的[收集](https://help.supermemo.org/wiki/Glossary:Collection)中的优势，使用的测试期为整整4年，可追溯至2015年4月2日。它是用24104个数据点（即有两种算法数据的重复案例）绘制的，并进行了平滑处理以显示趋势。纵轴上0线下的多个点（"R-metric<0"）已经被平滑掉了（它们对应的是前一版本的算法在较小的重复样本中出现优势的日子）。一些积极和消极的趋势与算法的变化相对应，因为数据是在新算法的测试期收集的。2016年2月至5月，指标逐渐增加，可能是统计学上的反常现象，也可能是新的区间值和[区间](https://help.supermemo.org/wiki/Glossary:Interval)的R-指标较大，偏离了早期SuperMemos中使用的最佳值的结果。后者的解释可能表明，[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)的好处可以随着时间的推移逐渐增加*。

#### 使用：元素数。主题和任务

[![SuperMemo:工具箱：统计：分析：使用：元素计数。主题和任务显示你在个别日子里有多少个主题和任务在你的集合中](https://help.supermemo.org/images/thumb/0/0d/Topics_and_tasks_count.jpg/800px-Topics_and_tasks_count.jpg)](https://help.supermemo.org/wiki/File:Topics_and_tasks_count.jpg)

> ***图：**示例图显示了存储在[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的[主题](https://help.supermemo.org/wiki/Glossary:Topic)的总数量。显示在底部的数据取决于鼠标的位置。在这个例子中，它表明在2009年3月6日，有251,228个[主题](https://help.supermemo.org/wiki/Glossary:Topic)在增量阅读过程中。*。

#### 使用 : 新的记忆

[！[SuperMemo:Toolkit : Statistics : Analysis : Use : Newly memorized 显示你在个别日子里记住了多少个元素](https://help.supermemo.org/images/thumb/3/3e/Newly_memorized.jpg/800px-Newly_memorized.jpg)](https://help.supermemo.org/wiki/File:Newly_memorized.jpg)

> ***图：**示范图显示了个别日子里记忆的[元素](https://help.supermemo.org/wiki/Glossary:Element)的数量。通过扫除图表的左右两部分，可以放大学习过程的一小部分。图中显示的时间跨度为2008年7月1日至2009年3月19日。

#### 使用 : 效率 : 遗忘指数

[！[SuperMemo:工具箱：统计：分析：使用：效率：遗忘指数显示你在个别日子里测量的遗忘指数的变化](https://help.supermemo.org/images/thumb/3/39/Daily_measured_forgetting_index.jpg/800px-Daily_measured_forgetting_index.jpg)](https://help.supermemo.org/wiki/File:Daily_measured_forgetting_index.jpg)

> ***图：**示范图，使[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)的分析更有意义。在**分析中对[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)的改变使用了每天的[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)（以前：信息量较小的累积[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)值是自上次使用**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：重置参数：遗忘指数记录后的整个时期取值）。请注意，[优先级队列](https://help.supermemo.org/wiki/Glossary:Priority_queue)可能会扭曲你的[收藏](https://help.supermemo.org/wiki/Glossary:Collection)中的实际[保留](https://help.supermemo.org/wiki/Glossary:Retention)，因为测量值主要取自顶级[优先级](https://help.supermemo.org/wiki/Glossary:Priority)材料。因此，[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)应该被理解为 "在重复中测量的遗忘指数"，而不是 "整体测量的遗忘指数 "*。

#### 使用：优先保护：项目

[！[SuperMemo:工具箱：统计：分析：使用：优先保护：项目显示你在个别日子里对高优先级项目的实际处理能力](https://help.supermemo.org/images/thumb/f/fa/Item_priority_protection.jpg/800px-Item_priority_protection.jpg)](https://help.supermemo.org/wiki/File:Item_priority_protection.jpg)

> ***图：**示范图显示在某一天的重复中被遗漏的最高优先级的[项目](https://help.supermemo.org/wiki/Glossary:Item)（最低的[优先级](https://help.supermemo.org/wiki/Glossary:Priority)%）。在图片中，你可以看到在一个月内，[项目](https://help.supermemo.org/wiki/Glossary:Item)的优先保护从0.5%增加到11%。这是通过专注于诚实的[优先级](https://help.supermemo.org/wiki/Priority_queue)，做大量的重复工作，避免大量的上调优先级等*而实现的。

#### 使用：优先保护：主题

[！[SuperMemo:工具箱：统计：分析：使用：优先保护：主题显示你在个别日子里对高优先级主题的实际处理能力](https://help.supermemo.org/images/thumb/3/3f/Topic_priority_protection.jpg/800px-Topic_priority_protection.jpg)](https://help.supermemo.org/wiki/File:Topic_priority_protection.jpg)

> ***图：**示范图显示审查中遗漏的最高优先级的[主题](https://help.supermemo.org/wiki/Glossary:Topic)（优先级最低的%）。显示在底部的数据取决于鼠标的位置。在这个例子中，它表明在2013年6月26日，在[主题](https://help.supermemo.org/wiki/Glossary:Topic)中最差的错过是一个[优先级](https://help.supermemo.org/wiki/Glossary:Priority)等于7.613%的最重要[主题](https://help.supermemo.org/wiki/Glossary:Topic)审查队列的主题。 *

## 遗忘

400条[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)是独立绘制的，以便计算[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)中的SInc矩阵。这些对应于20个稳定性类别和20个难度类别。通过选择图形底部的标签的适当组合，你可以选择一个感兴趣的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)。横轴代表时间，表示为。(1)可检索性，或(2)天数（仅针对第一次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)）。纵轴表示[知识保留](https://help.supermemo.org/wiki/Glossary:Retention)的百分比。

[！[SuperMemo:第一条遗忘曲线（第一次重复的项目没有失误）](https://help.supermemo.org/images/thumb/0/0f/First_forgetting_curve.jpg/600px-First_forgetting_curve.jpg)](https://help.supermemo.org/wiki/File:First_forgetting_curve.jpg)

> ***图：**用[SuperMemo](https://help.supermemo.org/wiki/SuperMemo)收集的新学知识的第一个[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)。由于学习过程中新引入的学习材料的异质性，在这种情况下使用了功率近似法。缺乏[记忆复杂性](https://supermemo.guru/wiki/Memory_complexity)的分离，导致了具有不同衰减常数的指数型遗忘的叠加。在半对数图上，功率回归曲线是对数的（黄色），而且看起来几乎是直线。曲线显示，在所提出的案例中，记忆力在四年内仅仅下降到58%，这可以解释为在现实生活中对所记忆的知识的高度重复使用。在[可检索性](https://help.supermemo.org/wiki/Glossary:Retrievability)为90%的情况下，复习的第一个[最佳间隔](https://help.supermemo.org/wiki/Glossary:Optimum_interval)是3.96天。遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)可以用公式R=0.9906\*power(interval,-0.07)来描述，其中0.9906是一天后的回忆，而-0.07是衰减常数。在这种情况下，该公式在4天后产生了90%的召回率。80,399个重复的案例被用来绘制所呈现的图表。如果材料中含有较高比例的困难知识（特别是[表述不清的知识](https://supermemo.guru/wiki/20_rules)），或者是记忆能力较差的新学生，记忆力会出现较大幅度的下降。间隔15-20的曲线的不规则性来自于较小的重复样本（在对数尺度上的后来的间隔类别包含了更大的间隔范围）。

## 遗忘 (UF)

该标签显示旧版SuperMemos中使用的遗忘数据。它只用于记录和显示新算法和旧算法之间的比较。

400条[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)是独立绘制的，以计算[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)中的RF矩阵。这些对应于20个重复次数类别和20个[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)类别。为了数据表示的方便，第一次重复的RF矩阵的列是由[记忆缺失](https://help.supermemo.org/wiki/Glossary:Lapse)的数量而不是由[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)来索引。通过选择图形底部的标签的适当组合，你可以选择感兴趣的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)。横轴代表时间，表示为。(1) [U-Factor](https://help.supermemo.org/wiki/Glossary:U-Factor)，即随后的重复间[间隔](https://help.supermemo.org/wiki/Glossary:Interval)的比率，或(2)天（仅针对第一次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)）。纵轴代表[知识保留](https://help.supermemo.org/wiki/Glossary:Retention)的百分比。

[！[SuperMemo:Toolkit : Statistics : Analysis : Forgetting (UF) graphs for 20 repetition number categories multiplied by 20 A-Factor category](https://help.supermemo.org/images/thumb/4/46/Forgetting_curves.jpg/600px-Forgetting_curves.jpg)](https://help.supermemo.org/wiki/File:Forgetting_curves.jpg)

> ***图：**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：分析：[遗忘（UF）](https://help.supermemo.org/wiki/Analysis#Forgetting_.28UF.29)**为20个重复次数类别乘以20个A因素类别。在图片中，蓝色圆圈代表在重复过程中收集的数据。圆圈越大，记录的重复次数就越多。红色曲线对应的是通过指数回归得到的最佳拟合[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)。对于结构不良的材料，[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_index)是弯曲的，也就是说，不完全是指数型的。水平的水蓝色线条与[要求的遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index)相对应，而垂直的绿色线条表示近似的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)与要求的遗忘指数线相交的时间点。这个时间点决定了相关的[R因子](https://help.supermemo.org/wiki/Glossary#R-Factor)的值，并间接决定了[最佳间隔](https://help.supermemo.org/wiki/Glossary:Optimum_interval)的值。对于第一次重复，[R-Factor](https://help.supermemo.org/wiki/Glossary:R-Factor)与第一个[最佳间隔](https://help.supermemo.org/wiki/Glossary:Optimum_interval)相对应。O-Factor](https://help.supermemo.org/wiki/Glossary:O-Factor)和[R-Factor](https://help.supermemo.org/wiki/Glossary:R-Factor)的值显示在图表的顶部。它们后面是用于绘制图表的重复案例的数量（即21,303）。在学习过程的开始，没有重复的历史，也没有重复的数据来计算[R-Factors](https://help.supermemo.org/wiki/Glossary:R-Factor)。在你的第一个[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)被绘制出来之前，需要一些时间。由于这个原因，[RF矩阵](https://help.supermemo.org/wiki/Glossary:RF_matrix)的初始值取自一个低于平均水平的学生的模型。没有使用平均学生的模型，因为从较差的学生参数向上收敛的速度比相反方向的收敛要快。显示在顶部的**偏差**参数告诉你负指数曲线对数据的拟合程度。偏差越小，拟合效果越好。偏差是以平方差的平均数的平方根计算的（如最小二乘法中所用）。

[！[SuperMemo:在SuperMemo 18中，遗忘曲线可以在不同的重复类别中对A因素进行归一化。因此，你可以显示（1）你的累积遗忘曲线（蓝点），（2）SuperMemo使用的其负指数近似值（红线）和（3）SuperMemo收集的所有遗忘曲线的单个数据点（黄圈）。](https://help.supermemo.org/images/thumb/2/21/Cumulative_forgetting_curve.jpg/800px-Cumulative_forgetting_curve.jpg)](https://help.supermemo.org/wiki/File:Cumulative_forgetting_curve.jpg)

> ***图：**在SuperMemo 18中，[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)可以在不同的[重复次数](https://help.supermemo.org/wiki/Glossary:Repetition)类别(**所有的重复次数**)上对[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)进行归一化处理（如上图）。因此，你可以显示：*

>

> 1.*你的累积[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)（蓝点）*。

> 2.*其负指数近似值由SuperMemo使用（黄线）*。

> 3.*由SuperMemo收集的所有[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)的个别数据点（黄色圆圈，红色边框）。

>

> ***时间（归一化）**代表[射频矩阵](https://help.supermemo.org/wiki/Glossary:U-Factor)每个卡片的最大[U-系数](https://help.supermemo.org/wiki/Glossary:RF_matrix)的100%。**Decay**代表[遗忘曲线]的衰减常数(https://help.supermemo.org/wiki/Glossary:Forgetting_curve)。**Cases**表示绘制图表时使用的[重复](https://help.supermemo.org/wiki/Glossary:Repetition)案例的数量。**Repetitions**代表确定[R-Factors](https://help.supermemo.org/wiki/Glossary:R-Factor)时执行的[重复次数](https://help.supermemo.org/wiki/Glossary:Repetition)。**偏差**是数据和近似的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)之间的平均平方根。*。

## 稳定

在**分析中标有**稳定的选项卡可以用来检查SuperMemo中的[稳定化曲线](https://help.supermemo.org/wiki/Glossary:Stabilization_curve)。

[！[检查不同程度的稳定和难度的稳定曲线](https://help.supermemo.org/images/thumb/9/99/Stabilization_curve.jpg/800px-Stabilization_curve.jpg)](https://help.supermemo.org/wiki/File:Stabilization_curve.jpg)

> ***图：**[超级备忘录18](https://help.supermemo.org/wiki/SuperMemo_18)使人们可以检查400条独立的[稳定化曲线](https://help.supermemo.org/wiki/Glossary:Stabilization_curve)。这些曲线因[稳定性](https://help.supermemo.org/wiki/Glossary:Stability)和[难度](https://help.supermemo.org/wiki/Glossary:Difficulty)的水平而不同。图中显示了难度=0.58，稳定性=59天的曲线。横轴显示[可检索性](https://help.supermemo.org/wiki/Glossary:Retrievability)（百分比）。纵轴显示的是[稳定化](https://help.supermemo.org/wiki/Stabilization)（与[稳定性](https://help.supermemo.org/wiki/Glossary:Stability)的比率）。早期的重复带来很少的稳定，复习的效果随着下降到[可检索性](https://help.supermemo.org/wiki/Glossary:Retrievability)*而迅速增加。

## 图表

###遗忘指数与优先权

**遗忘指数与优先级的关系**--这张图告诉你遗忘是如何取决于学习材料的[优先级](https://help.supermemo.org/wiki/Glossary:Priority)。如果你总是及时浏览你的[未完成的材料](https://help.supermemo.org/wiki/Glossary:Outstanding_element)，如果你坚持[20条知识制定规则](http://super-memory.com/articles/20rules.htm)，你的[测量遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)应该与[要求遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index)相同。这张图就会显示出一条在[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)水平上通过的平坦直线。然而，一旦你开始超负荷学习，并使用**[Postpone](https://help.supermemo.org/wiki/Postpone)**或**[Mercy](https://help.supermemo.org/wiki/Mercy)**，你的[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)将增加。如果你总是按照[优先级](https://help.supermemo.org/wiki/Glossary:Priority)对你的重复进行排序（例如，将**[学习](https://help.supermemo.org/wiki/Learn_menu)：[排序](https://help.supermemo.org/wiki/Learn_menu#Sorting)：自动排序重复**选中），你仍然应该确保你的[测量遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)等于高优先级[元素](https://help.supermemo.org/wiki/Glossary:Element)的[请求遗忘指数](https://help.supermemo.org/wiki/Glossary:Requested_forgetting_index) （即在图表的左侧）。你对低优先级材料的[测量的遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)会更高，[过载](https://help.supermemo.org/wiki/Glossary:Overload)越大，差异越大。如果你通过增加重复的随机性来改变你的[重复排序标准](https://help.supermemo.org/wiki/Priority_queue#Sorting_repetitions)，这张图会更平坦，高优先级材料的[测量遗忘指数](https://help.supermemo.org/wiki/Glossary:Measured_forgetting_index)会更高。

###第一个区间

**第一次间隔** - 第一次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)之后的第一次[间隔](https://help.supermemo.org/wiki/Glossary:Interval)的长度取决于某个[项目](https://help.supermemo.org/wiki/Glossary:Item)被遗忘的次数。请注意，这里的第一次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)是指遗忘后的第一次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)，*不是*第一次的重复。换句话说，一个重复了两次的[项目](https://help.supermemo.org/wiki/Glossary:Item)在被遗忘之后，其重复次数将等于1；重复次数将不等于3。第一个[间隔](https://help.supermemo.org/wiki/Glossary:Interval)图显示了指数回归曲线，近似于不同数量的[记忆中断](https://help.supermemo.org/wiki/Glossary:Lapse)（包括与新[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)[项目](https://help.supermemo.org/wiki/Glossary:Item)对应的零中断类别）的第一个[间隔](https://help.supermemo.org/wiki/Glossary:Interval)的长度。在下图中，蓝色圆圈对应的是学习过程中收集的数据（圆圈越大，记录的重复次数越多）。

[![SuperMemo:Toolkit : Statistics : Analysis : Graphs : First Interval显示了你的指数回归曲线，该曲线近似于不同数量的记忆缺失的第一个间隔的长度](https://help.supermemo.org/images/thumb/c/c7/First_interval.jpg/800px-First_interval.jpg)](https://help.supermemo.org/wiki/File:First_interval.jpg)

> ***图：**在上图中，包括了超过130,000次重复的数据，新[记忆](https://help.supermemo.org/wiki/Glossary:Memorized_element)的[项目](https://help.supermemo.org/wiki/Glossary:Item)在7天后得到最佳重复。然而，被遗忘了10次的[项目](https://help.supermemo.org/wiki/Glossary:Item)（这在SuperMemo中很罕见）将需要两天的[间隔时间](https://help.supermemo.org/wiki/Glossary:Interval)。(由于对数缩放，圆圈的大小与数据样本不成正比；[lapses](https://help.supermemo.org/wiki/Glossary:Lapse)=0的重复情况远远大于[lapses](https://help.supermemo.org/wiki/Glossary:Lapse)=10的情况，在**[工具包](https://help.supermemo.org/wiki/Toolkit_menu)：[统计](https://help.supermemo.org/wiki/Toolkit_menu#Statistics)：分析：[分布](https://help.supermemo.org/wiki/Analysis#Distributions)：[lapses](https://help.supermemo.org/wiki/Analysis#Lapses) **中可以看出) *

### D-Factor vs. A-Factor

**D因子与A因子** - DF-AF图显示了[R因子](https://help.supermemo.org/wiki/Glossary:R-Factor)的功率近似值沿[RF矩阵](https://help.supermemo.org/wiki/Glossary:RF_matrix)的列的衰减常数。你需要了解[SuperMemo算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)才能理解此图。横轴代表[A因子](https://help.supermemo.org/wiki/Glossary:A-Factor)，而纵轴代表[D因子](https://help.supermemo.org/wiki/Glossary:D-Factor)（即衰减因子）。[D-Factor](https://help.supermemo.org/wiki/Glossary:D-Factor)是曲线的功率近似的衰减常数，可以在**分析**对话框的**[Approximations](https://help.supermemo.org/wiki/Analysis#Approximations)**标签中进行检查。

###一年级与A-Factor的关系

**第一个等级与A因素** - G-AF图将一个[项目](https://help.supermemo.org/wiki/Glossary:Grade)获得的第一个[等级](https://help.supermemo.org/wiki/Glossary:Item)与它的[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)的最终估计值联系起来。在每次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)时，当前[元素](https://help.supermemo.org/wiki/Glossary:Element)的旧[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)估计值被从图中删除，新的估计值被加入。这个图被[SuperMemo算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)用来快速估计[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)的第一个值，此时我们对一个[元素](https://help.supermemo.org/wiki/Glossary:Element)的了解是它在第一次[重复](https://help.supermemo.org/wiki/Glossary:Repetition)中得到的第一个[成绩](https://help.supermemo.org/wiki/Glossary:Grade)。

###等级与遗忘指数

**评分与遗忘指数** - FI-G图将[预期遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo#expected_forgetting_index)与重复时的[成绩](https://help.supermemo.org/wiki/Glossary:Grade)联系起来。你需要了解[SuperMemo算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)才能理解这个图表。你可以想象，[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)图的纵轴上可能使用平均[成绩](https://help.supermemo.org/wiki/Glossary:Grade)，而不是[保留率](https://help.supermemo.org/wiki/Glossary:Retention)。如果你把这个成绩与[遗忘指数](https://help.supermemo.org/wiki/Glossary:Forgetting_index)相关联，你就会得到FI-G图。这个图形被用来计算[估计遗忘指数](https://supermemo.guru/wiki/Forgetting_index_in_SuperMemo#estimated_forgetting_index)，而这个指数又被用来对成绩进行归一化处理（对于延迟的或高级的重复），并估计[项目](https://help.supermemo.org/wiki/Glossary:Item)的[A因子](https://help.supermemo.org/wiki/Glossary:A-Factor)的新值。成绩是用公式计算出来的。*成绩=Exp(A*FI+B)*，其中A和B是在复读期间收集的原始数据上运行的指数回归的参数。

[！[SuperMemo:Toolkit : Statistics : Analysis : Graphs : Grade vs. Forgetting index graph](https://help.supermemo.org/images/thumb/5/53/Grade_vs_Forgetting_index.jpg/800px-Grade_vs_Forgetting_index.jpg)](https://help.supermemo.org/wiki/File:Grade_vs_Forgetting_index.jpg)

## 分布

## 间隔

**间隔** - 在一个给定的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，重复间的[间隔](https://help.supermemo.org/wiki/Glossary:Interval)分布。通过改变对话框底部的组合框的设置，你可以看到[集合](https://help.supermemo.org/wiki/Glossary:Collection)中所有[元素](https://help.supermemo.org/wiki/Glossary:Element)的[间隔](https://help.supermemo.org/wiki/Glossary:Interval)分布，只为[项目](https://help.supermemo.org/wiki/Glossary:Item)，以及只为[主题](https://help.supermemo.org/wiki/Glossary:Topic)。

##A-Factors

**A-Factors** - 在一个给定的[集合](https://help.supermemo.org/wiki/Glossary:Collection)中，[A-Factors](https://help.supermemo.org/wiki/Glossary#A-factor)的分布。分布本身并没有在[算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)中使用，而只是由它产生的。请注意，[主题](https://help.supermemo.org/wiki/Glossary:Topic)和[项目](https://help.supermemo.org/wiki/Glossary:Item)使用不同的[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)类别。在底部选择*仅项目*或*仅主题*，可以分别看到项目或主题的分布情况。如果你选择*所有元素*，你会看到一个不太有意义的集合体分布，由[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)类别编号索引。

[![SuperMemo:工具箱：统计：分析：分布。A-Factors告诉你A-Factors在你的集合中是如何分布的](https://help.supermemo.org/images/thumb/8/80/AFactors_distribution.jpg/800px-AFactors_distribution.jpg)](https://help.supermemo.org/wiki/File:AFactors_distribution.jpg)

###困难

**困难** - 由[算法SM-18](https://supermemo.guru/wiki/Algorithm_SM-18)确定的项目困难分布。也见。[困难](https://help.supermemo.org/wiki/Glossary:Difficulty)

### ＃＃＃重复次数

**重复次数** - 在给定的[集合](https://help.supermemo.org/wiki/Glossary:Item)中，[项目](https://help.supermemo.org/wiki/Glossary:Item)或[主题](https://help.supermemo.org/wiki/Glossary:Topic)的[重复次数](https://help.supermemo.org/wiki/Glossary:Collection)分布；在分布中只考虑[记忆的元素](https://help.supermemo.org/wiki/Glossary:Memorized_element)，即不存在零重复次数的类别。

### ＃＃＃孩子

**失误** - 在[集合](https://help.supermemo.org/wiki/Glossary:Collection)中的特定[项目](https://help.supermemo.org/wiki/Glossary:Item)被遗忘的次数分布；只考虑[记忆的元素](https://help.supermemo.org/wiki/Glossary:Memorized_element)。你不应该有超过10%的[项目](https://help.supermemo.org/wiki/Glossary:Item)有超过3-4次的失误。如果不是这样，你应该重新审视你制定[课题](https://help.supermemo.org/wiki/Glossary:Item)的方式（见[制定知识的20条规则](http://www.super-memory.com/articles/20rules.htm)）。由于[主题](https://help.supermemo.org/wiki/Glossary:Topic)在重复时永远不会被 "遗忘"，如果你在元素类型组合框中选择了*主题，那么**失效中就不会有[失效](https://help.supermemo.org/wiki/Glossary:Lapse)列出。

[![SuperMemo:工具包：统计：分析：分布。Lapses显示你的记忆缺失是如何在你的集合中分布的](https://help.supermemo.org/images/thumb/c/ce/Lapses_distribution.jpg/800px-Lapses_distribution.jpg)](https://help.supermemo.org/wiki/File:Lapses_distribution.jpg)

## 3-D 曲线

这些图表显示了3维的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)。有20个图形，底部有[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)标签。每张图都对应着不同的[A因子](https://help.supermemo.org/wiki/Glossary:A-Factor)（从1.2到6.9）。X轴代表时间（如**【遗忘曲线】(https://help.supermemo.org/wiki/Analysis#Forgetting_curves)**）。Y轴代表[重复类别](https://help.supermemo.org/wiki/Glossary:Repetition_category)（大致对应于重复次数）。纵向的Z轴代表[保持率](https://help.supermemo.org/wiki/Glossary:Retention)的百分比（即在某一时刻记住了多少）。为了提高可见度，你可以用**旋转**旋转三维[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)，或用**平滑**平滑它们。**Rotate**将图形的Z轴顺时针旋转90度（从上面看）。这意味着X轴和Y轴会互换。注意，平滑是沿着Y轴进行的。这样就有可能将不同的[重复类别](https://help.supermemo.org/wiki/Glossary:Repetition_category)中不完全绘制的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)对齐。然而，一旦你点击**旋转**，Y轴的平滑将产生不同的结果（例如，在第一次**旋转**之后，平滑将沿着[重复类别](https://help.supermemo.org/wiki/Glossary:Repetition_category)减少结点）。为了最好地说明遗忘的过程，在旋转图形之前要对其进行平滑处理。

[![SuperMemo：A-Factor=3.6的遗忘曲线典范3-D图](https://help.supermemo.org/images/thumb/5/52/AFactor_3D_Curve.jpg/800px-AFactor_3D_Curve.jpg)](https://help.supermemo.org/wiki/File:AFactor_3D_Curve.jpg)

> ***图：**[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve)的示范性3-D图，[A-因子](https://help.supermemo.org/wiki/Glossary:A-Factor)=3.6。轴。X--[重复类别](https://help.supermemo.org/wiki/Glossary:Repetition_category)，Y--回忆率([知识保留率](https://help.supermemo.org/wiki/Glossary:Retention))，Z(传入轴)--时间(用[U-Factor](https://help.supermemo.org/wiki/Glossary:U-Factor)表示) 。该图沿Y轴进行了平滑处理（通过对不同[重复类别](https://help.supermemo.org/wiki/Glossary:Repetition_category)对应的结果进行平均），并旋转了一次以获得更好的可见度（斜率说明了各种[重复类别](https://help.supermemo.org/wiki/Glossary:Repetition_category)在时间上的遗忘大致相似，除了那些重复次数高的，可能反映长[间隔](https://help.supermemo.org/wiki/Glossary:Interval)的数据稀缺）。要想更好地看到同样的数据在三维中的情况，请看。**[工具包](https://help.supermemo.org/wiki/Toolkit_menu) : [记忆](https://help.supermemo.org/wiki/Toolkit_menu#Memory) : [4D图形](https://help.supermemo.org/wiki/Memory_graphs_(4D)) :遗忘**.*

## 3-D图表

3-D图形直观地表示[RF](https://help.supermemo.org/wiki/Glossary:R-Factor)、[OF](https://help.supermemo.org/wiki/Glossary:O-Factor)和案例矩阵（见：[**矩阵**](https://help.supermemo.org/wiki/Analysis#Matrices)）。

## S. 衰减

显示SInc斜率是如何计算的图表。

## OF 衰减

20条功率近似曲线，显示了[R因子](https://help.supermemo.org/wiki/Glossary:R-Factor)沿[RF矩阵](https://help.supermemo.org/wiki/Glossary:RF_matrix)的列的下降。你需要了解[SuperMemo算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)才能理解这些图表。对于每个[A因子](https://help.supermemo.org/wiki/Glossary:A-Factor)，随着重复次数的增加，[R因子](https://help.supermemo.org/wiki/Glossary:R-Factor)的值会减少（至少理论上应该减少）。功率回归被用来说明这种下降的程度，这种下降最好地反映在这里称为[D-因子](https://help.supermemo.org/wiki/Glossary:D-Factor)的衰减常数上。通过选择图表底部的[A-Factor](https://help.supermemo.org/wiki/Glossary:A-Factor)标签，你可以查看相应的[R-Factor](https://help.supermemo.org/wiki/Glossary:R-Factor)近似曲线。横轴代表重复次数类别，而纵轴代表[R-Factor](https://help.supermemo.org/wiki/Glossary:R-Factor)。D-Factor](https://help.supermemo.org/wiki/Glossary:D-Factor)的值显示在图表的顶部。蓝色折线表示从重复次数数据中得出的[R-因子](https://help.supermemo.org/wiki/Glossary:R-Factor)。红色曲线显示的是[R-Factor](https://help.supermemo.org/wiki/Glossary:R-Factor)的定点功率近似值。绿色曲线表示从OF矩阵得出的[R-Factor](https://help.supermemo.org/wiki/Glossary:R-Factor)的定点功率近似值；这相当于用[R-Factors](https://help.supermemo.org/wiki/Glossary:R-Factor)的定点功率近似值得到的[D-Factor](https://help.supermemo.org/wiki/Glossary:D-Factor)替代从DF-AF线性回归得到的[D-Factor](https://help.supermemo.org/wiki/Glossary:D-Factor)。两个近似值都采用了定点法，因为对于重复数等于2的情况，[R-因子](https://help.supermemo.org/wiki/Glossary:R-Factor)等于[A-因子](https://help.supermemo.org/wiki/Glossary:A-Factor)。

## 矩阵

你需要了解[SuperMemo算法](https://help.supermemo.org/wiki/SuperMemo_Algorithm)来理解这些表格。

- **召回率** - 召回率来自[Recall[/]矩阵](https://help.supermemo.org/wiki/Glossary:Recall_matrix)

- **Metric** - 召回率指标，显示在不同的[稳定性](https://help.supermemo.org/wiki/Glossary:Stability)和[难度](https://help.supermemo.org/wiki/Glossary:Difficulty)水平下的召回预测的准确性。

- **案例** - 计算稳定化矩阵时使用的重复案例

- **R90** - 预测的[可检索性](https://help.supermemo.org/wiki/Glossary:Retrievability)，召回率为90%。

- **SInc** - 稳定化表示为[稳定增加矩阵SInc[/]](https://help.supermemo.org/wiki/Glossary:Stability_increase_matrix)

- **间隔** - 从OF矩阵得出的[最佳间隔]矩阵(https://help.supermemo.org/wiki/Glossary:Optimum_interval)

- **R-Factors** - [保留因素]的矩阵(https://help.supermemo.org/wiki/Glossary:R-Factor)

- **OF矩阵** - 由重复号和[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)索引的[最佳因素](https://help.supermemo.org/wiki/Glossary:O-Factor)矩阵（除了第一个[重复](https://help.supermemo.org/wiki/Glossary:Repetition)，[A因素](https://help.supermemo.org/wiki/Glossary:A-Factor)被替换成[记忆缺失](https://help.supermemo.org/wiki/Glossary:Lapse)）。

- **RF案例** - 用于计算[RF矩阵](https://help.supermemo.org/wiki/Glossary:RF_matrix)的相应卡片的重复案例矩阵(双击一个卡片可查看相关的[遗忘曲线](https://help.supermemo.org/wiki/Glossary:Forgetting_curve))。这个矩阵可以手动编辑（例如，如果你想改变重复过程中某些测量的权重）。

[![SuperMemo:工具箱：统计：矩阵。间隔显示从OF矩阵得出的最佳间隔矩阵](https://help.supermemo.org/images/thumb/3/39/Intervals_matrix.jpg/600px-Intervals_matrix.jpg)](https://help.supermemo.org/wiki/File:Intervals_matrix.jpg)

## ＃＃＃常见问题

- [我担心我的图表看起来很奇怪，我做错了什么] (https://supermemopedia.com/wiki/Weirdness_in_my_collection)

- [分析中的数据错误](https://supermemopedia.com/wiki/Random_numbers_showed_up_in_data_used_by_the_algorithm)

## 延伸阅读

- [记忆图谱（4D）]（https://help.supermemo.org/wiki/Memory_graphs_（4D））

- [SuperMemo 算法](https://supermemo.guru/wiki/SuperMemo_Algorithm)

- 超级备忘录算法SM-15](https://supermemo.guru/wiki/Algorithm_SM-15)

- [常见问题：记忆和学习](http://super-memory.com/help/faq/memory.htm)

- [超级备忘录理论](http://super-memory.com/articles/theory.htm)