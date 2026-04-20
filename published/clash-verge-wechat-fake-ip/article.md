# Clash Verge 开了 TUN 之后，微信头像和朋友圈加载慢的根治办法

最近把 Clash Verge 的 TUN 模式（虚拟网卡）打开之后，微信开始出问题——好友头像加载不出来，朋友圈刷半天白屏，偶尔聊天消息也要转圈。关代理就正常，开了就慢。

一开始我以为是规则没把微信的流量放 DIRECT，折腾半天 PROCESS-NAME 规则，结果发现规则早就命中 DIRECT 了，慢的根本不是代理本身。

真正的元凶是 **fake-ip**。

Clash Verge 的 TUN 默认用 `enhanced-mode: fake-ip`，所有 DNS 查询都被劫持，返回一个假 IP（198.18.x.x），等连接建立时再反查真实 IP。对大多数应用这套机制很快，但微信有两个特殊之处：

一是微信靠几条**长连接**（`long.weixin.qq.com`）维持在线，fake-ip 在长连接重连时容易异常；二是头像和朋友圈图片走 `*.qpic.cn`、`*.qlogo.cn` CDN，瀑布流并发几十张小图，每张都被 fake-ip 多绕一圈，累加起来就是肉眼可见的卡顿。

修复思路不是关 fake-ip（会影响其他代理 App），而是**把微信的域名加进 fake-ip 白名单**，让它们走真实 DNS 解析。在 Clash Verge 的订阅 Merge 模板里加这段：

```yaml
dns:
  fake-ip-filter:
    - '+.weixin.qq.com'
    - '+.wx.qq.com'
    - '+.wechat.com'
    - '+.qpic.cn'
    - '+.qlogo.cn'
    - long.weixin.qq.com
    - short.weixin.qq.com
    - szlong.weixin.qq.com
    - szshort.weixin.qq.com
```

保存后回到 Verge 主界面点一下当前订阅刷新（不用重启），微信立刻恢复正常，其他代理应用不受影响。

说实话，这个问题在官方文档里是找不到的，只能自己翻日志、看规则、做对比实验。写出来给遇到同样问题的朋友省点时间。
