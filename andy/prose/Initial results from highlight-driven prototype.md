# 来自高亮引导原型的初步结果

原文：[Initial results from highlight-driven prototype | Patreon](https://www.patreon.com/posts/initial-results-93831375)

[我一直在研究](https://www.patreon.com/posts/highlight-driven-90101210)一种以**高亮**为核心交互的新型阅读增强环境。这个想法旨在为读者提供一根具备两种非凡「力量」的魔杖：

1. 你可以用魔杖指向任何内容，并说：「确保我知道这个。」

2. 你可以对某个小节挥动魔杖，询问：「我错过了什么重要的东西？」

当然，这些都是理想化的设定。我目前的设计将这些力量具体实现为：

1. 你拥有一支特殊的紫色高亮笔。当你用它标记文本时，关于这些想法的间隔重复卡片将被添加到未来的复习环节中。

2. 在每个小节的结尾，你可以按一个按钮，显示「建议高亮」，并再次浏览前文。这个按钮会将作者认为重要的所有细节中那些语义上与你高亮的内容**没有**交集的细节标记出来。你可以快速浏览，检查自己的阅读理解中是否存在缺口。

可以想象出更多复杂的实现方式！这些只是为了实现更高远的目标而迈出的有意义的第一步。欲了解更多背景信息，请参阅我关于这一概念的[介绍信](https://www.patreon.com/posts/highlight-driven-90101210)。

## 初步原型

本月，我测试了这个概念的原型，对 [Jim Hefferon 的线性代数入门教程](https://hefferon.net/linearalgebra/index.html)进行了改编。你可以在[**这个新的演示视频**](https://youtu.be/n3ugRmARpYw)（6 分 17 秒）中看到原型的实际运行情况。我邀请了 14 位有学习线性代数的实际需求、且有使用间隔重复记忆系统经验的人参加学习会议。我们面对面、一对一进行交流，这样更有助于我深入了解新原型。

在进行简短的背景调查和界面介绍之后，参与者阅读了教材的第一节，用普通黄色高亮笔和特殊紫色高亮笔进行标记，想怎么用就怎么用。在本节结束时，我们利用「建议高亮」工具快速进行了第二轮浏览。我请读者对每一个额外的高亮发表意见：这是他们理解了但觉得不值得标记的内容，还是他们忽略了的内容？最后，我们复习了与紫色高亮部分相对应的所有间隔重复记忆卡片。我向读者询问了复习这些卡片的感受，以及他们是否认为自己的高亮得到了忠实呈现。

在深入探讨我观察到的情况之前，我应该解释一下，这个原型涉及一些重要的障眼法。读者们以为我实现了一些复杂的机器学习系统。但实际上，至少目前还没有。以下是它的工作原理：

- 在与任何读者会面前，我手动「精选」了与我们阅读的章节中所有重要细节相对应的高亮片段。

- 对于这些高亮，我为每一条都编写了一张或多张练习卡片。

- 然后，在每位参与者阅读的同时，我手动将他们的高亮内容映射到基于相同概念的精选高亮内容（如果有的话）。这有时需要灵活的判断！

- 「建议高亮」功能随后显示了所有未与读者高亮重合的精选高亮。

- 复习环节展示了与我将读者的高亮映射到的所有精选高亮相关的卡片。

这在文字描述中看起来相当复杂，但在实践中却创造了非常透明的体验。读者并没有察觉到手动操作的步骤；他们经常天真地询问，是否可以在我们的会议结束后继续在自己的阅读中使用这个工具。这种「人工」智能式的测试让我专注于交互设计概念，而不是在语言模型流水线中可能是无底洞的问题。目前来说，这是正确的权衡。

## 从读者那里学到的

对于用户研究，预筛选总是不完美的。对于我的 14 位参与者中的 3 位来说，这本书（作为本科生的第一门课程）读起来太难了。另外 2 位读者实际上并不想详细了解这个主题；他们只是想了解「大局」。在讨论我学到了什么时，我将重点关注属于我目标受众的 9 位读者。

### 将高亮内容映射到卡片似乎非常有前景

读者们普遍喜欢增强高亮交互这一概念。他们中的大多数都有高亮文本的习惯，尽管他们都承认，这并没有实际影响他们的学习效果。相反，读者将高亮描述为一种发泄行为、一种保持更高参与度的方式，以及一种临时的书签。一位读者最后没有使用特殊高亮笔；他自称具有过人的记忆力，认为自己不需要针对本节材料的练习支持。其余人则大量使用了高亮笔。

大多数读者对给他们提供的提取练习卡片非常满意。一位读者说：「它捕捉到了我的意图，以至于我花了一些时间才意识到它们不是我写的。」另一位说：「这些是我希望能真正拥有的高亮系统。……它不仅仅是原样把东西扔回给我。……对于我高亮的概念，它让我思考重要的逻辑关系。」大多数读者自发地询问他们是否可以在其他书籍中使用「魔法高亮笔」。

有趣的是，**尽管**我并没有为他们每一条高亮都准备相应的卡片，但读者们对我将高亮映射到卡片的看法仍然非常积极。大多数读者高亮了一些我认为不够重要的点。虽然没有人注意到这些遗漏，但我担心这种悄无声息的遗漏会随着时间的推移削弱对这个工具的信任。要完全解决这个问题，需要可靠的机器生成卡片；在没有这个功能的情况下，我们可以为读者提供一个备用工作流，让他们为这些「遗漏」的高亮编写自己的卡片。

正如我所愿，这种设计在很大程度上消除了我在过去的助记媒介原型中经常看到的两种失败模式。因为每张卡片（原则上）都对应着读者「说」他们想要了解的东西，所以读者在复习环节中不太可能感到[令人不悦的权威或「学校式」的氛围](https://www.patreon.com/posts/revamping-medium-55309960)。出于同样的原因——结合阅读理解的辅助机制——读者[对问题或答案的困惑](https://www.patreon.com/posts/reading-and-85345515)也减少了。当然，读者可能在没有真正理解的情况下高亮某些段落，但当这种情况发生时，读者并没有抱怨这些卡片像在之前的原型中那样显得武断或不合情理。复习界面提供了一个「查看来源」的按钮，可以显示与他们高亮的原始材料之间的联系。我认为这通常会让读者觉得这种困惑是他们自己「要求」的，而不是「强加给」他们的。

这些会议并不是严格的实验；我只是寻求整体上的定性评估。但我的初步印象是，将卡片与高亮相结合的设计概念似乎有很大的潜力，值得进一步推进。

### 建议高亮诊断出了一些理解缺口，而且感觉非常轻量

这个原型的第二个重要想法是将「建议高亮」作为一种轻量级的阅读理解辅助干预。在这方面，结果相对更模棱两可。与我合作的读者们在阅读速度和认真程度上差异极大。有些人小声念着每个单词，经常停下来向文本提问并回答问题，多次重读段落以澄清误解。另一些人则用不到一半的时间匆匆浏览，跳过看似重复或显而易见的段落。 「测试」情境本身也引入了失真：尽管我在最初的指导中明确要求他们不要这样做，但一些读者承认，如果我不在场，他们的阅读速度会快得多。

在符合我预期目标用户的 9 位读者中，有 4 位在阅读理解方面存在实质性的缺口。 「建议高亮」交互迅速识别出了这些读者没有注意到的某些重点，并为他们提供了一个简单直接的机会来填补这一理解缺口。有时，读者觉得他们错过的细节并没有那么重要，但通常在读者重新阅读段落后，他们会用特殊的紫色高亮笔标记「建议高亮」。我认为这是一个迹象，表明这种交互发现了一些有意义的东西。

这些读者对这个设计非常热衷。有人说：「这正是我想要的工具！」还有人说：「这太酷了！哇，我真希望这个工具无处不在。」我有一个顾虑，那就是如果这些读者存在一些我的工具可以发现的明显理解缺口，那么他们可能还有其他难以察觉的缺口。也许这没关系，也许这些细节在做习题时就能轻易解决。至少，这种交互确保读者在理解材料时不会被要求做提取练习——这是[一个关键目标](https://www.patreon.com/posts/highlight-driven-90101210)。我需要进行更多针对性的实验，以更好地了解我的干预对阅读理解的影响。

另外 5 名「目标」用户没有明显的理解缺口；「建议高亮」全都是误报。我对这些读者的理解进行了额外的即兴提问，他们的表现都相当不错。因此，至少在测试环境中，这些读者不需要额外的阅读理解辅助。令人高兴的是，其中 3 名喜欢这个工具的**想法**，并表示他们不介意误报；他们觉得这种交互足够轻量，仍然愿意使用它：「我仍然认为它有帮助。它给了我一个安全网——护栏。」另外两人则不太确定。

### 紫色高亮作为待办事项

有些读者以一种出乎意料的方式使用特殊的紫色高亮笔：他们标记了尚未理解的段落。这些读者希望继续阅读，但他们想确保最终能理解他们标记的细节。他们实际上为自己留下了一个「待理解」的待办事项。

这种做法非常合理！毕竟，我告诉他们，如果他们用紫色高亮笔标记某段文字，系统会确保他们内化这些想法。目前的机制**在某种程度上**实现了这个目标。这些读者收到了关于他们「待办」标记的提取练习卡片。不出所料，他们不知道答案，并点击「查看来源」按钮返回原文重新阅读。在几个案例中，原文的解释在第二次阅读时更容易理解了，因为他们已经见过这些想法是如何融入后文的。

因此，至少有时候，提取练习卡片间接地完成了这些读者的「待办」意图，因为它促使他们重新阅读相关段落。但在某些情况下，段落仍然令人困惑，读者需要进行一些对话来理解它。在其他情况下，令人困惑的段落并没有对应任何提取练习卡片——例如，一位读者对示例问题中的某个特定步骤感到困惑——因此这个待办事项实际上被放弃了。考虑如何更直接地支持「待办事项」工作流程会很有趣。

### 高亮与卡片的透明映射

我的一位「目标」读者觉得高亮与卡片之间的映射有点「神奇」得令人不安。当我问他觉得复习卡片在多大程度上代表了他的高亮时，他说他真的不知道：他无法轻松地看到对应关系，所以无法判断他的意图得到了多好的体现。整个系统给他的感觉就像一个黑盒子。

这是合理的！我很惊讶居然没有更多的读者有这种感觉。科技人员喜欢将他们的产品描述为「神奇（magical）」，但我们真正想要的「神奇」是指「惊人的能力、便捷性、表现力」，而不是「难以言喻、高深莫测、神秘、古怪」。关于人工智能界面设计，我最喜欢的的论文是 Jeffrey Heer 2019 年的[《代理加自动化》](https://andymatuschak.org/files/papers/Heer - 2019 - Agency plus automation Designing artificial intel.pdf)。他在论文中认为，这样的界面可以从**共用的表现形式**中受益。你希望自动化系统以你自己可以创建和操作的形式清晰地展示它的建议，并且你希望清楚地看到这些建议与影响它们的输入之间的联系。

然而，我的当前设计缺少了这一点。你无法编写自己的卡片，也无法修改系统提供的那些。在复习时，你可以在每张卡片上点击「查看来源」以查看它是从哪个高亮「产生」的，但这作为一种了解对应关系的方法，相当繁琐。在阅读时也没有类似的功能：也就是说，当你标记一个紫色高亮时，系统并没有给你任何提示，告诉你它理解了你的什么意图——会生成哪些卡片。理想情况下，这些表现形式应该启动一个交互反馈循环。也就是说，你应该能够说「哦，不，那不是我的意思；请关注**这**一部分。」

一个朴素的解决方案：每当读者标记一条紫色高亮时，我们将展示对应卡片的预览，让读者在需要时进行干预。但我想谨慎避免重新引入[我去年年底的原型遇到的问题](https://www.patreon.com/posts/lessons-from-73309142)。在那个设计中，精选的卡片与关联的内容一起呈现在侧边栏中。这种方法使得交互非常清晰：如果你点击保存一张卡片，你将得到你所看到的内容；你可以在原地编辑它以便按需调整。但这也导致阅读体验相当令人分心。那些侧边栏的卡片让读者的目光不由自主地从正文中移开。在用户观察中，我发现他们不断地来回跳跃，丢失阅读位置，然后再找回来，眼睛跳到下一页与侧边栏卡片相邻的文本中。我认为大多数人在评估和选择卡片上花费了过多的注意力。

我采用这种新的以高亮为中心的设计的一个重要动机，就是为了解决这个问题。我希望让读者在阅读文本时更容易沉浸其中，同时仍能从可选的增强中受益。我认为这个原型在这方面表现得相当不错。但我还不确定如何在为卡片创造更透明、更共用的表现形式的同时，保持这种成功。

### 可定制的卡片映射：强调注解与反馈

这个原型的阅读界面将高亮与卡片的映射视为一个黑盒子，但作为实验，它确实提供了一种「指引」卡片的方法。读者在使用紫色高亮笔时，可以附上一个小注解，明确指出他们特别想强调什么。举个例子，你可能高亮了一个定义，但你真正想记牢的是它的表达方式；或者你想确保内化这个定义与之前某个概念的**对比**。因此，你可以高亮线性方程的定义，并在旁边写条注解：「与线性组合对比」。

大多数用户并没有重度使用这个功能，但至少用过一次。可以想象，随着他们建立起将高亮内容映射到卡片的心智模型，以及这种映射有时并不完全符合他们的期望，他们可能会倾向于更多地使用这个功能。

在实践中，我只能用我预先制作的精选卡片满足这些请求中的大约三分之一。另外三分之一能映射到更宽泛的卡片，这些卡片包含或间接强化了他们提到的细节。其余的请求则相当独特，可能只有通过机器生成的卡片才能满足。只有一位读者注意到他的请求并没有完全得到满足，而且他并没有表现得很在意。但我认为随着时间的推移，这个问题会更严重，如果「强调笔记」功能不可靠，我不想将其纳入。

「强调笔记」的视角将用户的指导置于首位。另一种考虑这种控制的途径是通过迭代的反馈。例如，一位读者高亮了一个定理，该定理表示，如果一个线性系统通过三种列出的操作之一转换为另一个系统，那么第二个系统与第一个系统具有相同的解集。在他的复习过程中，他收到了一张卡片，写着这个定理在高斯方法安全性中的作用。他对此感到困惑，一旦他点击「查看来源」查看卡片来自何处，他说：「哦，不，我在这里并不关心证明正确性——我想确保我知道这三个『安全』操作。」理想情况下，他应该能在复习过程中告诉系统：「只需确保我知道安全的操作。」

另一位读者希望他能让卡片更加非正式：更多的口头解释和例子；降低符号和抽象的程度。这种反馈应该不仅影响当前的卡片，而且可能影响整本书的所有卡片，甚至是过去、现在和将来的所有卡片。

我的简短实验表明，对于大型语言模型来说，调整预制卡片比要求它们重新生成卡片更可行。例如，考虑这张卡片：「问：在线性系统中，一行的**首变量**（leading variable）是什么？答：第一个非零元素对应的变量。」我的一位读者希望这种抽象的答案能附上具体的实例。GPT-4 [能够](https://chat.openai.com/share/ed8404b4-c4e6-47dc-b4d2-2e9c6b9e4aa7)根据这个要求适当地重写卡片。当然，这个例子手动完成并不难，所以这里的权衡可能没有意义，除非它们可以应用到许多卡片，或者机器生成非常可靠。

## 下一步

这里我想说点自己的感受：这最后一轮测试对我来说相当令人兴奋！新设计似乎解决了多年来我在各种记忆系统设计中观察到的许多问题。而且——非常谨慎地说——它似乎还能在阅读理解方面提供支持，帮助一些读者。这是一个很好的迹象，说明**我**真的很想在日常阅读中使用这个工具。

尽管如此，这轮测试还相当肤浅。我想了解各种人对设计理念的反应，所以我与 14 人分别进行了约一个小时的交流。因为我们只读了书的第一节，所以这些概念之间没有太多机会建立联系，对记忆和理解的要求也不高。而且，由于我只观察了一次会议，我没有机会看到随着时间的推移，遗忘的影响变得显著时，记忆和理解支持的表现如何。

因此，从本周开始，我将转向深度优先的方法。就像[今年早些时候](https://www.patreon.com/posts/becoming-wizard-79359297)一样，我将每周与一名学生会面几个小时。我们将继续深入阅读这本书，其中的材料将以更具挑战性的方式逐渐累积。在这些会议期间，我们还将完成一些习题集，观察这种增强如何与实际能力相互作用。

这些观察仍然是定性的。与此同时，我想开始更系统地了解我的设计对阅读理解的影响。它帮助读者发现有意义的缺口的频率如何？是否有某些类型的缺口容易被忽视？接受这种干预的读者是否能更好地理解材料？在面对材料时是否感觉更有能力或更投入？

目前，我的原型需要我手动将读者的高亮内容映射到精选高亮内容。而且我必须尽快完成，这样他们在阅读完该部分后才能点击「建议高亮」功能。如果我想与几十名用户进行实验，这将耗费大量时间。因此，在与一名学生进行深入研究的同时，我将尝试自动化读者高亮与精选高亮之间的映射。

我的初步测试表明，与我设计中的另外两个目前需要手动完成的任务相比（识别文本中最重要的元素，并为每个元素编写优质卡片），这个任务更容易自动化。这些任务在某种程度上是可分开进行的，这很好，这样我可以通过仅自动化高亮到卡片的映射来取得一些进展。

如果我能自动化这种映射，我就可以把这个原型公之于众，尽管它只限于这一本书。这是一个值得期待的里程碑，我相信——像往常一样——公众使用会带来许多意想不到的启示。从那里开始，是的，自动化精选和卡片编写任务固然很好，但我对使用一本大部头作为深度优先的实验室，探索其他阅读增强想法的前景也很感兴趣，其中许多我在这些文章中都已经讨论过。

让我的作品充满活力的一个断言是「[书本不起作用](https://andymatuschak.org/books)」。展开来说，为了真正理解、内化和记住解释性文本的观点，读者必须采用各种隐含的、往往不可靠的策略，而书这一媒介对此帮助甚微。如果处理文本的经验自然能保证所有这些额外的工作得以完成呢？我希望在处理解释性文本时，能创造出一种**异乎寻常的能力和轻松**。

分解一些你可能需要的东西，让一本书真正以你所希望的方式「起作用」：

- **理解。**你需要真正加工页面上的文字，并在你未能做到这一点时察觉到。对大多数读者来说，这在大多数时候都是[出乎意料的困难](https://www.patreon.com/posts/reading-and-85345515)！[大多数干预手段都相当突兀](https://www.patreon.com/posts/initial-in-self-87053505)；当前的原型是我尝试的一种更实用的增强方式。

- **记忆。**你需要记住你读过的内容。这促成了[《量子国度》](https://quantum.country/)和[助记媒介](https://numinous.productions/ttft)的诞生。但我发现，现今的记忆系统往往产生脆弱的记忆，而我希望探索像[变化卡片和逐步提升综合性](https://www.patreon.com/posts/fluid-practice-83882597)等想法来改善这一点。

- **阐述。**你不仅仅需要理解文本的字面意思，还要理解其**意义**和**重要性**。你需要将文本的想法与之前的知识和经验相联系。[讨论](https://early.khanacademy.org/open-ended/)是我喜欢的一种方法；深思熟虑的写作（最好出于某种实际目的）是另一种。我希望发掘更多此类方法，并找到将这些活动更好地融入阅读体验的方式。

- **流利。**你需要通过实践来巩固你所读的知识，使之内化为一种自然反应。这涉及到模式归纳、图式习得和知识编译。在技术领域，这常常指的是[解决问题的实践练习](https://www.patreon.com/posts/memory-systems-80865178)——参见像 [Mathigon](https://mathigon.org/) 和 [Execute Program](https://www.executeprogram.com/) 这样的项目。项目式学习是另一种常见的方法，我对「[以实践为中心的解释媒介](https://andymatuschak.org/doing-centric/)」等想法很感兴趣。

- **干预。**你需要诊断并解决可能存在的困惑和误解。[专注过程步骤的题目通常无法明确识别概念性问题](https://www.patreon.com/posts/studying-myself-88583610)。在这方面，教授他人是一种经典方法（译注：即费曼学习法），催生了像 [AutoTutor](https://notes.andymatuschak.org/AutoTutor) 这样的综合干预工具。当用户能够清楚地表达时，前沿的大型语言模型通常能在解决困惑方面表现出色。我对于轻量级、一体化的困惑识别和解决方法很感兴趣。

- **整合。**大多数时候，你阅读一本书不仅仅是为了获取知识，而是因为你希望它能以某种方式**改变**你——改变你的思考方式、看待世界的方式，或你在特定情境中的行为和感受。为了让一本书真正成为现实，你必须将它的想法带入你的生活。与之相关的一些想法，请参阅[启明卡](https://andymatuschak.org/prompts/#prompting-salience)和[穿越时间的文本](https://numinous.productions/timeful)。阅读俱乐部在这方面很有用；我也想探索更多结合新媒体与社交活动的创新方式。

当然，这足够作为几辈子的研究计划了。但我之所以在这里详细阐述，是为了帮助自己抵抗旧金山周围的文化压力。这种文化压力使我感到，一旦我有了一个创意——比如高亮引导的记忆卡片——就应该大力推广，使其影响尽可能多的地区和人群。当然，这种做法有其价值。我确实想在所有地方都用上这种特别的高亮笔。但同时，我也需要权衡这种冲动，与发掘更深层次的基础理念并更全面解决我所关注问题的可能性。

————————

感谢所有在这第一轮测试中与我一起合作的学生，也感谢 Benjamin Reinhardt 对我下一步计划的有益讨论。