# 应用卡在多大程度上可以取代助记媒介中的回忆卡？

原文：[To what extent can application prompts supplant recall prompts in the mnemonic medium? (andymatuschak.org)](https://notes.andymatuschak.org/z3ERHM3aC9jCyTR5KpgxTAyXf7kNSkG57SqrR)

[助记媒介可以通过简单的应用卡帮助读者应用他们所学的知识](https://notes.andymatuschak.org/z6Y8xDS2AJyE1d34X99y14Sk1A7YCNas5kFjA)。在实现了这种卡片后，在多大程度上还需要传统的原子回忆卡呢？

想象一下，我们在高中的微积分课程中，你刚刚学会 `e^ x` 是导数为其本身的函数。如果这节课是用[助记媒介](https://notes.andymatuschak.org/z4rRX3qwSSJRsEkdXKwH2shamgHNeRthrMLiF)写的，我们可能会问这些回忆卡：

> 问：什么函数是它自己的导数？

> 答：`e^ x`

> 问： `f(x)=e^x` 的导数是什么？

> 答：`e^x`

但是，我们也可以想象将其做成一张应用卡：

> 问： `e^8x` 的导数是什么？

> 答： `8e^8x` [解释：e^x 的导数是它本身](https://notes.andymatuschak.org/z3ERHM3aC9jCyTR5KpgxTAyXf7kNSkG57SqrR)

如果我们只给他们这一个问题，我不一定期望他们对 `e` 的陈述性知识最终会很扎实：他们很可能最终只是记住这个问题的答案。[应用卡在重复时应该有所变化](https://notes.andymatuschak.org/z7hqxNNJkeS2eta2eVaUx7cGB27axq2bw3h2y)，所以想象一下，我们还问了一堆变体，比如：

> 问：令 `f(x)=14e^[x]`。`dy/dx` 是什么？

> 答： `14e^[x]` [解释：e^x 的导数是它本身](https://notes.andymatuschak.org/z3ERHM3aC9jCyTR5KpgxTAyXf7kNSkG57SqrR)

想象一下，读者可以解决这个问题，也可以解决其他半打的变体 ，现在距离最初的课程已经过去一个月了。让我们回到我们提出的回忆卡上。我们是否希望读者能够回忆起：「什么函数是它自己的导数？」我认为这是很有可能的......但我怀疑，与回忆卡的准确性相比，变体准确性之间的相关度会更高。

从概念属性上理解 `e` 与从程序上理解 `e` 是不同的。我猜想，包括这两种类型的问题可能会产生更丰富的精细编码。

现在，我们是否期望读者能够回答提出的回忆卡：「`f(x)=e^x` 的导数是什么？」我希望如此，而且可能性很大：毕竟这个问题可以被解释为一个微不足道的应用卡，而且读者已经解决了更难的变体。

这是否意味着，在有那些应用卡的情况下，这张回忆卡是不必要的？考虑一下：如果读者**没能**够一致地回答那些应用卡呢？第一个变体需要同时应用链式规则（以及 `d[kx]/dx = kx` 的知识）。第二种变体还需要理解 `dy/dx` 的语法。这些都是比较复杂的问题。

当读者忘记了回忆卡的答案时，他们会看一下答案，并试图记住它以便下次使用。如果问题是原子性的，而且复习安排调整得很好，这通常会奏效！但如果读者不能回答应用卡，他们就不能只看答案并试图在下一次记住它：[应用卡的答案不应该从记忆中得出](https://notes.andymatuschak.org/z8kP66eb8mLNQg3tevRg6gN7TETnYFpwyVVNK)。他们必须分析答案（可能包括其解释），分辨出他们没有记住的内容，并尝试在下一次回忆这部分内容。这比回忆卡所需的难度要大得多。一个对链式法则仍不放心的读者可能不会注意到他们无法回忆起 `e^x` 的导数。如果没有单独的以回忆为主的卡片，他们对这个应用卡的回答可能在相当长的一段时间内都是不可靠的。

对这个问题进行实证实验将是非常有趣的！当相关的回忆卡被搁置时，读者的应用卡准确性会受到怎样的影响？

一个有趣的实证例子是 [Execute Program](https://notes.andymatuschak.org/z2LGZ8cXBcQMP7YuAHbeVyCSLZoiMXvQNKCok)：[Execute Program 的卡片既是应用卡又是回忆卡](https://notes.andymatuschak.org/z28P3kw9MjfiPYe7RGhvRnjHNCiLjJi8YA2U2)。