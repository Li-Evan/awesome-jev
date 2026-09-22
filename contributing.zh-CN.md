# 贡献指南

[English](contributing.md) · **简体中文**

谢谢你帮忙把这里做成最全的 Jev 用例合集。参与贡献即表示你同意遵守[行为准则](code-of-conduct.md)。

## 最简单的方式：填表

不会写代码也没关系。打开[提交表单](https://github.com/Li-Evan/awesome-jev/issues/new/choose)，填名字、链接、一句话说明和场景，一分钟就够。表单是英文的，内容用中文写也可以，我们会整理成双语条目。

## 收什么

只要是真实的、用到了 Jev（TypeSafe 的 System One 模型）的东西，或者能帮人用好 Jev 的内容：

- 项目、应用、演示和实验，包括 X、Reddit、Hacker News 上展示你做了什么的帖子。
- 集成、SDK，以及兼容 Jev 接口的开源模型。
- 教程、评测、案例分析、演讲和视频。失败的实测同样欢迎，别人踩过的坑最有价值。

不收：

- 别人整理的列表和导航站。请直接提交原始项目。
- 纯新闻转述、营销页面，以及冒充官方的仿冒站点。
- 任何泄露 API key 或隐私数据的内容。

## 两条规则

1. **链接原始出处。** 链接必须指向项目自己的仓库、应用、帖子、文章或视频，不能是别人的聚合列表或目录。构建脚本会自动拦截这类链接。
2. **说清楚它做了什么。** 一两句大白话：它是什么、干什么；如果知道的话，再说一下它怎么用 Jev（用了哪种原语或模式）。

## 直接改数据

README 和各场景页都是自动生成的，请不要手改 `README.md`、`README.zh-CN.md`、`scenarios/`、`pages/` 和 `zh-CN/` 下的文件。

1. 在 `data/` 里找到对应场景的文件，例如 `data/finance.yaml` 或 `data/coding.yaml`。实在归不了类就放 `data/other.yaml`。
2. 加一条：

   ```yaml
   - name: jev-ultrafast
     url: https://github.com/browser-use/jev-ultrafast
     kind: repo            # repo, app, post, reddit, thread, video, article, model, package, docs
     author: browser-use
     description: Browser agent that picks each step's action from the page's element table in one request.
     description_zh: 浏览器 agent，每一步在一次请求里从页面元素表中选出要执行的操作。   # 可选
     jev: One Choice per step with speculative targets per operation.   # 可选
     image: https://raw.githubusercontent.com/owner/repo/main/screenshot.png   # 可选
     metrics: {stars: 14484}   # 可选：stars、likes、points、views 或 downloads
     date: 2026-09-16          # 可选
     links: {demo: https://x.com/user/status/123}   # 可选
   ```

   `description` 用英文写；`description_zh` 可以不填，不填时中文页面显示英文描述。

3. 运行构建，然后提交生成的文件：

   ```bash
   uv run scripts/build.py
   ```

4. 提 PR。一个 PR 放一个项目最好审。

在线画廊 <https://li-evan.github.io/awesome-jev/?lang=zh> 用的是同一份数据（`index.html` 和 `site/data.json`），改动合并到 `main` 后会自动更新。

## 图片

- 用项目自己页面上的图：README 里的截图、网页的 `og:image`、原帖里的图片，或视频封面。
- 直接引用图片原地址，不要把图片副本上传到本仓库。
- 优先 PNG、JPEG、WebP；超过 3 MB 左右的动图就别用了。
- 没有图片时，GitHub 仓库和 YouTube 视频会自动显示预览卡片。

## 描述风格

- 说事实，不说口号：“用两个 Choice 给 IRS 税表页面分类”比“革命性的 AI 报税神器”有用得多。
- 引用的数字和原文保持一致。

## 更新或删除

如果链接失效、项目已经不在了，或者描述有误，开个 issue 或 PR 简单说明一下就行。
