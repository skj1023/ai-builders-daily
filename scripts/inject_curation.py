#!/usr/bin/env python
"""Inject curated dailyInsight + highSignalItems into 2026-07-02 archive JSON."""
import json
from pathlib import Path

import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = Path(base) / "data" / "archive" / "2026-07-02.json"
data = json.loads(path.read_text("utf-8"))

dailyInsight = {
    "paragraphs": [
        "今日最重磅的消息是 Anthropic 正式发布了 Claude Sonnet 5。官方称其在推理、工具使用、编码和知识工作方面相比 Sonnet 4.6 有实质性提升，性能接近 Opus 4.8 但价格更低。早期合作方（如 Box）反馈 Sonnet 5 能完成此前 Sonnet 系列无法收尾的复杂任务、会自动检查自身输出，且 Agent 能力在真实企业场景中表现突出。已作为 Free/Pro 的默认模型上线，并推出到 8 月底的优惠定价。",
        "与此同时，OpenAI 的 Fable（推测为 GPT-5.6）的发布-安全审查-回撤-回归事件成为社区另一焦点。Peter Yang、Dan Shipper、Nikunj Kothari 等多位 Builder 在深夜表达期待，Aaron Levie 则给出了冷静的判断：Fable 的遭遇为未来 Frontier Model 发布开创了一个先例——具备显著编码和网络能力的新模型，将面临更严格的安全评估流程。这很可能成为后续模型（包括 GPT-5.6 和未来更新）的常态化流程。",
        "工程侧有三条值得关注的信号。Guillermo Rauch 发布了 Vercel Services，允许在单个 Vercel 项目中同时部署 Python 后端、ExpressJS 服务器和 React SPA，统一本地开发、部署回滚和可观测性——这延续了 Vercel 将前后端边界模糊化的战略。Amjad Masad 分享了 Etched（针对 LLM 推理从零设计的芯片），指出 AI 昂贵的核心原因之一是大多数工作负载跑在预 LLM 时代的通用硬件上。Thariq 则澄清了 Claude Code 更新后的分类器机制：少量常规编码任务会被标记并回退到 Opus，团队正在持续降低误报。",
        "组织方法论层面，Madhu Guru（前 Google Gemini/Veo PM）指出传统 PM 转型 AI-native 时最大的障碍是缺乏「魔法思维」——十年框架化、敏捷化和指标导向的培养让 PM 习惯于约束优先的渐进式思考。Aaron Levie 则用 Box 和 Ramp 的数据给出了一个反直觉结论：AI 采用率越高的公司，人员规模增长越快。58% 的受访中大型企业预计 AI 会带来人员增加而非减少。",
        "最后，Aditya Agarwal（Dropbox 前 CTO）的一句观察值得反复品：驱动美国创新的主力模型，竟是中国的开源模型。这一格局在过去一年加速形成，对 AI Builders 的模型选择、成本结构和供应链思考都有深远影响。"
    ],
    "filteredNote": "过滤掉了 Swyx（AIEWF 会议动态）、Peter Yang（Fable 兴奋）、Dan Shipper（同上）、Matt Turck（非 AI 内容）、Zara Zhang（无实质 AI 内容）、Garry Tan（非 AI 内容）等低信号 / 日常内容。共保留 10 条高信号条目。"
}

highSignalItems = [
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Claude / Anthropic",
        "meta": "Anthropic · X 动态",
        "title": "Claude Sonnet 5 发布：性能逼近 Opus 4.8，价格更低",
        "summary": "Anthropic 正式发布 Sonnet 5，在推理、工具使用、编码和知识工作方面全面超越 Sonnet 4.6，接近 Opus 4.8 水平。早期合作方（含 Box）报告它能完成此前版本无法收尾的复杂任务，且会自动检查输出质量。已作为 Free/Pro 默认模型上线，提供到 8 月底的优惠定价。",
        "keyPoints": [
            "性能接近 Opus 4.8，但定价更低",
            "Agent 场景下能独立完成复杂多步任务",
            "已作为 Free/Pro 默认模型，Max/Team/Enterprise 也可使用",
            "Box 的企业 Agent 评测中在能源、金融等领域超越 Sonnet 4.6"
        ],
        "whyItMatters": "Sonnet 系列首次在实用性上逼近 Opus 级别，且定价更低，将显著影响 AI Builders 的产品选型和成本结构。",
        "tags": ["产品", "Agent", "工程"],
        "qualityScore": 92,
        "url": "https://x.com/claudeai/status/2072017452335087996"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Aaron Levie",
        "meta": "Box CEO · X 动态",
        "title": "AI 采用越多，公司招人越多：反直觉的数据信号",
        "summary": "Aaron Levie 引用 Ramp 的数据和 Box 对 1600+ 中大型企业的调研指出：AI 采用率越高的公司，人员规模增长反而越快。58% 受访企业预计 AI 将带来人员增加而非减少。这一发现与「AI 消灭工作」的主流叙事直接矛盾。",
        "keyPoints": [
            "Ramp 发现高 AI 采用率公司的人员增长更高",
            "Box 调研 1600+ 中大型企业，58% 预期 AI 增加人员",
            "AI 更多是扩展能力而非替代岗位"
        ],
        "whyItMatters": "为 AI Builders 提供了面向企业客户时的核心叙事依据——AI 的价值主张不应建立在「省人」上。",
        "tags": ["组织", "市场", "产品"],
        "qualityScore": 85,
        "url": "https://x.com/levie/status/2071992799109824562"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Aaron Levie",
        "meta": "Box CEO · X 动态",
        "title": "Fable 事件为前沿模型安全评估开创先例",
        "summary": "Levie 认为 Fable（疑似 GPT-5.6）的发布-回撤-回归过程已为未来所有具备显著编码和网络能力的 Frontier Model 设立了安全审查先例。后续的生物安全等领域可能也会面临类似流程。",
        "keyPoints": [
            "Fable 安全评估流程可能成为行业标准",
            "类似审查未来可能扩展到生物等敏感领域",
            "模型发布节奏将受安全审查周期影响"
        ],
        "whyItMatters": "AI Builders 需要理解：前沿模型的发布将不再是简单的「发版」，而是一个包含安全审查、回撤和分阶段放开的复杂流程。",
        "tags": ["产品", "工程", "研究"],
        "qualityScore": 80,
        "url": "https://x.com/levie/status/2072172275017879829"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Guillermo Rauch",
        "meta": "Vercel CEO · X 动态",
        "title": "Vercel Services：一个项目里同时跑 Python 后端 + Express 服务器 + React SPA",
        "summary": "Rauch 发布 Vercel Services，允许在单个 Vercel 项目中协同部署多种运行时（Python API、ExpressJS、React SPA），统一本地开发（`vc dev`）、一键部署回滚、集中可观测性和内部网络。",
        "keyPoints": [
            "支持多运行时（Python、Node.js、React）同项目部署",
            "统一本地开发和部署回滚体验",
            "内部网络免去公网通信开销",
            "进一步模糊前后端工程边界"
        ],
        "whyItMatters": "对于使用 Vercel 的 AI Builders 团队，这大幅降低了全栈 AI 应用（Python 推理层 + Node 中间层 + React 前端）的部署复杂度。",
        "tags": ["工程", "产品", "组织"],
        "qualityScore": 82,
        "url": "https://x.com/rauchg/status/2071966055308607765"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Madhu Guru",
        "meta": "前 Google Gemini/Veo PM · X 动态",
        "title": "传统 PM 转型 AI-native 的最大障碍：缺乏魔法思维",
        "summary": "Madhu Guru 指出十年框架化、敏捷化和指标导向的训练，让传统 PM 习惯约束优先的渐进式思考。他曾在团队中使用「假设你拥有一百年后的技术」的方法来对抗这种思维定式。",
        "keyPoints": [
            "框架和经验在 AI 时代可能成为认知枷锁",
            "「魔法思维」是 AI-native PM 的核心能力",
            "从约束优先转向可能性优先的思考方式"
        ],
        "whyItMatters": "对正在组建 AI 团队的 Builders 来说，团队成员的思维模式可能比技术能力更关键——传统 PM 需要主动「反驯化」。",
        "tags": ["组织", "产品"],
        "qualityScore": 78,
        "url": "https://x.com/realmadhuguru/status/2071970221477470694"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Amjad Masad",
        "meta": "Replit CEO · X 动态",
        "title": "AI 昂贵是因为硬件是预 LLM 时代的通用设计",
        "summary": "Masad 指出当前 AI 推理成本高企的根本原因之一是大多数工作负载跑在预 LLM 时代的通用硬件上。Etched 是第一个从零设计、针对现代推理任务的系统。",
        "keyPoints": [
            "通用硬件（GPU）并非为 LLM 推理优化",
            "专用芯片（如 Etched）有潜力大幅降低推理成本",
            "硬件-软件协同设计是 AI 规模化的关键路径"
        ],
        "whyItMatters": "推理成本仍然是 AI 产品规模化的最大瓶颈之一。专用硬件的发展会直接影响 Builders 的产品经济模型。",
        "tags": ["工程", "产品"],
        "qualityScore": 80,
        "url": "https://x.com/amasad/status/2071992110132117740"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Thariq",
        "meta": "Claude Code @ Anthropic · X 动态",
        "title": "Claude Code 更新分类器机制：少量常规编码会被标记并回退到 Opus",
        "summary": "Thariq 澄清了 Claude Code 更新后的分类器工作方式：一小部分常规编码和调试任务会被标记并回退到 Opus 处理。团队正在持续优化分类器，更好地区分真实滥用和合法请求，降低误报率。",
        "keyPoints": [
            "分类器会标记少量常规编码任务并回退到 Opus",
            "团队在持续降低误报率",
            "这是安全与用户体验之间的经典权衡"
        ],
        "whyItMatters": "Claude Code 的安全分类器机制反映了 AI 编程工具在产品化过程中面临的核心矛盾——安全防护 vs 开发效率。",
        "tags": ["工程", "产品"],
        "qualityScore": 76,
        "url": "https://x.com/trq212/status/2072185565076988326"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Peter Steinberger",
        "meta": "独立开发者 · X 动态",
        "title": "Price per token ≠ Cost per task：模型选型的关键思维转变",
        "summary": "Steinberger 指出 AI Builder 社区过度关注 token 单价，而真正重要的是完成一个任务的「总成本」。这涉及到模型选型、循环次数、错误重试率等多个维度。",
        "keyPoints": [
            "低 token 单价可能因高重试率导致总成本更高",
            "更强的模型即使单价更高，任务总成本可能更低",
            "工程团队应建立「任务级」成本监控而非 token 级"
        ],
        "whyItMatters": "在模型选择日趋多样化的当下，以「任务完成成本」而非「token 单价」做决策，能帮助 AI Builders 做出更理性的架构选择。",
        "tags": ["工程", "产品"],
        "qualityScore": 75,
        "url": "https://x.com/steipete/status/2072144627474579925"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Aditya Agarwal",
        "meta": "South Park Commons GP · X 动态",
        "title": "推动美国创新的主力模型，来自中国的开源社区",
        "summary": "Dropbox 前 CTO Aditya Agarwal 指出一个反常但已成现实的现象：驱动美国科技创新的基础模型，正在变成中国的开源模型。这一趋势在过去一年快速加速。",
        "keyPoints": [
            "中国开源模型（如 DeepSeek、Qwen）在美国创新生态中占据核心位置",
            "开源模型 vs 闭源模型的竞争格局正在重塑",
            "对模型供应链和地缘风险的长期影响"
        ],
        "whyItMatters": "AI Builders 在做模型选型和基础设施决策时，需要把开源模型的全球供应链格局纳入长期考量。",
        "tags": ["研究", "市场", "组织"],
        "qualityScore": 78,
        "url": "https://x.com/adityaag/status/2071983952894837062"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Boris Cherny",
        "meta": "Claude Code @ Anthropic · X 动态",
        "title": "Claude Desktop 正式支持 Linux",
        "summary": "Boris Cherny 宣布 Claude Desktop 推出 Linux 版本，提供下载链接。此前 Linux 用户仅能通过 API 或浏览器使用 Claude。",
        "keyPoints": [
            "Claude Desktop 现支持 Linux 原生桌面环境",
            "社区长期呼吁的功能终于落地",
            "对 Linux 为主的 AI 工程团队意义重大"
        ],
        "whyItMatters": "Linux 在 AI 工程社区中的普及率极高，原生桌面客户端的缺失一直是 Claude 用户的最大痛点之一。这一补全将直接影响开发者采用决策。",
        "tags": ["产品", "工程"],
        "qualityScore": 74,
        "url": "https://x.com/bcherny/status/2072000214634742243"
    }
]

# Sort highSignalItems by qualityScore descending
highSignalItems.sort(key=lambda x: x["qualityScore"], reverse=True)

data["dailyInsight"] = dailyInsight
data["highSignalItems"] = highSignalItems

path.write_text(json.dumps(data, ensure_ascii=False, indent=2), "utf-8")

# Also update latest.json
latest_path = Path(base) / "data" / "latest.json"
latest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), "utf-8")

# And digests.json - find and update the matching entry
digests_path = Path(base) / "data" / "digests.json"
digests = json.loads(digests_path.read_text("utf-8"))
if isinstance(digests, list):
    for i, d in enumerate(digests):
        if d.get("date") == "2026-07-02":
            digests[i] = data
            break
    else:
        digests.insert(0, data)
    digests.sort(key=lambda d: d.get("date", ""), reverse=True)
    digests = digests[:60]
    digests_path.write_text(json.dumps(digests, ensure_ascii=False, indent=2), "utf-8")

print("Done. dailyInsight + highSignalItems injected into archive, latest, digests.")
print(f"Items: {len(highSignalItems)}")
