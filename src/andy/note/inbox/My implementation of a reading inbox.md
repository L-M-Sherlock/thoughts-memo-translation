# 我的阅读收件箱实践

原文：[My implementation of a reading inbox (andymatuschak.org)](https://notes.andymatuschak.org/z61sPhxF8ZiXcDQF36W4HaYKnSxYJfZmLrkb4)

本笔记描述了我是如何在我的系统里实践[为有潜在价值的参考引用建立一个阅读收件箱](https://notes.andymatuschak.org/z3N113rxPFreW9xUkLkUFomr2LUqfXbdCo3M)的。

阅读有多种口味，不同的工具适合捕捉和阅读不同类型的媒体，但我会同时「清空」这个收件箱内的所有类型的项目。而由于[不应该设置多处收件箱](https://notes.andymatuschak.org/z7bj6MiUnFnP3GvM5QqHafy3LTaqQV56e1Mek)，所以我创建了一个「虚拟」收件箱，为所有类型的项目构建出一个统一操作的抽象层。

## 网页

数据库是由 Pocket 管理的。我可以通过桌面和手机上的浏览器扩展来添加网页。

我选择 Pocket 是因为它是免费的，有像样点的 API、不错的扩展，而且可以用作书签管理器。

我通过归档网页来整理它们；我通过将它们扔入回收站来销毁它们。

## PDFs

我把它们保存在 `~/Documents/Archive/Inbox`。我有一个 Alfred 工作流程，将当前在预览中打开的 PDF 复制/移动到这个文件夹。

我在 Skim 中阅读 PDF，因为它支持链接到特定位置和可导出注释。

我把 PDF 文件移到 `~/Documents/Archive`，然后把它们添加到 Zotero。我想丢弃它们时就将他们移入回收站。

## 电子书

我把它们保存在 `~/Documents/Archive/Inbox`。

我用 Clearview 阅读电子书，但我很讨厌它（参见[所有桌面 EPUB 阅读器都很糟糕](https://notes.andymatuschak.org/z5EgfjG9cqZKWW16JQD7Pd51bXZVeNpiFaYJS)）。

电子书也一样，我通过将它们转移到 `~/Documents/Archive` 并将其添加到 Zotero 来存档。我想丢弃它们时就将他们移入回收站。

## 实体书

我把代表书的 .bib 保存到 `~/Documents/Archive/Inbox`。我创建了一个快捷方式来使其快速完成。

我通过将电子书移到 `~/Documents/Archive` 来归档，然后运行 `file_epub.sh`，根据它们的元数据重命名。然后我从 `Inbox` 文件夹的 `.bib` 中删除它们的条目。