# 把 X 上最值得看的推，每天早晚送到你邮箱

我每天早上第一件事是打开 X 找选题灵感。但这个动作越来越难坚持——一刷开就是几十条卖货广告、陌生人的梗图、和"震惊体"AI 号的复读。想看的那几位，Karpathy、Aaron Levie、dharmesh、宝玉，信号淹在噪声里。

说实话，X 上的内容质量其实没降。Levie 一条关于"Agent 架构每季度推倒重来"的观察，比大部分科技媒体一整天的稿子都有用。问题出在获取方式：我们在用刷信息流的姿势读一份本该高密度筛过的情报。

所以我写了一个开源小工具，叫 **X Radar**。

## 它做的事

每天早 6 点、晚 10 点两次，抓你指定的 X 账号过去几小时的新推，让 Claude 读一遍、写一段"今日观察"、按跟你工作的相关度排序，然后把结果邮件发到你邮箱。英文推自动附一句中文要点。原始 JSON 全量落盘，回头写文章做视频时翻得到。

这是我刚收到的那一封：

![邮件概览](./asset/email-overview.png)

顶上是 Claude 写的一段综述，下面是它推荐的阅读顺序。每条推都带"为什么值得看"一句话——不复述原文，只告诉我对我的选题有什么用。

![单条详情](./asset/email-detail.png)

上面这条 Levie 的"每家非科技公司都将是软件公司"——这种级别的观察我一年也读不到几条，过去基本靠运气。这就是 X Radar 想做的事：把"刷"变成"读"。

## 数据从哪来

需要一个 [twitterapi.io](https://twitterapi.io) 账号，这是目前我用过最便宜也最稳的 X 数据接口。

![twitterapi.io](./asset/twitterapi-home.png)

计价很直白：每返回一条推文收 15 credits，$1 = 100,000 credits。

![Credit Usage](./asset/credit-usage.png)

我默认配置的 25 个账号，每天两次拉取，一天大概 15,000 credits。**充 10 美金够跑两个多月**。

关键是支持支付宝，10 美金起充，国内开发者零门槛：

![支付宝支付](./asset/payment-alipay.png)

## 怎么用

前置：macOS/Linux、Claude Code、Python 3.10+。

```bash
git clone https://github.com/andyleimc-source/x-radar
cd x-radar && cp .env.example .env
# 填入 TWITTERAPI_IO_KEY
```

改 `config/accounts.yaml` 换成你关注的人。在 Claude Code 里跑一句 `/twitter-digest morning`，第一次会回填过去 24 小时的推文。

定时任务用 launchd，项目 `ops/install.sh` 一键装好早晚两个时段。

## 不想用邮件？推到微信

邮件是默认渠道。如果你更习惯微信，改最后一步的发送逻辑，接 [OpenClaw](https://openclaw.ai/) 或 [Hermes](https://github.com/nousresearch/hermes-agent)，把摘要推到你自己搭的微信 ClawBot：

![微信 ClawBot](./asset/clawbot-wechat.png)

睡前一条微信，比爬起来看邮件舒服多了。

## 仓库

https://github.com/andyleimc-source/x-radar · MIT

欢迎 fork 改成你自己的口味。我自己这份默认选的是 AI、低代码、SaaS、营销技术领域的人，你换成投资、设计、学术随便怎么切都行。

本质上它就是一个"用 Claude 替你读 X"的管道——**把信息搜集自动化，把判断留给自己**。

---

**老雷（Andy）**，明道云 & Nocoly CMO，SaaS 行业从业十余年。骨子里是个技术迷，乔布斯的信徒，相信好的产品能改变世界。深度关注 AI、商业与科技趋势，目前在深度使用和实践 Claude Code，专注探索 AI 如何重塑产品形态和商业逻辑。不聊概念，只聊真实发生的事。
