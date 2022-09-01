# 没有作者参与时，我们如何将现有文本转化为助记媒介？

原文：[How might we adapt existing texts to the mnemonic medium, without participation of the author? (andymatuschak.org)](https://notes.andymatuschak.org/zvG5X4scr9mGCnR52dtkPGeHLBUntANhBvf)

[普及助记媒介似乎需要网络出版的普及](https://notes.andymatuschak.org/zLbzDQF4MLSUEgDKu16i2h9q1ea8jC5crTV)。此外，许多重要的书籍根本没有任何数字版本；许多人更喜欢纸质书籍和电子墨水阅读器。技术受众将在很长一段时间内继续使用 PDF. 那[有声书](https://notes.andymatuschak.org/zhjve4ix3DcGqVGZn3a7FCP7bZTvzVR99fd)和视频呢？如果我们能在不牺牲现有媒介力量的情况下，将现有媒介「升级」成助记媒介，那将是非常强大的。

下面的这些方法实际上都差强人意，但也许迭代之后就可以了呢？

## 「伴读」APP

你面前有本敞开的纸质书；你把手机放在书旁边，打开「记忆伴侣（Mnemonic Companion）」应用程序。你扫描图书的条形码，应用会显示目录（可能出于法律原因被部分删节）和页码选择器。你告诉应用程序你正在阅读第 312 页。屏幕上显示了一堆问题和一个大标题，上面写着：「在第 314 页的分隔处回答这些问题。」你开始阅读纸质书，一边标注重点，一遍粘上便利贴写注释，然后在适当的地方提交问题。应用程序将移动到下一个断点，你可以继续阅读。

这种方法缝合了太多流程。读者必须记住应该在哪里停下来，查看有没有到达这一点，并在两种媒介之间来回切换。听起来很痛苦。我怀疑能遵循这套流程的人会比《量子国度》少得多。

但这是一种非常灵活的方法，基本上可以适用于任何先前的媒体形式。它不需要作者/出版商合作，问题可以来自不同的制作人（相关笔记：[有声读物是在各种各样的商业模型下制作的](https://notes.andymatuschak.org/zbdNE8WLUE8SgBKvUgd8TCdQnmTj6CjJ94B)）。

另外，分销渠道很糟糕：阅读一本书的人必须决定单独寻找周围的其他材料，检查我们的应用程序以获得支持，并可能为这些材料单独付费。在 Twitter 上对一本书/PDF 的讨论并不会将人们引向这个同伴。无法形成任何有意义的网络效应。

## 给在线图书的浏览器扩展页面

对于已经在线的图书（如 [Cell Biology by the Numbers](https://notes.andymatuschak.org/zXBk7GLFDaxgd6oMsRd5Jdr17dnCtik3MQ8)），可以通过浏览器扩展来扩充它们。我不喜欢这样——这对用户来说是极高的要求。如果能将页面包装在 IFRAME 中并跨域操纵就好了，但是当然没有浏览器会允许这样做。

## 内容转换代理

添加一个 `<script>` 标签，通过「非透明」的网页代理重新提供目标网页。起码对于新用户来说，这种做法相比浏览器扩展的解决方案效果相同，而且更轻量。甚至可以提供可供链接的 URL！

[Hypothes.is](https://notes.andymatuschak.org/z24wddcuZTB2YvHTA4LkZ759DhydyufhrzCh) 使用其中的一种方法来使其「可共享链接」生效：via.subthe.is 注入目标 url。

这…实际上看起来挺可行的！

### 实现的注意事项

甚至还有一篇 W3C 文章！https://www.w3.org/TR/ct-guidelines/（这是「工作组笔记」，而不是已批准的文件）。

```

如果代理更改了回应体，则：

1. 必须在 HTTP 头字段添加 214 警告，表示应用了内容转换；

```

请参阅[警告代码](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Warning)。

```

代理应该在 Via HTTP 头字段留下注释，其中包含 URI "http://www.w3.org/ns/ct"，表示其转换内容的能力。

```

注意链接重写的安全问题：重写代理可能会意外地使两个不同的站点同源（例如与代理站点同源）。这可能会引入漏洞。另外：

```

**强烈反对**拦截 HTTPS 链接的做法。

如果代理重写 HTTPS 链接，它必须告知用户这样做的安全影响，并且必须提供绕过它并直接与服务器通信的选项。

...

转发来自服务器的响应时，代理必须通知用户无效的服务器证书。

```

现在基本上所有的链接都是 HTTPS，所以这或多或少相当于「不要重写链接」！或者至少：要「极其」小心。

另请参阅 HTTP 1.1 RFC 的[对中间层转换的评论](https://datatracker.ietf.org/doc/html/rfc7230#section-5.7.2)。

```

转换 200（OK）响应的有效载荷的代理还可以通过将响应状态代码更改为 203（非权威信息）来进一步通知下游接收者已经应用了转换

```

另请参阅此初步文档：[内容转换前景 1.0](https://www.w3.org/TR/2009/NOTE-ct-landscape-20091027/#d0e276)

## 自定义 PDF / EPUB 阅读器

我们可以制作自己的 PDF 或 EPUB 阅读器应用程序，将这些元素内联到现有的媒体形式中。或者它可能是基于 Web 的书签式阅览器：在任何 PDF URL 前面加上 [“http://mnemonic.com”](http://mnemonic.xn--com-9o0a/)，以便以这种形式阅读它，等等。

在 DRM 仍然无处不在的情况下，为 EPUB 做这件事不太可行。合法购买的电子书无法在我们的阅读器中打开。因此，为电子书这样做需要成立一家电子书商店。真恶心。

这将是一项繁重的工作。这里的分销渠道问题很大。

老实说，处理 PDF 的一个更好的方法可能是通过无数的「PDF 到网页」工具中的一种。获取学术 PDF；将其转换为网络出版物；**然后**对其增强（例如，通过[把任意网页转化成助记媒介](https://notes.andymatuschak.org/z2hABbXxq3dz9XQ6bWrqLyModyC5EC2MXxNA)）。

## AR 眼镜

如果我们将来都戴 AR 眼镜，我们可以用各种有趣的方式神奇地增强书籍。太遥远了，难以认真考虑？如果有关苹果 2022 年推出眼镜的传言属实，AR 覆盖即将引领新潮流…