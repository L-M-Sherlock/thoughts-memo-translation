# 论证对权威的屏蔽效应

原文：https://www.readthesequences.com/Argument-Screens-Off-Authority

**场景1**：Barry 是一位德高望重的地质学家，而 Charles 则是一个 14 岁的问题少年，他有着一长串的犯罪记录，还不时会精神病发作。Barry 对 Arthur 信誓旦旦地做出一个有悖常理的关于岩石的论断，Arthur 认为此论断有九成把握是正确的；而当 Charles 也做出同样违背直觉的论断时，Arthur 却只给出了一成的可信度。显然，在评判论点的可靠性时，Arthur 将说话者的**权威**也考虑在内了。

**场景 2**： David 就物理学提出了一个违背直觉的观点，并向 Arthur 详细解释了他的论证过程，包括相关的参考文献。Ernie 也提出了一个同样悖离常理的说法，但他的论证漏洞百出，有几处前后逻辑不连贯。David 和 Ernie 都声称，这是他们能给出的最佳解释（不仅仅是向 Arthur 解释，而是面向任何人）。听完 David 的解释后，Arthur 认为他的观点有 90％ 的可能性是正确的；而对于 Ernie 的说法，Arthur 只给出了 10％ 的可信度。

乍看之下，这两个场景似乎大体对称：它们都需要考虑有用的证据，不管是来自强有力的权威还是站不住脚的权威，亦或是严密的论证还是漏洞百出的论证。

现在让我们进一步假设，Arthur 要求 Barry 和 Charles 给出完整严密的技术论证，并列明所有参考文献出处。而 Barry 和 Charles 各自递交的论证质量旗鼓相当。Arthur 仔细核查了所有引文，发现它们确实能够支撑各自的论证过程。接下来，Arthur 又调查了 David 和 Ernie 的背景资历，结果发现他们的履历其实很相似——可能他们都是马戏团的小丑，也可能他们都是专业的物理学家。

假设 Arthur 完全能够理解这些技术论证（否则那些论证对他而言只是些华丽但空洞的辞藻），那么在他看来，David 的可信度应该远胜于 Ernie，而 Barry 与 Charles 之间的差距则显得微不足道了。

事实上，如果技术论证本身足够严谨有力，Barry 对 Charles 的身份优势或许根本不值一提。一个真正优秀的技术论证，应该能够**消除**对论证者个人权威的依赖。

同理，如果我们真的相信 Ernie 给出的论证已经是他**所能**做到的最好论证——包括他的全部推理过程、所有论据，以及他参考的任何权威——那么，我们完全可以忽略 Ernie 资历的任何信息。不管 Ernie 是物理学家还是马戏团小丑，都不应影响我们对论证本身的判断。(当然，这里假设我们有充分的知识背景去理解他的论证。否则，Ernie 不过是在说一些玄乎的话，我们能否「信服」，很大程度上就取决于他的权威了。) 

由此可见，论证和权威之间存在某种不对称性。一方面，即便面对权威，我们仍然渴望听到有说服力的论证；另一方面，如果论证本身已经非常充分，那么论证者的权威身份几乎不会再提供任何额外信息。

（一个新手会说）权威和论证显然是本质上不同的[证据](https://www.readthesequences.com/What-Is-Evidence)类型，这种差异无法用[贝叶斯概率理论](https://www.readthesequences.com/An-Intuitive-Explanation-Of-Bayess-Theorem)那一套简洁明了的方法来解释。因为尽管两种情况下的证据强度是一样的——都是 90% 对 10%，但将它们组合起来后的表现却大不相同。我们该如何解释这一点呢？ 

接下来我将从概率论的角度进行技术演示，阐明如何体现二者的差异。（剩下的部分，要么相信我的权威，要么自己去查阅参考文献吧。）

假设已知条件概率 P(H|E1)=90%，P(H|E2)=9%，那么当 E1 和 E2 同时为真时，H 的概率 P(H|E1, E2) 会是多少呢？仅凭这些信息，我们无法运用概率论求出答案。求解 P(H|E1, E2) 所缺少的关键条件，不是 H 的先验概率，而是 E1 和 E2 两个事件之间是否相互独立。如果它们并非独立事件，就会影响最终概率的计算结果。

假设 *H* 表示「我的人行道很滑」，*E*1 表示「我的洒水器正在工作」，*E*2 表示「现在是晚上」。从洒水器启动后的一分钟开始，人行道就会变得湿滑，一直持续到洒水器停止，而洒水器每次会连续工作十分钟。因此，如果我们知道洒水器正在工作，那么人行道滑的概率就是 90%。在夜间，洒水器工作时间占 10%，所以如果我们知道现在是晚上，人行道滑的概率是 9%。如果我们同时知道现在是晚上，并且洒水器正在工作——换句话说，如果这两个条件都满足——人行道很滑的概率就是 90%。

我们可以用下面的图模型来表示这种关系：

 ![diagram: [Night] → [Sprinkler] → [Slippery]](https://www.readthesequences.com/wiki/uploads/ArgumentScreensOffAuthority_diagram_1.svg)

是否是夜晚**决定了**洒水器是开还是关，而洒水器是否开启则**决定了**人行道是否湿滑。

在图示中，箭头的指向具有特殊的含义。让我们看第一个例子：

 ![diagram: [Night] → [Sprinkler] ← [Slippery]](https://www.readthesequences.com/wiki/uploads/ArgumentScreensOffAuthority_diagram_2.svg)

它表明，如果我们对洒水器**一无所知**，那么「夜晚」和「路面湿滑」这两个情况就互不相干。再看第二个例子，假设我掷出两枚骰子，并把点数相加：

 ![diagram: [Die 1] → [Sum] ← [Die 2]](https://www.readthesequences.com/wiki/uploads/ArgumentScreensOffAuthority_diagram_3.svg)

如果你只告诉我第一枚骰子是 6 点，我还无法判断第二枚骰子的点数。但如果你再告诉我总和是 7 点，我马上就能推断出第二枚骰子是 1 点。

在不同的知识背景下，要判断各类信息之间是存在依赖关系还是相互独立，实际上是一个相当专业的研究课题。推荐阅读 Judea Pearl 所著的两本专著：[《智能系统中的概率推理：可信推理网络》](https://smile.amazon.com/Probabilistic-Reasoning-Intelligent-Systems-Plausible/dp/1558604790/?sa-no-redirect=1)[1]和[《因果关系：模型、推理与推断》](https://smile.amazon.com/Causality-Reasoning-Inference-Judea-Pearl/dp/052189560X/ref=dp_ob_title_bk?sa-no-redirect=1)[2]。（如果你只能抽出时间读一本，建议选择第一本。）

如果你懂得解读因果图，看到掷骰子的图，就能马上得出以下结论：

*P*(骰子 1, 骰子 2) = *P*(骰子 1) × *P*(骰子 2)

*P*(骰子 1, 骰子 2 | 点数和) ≠ *P*(骰子 1 | 点数和) × *P*(骰子 2 | 点数和).

仔细观察人行道湿滑的因果图，不难发现一些事实：

*P*(湿滑|夜晚) ≠ *P*(湿滑)

*P*(湿滑|洒水器) ≠ *P*(湿滑)

*P*(湿滑|夜晚, 洒水器) = *P*(湿滑|洒水器).

换言之，如果我们已经知道洒水器的状态，那么无论时间是否是夜晚，人行道变滑的概率都是相同的。洒水器的信息使得「夜晚」这个因素在判断路面滑度时变得无关紧要。

这种现象被称为「屏蔽」，而允许我们从因果图中识别这种条件独立性的标准被称为「D-分离」。

在论证和权威的关系中，因果图可以表示为：

 ![diagram: [Truth] → [Argument Goodness] → [Expert Belief]](https://www.readthesequences.com/wiki/uploads/ArgumentScreensOffAuthority_diagram_4.svg)

如果某个观点是正确的，通常会有支持它的有力论证，专家们在看到这些证据后就会相应地调整自己的看法。（理论上是这样的！）

当我们发现一位专家持有某种观点时，我们会推断背后可能存在某些证据（尽管我们可能不知道具体是什么证据），然后基于这些抽象的证据来推断该观点的真实性。

然而，如果我们直接了解了论证的质量，这就在「真相」和「专家观点」之间形成了 D-分离，阻断了它们之间的所有联系路径。这是基于某些在这种情况下看似显而易见的「路径阻断」技术标准。因此，即使不查看具体的概率分布，我们也能从这个图中得出结论：

*P*(真理|论证, 专家) = *P*(真理|论证)。

这并不意味着与普通概率理论相矛盾，而只是一种更简洁的方式来表达某些概率事实。你可以从一个简单的概率分布中得出同样的等式和不等式，只是单凭直观观察会更难发现。权威和论证并不需要依赖两种不同的概率体系，正如洒水装置并非由本质上有别于阳光的物质构成一样。

在实践中，我们无法**完全**摆脱对权威的依赖。优秀的权威更有可能全面了解所有支持和反对的证据，并加以权衡；而相对次等的权威则可能遗漏一些关键证据，使得他们的论证缺乏说服力。这种权威的影响并非仅仅听取他们**的确**考虑过的证据就能消除。

此外，将论证简化为**纯粹的**数学表述也是一项极具挑战的任务；否则，评判论证步骤的合理性就可能取决于某些没有相应的几十年经验就难以形成的直觉。

在判断一个观点的可信度时，我们或许会**稍微**更倾向于相信权威人士的看法。比如在贝叶斯概率的问题上，E. T. Jaynes 比 Eliezer Yudkowsky 多了 50 年的经验，这让人觉得 Jaynes 的观点应该**略微**更有说服力一些。 

但权威的这点可信度优势，仅仅在**其他条件都相同**时才能占上风。一旦出现了更有力的证据和推理，它很容易就会被击败。就像我在 Jaynes 的书中发现了一处代数错误一样——逻辑证明的力量是无可辩驳的，再权威的人也得服从事实。