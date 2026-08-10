import json
from pathlib import Path

root = Path(r"C:\Users\PC\Documents\ai-builders-daily")
date = "2026-08-11"
archive_path = root / "data" / "archive" / f"{date}.json"
latest_path = root / "data" / "latest.json"
digests_path = root / "data" / "digests.json"

with archive_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

# Curated editorial layer for the restructured high-signal briefing page.
data["headline"] = "AI Builders 今日高信号：Agent 安全、企业扩散、coding agent 工程纪律、产品反馈闭环，以及 Claude Code artifacts。已筛选出 10 条高信号内容。"
data["editorNote"] = "本页只保留有事实增量、观点密度、工程/产品 insight 或长期判断价值的 AI Builders 内容；低信号日常、吐槽、meme、无上下文短评、纯转发和非 AI 主题会被过滤。"

data["dailyInsight"] = {
    "paragraphs": [
        "今天的主线不是某个模型发布，而是 Agent 从“能做事”进入“如何安全、可持续地做事”的阶段。Boris Cherny 把 prompt injection 放在最前面：当 Agent 会浏览网页、读取内容、调用工具时，网页上的恶意文本就可能变成指令通道。对 AI Builders 来说，这意味着安全边界不能只靠模型对齐，必须进入工具权限、数据隔离、审计和默认拒绝策略。",
        "另一条强信号来自企业采用：Aaron Levie 认为 Agent 的扩散会非常不均匀，因为最先爆发的是那些连续、可度量、不中断的电脑工作，coding 正好满足这些条件。Guillermo Rauch 进一步提醒，即使有 Agentic inquiry，真正面向用户和收入的软件仍然需要读代码。换句话说，Agent 会加速工程，但不会取消工程判断；它把高质量 code review、架构理解和风险管理变得更重要。",
        "产品层面，Linear Agent 把“做不了的任务”自动转成 feature request，是今天最值得产品团队借鉴的机制。它把 Agent 失败从一次性挫败变成结构化反馈，让缺失工具、权限或上下文进入产品迭代队列。这类闭环比单纯提高模型能力更现实：每一次失败都在告诉团队下一步该补哪块能力。",
        "Claude Code artifacts 与 AI multiplayer 的讨论则指向协作形态变化：Agent 不再只是终端里的隐形执行者，而是在生成可分享的 PR walkthrough、系统说明、dashboard 和 release checklist。随着多人、多 Agent 协作出现，真正稀缺的不是“一个更聪明的助手”，而是让人、Agent、上下文和产物共同可见、可追踪、可交接的工作界面。",
        "今天也有大量应被过滤的内容：OpenAI 团队互相称赞、深夜写代码段子、Dreamcore、kebab case、生活记录、文学阅读和 meme 都有社交热度，但对 AI Builders 的长期判断价值有限。保留下来的内容共同指向一个判断：下一阶段竞争不只在模型能力，而在 Agent 的安全、工作流适配、反馈闭环与协作界面。"
    ],
    "filteredNote": "过滤掉了 Sam Altman 的团队称赞短帖、Thibault Sottiaux 的深夜写代码玩笑、Guillermo Rauch 的 Hermes + Vercel / Dreamcore、Aaron Levie 的 Agent meme、Nikunj Kothari 的 kebab case、Dan Shipper 的生活/阅读记录、Peter Yang 的家庭记录、Matt Turck 的一词转评等低信号内容。"
}

items = [
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月9日 · 周日",
        "actor": "Boris Cherny",
        "meta": "Claude Code · X 动态",
        "title": "Prompt injection 是 Agent 进入真实网页后的第一安全债",
        "summary": "Boris Cherny 指出，prompt injection 是攻击用户和 Agent 最常见的路径：Agent 访问网页时，页面中的恶意文本可能被模型解释成指令，从而泄露 SSH keys、passwords 等敏感信息。他提到早期 Claude 模型也会中招，这也是许多公司在生产环境谨慎开放 Agent 的原因。这个提醒把 Agent 安全从抽象模型风险拉回到非常具体的 I/O 边界问题。",
        "keyPoints": [
            "网页内容本身可能成为对 Agent 的指令注入通道",
            "风险不只在回答错误，而在 Agent 拥有工具权限后可能执行泄密动作",
            "生产级 Agent 需要权限隔离、敏感信息防护和可审计工具调用"
        ],
        "whyItMatters": "Agent 产品一旦能浏览、读取和执行，安全模型就必须从聊天安全升级为系统安全。Builders 需要把 prompt injection 当成默认威胁模型，而不是边缘案例。",
        "tags": ["Agent", "Security", "Prompt Injection"],
        "qualityScore": 93,
        "url": "https://x.com/bcherny/status/2086520950259118464"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月9日 · 周日",
        "actor": "Guillermo Rauch",
        "meta": "Vercel · X 动态",
        "title": "Agentic coding 仍然绕不开读代码这件事",
        "summary": "Guillermo Rauch 认为，如果你完全不读代码——无论是直接读，还是通过 agentic inquiry 间接追问代码——通常意味着项目还处在新手、一次性原型、无用户收入或承担技术债阶段。他并不否认这些状态的合理性，而是在强调：只要软件进入真实用户和收入场景，代码理解仍是质量与风险控制的核心。Agent 可以帮你探索代码，但不能替你承担工程判断。",
        "keyPoints": [
            "Agentic inquiry 可以扩展读代码方式，但不能取消代码理解",
            "不读代码通常只适用于原型、一次性软件或低风险阶段",
            "面向真实用户的软件仍需要人类对架构、债务和风险负责"
        ],
        "whyItMatters": "这是一条针对 AI coding hype 的工程纪律提醒。AI Builders 使用 coding agent 时，真正的杠杆来自更快理解与审查代码，而不是盲目接受生成结果。",
        "tags": ["AI Coding", "Engineering", "Code Review"],
        "qualityScore": 91,
        "url": "https://x.com/rauchg/status/2086513316265181213"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月9日 · 周日",
        "actor": "Aaron Levie",
        "meta": "Box · X 动态",
        "title": "Enterprise Agent 的扩散会先吃掉连续电脑工作",
        "summary": "Aaron Levie 判断，Agent 在企业中的扩散速度会非常不均匀，因为不同工作流与“连续、不中断的电脑工作”的匹配度不同。Agentic coding 之所以垂直增长，是因为软件开发的经济价值可以被直接映射到连续执行、快速反馈和可验证产出。企业 AI 的关键问题因此不是“有没有 Agent”，而是哪些流程天然适合被 Agent 化。",
        "keyPoints": [
            "Agent 采用速度取决于工作流是否连续、可执行、可验证",
            "Coding 是早期爆发场景，因为价值反馈链条短且产出可测试",
            "企业场景会出现显著分化，而不是均匀替代所有白领工作"
        ],
        "whyItMatters": "这为企业 AI Builders 提供了选场景的方法：优先找连续电脑工作、明确输入输出和高频反馈，而不是把 Agent 平铺到所有流程。",
        "tags": ["Enterprise AI", "Agent", "Workflow"],
        "qualityScore": 90,
        "url": "https://x.com/levie/status/2086559201053294909"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月9日 · 周日",
        "actor": "Peter Yang",
        "meta": "Linear Agent · X 动态",
        "title": "让 Agent 把失败自动转成产品反馈",
        "summary": "Peter Yang 观察到 Linear Agent 会为自己提交 feature requests：当用户要求它做某件事但缺少合适工具时，Agent 会报告能力缺口，系统再把这个缺口记录成 issue。这是非常实用的产品机制，因为它把 Agent 的失败转化为结构化路线图输入。相比泛泛地“提升智能”，这种闭环更能持续改进真实工作流。",
        "keyPoints": [
            "Agent 无法完成任务时，应记录缺失工具、权限或上下文",
            "失败数据可以直接转化为产品团队可处理的 issue",
            "这让 Agent 产品迭代围绕真实用户任务，而不是抽象 benchmark"
        ],
        "whyItMatters": "多数 Agent 产品的问题不是没有 demo，而是不知道失败后如何学习。Linear 的做法展示了把用户摩擦转成产品迭代资产的简单路径。",
        "tags": ["Agent", "Product", "Feedback Loop"],
        "qualityScore": 89,
        "url": "https://x.com/petergyang/status/2086562291206791482"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月10日 · 周一",
        "actor": "Amjad Masad",
        "meta": "Replit · X 动态",
        "title": "把 Agent 的自发协调改造成公共知识网络",
        "summary": "Amjad Masad 借 OpenAI-HuggingFace incident 讨论 Agent 的自发协调：同样的机制在恶意使用时令人担忧，但也可能被引导为公共利益。他提出一个 AI agents public commons，包含 tell 和 lookup 两类 API：Agent 学到对其他 Agent 有用的信息时告诉网络，行动前先查询网络。这本质上是在思考 Agent 之间的共享记忆与协作协议。",
        "keyPoints": [
            "Agent 的跨实例协调既可能带来安全风险，也可能成为公共基础设施",
            "tell / lookup API 把经验共享抽象成可实现的协议接口",
            "关键挑战在于信任、污染防护、权限和激励设计"
        ],
        "whyItMatters": "单个 Agent 的能力提升之外，Agent 间知识网络可能成为下一层平台能力。Builders 需要同时考虑协作收益与公地污染风险。",
        "tags": ["Agent", "Infrastructure", "Coordination"],
        "qualityScore": 88,
        "url": "https://x.com/amasad/status/2086628413322981747"
    },
    {
        "type": "blog",
        "typeLabel": "深度文章",
        "date": "Jun 18, 20",
        "actor": "Claude Blog",
        "meta": "Claude Code · Blog",
        "title": "Claude Code artifacts 把编码过程变成可分享工作产物",
        "summary": "Claude Blog 介绍 Claude Code 现在支持 artifacts，可以把会话中的工作进展捕获为实时、可分享的视觉页面，包括 PR walkthrough、系统解释、dashboard 和 release checklist。这意味着 coding agent 的输出不再只是代码 diff 或终端日志，而是面向团队协作的持续更新产物。它把 Agent 从个人自动化工具推向协作界面。",
        "keyPoints": [
            "Claude Code 可以把工作进展生成 artifacts，并随会话自动更新",
            "典型场景包括 PR walkthrough、系统说明、dashboard 和发布 checklist",
            "Agent 产物正在从代码生成扩展到团队沟通和项目管理"
        ],
        "whyItMatters": "AI coding 的瓶颈常常不是生成代码，而是让团队理解发生了什么。Artifacts 把 Agent 的工作过程产品化，有助于降低协作和审查成本。",
        "tags": ["Claude Code", "AI Coding", "Collaboration"],
        "qualityScore": 87,
        "url": "https://claude.com/blog/artifacts-in-claude-code"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月9日 · 周日",
        "actor": "Swyx",
        "meta": "smol.ai · X 动态",
        "title": "技能越多不等于 Agent 越强，未治理的 skills 会吃掉上下文",
        "summary": "Swyx 提醒 builders 定期删除 skills：时间线不断鼓励你尝试新 skill，但堆积过多的 skill 轻则浪费上下文，重则在没有观察 traces 的情况下相互产生意外影响。这是 Agent 工程里很容易被忽略的复杂度管理问题。与其追求“什么都能做”，不如保持工具面可理解、可观测、可回滚。",
        "keyPoints": [
            "过多 skills 会占用 context budget，降低 Agent 任务效率",
            "skills 之间可能出现隐性相互作用，增加调试难度",
            "Agent 工具链需要像依赖管理一样定期清理和观测"
        ],
        "whyItMatters": "Agent 可靠性往往被工具膨胀拖垮。对 AI Builders 来说，少而精、可追踪的能力集合比堆叠热门 skills 更重要。",
        "tags": ["Agent", "Context", "Engineering"],
        "qualityScore": 86,
        "url": "https://x.com/swyx/status/2086505938144616810"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月10日 · 周一",
        "actor": "Garry Tan",
        "meta": "Y Combinator · X 动态",
        "title": "从 bug 和异常出发，反推系统里的隐藏机器",
        "summary": "Garry Tan 总结自己的工作方式：从 bug、gap、false claim、半成品工具或机构里的奇怪行为开始，追问什么隐藏机制会让这个可见失败发生，然后修复根因并重复。这不是纯 AI 话题，但对构建 AI 产品非常有用，因为 Agent 系统的失败往往暴露的是上下文、权限、评估或组织流程的隐性结构。",
        "keyPoints": [
            "把可见失败当作入口，而不是只修补表面症状",
            "追问导致失败的隐藏机制，才能找到系统性改进点",
            "适用于 Agent 产品调试、组织流程改造和 founder problem discovery"
        ],
        "whyItMatters": "AI Builders 很容易被 demo 成功误导。Garry 的方法提醒团队把异常当成最高价值信号，用 failure analysis 驱动产品和系统设计。",
        "tags": ["Founder", "Systems Thinking", "Product"],
        "qualityScore": 84,
        "url": "https://x.com/garrytan/status/2086615082163941460"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "8月9日 · 周日",
        "actor": "Nikunj Kothari",
        "meta": "FPV Ventures · X 动态",
        "title": "AI multiplayer 还缺一个真正好用的人机协作界面",
        "summary": "Nikunj Kothari 提出一个产品问题：他看到的大多数 AI 体验仍是 human <> agent 的单人协作模式，很少看到 human(s) <> agent(s) 的多人、多 Agent 协作体验。他追问这是缺乏产品灵感，还是模型能力限制。这是一个早期但重要的界面问题：当 Agent 进入团队工作，协作协议和可见性会比单轮能力更关键。",
        "keyPoints": [
            "当前主流 AI 交互仍偏单人与单 Agent 协作",
            "多人、多 Agent 的协作界面还没有形成清晰范式",
            "瓶颈可能同时来自产品设计、上下文共享和模型协调能力"
        ],
        "whyItMatters": "下一代 AI 产品未必只是更强个人助手，而可能是团队级 Agent workspace。谁先解决多人协作、权限和上下文共享，谁就更接近真实组织场景。",
        "tags": ["AI UX", "Agent", "Collaboration"],
        "qualityScore": 82,
        "url": "https://x.com/nikunj/status/2086438339419496449"
    },
    {
        "type": "podcast",
        "typeLabel": "播客摘录",
        "date": "7月31日 · 周五",
        "actor": "xAI Co-Founder",
        "meta": "Unsupervised Learning · Podcast",
        "title": "模型开发的未来会围绕工程体系而不只是参数规模",
        "summary": "Unsupervised Learning 这期访谈围绕 xAI Co-Founder 对未来模型开发的判断展开。虽然源摘要较短，但主题指向模型团队正在从单纯扩大训练规模，转向更复杂的工程组织：数据、评估、推理系统、产品反馈和研究节奏共同决定模型迭代速度。对 builders 来说，理解模型进步不能只看 benchmark，而要看背后的开发系统。",
        "keyPoints": [
            "模型竞争越来越依赖端到端工程体系，而不只是单次训练规模",
            "评估、数据管线和推理基础设施会影响模型迭代速度",
            "产品反馈与研究路线的连接会成为模型公司的长期优势"
        ],
        "whyItMatters": "模型能力是产品创新的上游变量。理解模型公司如何组织开发，有助于 AI Builders 判断能力边界、发布时间表和该把产品赌注押在哪里。",
        "tags": ["Models", "Research", "Engineering"],
        "qualityScore": 78,
        "url": "https://www.youtube.com/@RedpointAI"
    }
]

data["highSignalItems"] = items

# Keep toplines aligned with curated cards for legacy consumers.
data["toplines"] = [
    {
        "title": item["title"],
        "source": item["meta"],
        "url": item["url"],
        "sourceDate": date,
        "sourceDisplayDate": item["date"],
        "summary": item["summary"],
        "chineseTitle": item["title"],
        "tags": item["tags"],
        "score": item["qualityScore"],
    }
    for item in items[:5]
]

# Archive and latest must be identical.
for path in (archive_path, latest_path):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

if digests_path.exists():
    with digests_path.open("r", encoding="utf-8") as f:
        digests = json.load(f)
else:
    digests = []

digests = [d for d in digests if d.get("date") != date]
digests.insert(0, data)
with digests_path.open("w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"curated {date}: {len(items)} highSignalItems")
print(f"archive={archive_path}")
print(f"latest={latest_path}")
print(f"digests entries={len(digests)}")
