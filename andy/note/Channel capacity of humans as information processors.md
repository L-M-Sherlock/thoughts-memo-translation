# 人类作为信息处理机时的 “信道容量”

原文：[Channel capacity of humans as information processors (andymatuschak.org)](https://notes.andymatuschak.org/z8iJEzmLdBMoWYtQHkDohDgeWz6UBGm74qEiW)

要探究一个人信息处理能力的极限，一个方式是询问他能从观察到的刺激中，重现出多少信息。在这个框架下，我们可以利用信息论提供的工具，将观察者作为一个通讯信道来建模。 zhèi 个示意图 (Pollack, 1953, p. 422)  描绘了这个模型：

![img](https://notes.andymatuschak.org/BearImages/9119F79E-226A-4444-812A-95ECE478725D-84615-0002BE6722045500/54B6FF53-D8F9-4EF4-9637-501FC3D620C7.png)

理想的信道可以重现你给定的任何输入。而实际的信道，多数（包括人类）的复现会掺杂错误，并且随着输入中的信息增多而增多。这个行为通常是渐进发生的：一个信道会完美地传输它的输入，直到超过了一定的阈值。过了这个阈值 —— 即我们所称为**{信道容量（channel capacity）}** ——，输入输出的相关性随之下降，而传输的总 bit 数保持不变

对人类 [绝对判断域](https://notes.andymatuschak.org/ziwhFzgTbrS2uxWEkCvoJzQrDzRz5EAWWZFy) 的实验可以用来建模人类的信道模型。Miller （1956）回顾了历史经验数据，认为对于无维度的刺激，人类的信道容量大约为 {2.6} bits

例如这里 Miller 给出的一张图 (1956, p. 83), 使用了 Pollack (1952, 1953) 关于人类对音高绝对判断的实验数据，并用信息论的方法进行了重构。

![img](https://notes.andymatuschak.org/BearImages/DA4C7164-D6A1-4071-9E7A-A3FB315492B7-30732-0002A0FA5EE4ABE5/3D12BA5B-64F8-4AD4-8D08-1BE3F86CBCB8.png)

------

问：如果知道一个受试者的绝对判断域（对于单项、单维量级），你如何获得他们的通道容量？

答：通道容量=log_2（绝对判断的跨度）

问：为什么绝对标度的跨度，与人的信道容量有log2的关系？

答：通道容量以比特表示。如果绝对标度的跨度是 8 个类别，你需要log2_(8) bits 来表示每个状态。

------

## 参考文献

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review, 63(2), 81–97. https://doi.org/10.1037/h0043158 [Miller - The magical number seven, plus or minus two](https://notes.andymatuschak.org/zjfsd9pyxWQAF3HU5k7RAXhRjJBqtMEGKK27)

Pollack, I. (1952). The Information of Elementary Auditory Displays. The Journal of the Acoustical Society of America, 24(6), 745–749. https://doi.org/10.1121/1.1906969

Pollack, I. (1953). Assimilation of Sequentially Encoded Information. The American Journal of Psychology, 66(3), 421–435. JSTOR. https://doi.org/10.2307/1418237