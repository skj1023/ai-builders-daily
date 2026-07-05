#!/usr/bin/env python3
"""Curate the 2026-07-06 raw feed into a high-signal digest."""

import json
from datetime import date

ARCHIVE = r"C:\Users\PC\Documents\ai-builders-daily\data\archive\2026-07-06.json"
LATEST = r"C:\Users\PC\Documents\ai-builders-daily\data\latest.json"
DIGESTS = r"C:\Users\PC\Documents\ai-builders-daily\data\digests.json"

with open(ARCHIVE, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---- dailyInsight ----
data["dailyInsight"] = {
    "paragraphs": [
        "今天最值得关注的信号来自产品层面的自省。Thibault Sottiaux（Codex @ OpenAI）公开提问「Codex 仍然做不好什么我们早就该做好的事？」——这不是一个开发者抱怨，而是产品团队主动暴露盲区、收集反馈。对于所有在做 coding agent 的 AI Builders 来说，这个方向性问题本身就是信号：OpenAI 意识到 Codex 有系统性短板，并且正在有意识地搜集差距清单。谁先发现这些 gap 并填补，就有机会在 agent 编程战场里卡位。",
        "Claude Fable 5 正在用真实用户案例证明其判断力的提升。Cat Wu（Anthropic）提到，在她做留存分析时，Fable 5 主动使用了倾向得分匹配（propensity score matching）来对比相似用户群——而她没有要求这样做。这意味着 Fable 5 在数据分析场景下拥有了超越指令的统计直觉。对于将 agent 用在内部分析、报告和运营决策的团队，这直接降低了 prompt 精度的门槛：模型不再只是执行者，而是能主动建议更合理的分析方法。",
        "Vercel CEO Guillermo Rauch 公布的 token 消耗可视化揭示了另一个宏观趋势：从 Vercel AI Gateway 聚合的千万级开发者月 token 消耗来看，Anthropic 占据绝对优势，同时 open-weight 模型正在上升。这组实时数据比任何基准测试都更直接地反映了开发者实际选择。结合同日 Claude Blog 发布的 Apple Foundation Models 框架支持，Claude 正在从模型 API 扩展到原生 Apple 平台开发者生态——这是基础设施层面的一次平台化跃进。",
        "The MAD Podcast 中 Cloudflare CEO 的论断「互联网的商业模式已死」看似宏观，实则与 AI Builders 每日面对的现实直接相关：2026 年上半年，机器人流量首次超过人类流量。这意味着：web 作为 training data 和 agent 交互界面的质量在下降，防爬与开放之间的矛盾会加剧，而依赖于互联网内容生态的 AI 产品需要重新审视自己的数据采集、反爬策略和用户真实性判断。这不是远期的哲学问题，而是当下产品架构就需要回应的变化。"
    ],
    "filteredNote": "过滤掉了 Sam Altman、Amanda Askell、Nikunj Kothari 的美国独立日感慨，Peter Yang 和 Matt Turck 的足球内容，Swyx 的个人生活动态，Guillermo Rauch 的国旗 emoji 艺术，Thibault Sottiaux 的无上下文 lul 与 meme，Peter Steinberger 的 tokenmaxxing 玩梗与单句感慨，Dan Shipper 的低上下文戏谑、Garry Tan 的 SF 住房政治讨论，以及所有非 AI 相关的日常、体育、节日感慨、meme 和无上下文单句。"
}

# ---- highSignalItems ----
data["highSignalItems"] = [
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月4日 · 周六",
        "actor": "Thibault Sottiaux",
        "meta": "Codex @ OpenAI · X 动态",
        "title": "Codex 产品团队公开征集未被解决的能力差距",
        "summary": "Thibault Sottiaux（Codex PM）在 X 上公开提问：有哪些事你们觉得 Codex 早该做好但至今做不好？这不是用户抱怨，而是产品团队主动暴露未知短板、收集外部信号。问题本身就值得关注——它意味着 OpenAI 内部承认 Codex 存在系统性 gap，并且正在有意识地图谱化这些差距。",
        "keyPoints": [
            "Codex 产品团队正在主动寻找自身盲区，说明他们对现状不满足。",
            "收集到的 gap 清单可能成为下一阶段 Codex 能力改进的优先方向。",
            "对于 coding agent 赛道的竞争者，这些 gap 就是产品定位的切入点。"
        ],
        "whyItMatters": "这给 AI Builders 一个直接信号：Codex 的方向可能正在调整，而调整的依据来自用户反馈——你的体验问题可能正在影响产品路线图。",
        "tags": ["Codex", "产品", "能力差距"],
        "qualityScore": 85,
        "url": "https://x.com/thsottiaux/status/2073551549494596079"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月4日 · 周六",
        "actor": "Cat Wu",
        "meta": "Claude Fable / Cowork · Anthropic · X 动态",
        "title": "Fable 5 能在数据分析中主动使用统计方法提升分析质量",
        "summary": "Cat Wu（Anthropic）发现 Claude Fable 5 在做留存分析时，主动使用了倾向得分匹配（propensity score matching）来对齐用户活动水平后再做对比——她没有要求这样做。这直观展示了 Fable 5 判断能力的进步：模型不再只执行指令，而是在统计方法论层面提供了超出预期的分析质量。",
        "keyPoints": [
            "Fable 5 能自主选择更适合的统计方法，不依赖用户明确要求。",
            "倾向得分匹配是非常具体且高阶的分析策略，非偶然行为。",
            "这说明 Agent 的 judgment 正在从「执行」进化到「建议更好的方法」。"
        ],
        "whyItMatters": "它提供了一个可观测的指标：当 Agent 能主动改进分析路径时，产品设计和 Prompt 工程的门槛都会降低——更多用户可以直接使用 AI 完成高质量分析。",
        "tags": ["Claude Fable", "Agent", "数据分析", "判断力"],
        "qualityScore": 88,
        "url": "https://x.com/_catwu/status/2073439890482794966"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月5日 · 周日",
        "actor": "Guillermo Rauch",
        "meta": "Vercel / AI Gateway · X 动态",
        "title": "Vercel 聚合数据显示 Anthropic 占 Token 消耗主导地位",
        "summary": "Guillermo Rauch（Vercel CEO）用动画展示了 Vercel AI Gateway 自上线以来的 token 金额消耗排名，数据汇聚来自数百万开发者的每月数万亿 token。结果清晰显示 Anthropic 持续领先，同时 open-weight 模型正在追赶。这是来自基础设施层的真实开发者采用数据，比任何 benchmark 都更能反映市场的实际选择。",
        "keyPoints": [
            "Anthropic 在开发者 token 消费中占据明显的领先份额。",
            "Open-weight 模型的 token 消耗正在上升，说明开发者对开源方案的偏好增强。",
            "各模型厂商的消长波动反映了定价、能力与开发者体验的综合竞争。"
        ],
        "whyItMatters": "它用真实的使用量数据回答了「哪个模型开发者用得最多」，而不是「哪个模型跑分最高」——这对 AI Builders 的模型选型和平台策略有直接参考价值。",
        "tags": ["Token Economy", "Vercel", "Anthropic", "开源模型"],
        "qualityScore": 90,
        "url": "https://x.com/rauchg/status/2073563586270781674"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月4日 · 周六",
        "actor": "Nan Yu",
        "meta": "Linear / AI Accountability · X 动态",
        "title": "AI Agent 造成生产事故时，谁该负责？",
        "summary": "Nan Yu（Linear 产品负责人）用一个假设性问题点出了 AI 工程中的 accountability 盲区：如果一个 agent 执行了「删所有生产表」的操作，是该解雇模型，还是解雇批准它执行的人？问题简短，但直指关键——随着 Agent 越来越自主，责任归属将成为团队安全管理绕不开的议题。",
        "keyPoints": [
            "Agent 的自主执行权越高，事故归属越模糊。",
            "当前多数团队缺乏明确的 Agent 操作问责机制。",
            "这不仅仅是安全话题，也是产品设计和权限管理的问题。"
        ],
        "whyItMatters": "它点出了一个每个引入 AI agent 的团队终将面对的问题：自主性的报酬越高，问责的代价也越高——提前建立责任框架比事后追责重要得多。",
        "tags": ["Agent", "工程", "安全", "问责"],
        "qualityScore": 78,
        "url": "https://x.com/thenanyu/status/2073410944969932877"
    },
    {
        "type": "blog",
        "typeLabel": "深度文章",
        "date": "6月8日 · 周一",
        "actor": "Claude Blog / Anthropic",
        "meta": "Apple Foundation Models · 官方博文",
        "title": "Claude 正式进入 Apple Foundation Models 框架，面向 Apple 开发者",
        "summary": "Anthropic 发布了新的 Swift 包，让 Apple 开发者可以通过 Apple 的 Foundation Models 框架直接调用 Claude，构建更复杂的工作流。这意味着 Claude 不再只是一个 API 或聊天产品，而是正式成为 Apple 原生生态中的 AI 基础设施组件——从 visionOS 到 iOS 的 Apple 全平台开发者都可以像使用系统框架一样使用 Claude。",
        "keyPoints": [
            "Claude 可通过 Foundation Models 框架在 Apple 全平台原生使用。",
            "Swift 包支持复杂工作流，不只是简单的 API 调用。",
            "这是 AI 模型进入移动端原生开发栈的重要一步。"
        ],
        "whyItMatters": "对于在 Apple 生态构建 AI 产品的开发者，这大幅降低了集成成本——不再需要维护桥接层，可以直接用 Apple 的标准开发范式调用 Claude。",
        "tags": ["Claude", "Apple", "Swift", "移动端"],
        "qualityScore": 82,
        "url": "https://claude.com/blog/claude-for-foundation-models"
    },
    {
        "type": "podcast",
        "typeLabel": "播客摘录",
        "date": "6月25日 · 周四",
        "actor": "The MAD Podcast with Matt Turck",
        "meta": "Cloudflare CEO · YouTube",
        "title": "Cloudflare CEO：互联网的商业模式已因 Bot 流量而失效",
        "summary": "Cloudflare CEO Matthew Prince 在 MAD Podcast 中指出，2026 年上半年，机器人流量首次超过人类流量。这个里程碑意味着依赖广告和用户真实互动的互联网商业模式正在瓦解。对于 AI Builders 来说，这意味着：你的 agent 访问的 web 页面质量在下降、反爬成本在上升、用户真实性判断变得更加困难。这不是未来问题，而是现在就需要在产品架构中回应的变化。",
        "keyPoints": [
            "Bot 流量正式超过人类流量，互联网的信号/噪声比进一步恶化。",
            "依赖网页内容作为 AI training data 或 agent context 的质量会下降。",
            "AI 产品需要更强的反爬、用户验证和数据质量保障策略。"
        ],
        "whyItMatters": "它让 AI Builders 意识到：互联网本身的基础数据质量正在被 AI 流量改变——如果你的产品依赖网页内容或面向网页的 agent 交互，现在就需重新评估数据策略。",
        "tags": ["Cloudflare", "Bot", "互联网", "数据质量"],
        "qualityScore": 85,
        "url": "https://www.youtube.com/watch?v=UN47z_opfmo"
    }
]

# ---- Write ----
with open(ARCHIVE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open(LATEST, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Update digests.json
with open(DIGESTS, "r", encoding="utf-8") as f:
    digests = json.load(f)

# Find if today already exists
today = "2026-07-06"
replaced = False
for i, entry in enumerate(digests):
    if entry.get("date") == today:
        digests[i] = data
        replaced = True
        break

if not replaced:
    digests.insert(0, data)

with open(DIGESTS, "w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print(f"✅ Curated digest for {today}")
print(f"   Items: {len(data['highSignalItems'])}")
print(f"   Filtered from {len([b for b in data['builders']])} builders / {data['stats']['tweets']} tweets + {data['stats']['blogs']} blogs + {data['stats']['podcasts']} podcasts")
