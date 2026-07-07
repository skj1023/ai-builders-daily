"""Build curated digest for 2026-07-08"""
import json, os

data_dir = os.path.join(os.path.expanduser("~"), "Documents", "ai-builders-daily", "data")

# Read current archive
with open(os.path.join(data_dir, "archive", "2026-07-08.json"), "r", encoding="utf-8") as f:
    raw = json.load(f)

# Build curated structure
curated = {
    "date": "2026-07-08",
    "displayDate": "7月8日 · 周三",
    "generatedAt": raw["generatedAt"],
    "source": "follow-builders public central feed",
    "sourceRepo": "https://github.com/zarazhangrui/follow-builders",
    "stats": raw["stats"],
    "dailyInsight": {
        "paragraphs": [
            "Claude Code 的起源故事成为今日最高信号话题。Boris Cherny 首次公开讲述了它如何从 Anthropic 安全研究中孵化而来。这不仅是产品发布的历史回顾，更揭示了一个重要模式：前沿实验室的安全基础设施可以被产品化，转化成开发者工具。Vercel 的 Rauch 同步讨论了一个更根本的评价标准——「AI 编程到底有没有让软件整体变好？」他把测试权交还给用户，认为最终指标是产品和体验质量的提升。",
            "Agent 自我进化的闭环正在成为行业共识。Replit 的 Amjad Masad 明确宣布「agent is self-improving」，他们关闭了反馈循环，让 Agent 自身的改进融入产品迭代。同时 Replit 上的一家房地产公司用自建 CRM 替代 Salesforce 省下了 10 万美元——这是低代码 + Agent 的真实商业案例，印证了 AI 降低企业软件替代门槛的趋势。",
            "在 Agent 评估基础设施方面，Rauch 宣布 Vercel 的 eve 框架内置了 eval 系统（eve eval），核心观点是「Web 框架让测试变成了生态选择，但对 Agent 来说 eval 是必需品」。这与 Swyx 分析的 Anthropic J-space 论文形成呼应——模型能够检测推理中的干预，实际上是一种内置的 eval 能力。AI 的「自我认知」和「自我评估」正在从元研究走向工程实践。",
            "Aaron Levie 提出了一个简洁的框架：前沿模型将始终占据解决新用例和复杂编排的角色，而开源/应用层则负责已验证用例的规模化落地。这个分层观点帮助 Builder 们思考自己的定位——是做探索边界的「大 swing」，还是在已证实的路径上打磨执行。与此同时，Peter Yang 在 Fable 5 离开订阅前整理了一份实用案例集，展示了当前最强模型在实际工作流中的正确打开方式。",
            "Zara Zhang 补充了一个信号：AI Engineer、Cursor Compile 和 Figma Config 三场大会的演讲录像已经全部上线，想在 AI 领域升级的 Builder 可以直接刷完。这三场会议集中了过去一年最前沿的实践分享。"
        ],
        "filteredNote": "过滤掉了 Thibault Sottiaux（无内容高互动推）、Garry Tan（非 AI 政治话题）、Thariq/Cat Wu（单行转发无分析）、Peter Yang（日常/情绪推）、Peter Steinberger/Dan Shipper（简短无增量内容）等低信号内容。"
    },
    "highSignalItems": [
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月7日 · 周二",
            "actor": "Swyx",
            "meta": "Builder · X 动态",
            "title": "Anthropic 实现推理中的「脑外科手术」干预",
            "summary": "Swyx 指出 Anthropic J-space 论文的核心有两部分：Anthropic 证明了对模型推理过程进行「脑外科手术式」干预（中途改变推理主题）是可行的；更关键的是，模型能够检测出自己被做了什么干预——这接近于 eval 自我认知的能力。控制超越了相关性。",
            "keyPoints": [
                "Anthropic 实现了对推理过程的有向干预，可以中途改变推理主题",
                "模型能感知到干预操作——与 eval awareness 是近亲",
                "控制(causal)超越了相关(correlation)，这是可解释性的重大进展"
            ],
            "whyItMatters": "如果模型能感知并报告推理中的外部干预，这意味着更透明的 AI 系统成为可能，也是 Agent 自我评估的底层能力。",
            "tags": ["研究", "可解释性", "安全"],
            "qualityScore": 90,
            "url": "https://x.com/swyx/status/2074344727202463832"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月6日 · 周一",
            "actor": "Boris Cherny",
            "meta": "Claude Code @ Anthropic · X 动态",
            "title": "Claude Code 从安全研究到开发者工具的进化之路",
            "summary": "Anthropic 的 Boris Cherny 首次公开讲述了 Claude Code 的完整起源——从 Anthropic 安全研究项目孵化，到最终成为面向开发者的产品。他强调「我们只完成了 1%」，暗示 Claude Code 还有巨大的进化空间。",
            "keyPoints": [
                "Claude Code 起源于 Anthropic 内部的安全研究方向",
                "这是团队首次公开讲述产品从研究到落地的完整故事",
                "「只完成了 1%」——还有大量能力尚未释放"
            ],
            "whyItMatters": "安全研究能力被产品化为开发者工具，这是前沿实验室从纯研究向平台化转型的标志性案例。",
            "tags": ["产品", "工程", "Anthropic"],
            "qualityScore": 88,
            "url": "https://x.com/bcherny/status/2074247226038063316"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月6日 · 周一",
            "actor": "Peter Yang",
            "meta": "Practical AI · X 动态",
            "title": "Fable 5 离开订阅前值得尝试的 5 个用例",
            "summary": "Peter Yang 在 Fable 5（最强 Claude 模型）即将离开订阅服务前，整理了 5 个值得一试的使用场景并附带了可直接复制的提示词。涵盖了发现高价值任务、深度分析、代码审查等方向。",
            "keyPoints": [
                "5 个经过验证的高价值使用场景",
                "附带可直接复制粘贴的提示词",
                "展示了最强模型在实际工作流中的正确用法"
            ],
            "whyItMatters": "模型能力的上限和实际使用方式直接相关，这些案例为 Builder 们提供了当前模型能力的实操参考。",
            "tags": ["产品", "Agent", "提示词工程"],
            "qualityScore": 82,
            "url": "https://x.com/petergyang/status/2074206798631071796"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月6日 · 周一",
            "actor": "Amjad Masad",
            "meta": "CEO @ Replit · X 动态",
            "title": "Replit 上的 CRM 替代 Salesforce，省下 10 万美元",
            "summary": "一家亚特兰大房地产公司用 Replit 自建的 CRM 系统替换了 Salesforce，省下了 10 万美元。这是低代码平台 + AI Agent 直接冲击传统 SaaS 的鲜活案例。",
            "keyPoints": [
                "真实商业场景中用 Replit 自建 CRM 替代 Salesforce",
                "节省成本 10 万美元",
                "AI 大幅降低了企业软件替代的工程门槛"
            ],
            "whyItMatters": "AI Builder 平台正在催生新一代的「内部工具革命」——许多 SaaS 产品可能被低成本的自建替代方案挑战。",
            "tags": ["市场", "产品", "商业案例"],
            "qualityScore": 85,
            "url": "https://x.com/amasad/status/2074274666709987663"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月6日 · 周一",
            "actor": "Amjad Masad",
            "meta": "CEO @ Replit · X 动态",
            "title": "Replit Agent 实现自我改进闭环",
            "summary": "Amjad Masad 解释 Replit 最近快速提升的原因：他们关闭了反馈循环，让 Agent 能够自我改进——Agent 的输出结果被回传用于训练和改进 Agent 自身，形成持续进化的飞轮。",
            "keyPoints": [
                "闭环反馈：Agent 的产出被用于训练改进 Agent",
                "这一机制解释了 Replit 近期的快速提升",
                "自我进化的 Agent 正在成为行业新范式"
            ],
            "whyItMatters": "如果 Agent 能通过使用自身产出持续改进，这会形成其他平台难以复制的数据飞轮优势。",
            "tags": ["Agent", "工程", "反馈闭环"],
            "qualityScore": 92,
            "url": "https://x.com/amasad/status/2074257906594177279"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月6日 · 周一",
            "actor": "Guillermo Rauch",
            "meta": "CEO @ Vercel · X 动态",
            "title": "AI 编程的终极检验标准：软件整体在变好吗？",
            "summary": "Rauch 提出评价 AI 编程效果的核心指标：软件整体质量在提升吗？公司交付速度加快了吗？你拥有了以前不敢想的应用和游戏吗？对 Rauch 本人而言，他对个人生产力的控制力「急剧增加」，感受到了一种前所未有的主动权和创造力。",
            "keyPoints": [
                "终极问题不是模型 benchmark，而是「软件变好了吗」",
                "个人生产力控制力大幅提升是真实感受",
                "评价标准应从技术指标转向产品体验指标"
            ],
            "whyItMatters": "这是一个从开发者体验倒推评价体系的视角——AI 工具好坏的最终裁判是产品结果，不是代码行数。",
            "tags": ["产品", "Agent", "评价体系"],
            "qualityScore": 85,
            "url": "https://x.com/rauchg/status/2074222247548735996"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月7日 · 周二",
            "actor": "Guillermo Rauch",
            "meta": "CEO @ Vercel · X 动态",
            "title": "Agent 框架应内置 eval，像浏览器内置渲染引擎一样",
            "summary": "Rauch 宣布 Vercel 的 eve 框架自带 eval 系统（eve eval），并给出重要类比：Web 框架把测试变成了生态选择（React 没有内置测试方案），但对 Agent 来说 eval 是基础设施级的必需品，不应是插件或可选功能。",
            "keyPoints": [
                "eve 内置了 eval 系统用于 Agent 和自身进化评估",
                "Web 框架让测试成为生态选择，Agent 框架不应重蹈覆辙",
                "Eval 对 Agent 来说不是可选项，是基础设施"
            ],
            "whyItMatters": "这与 Web 框架早期缺少测试的故事类似——谁先解决 Agent eval 基础设施问题，谁就可能定义下一代开发范式。",
            "tags": ["Agent", "工程", "Eval"],
            "qualityScore": 88,
            "url": "https://x.com/rauchg/status/2074287795028512773"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月6日 · 周一",
            "actor": "Aaron Levie",
            "meta": "CEO @ Box · X 动态",
            "title": "AI 的分层：前沿模型做新用例，应用层做规模化",
            "summary": "Box CEO Aaron Levie 总结了一个关于开源 AI 和应用层的框架：前沿模型将持续解决全新用例和复杂编排，而开源/应用层负责已验证用例的规模化落地。这两个层面将始终共存。",
            "keyPoints": [
                "前沿模型 = 探索新用例 + 复杂工作流编排",
                "开源/应用层 = 已验证场景的规模化执行",
                "两个层面不是替代关系，是互补共存"
            ],
            "whyItMatters": "这个简洁的框架帮助 Builder 明确自己在 AI 栈中的生态位——做探索者还是执行者，或是连接两者的桥梁。",
            "tags": ["研究", "开源", "市场"],
            "qualityScore": 82,
            "url": "https://x.com/levie/status/2074163686990913576"
        },
        {
            "type": "post",
            "typeLabel": "观点动态",
            "date": "7月7日 · 周二",
            "actor": "Zara Zhang",
            "meta": "Builder · X 动态",
            "title": "三场 AI 大会演讲录像全上线，值得刷完",
            "summary": "AI Engineer Conference、Cursor Compile、Figma Config 三场高质量会议的演讲录像已全部免费上线。无论是什么背景的 Builder，都可以在家中跟随一线从业者学习最前沿的实践。Zara 同时指出：不要被自己的职位头衔限制——现在每个人都是工程师、产品和设计师。",
            "keyPoints": [
                "AI Engineer、Cursor Compile、Figma Config 三场会议录像可看",
                "覆盖了 AI 工程、AI 编程工具和 AI 产品设计三大方向",
                "头衔不再限制你的角色——人人都是 builder"
            ],
            "whyItMatters": "这是获取 AI 行业最新实践的极低成本渠道，对个人 Builder 提升帮助巨大。",
            "tags": ["工程", "组织", "学习资源"],
            "qualityScore": 80,
            "url": "https://x.com/zarazhangrui/status/2074304295097561490"
        },
        {
            "type": "blog",
            "typeLabel": "深度文章",
            "date": "6月18日 · 周四",
            "actor": "Claude Blog",
            "meta": "Anthropic · 官方博客",
            "title": "Claude Code 新增 Artifacts 支持",
            "summary": "Claude Code 现在可以将工作进展保存为 Artifact，将其变成实时更新的可视化页面——包括 PR 代码走查、系统架构说明、监控面板和发布检查清单等。Artifact 会在会话中自动更新。",
            "keyPoints": [
                "工作产出变为可视化、可分享的 Artifact 页面",
                "支持 PR 走查、系统解说、仪表盘等实用模板",
                "Artifact 随会话进展自动更新"
            ],
            "whyItMatters": "将 CLI 工具的临时输出转化为持久化的、可协作的可视化页面，大幅降低了 AI 辅助开发中的沟通成本。",
            "tags": ["产品", "Agent", "工程"],
            "qualityScore": 80,
            "url": "https://claude.com/blog/artifacts-in-claude-code"
        }
    ]
}

# Save archive
with open(os.path.join(data_dir, "archive", "2026-07-08.json"), "w", encoding="utf-8") as f:
    json.dump(curated, f, ensure_ascii=False, indent=2)

# Save latest
with open(os.path.join(data_dir, "latest.json"), "w", encoding="utf-8") as f:
    json.dump(curated, f, ensure_ascii=False, indent=2)

# Update digests.json - replace matching date or prepend
digests_path = os.path.join(data_dir, "digests.json")
if os.path.exists(digests_path):
    with open(digests_path, "r", encoding="utf-8") as f:
        digests = json.load(f)
    # Replace entry for 2026-07-08 if exists
    replaced = False
    for i, entry in enumerate(digests):
        if entry.get("date") == "2026-07-08":
            digests[i] = curated
            replaced = True
            break
    if not replaced:
        digests.insert(0, curated)
else:
    digests = [curated]

with open(digests_path, "w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print("Digest built and saved successfully.")
print(f"- archive/2026-07-08.json: {len(json.dumps(curated, ensure_ascii=False))} chars")
print(f"- latest.json updated")
print(f"- digests.json: {len(digests)} entries, 2026-07-08 {'replaced' if replaced else 'prepended'}")
