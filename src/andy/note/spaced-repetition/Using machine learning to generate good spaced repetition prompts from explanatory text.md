# 使用机器学习从解释性文本中生成优质的间隔重复卡片

原文：[Using machine learning to generate good spaced repetition prompts from explanatory text (andymatuschak.org)](https://notes.andymatuschak.org/z2DY7qsP5iHsiA5hxUHheV8hu7Xe96vdGyYX)

一个颇具挑战的问题。一些相关笔记：

- [GPT-4 在指导下，通常能够从解释性文本中为陈述性知识生成可用的间隔重复卡片](https://notes.andymatuschak.org/z2VVmj24FLixtrijdAbkKty91JQruAaZGbHE6)

  - [对于卡片生成任务，选择要强化的目标概念，和为这些目标概念编写卡片，是两个独立的问题](https://notes.andymatuschak.org/z62s1nNLEfhGbDmpb8Z7dZiYyi3kaSziuLVXd)

    - [将卡片生成任务定义为强化目标的过滤问题](https://notes.andymatuschak.org/zQ4E1DXZoZTTitsik89ZcvXMu8dQMkJzRUS)

  - [对于卡片生成任务，如果提供了编写卡片的原则，大型语言模型（LLM）的表现可能会有所提升](https://notes.andymatuschak.org/zrqgkr9n3eCMNsAPDsRozt3HLd8nRT5nVASc)

  - [对于卡片生成任务，大型语言模型（LLM）经常需要额外的提示来确定需要强化何种角度](https://notes.andymatuschak.org/zomoPzCNzSi5GqtfTeVWgm7RjmiArjS8vvM5)

  - [对于卡片生成任务，如果提供了充足的上下文，大型语言模型（LLM）可能会表现得更好](https://notes.andymatuschak.org/z5LQFLXHFLrb4nYAtLrB3JBzNyJng8fYHVJYN)

- [对于卡片生成任务，大型语言模型（LLM）缺乏为复杂概念材料编写卡片的模式](https://notes.andymatuschak.org/zmrbnm683nVZi9ut63vsr8BwYKEtATA6e4B3)

- LLM 可以完成的一些更简单的子任务：

  - [GPT-3 能够产生间隔重复记忆卡片问题的简单变体](https://notes.andymatuschak.org/zEhne31FD53eNQw3bpcuomfxMYL3s1qkhbF)

  - [GPT-3 可以基于填空卡生成问答卡](https://notes.andymatuschak.org/z4A7LCXBAkAUH2uZ21JnNrBhJHCjkobFMyn)

  - [GPT-4 或许可以判断两张卡片在功能上是否是等价的](https://notes.andymatuschak.org/z3r1Lqmf4W9KPU2scVDSdbafthRBisJgv3G6a)

  - [GPT-4 或许可以判断一张卡片是否会剧透另一张卡片](https://notes.andymatuschak.org/z3PxNiZC25rkdrbgig9zm6oYk9AAECVKySYKG)

- [专家编写的卡片数据集将有助于开发卡片生成系统](https://notes.andymatuschak.org/z6ZUDZaQrh43M64sHsZL48QZVKcFKQsTi4kTY)

## 模型

- 来自 [OpenAI](https://notes.andymatuschak.org/z3HA4Pzw3eyayQWh99237BuH9L577TFxzq1V2) Sunny Chen 的 [http://autonki.com](http://autonki.com/)

- 使用 OpenAI GPT-3 API 的 Polar 和 [Sana Labs](https://notes.andymatuschak.org/z4xUYCRTU7uUjZhafKD3jAcn5u5mHsDJwPMcc)

  - [Sana Labs](https://notes.andymatuschak.org/z4xUYCRTU7uUjZhafKD3jAcn5u5mHsDJwPMcc) 使用公认高质量的内容/问题/答案数据[微调](https://openai.com/blog/improving-language-model-behavior/) GPT-3

- [Ozzie Kirkby](https://notes.andymatuschak.org/zn9igQGgecLncBSpKbgv5123mC5YEAP3hnfP) 使用 [iarfmoose/t5-base-question-generator · Hugging Face](https://huggingface.co/iarfmoose/t5-base-question-generator)（一个经过微调的 [T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) 模型）进行了一系列实验。

- [Aithal, S. G., Rao, A. B., & Singh, S. (2021). Automatic question-answer pairs generation and question similarity mechanism in question answering system. Applied Intelligence.](https://notes.andymatuschak.org/zUb4zm9zcMaRki1rhXLofjzzYciBrZrFqjC) 使用了在 SQuAD 数据集上微调的 ProphetNet 模型从文本段落生成问题，并应用 BERT 模型来回答这些问题。

- Steuer, T., Filighera, A., Meuser, T., & Rensing, C. (2021). I Do Not Understand What I Cannot Define: Automatic Question Generation With Pedagogically-Driven Content Selection. ArXiv.

  - 一个基于BERT的模型，该模型配备了独立的内容选择机制

  - 有价值的参考文献目录

## 阅读队列

- A systematic review: Kurdi, G., Leo, J., Parsia, B., Sattler, U., & Al-Emari, S. (2020). A Systematic Review of Automatic Question Generation for Educational Purposes. International Journal of Artificial Intelligence in Education, 30(1), 121–204. https://doi.org/10.1007/s40593-019-00186-y

## 坟场

- [日志：尝试使用 GPT-3 生成间隔重复卡片](https://notes.andymatuschak.org/z2FBdAnkR9BXc9YZE924sfFRXMKwmHFQAhLXv)