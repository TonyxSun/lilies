# Xiaohongshu research notes (read-only; viewed via www.rednote.com)
Note: xhslink.com over http errored in browser (ERR_HTTP_RESPONSE_CODE_FAILURE); https://xhslink.com/o/<code> worked and redirected to xiaohongshu.com/explore/..., which I rewrote to rednote.com.
No captcha encountered. Post dates shown by the site have no year (assumed 2026; note IDs decode to 2026 timestamps).

---------------------------------------------------------------
## POST 1 — 诶哟哟 "Agentic Investing实验记录：9.29"
- Short link: http://xhslink.com/o/29Oj2RymiOA
- Final URL: https://www.rednote.com/discovery/item/6ac05ccb0000000015001604  (xiaohongshu: https://www.xiaohongshu.com/explore/6ac05ccb0000000015001604)
- Author: 诶哟哟 — https://www.rednote.com/user/profile/5b337cdbe8ac2b4c65088bd0
- Date: Oct 2 (美国) [2026]. Stats: 290 likes, 253 saves, 34 comments. 2 slides.
- Title: Agentic Investing实验记录：9.29
### Full text
Robinhood前阵子推出了agentic account，于是决定浅投5000💰做个实验，看看AI能走多远。
我花了一个月做了套agent，由grok搭建一个15支ticker的portfolio，目标是跑赢SP500。
只允许买正股，不许加杠杆不许做空。
每30天做一次rebalance。期间AI可以自主决定是否进行月中调仓。
目前跑了一个月，surprisingly跑出了近12%的回报[呃R][呃R]
因此我决定做个记录，成本是每月30🔪的grok会员费，看看他能跑多远
最近一次更新持仓是9.29（P2）
#金融投资 #我的理财日记 #aiagent #ai投资
### Image text
- Slide 1: Robinhood app screenshot (18:02). "Agentic" account tab: $5,582.07, ▲ $582.07 (11.64%) Past 3 months; (Predict $0.00, Custodial tabs). Chart flat then sharp dip then big rise at the end. Buying power $0.70. Connected agent: "Grok" (Disconnect).
- Slide 2: table 代码 / 权重 / 每股成本 (ticker / weight / cost per share):
  MU 12% $950.09; LRCX 9% $297.04; EOG 9% $139.22; AVGO 8% $364.38; JPM 8% $335.35; FANG 7% $183.56; TER 6% $343.51; BAC 6% $55.09; CVX 6% $204.06; NVDA 6% $217.05; XOM 5% $161.36; AMAT 5% $450.73; SCHW 5% $98.85; KLAC 4% $172.44; COP 4% $125.58  (15 tickers: semis/semi-equipment, oil & gas, banks)
### Comments (34 total; [A]=author 诶哟哟)
1. 小红薯63697F0F: oa的模型现在都不让直接炒股了 (Oct 6 陕西)
   - [A] 为啥？接rh的mcp不能用吗
   - 小红薯63697F0F: 对的，会说它不能下单
   - [A] interesting
   - 不CODE: 我一直用cc在炒啊，最近也没发现什么异常
   - 小红薯63697F0F: 我换个新的session开始几次还可以，用一下就说它不能交易了，看了reddit好像也有很多例子，不知道怎么触发的
2. 😪: 要用routine
3. Ch: 只能用grok吗
   - [A] grok，claude，codex都能用。 只是炒股方面我更信grok一点
   - Ch: 是因为能实时接twitter的舆论数据吗
   - [A] 对。但其实也没什么依据，这玩意没法证明
4. 至尊宝: 可以出一个教程吗
   - [A] agentic account开户的时候会教你怎么连各个ai，或者直接跟agent说让他帮你连接robinhood的mcp就好啦
   - 至尊宝: 谢谢🙏，祝你发财 / [A] 一起发财
5. ovo - 冰面卡刃版 (pushback): 咋说呢，你买qqq这个月都有5%的收益，见仁见智吧
   - [A] yeah，只是个实验
   - [A] 我并不鼓励大舱位扔给AI，还是应该大盘为主，小仓位搏一搏
6. CC的灵魂炼金术: 未来ai们会不会疯狂买对自己公司好的相关股票 — [A] 非常合理
7. ABE: agent买卖是能把交税，wash sale考虑进去吗？
   - [A] 我设定30天的周期做复盘就是为了尽可能避免washsale。但是月中如果有事件驱动也会做一些小改动，没有让ai刻意避开washsale。
8. Jonathan: 你的prompt是什么 — [A] 我做了几个slash command分别抓宏观信息和个股数据，最后再汇总
9. 得意的一天: 這是亂槍打鳥嗎？ 5000 買 15隻股票 — [A] agent只负责规划比例，5000还是50000都一样啊
10. 小金毛: 哇对半导体设备这么看好，lrcx amat klac都买了 — [A] 半导体确实回调了不少。长期我个人也是看好半导体的。
11. 观山: 在有重大或突发消息时，AI的自主调仓积极吗 — [A] 一个月还看不出来
No links in comments.
### Core claims
Grok-built agent picks a 15-stock long-only portfolio (no leverage/shorts) on a $5k Robinhood Agentic account; rebalance every 30 days with optional mid-month changes; ~+11.6% in ~1 month (vs commenter noting QQQ +5%); prompt = slash commands for macro + single-stock data then synthesis; costs $30/mo Grok sub; author says experiment, not for big positions.

---------------------------------------------------------------
## POST 2 — 抢走所有人的薯条 "我开源了十三万人看过的claude自动交易流程"
- Short link: http://xhslink.com/o/AoGJMwqPNoK
- Final URL: https://www.rednote.com/discovery/item/6a75681100000000260349c1 (xiaohongshu: https://www.xiaohongshu.com/explore/6a75681100000000260349c1)
- Author: 抢走所有人的薯条 — https://www.rednote.com/user/profile/619e6e6b00000000020208bd (rednote ID 2733465990; bio: 物理PhD｜AI自动交易｜FriesTrader 开发者; 2.8K followers)
- Date: posted ~Aug 7 2026 (note-ID timestamp; first comments dated Aug 7); page shows "Edited at Sep 19". 3379 likes, 4859 saves, 162 comments. 3 slides.
### Full text
上一篇分享了我用 Claude 接入美股账户做自动交易的实验，没想到有这么多人关注
评论区大家问得最多的不是收益，而是具体是怎么实现的。所以我把一个简化后的模板整理分享了出来，希望能给想折腾AI agent的朋友一点参考。（我目前也还在探索调整策略和修改bug，会经常更新）
整个流程其实很简单：
📌 第一步：收盘后分析，不下单
每天收盘后，Claude 会收集当天真正影响股价的事件，比如财报、业绩指引、诉讼、产品发布等，而不是盯着 K 线猜涨跌。然后给每个机会写出投资逻辑、引用信息来源，并给出一个置信度。这一步只负责分析，不负责交易。
📌 第二步：第二天开盘重新验证后下单
市场一晚上可能已经发生变化，所以不会直接按照前一天的结论交易，系统会重新检查最新信息。然后再经过一系列固定的风控规则，比如单只股票仓位限制、止损规则、每日最大亏损限制、Wash Sale 检查......只有全部通过，才允许执行交易。这些规则全部都是机械执行。哪怕 Claude 再相信一只股票，也没有权限为了一个"好故事"修改止损或者加仓。
我觉得这反而是 AI 做交易最大的价值，不是它比人更会预测，而是它不会因为侥幸心理或者情绪失控去违反纪律。
除此之外，系统还会记录每一步分析、决策和执行日志。新的使用者默认必须先跑一段时间模拟交易，只有确认日志没问题以后，才可以手动打开真实的自动交易。
第一次公开这种项目，肯定还有很多问题，如果发现 bug，或者有更好的想法，也欢迎一起交流！
最后还是提醒一句：本人不是什么大佬，就是个搞物理的，不是CS也不是金融专业，这只是一个实验项目，不保证收益，也不构成任何投资建议。感恩🙏🙏
#claude #大模型 #AI工具 #开源  #AI投资  #人工智能 #独立开发者 #量化交易
### Image text (slide order approximate)
- Image A: GitHub repo page "FriesTrader" (author YizhiSong; MIT license; files: scripts/, .gitignore, LICENSE, PHASE_A_TASK.md, PHASE_B_TASK.md, README.md, risk_rules.json, trade_log_template.jsonl; README heading "FriesTrader"). (Commenter: "工具在哪里下载" → author: "Github 看图二")
- Image B: Mermaid flowchart: Robinhood MCP →(watchlist + scan / quotes / historicals)→ Phase A: Screen & Thesis →(thesis per candidate)→ pending_proposals.jsonl → Phase B: Re-verify & Risk Enforcement (also gets risk_rules.json "mechanical limits" and Robinhood MCP "fresh open price / positions") →(dry_run or gated live order)→ Robinhood MCP; every decision logged → trade_log.jsonl → plain-English recap → trade_log_recent.md.
- Image C: Cover/screenshot of earlier post: Robinhood $510.65 ▲ $10.98 (2.20%) Past week; overlay "Claude替我炒股 第1周 500刀小实验"; linked card "让Claude替我炒股第一周" (07-31, 4788 likes, 139778 views).
### Comments (162 total; [A]=author 抢走所有人的薯条)
- [A] PINNED: 第一期的完整实验记录在这里： 让Claude替我炒股第一周
- Bjergsen: 确实可行噢，用fable还挺稳的。赚多少看来关键还在于个人策略的prompts和skills怎么写，每天下午四点设一个cron节点触发分析反思这一天做的策略并自动更新skill，后面应该会越来越稳。但这几天出现skills过于冗长的问题，现在尝试自动把七天即以前的自动压缩。
  - 废墟定稿人: 可以请教一下关于策略prompts & skills有什么建议吗🙏
  - **Bjergsen: 开盘前分析或收盘总结prompts可以参考这篇推 https://x.com/tychozzz/status/2058496485969576269?s=12 个人skills我是根据个人盈亏不断修正进化就不分享了**  <-- X LINK
  - 废墟定稿人: 非常感謝！！！
- Jerry G.: 请问会自己实盘下单吗？Claude和我对话是说不会下单 没有权限…
  - Bjergsen: 会下单的，能触发。我是cli里用的claude，cron是里面自带的会话级调度器，定时会把prompts丢进来然后claude分析后去执行下单，当然前提是给权限。
- 米饼佐清酒: 赞！对于ibkr来说，目前官方不提供mcp，但拿数据的api都有，正准备做个agentic trading tool 4 ibkr (replies: 要做出来请发帖 / 会分享 / 蹲蹲 / 拉个群一起搓)
- 迟海默ò: 请问codex可以用吗 — [A] 我没用过codex呢，理论上应该是差不多的 — 迟海默ò: Codex其实会有一点麻烦 因为openai有那种policy不允许agent交易，所以得想办法绕开 — Shary🌟: 我现在正在试用codex / 换claude了; HarvWoo: 退订codex
- 我还能说什么呢: 太厉害了 请问别的券商也可以吗 — [A] 我这个工具是专门给Robinhood 写的，因为Robinhood 有官方的agentic trading 的功能 — 权星: 理论上都可以，只要券商给你配量化投资软件权限。我在国内a股也用ai进行自动化交易。(国金证券开户充十万就可以)
- prizebox: 自己写个量化又不难 以后只有韭菜和高手是自己交易 当中那批全是量化
- 达拉斯地区较为幽默的人: 我run起来了才发现，原来我们住在一个城市 — [A] 这么巧吗 … 现在确实在tx
- 破🍐在逃博士生: 可以接入富途吗 — 中专说唱尼格: 应该行 有API
- 小红薯6ADA7491: 找到了主包领英 是超牛的大佬！ — [A] 过奖了过奖了
- jeffrey (pushback): 那如果所有人都会用ai炒股都赚钱了那谁在亏钱 — [A] 不够聪明的AI亏钱; TuffyTheRat: 永远不可能所有人都会用ai炒股的…
- Jerry G.: 这个写好参数之后得电脑一直开着然后自己下单？ — [A] 如果不想一直开着电脑的话可以在Claude云端运行
- 探路er: 刚刚在别的平台看到有人推你这个了 — [A] 啊，什么平台呀 — 探路er: 马斯克的 (i.e. X) — [A] 有这种事 方便发个链接吗好好奇
- 枫叶红: 那你都买了啥？ — [A] 主页帖子有记录agent的操作
- Jason: 起步两百的订阅…每月赚到200才回本？ — [A] 起步200/year 哈
- 风起: 怎么获取呢 — [A] 直接google可以搜到
- LeiLei1028: 请问工具在哪里下载 — [A] Github 看图二
- 你工人爷爷: 我参考你的逻辑写了套给ibkr的，现在ibkr也支持claude code mcp了，截止8月7号没有读subscription和交易的权限。最大的问题是CRA（加拿大税务局），如果发现你的交易记录可疑直接判定成professional然后税率暴涨。 — [A] 交易记录可疑怎么体现呢，操作频率过高吗？ — 你工人爷爷: 报税时看税单就知道了; Vivian: 多次交易确实会引发税务报警…; 白桃喵喵酱: 如果一定要在tfsa里做…开个自顾公司; 妖精本精: 自己的investment account不是TFSA没人管的
- Hensen的AI工具箱: 收盘不下单、第二天再验证那步挺稳，我吃过隔夜反转的亏，现在也加了盘前复核。
- Nathan: 很好奇做了回测吗 — [A] 因为涉及到llm对新闻的推理，没法做回测，因为历史信息会造成llm的幻觉
- rowan🌳: 请问是ai自己选股吗？ — [A] 我写的逻辑是自己先列一个单子，然后AI再从里面挑，并且AI会另外进行一些supplementary scan 挑一些别的
- 定格AI: 是用的 robin 吗 — [A] 是的
- 阿莉克斯: 嘉信可以agentic trading 嘛 (no reply seen)
- X.: 买VOO也赚这么多啊 — [A] 上一篇做了和VOO的对比 … 不是全天运行，一天运行两个session
- Cody: 这能赚到钱我吃 — [A] 做个实验 不必较真
- 玖安: okx能接吗 — [A] 我不太懂这个呢
- CG: 为什么我的claude接了robinhood mcp之后不管如何prompt都拒绝自动下单 — [A] 如果是直接和Claude 聊天叫他下单是有可能被拒绝的
- Kira晶烊: 这不就是做量化嘛 — [A] 量化青春版
- randomName: @fnj1017 准备严肃学习并实施
### (a) x.com link (exact, from Bjergsen's comment)
https://x.com/tychozzz/status/2058496485969576269?s=12
(Page-level only; I did not open x.com. Described by commenter as a tweet with pre-market analysis / close-of-day summary prompts.)
### (b) Author profile (https://www.rednote.com/user/profile/619e6e6b00000000020208bd) — related posts seen (132-ish notes; list below is what loaded)
| Title | URL id | Date | Likes |
|---|---|---|---|
| 我开源了十三万人看过的claude自动交易流程 (pinned) | 6a75681100000000260349c1 | ~Aug 7 | 3379 |
| ⚠️ 关于冒充账号及原创内容的严正声明 (impersonation notice) | 6ad65c05000000002802091c | Oct 19 | 4 |
| Claude 替我管钱第三个月 | 6ad59210000000002702334f | Oct 19 (edited) | 474 |
| Claude 替我炒股week8｜本周摆烂跑赢大盘 | 6aacc068000000002803acd8 | Sep 18 | 754 |
| Claude 替我炒股week 7 | 6aa4bebc000000002602055f | Sep 12 (edited Sep 18) | 47 |
| 我发现还有很多人都没用对AI | 6a839164000000002c005fc7 | Aug 17 | 98 |
| Claude替我炒股week 3 | 最难的不是代码 | 6a7e936000000000320215f2 | Aug 14 (edited Sep 19) | 388 |
| 让Claude替我炒股第一周 (first-week post, linked in pinned comments; not listed/visible in profile load; 07-31, 4788 likes) | – | Jul 31 | 4788 |
URL pattern: https://www.rednote.com/explore/<id> (needs xsec_token from profile; xiaohongshu equivalent https://www.xiaohongshu.com/explore/<id>). Non-investing posts also on the profile (Philly airport, UTI, SHEIN).
Author's pinned-comment note (week8): "被平台提醒了，谨言慎行一段时间" (platform warned them).

### Related post 2.1 — Claude 替我管钱第三个月 (Oct 19, edited; 474 likes/322 saves/39 comments; 4 slides)
Text: 停更一个月后回来了，这个月大盘横盘微跌，AI 跑出了正收益，继续跑赢 QQQ 和 VOO。
金额不大，但cover掉了 Claude 的订阅费还有余，作为实验记录来说已经很满意了。AI 的表现至少证明了它没有被情绪左右。
本月策略没什么大改动，修了一些小bug，优化了买入的触发逻辑，加了一些限制条件。
具体数据可以看图～继续观察，下个月适当加仓。
⚠️ 仅为个人实验记录，不构成任何投资建议，市场有风险，投资需谨慎。
#投资需谨慎 #AI工具 #投资记录 #个人实验 #AI进化生活howto #大模型 #编程实战 #自动化
Images: (1) Robinhood "MCP" account $1,538.82 ▲$35.04 (2.33%) past month, buying power $675.14, agent Claude. (2) QQQ $707.89 ▼$7.52 (1.05%) past month. (3) VOO $699.71 ▼$0.085 (0.01%) past month. (4) flowchart: risk_rules.json →thresholds→ scripts/*.py deterministic risk math →JSON results, read verbatim→ Phase B Re-verify & Risk Enforcement ↔ Robinhood MCP (fresh open price/positions; dry_run or gated live order) ; Phase A Screen & Thesis (watchlist+scan/quotes/historicals) → pending_proposals.jsonl → Phase B; every decision logged → trade_log.jsonl → trade_log_recent.md.
Comments: 2031: 这就跟我一个月没动，也赢了大盘差不多 — [A] 可以继续观察大盘涨的时候的表现～ | 小布在东京: 它帮你管理的账户还是只是给你说买啥？ — [A] 自动交易哈 | 玥清眉: 自己炒也差不多啊 — [A] 主要是懒得自己炒才做了这个 | 左右盲: 模型费呢 — [A] Claude pro 一个月20刀 | 密西根风潇潇: 自主交易？ — [A] 是的 | 阿克拉: 沉没成本算上大亏 — [A] 只是做个实验，谈不上亏不亏的 | 点点 (AI summary reply to @): says Robinhood API, initial $1500, +$35 (+2.33%) vs QQQ -1.05%, VOO -0.01%; holdings seen LTH, STT, SDGR, GTLB, NTAP short-term swings. Pinned [A]: link to first-week post.

### Related post 2.2 — Claude 替我炒股week8｜本周摆烂跑赢大盘 (Sep 18; 754 likes/628 saves/92 comments; 4 slides)
Text: 本周收益：+1.62% 同期QQQ：-0.15% 同期VOO：-0.30%
最近说实话有点懒主要在忙学校里的事，策略也没调，也没来得及加仓（对不起！）甚至到发这篇帖子我都没有检查过一次Claude 的操作。
结果这周还好，又一次跑赢了大盘。
有时候我在想，之前的收益到底是AI的能力还是运气？如果是靠过度操作赚来的，那风险可能比我想象的大。而这一周摆烂，反而验证了一件事：不做决策，有时候或许就是最好的决策。
8周下来，Claude 的表现比我预期的要稳。但或许真正的挑战不是写代码、不是调prompt，而是忍住不干预
下周看看能不能继续保持这个摆烂的状态。
#howto投资 #我的炒股日记 #大模型 #投资需谨慎
Images: (1) Robinhood Agentic $1,360.30 ▲$21.69 (1.62%) past week, buying power $874.13, Claude connected. (2) QQQ $715.40 ▼$1.09 (0.15%) wk. (3) VOO $700.24 ▼$2.12 (0.30%) wk. (4) 4th image (flowchart, same as above; not viewed).
Comments (substantive): pinned [A] 被平台提醒了，谨言慎行一段时间 | 你的鸭鸭鸭: 博主有x吗想在那边看xhs | Jay: 用chatgpt总不给下单 — [A] 我这边是用的claude code的routine，如果直接对话让下单他是会拒绝的 | Momo (security pushback): 我是做网络安全的，这个目前暂时并不安全，我做了几次test均破了…没有access下问ChatGPT "how much do I have" 它全说了 | Jerry G.: 这周我亏了 — [A] 看来策略还需要打磨 | HarvWoo: 可以自动买卖吗 — [A] 是全自动的 | 五花马千金裘: 怎么接券商 — [A] Rh官方有agent trading 的功能 | Kg🌴: 消耗多少额度 — [A] 基本不影响日常使用 | AChi_阿驰: 怎么连接robinhood — [A] 官方接口，google搜 | 小红薯6AC7DA8D: 丢大A试试?

### Related post 2.3 — Claude 替我炒股week 7 (Sep 12, edited Sep 18; 47 likes; 6 comments; 3 slides)
Text: 这周比较忙，没什么时间看，agent 账户跟着大盘一起跌了，问题不大，调整了策略，继续加仓就完事了。主页置顶有实现方式的详细介绍。
无论盈亏每周更新，欢迎关注！
⚠️个人实验项目分享，不构成任何投资建议。
#howto投资 #我的炒股日记 #量化 #美股
Images: (1) Robinhood Agentic $1,348.67 ▼$22.18 (1.62%) past week, buying power $266.11; overlay "Claude替我炒股第7周 当前粉丝量：1500". (2) VOO $702.94 ▼$8.46 (1.19%) wk. (3) not viewed (likely QQQ).
Comments: 白胖球: 主包怎么不更新啦 (others not captured).

### Related post 2.4 — Claude替我炒股week 3 | 最难的不是代码 (Aug 14, edited Sep 19; 388 likes; 31 comments; 3 slides)
Text: 背景介绍：我拿500美元开了一个真实交易账户，交给Claude全自动操作，每周记录盈亏。
Update: 这周有过吃肉的时候，买入GitLab当天一度涨了快4%，后面大股东套利抛售，涨幅全吐回去了。最终小亏1刀 😂
这段时间最大的感受是：AI执行的层面没什么问题，真正难的是你给它的规则本身够不够好。比如什么时候该止损，是固定比例还是根据波动率动态调整，这些问题光靠写代码解决不了，得靠一次次实盘反馈来磨。
过去半个月，我基本每天晚上都会检查当天的交易和完整log，根据实际运行情况不断调整完善策略以及修bug。近期主要完善了两个方向：
【风控升级】
• 增加Wash Sale检查（感谢上期评论区指出）
• 固定7%止损 → 根据每只股票波动率动态调整
• 跟踪持仓后最高价，避免利润大幅回吐
【选股优化】
• 增加200日均线趋势过滤
• 增加市值上限过滤
• 优化诉讼风险判断
我的自动交易模板已经整理好，支持自定义参数和风控规则，目前持续更新中。
目前只有500美元、三周的样本，远远不够得出任何投资结论。我只是想看看，如果给AI一套非常明确的规则和一个真实账户，它到底能做到什么程度。
继续跑下去，赚了亏了都会更新。感恩🙏
#howto投资 #AI工具 #大模型 #投资实验 #claude #美股 #量化交易 #AI进化生活howto
Images: (1) Robinhood Agentic $511.80 ▼$1.27 (0.25%) past week, buying power $193.59, overlay "Claude替我炒股 第3周 500刀实验". (2) Order history August: GIS market buy -$60.84 (1.56643 sh @ $38.84, Aug 13); GTLB market sell +$103.95 (2.541494 @ $40.90, Aug 13); GOOGL sell +$63.08 (0.183682 @ $343.42, Aug 12); GTLB sell +$100.77 (Aug 10?); AMZN buy -$2.28 (Aug 5); KO buy -$1.24 (Aug 5); AMZN buy -$102.14 (0.356534 @ $286.48, Aug 3); AMD sell +$55.50; overlay "最近更新策略，降低了操作频率". (3) GitLab (GTLB) $40.73 ▲4.52% today, overlay "一度起飞🤣", Cortex Digests blurb.
Comments: only skimmed (31); first is [A] series-post pointer.

### (Related but tangential) 我发现还有很多人都没用对AI (Aug 17; 98 likes; 4 slides)  id 6a839164000000002c005fc7 — general essay urging people to try paid AI agents (Claude Pro); mentions building an auto-trading side project. Images not transcribed.

### Core claims (post 2)
Open-sourced FriesTrader template: Phase A after close (Claude gathers real catalysts—earnings, guidance, lawsuits, product launches—writes thesis w/ sources + confidence, no orders); Phase B next open re-verifies fresh info then mechanical risk rules (position size cap, stop-loss, daily max loss, wash-sale check) gate execution; Claude can't override stops/add on "good stories"; full logs; new users must paper-trade (dry_run) before enabling live. Robinhood agentic account + MCP specific; runs via Claude Code routine/cron (two sessions/day), can run in Claude cloud. Can't backtest (LLM hindsight hallucination). Watchlist is author-made; AI picks + supplementary scans. Later refinements: volatility-adjusted stops (was fixed 7%), trailing-high tracking, 200-DMA trend filter, market-cap cap, litigation-risk logic, lower trade frequency. Results: wk1 $500 acct +2.2%; month-3 acct ~$1,539 (+2.33%/mo) beating QQQ/VOO; small sample, "experiment, not advice."

---------------------------------------------------------------
## POST 3 — 存1500w🔪退休 "muse今天的操作还是可圈可点"
- Short link: http://xhslink.com/o/1MPvf3TRBlI
- Final URL: https://www.rednote.com/discovery/item/6ac919710000000019038400 (xiaohongshu: https://www.xiaohongshu.com/explore/6ac919710000000019038400)
- Author: 存1500w🔪退休 — https://www.rednote.com/user/profile/652b6abf000000002b0011d2
- Date: Oct 9 (shown as "Edited at Oct 9 美国"; note-ID date Oct 9 2026). 260 likes, 242 saves, 67 comments. 2 slides. No separate title (first line is the title/body).
### Full text
muse今天的操作还是可圈可点
给他的策略是抓趋势做末日期权，单笔不超过100，每天最多开两仓
最近加入了macd止盈，这周效果相当不错。
更新一下：目前muse的策略是确认趋势以后右侧交易小额末日期权，codex的策略是收盘买入超跌股票，开盘卖出
### Image text
- Slide 1: Robinhood Agentic (dark) $375.46 ▲ $107.97 (40.36%) Past week; buying power $340.13; "2 connected agents"; Activity: Sell ASTS $48 Put 10/9 +$63.00 (Oct 9, 2026).
- Slide 2: History (Agentic/Orders), Past 30 Days: Sell ASTS $48 Put 10/9 +$63.00 (Oct 9); Buy ASTS $48 Put 10/9 -$36.00; Sell ASTS $51 Put 10/9 +$75.00; Buy ASTS $51 Put 10/9 -$38.00; AVGO market buy -$35.00 (0.097439 sh @ $359.20, Oct 8); Sell ASTS $57 Put 10/9 +$107.00 (Oct 8); Buy ASTS $57 Put 10/9 -$66.00 (Oct 8); more partly hidden.
### Comments (67 total; [A]=author)
- 小灰小灰: 为什么我的muse不允许这么操作呢 — [A] ib应该是可以的。我连了ib的账户看行情 / 我的ib是只读的，没试过下单 — 小灰小灰: 能读也不错啊，我现在还是截屏发给他呢
- 森: 我这还有28个，欢迎自取… 邀请码：LB6HZ9 (invite-code spam) — [A] 你们那么缺token吗？我都用不完
- 慢吞吞搞钱: agent自己操作的吗 — [A] 是，但是还是我喂的策略 — Lily在美国: 去哪里找策略喂 — [A] 你可以让他自己上网找，然后自己再慢慢调 — 小红薯650E3079 (joke): 策略调通了就可以去银行贷个200万 — [A] 不用去银行，200万我自己就有
- momo_xhs: muse也可以接入啦 — [A] 我同时接了muse和codex。 — momo_xhs: 怎么接 agentic account? … 对哦，你这个view是agentic
- 猪哥好坏: 为啥我codex老拒绝给我自动操作rh — [A] 跟他说preapproval
- Lemonmomo: 这是哪家平台啊？ — [A] robinhood啊 (怡之: robinhood最好用)
- momo: Muse 你走token的吗？他们家没有订阅的哇 — [A] 有啊，有订阅啊
- 鲁皮（装修中）: muse咋接啊 mcp里没有啊 — 薛几几: 同问
- 邓勋林: 厉害！可以加大剂量了！ — [A] 再跑两周
- Heath man: 自动交易？
No links in comments (only an invite code).
### Core claims
Two agents on one Robinhood Agentic account: "muse" trades 0DTE (末日) options — confirm trend then right-side entries, each trade ≤$100, max 2 new positions/day, MACD take-profit added; "codex" buys oversold stocks at close and sells at open. Account ~$375 after +40% in one week (small base; sells/buys of ASTS puts). Connect via Robinhood MCP; tell codex "preapproval" to avoid refusals; IB read-only only.
