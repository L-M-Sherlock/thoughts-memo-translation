# 通过间隔证明复习来理解证明中的关键点

原文：[Spaced proof review as a way to understand key insights in a proof](https://wiki.issarice.com/wiki/Spaced_proof_review_as_a_way_to_understand_key_insights_in_a_proof)

我认为数学有一个核心难点就是「[组合爆炸](https://wiki.issarice.com/wiki/Combinatorial_explosion_in_math "Combinatorial explosion in math")」，换句话说就是可能性的问题。比如说一份证明中，有一处不等式符号是 ≤ 而不是 < 或者其他符号（比如说反过来的 ≤），那么当你阅读这份证明时，你必须准备好去解释「为什么这么用」。对于证明中的每个环节，你必须有能力解释，为什么作者是如此操作，而非采用其他办法。最终你[不仅仅记住了表面上短短几行的证明](https://wiki.issarice.com/wiki/Spaced_proof_review_is_not_about_memorizing_proofs )—— 而是在解答一类更大的问题：「为什么作者选择这个办法，而不是其他那些行不通的办法」，这样一来，你写自己的证明时便有了思路。随着证明一点点淡忘，你的想法是「等一下，所以这里我应该做**这件事**还是**那件事**？」所以你测试这两条路，之后你会恍然大悟，「原来书上写成了那个样子是这个原因」。

有一次我想证明 Löb 定理，但我连证明开头使用的技巧都忘记了。（也许这样也挺好，因为我不仅仅是依赖于记忆技巧！）最终我想起来了，Löb 定理和圣诞老人命题有关，所以我写下了「如果这句话是真的，那么圣诞老人存在」。于是我回忆起了我需要一些类似 $T \vdash L \leftrightarrow (L \to \varphi)$ 的命题，继而回忆起，它并不仅仅是一句光秃秃的命题， 而且在某个地方有一个可证明谓词，基于此我又回忆起，我们应该将 $\mathrm{Bew}(x) \to \varphi$ 对角化。因此 $T \vdash L \leftrightarrow (\Box L \to \varphi)$。在这之前，对于为什么我应该将那个特殊的公式对角化（或者那个公式是哪里冒出来的），我是感到疑惑的。

## 参见

* [通过间隔证明复习来发明新的证明方法](https://wiki.issarice.com/wiki/Spaced_proof_review_as_a_way_to_invent_novel_proofs)

## 外部链接

* [https://mathoverflow.net/a/3957](https://wiki.issarice.comhttps://mathoverflow.net/a/3957)