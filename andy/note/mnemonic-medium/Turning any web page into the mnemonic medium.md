# 把任意网页转化成助记媒介

原文：[Turning any web page into the mnemonic medium (andymatuschak.org)](https://notes.andymatuschak.org/z2hABbXxq3dz9XQ6bWrqLyModyC5EC2MXxNA)

[量子国度](https://notes.andymatuschak.org/z2fBHADWa93EZTuNzuww7V3Vi587ZyZ4FHTHm)是专门制作的网站；文章的呈现与助记媒介的机制紧密结合在一起。然而，助记媒介的主要交互是足够独立的，因此，这些交互应该可以通过简单的 HTML 代码嵌入任意网页。

我有[操作系统层级的间隔重复系统](https://notes.andymatuschak.org/z36iMKLe4CDAXdtLSJD4Z6qPPFUS8ZXymUk3i)这一愿景，能任意嵌入这点对这个愿景是核心的一环。

## Web 组件

通过设定新的 HTML 标签（比如 `<card>`），我们可以定义助记卡片的规格。之后我们会提供 Javascript 库，其功能是对导入这个库的页面，将这些组件「注水」，在运行时把标签替换为 DOM 节点。除了 Edge 的所有现代浏览器都支持这样的 [Web 组件](https://www.webcomponents.org/)，而且似乎有 Web 组件的 polyfill。

这种实现方式无需将发布者绑定到特定的用户数据存储服务器：我们的客户端库可以灵活接入各种存储方案，包括支持客户端本地持久化存储（无需账号！）。

这个方法非常灵活：你可以替换客户端的库，只要支持同一个 Web 组件规格即可；未来可以增加对不同后端服务器的支持。可以扩充这个 JS 库所支持的功能。出版者可以自己部署 JS，或者利用我们手下的 CDN。如果 JS 被禁用了，或者脚本无法获取，卡片只是会不显示。甚至可以定义标签打印时的样式。

这个方法需要不少抽象。如果需要大改协议、规格、状态格式之类，我们可能会遇到兼容问题。

更重要的是，这个方法需要作者/出版者撰写 HTML。假如作者的工作流是从 InDesign 源文件导出 HTML，在这样的工作流里加入卡片就比较困难了。如果 HTML 文档不是「真相之源（source of truth）」，只要作者重新从源文件导出，卡片标签会被删除。

对于这种方法，可能需要为 Wordpress 之类的平台写插件。

### 第三方的用户验证有很高门槛

只要用户登录了，他们应该不用在每个网站登录就在边上网边积累卡片。这样很难实现啊！

托管网站不能写 cookie 让其他托管网站读取；cookie 是按来源锁定的。

我们可以把验证机制嵌入在 iframe 里，在同一来源托管，但这样的 cookie 是「第三方 cookie」。最近几年来，浏览器开始激进地锁定第三方 cookie，其中以 Safari 为最。其原因是第三方 cookie 被广泛用于实现侵犯隐私的跟踪和广告功能。

问题的症结在于，任何允许嵌入式身份验证提示共享凭据的机制，都可能被滥用于用户跟踪和隐私侵犯。我们似乎难以避免被卷入浏览器安全政策的交叉火力中。虽然 Chrome 和 Edge 目前还能「照常运转」，但 Safari 和 Firefox 却不然。值得注意的是，微软 Edge 浏览器已将存储访问 API 列入了「实现中」的功能清单。

苹果和 Mozilla 提供了存储访问 API，允许第三方站点申请访问其存储的身份验证凭据，但在 Safari 浏览器中，这似乎**总是**需要明确的用户批准，多少有些令人不快。更加严苛的是，Safari 可能**仍然**只有在用户已经在第一方上下文中与网站产生交互后，才会允许设置 cookie。这无疑是非常苛刻的现实，我们可能需要开发 Safari 扩展来优化和提升浏览体验。

值得欣慰的是，Safari 至少新增了一个 API，供第三方站点判断用户的登录状态。[变更集 250944 – WebKit](https://trac.webkit.org/changeset/250944/webkit)

## 解析并替换文本块

一些工作流中用户不能随意添加 HTML 标签。比如利用只有可视化编辑手段的博客软件制作网站。

这时候，如果假定我们能注入脚本，作者便可以像[我的个人助记媒介实现](https://notes.andymatuschak.org/z4mAF1uBV96r72e4NjLcDaujEyTPGiUQJEj8C)里一样添加问题，之后在运行时由脚本解析提取。