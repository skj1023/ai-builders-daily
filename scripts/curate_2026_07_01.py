import json
from pathlib import Path

root = Path(r"C:\Users\PC\Documents\ai-builders-daily")
date = "2026-07-01"
archive_path = root / "data" / "archive" / f"{date}.json"
latest_path = root / "data" / "latest.json"
digests_path = root / "data" / "digests.json"

data = json.loads(archive_path.read_text(encoding="utf-8"))

data["headline"] = "今天的信息流集中在 agent 产品化、权限与用量信任、企业云分发、开放模型基础设施以及 AI 半导体供应链：已筛选出 10 条高信号内容。"
data["editorNote"] = "本页只保留有事实增量、观点密度、产品/工程洞察或长期判断价值的 AI Builders 内容；低信号日常、meme、无上下文短评、纯转发和非 AI 主题会被过滤。"

data["dailyInsight"] = {
    "paragraphs": [
        "今天最强的主线是 agent 产品正在从“会做事”转向“可并行、可控、可计量”。Claude Code 准备让 subagents 默认在后台运行，Codex 则同时处理用量异常和更细粒度的权限 profile：这些都不是炫技功能，而是 agent 进入高频工作流后必须补齐的操作系统层能力——任务调度、权限边界、账单信任和失败处理。",
        "Anthropic 相关信号非常密集：Claude in Microsoft Foundry GA、Managed Agents 的自托管 sandbox / MCP tunnels、以及 Managed Agents 架构文章都指向同一件事：企业不会只买一个聊天入口，而会买能接入现有身份、账单、私有工具、私有网络和审计体系的 agent 平台。对 AI Builders 来说，分发渠道和安全边界正在和模型能力一样重要。",
        "开放模型与闭源前沿的产业判断也在升温。Madhu Guru 认为 GLM 这类强 open-weight 模型反而会加强 Google 这类云基础设施方的位置，因为企业会更多实验微调和自部署；Aaron Levie 则把问题推到更宏观的层面：如果闭源 stack 不能长期保持大幅领先，开放模型会削弱 gatekeeping，并推动替代技术栈转移经济价值。",
        "产品层面的小信号同样值得看。Peter Yang 对比 Claude web 与 coding agents 的写作质量，提示 system prompt 和工具定位会塑造模型输出风格；Zara Zhang 的本地优先 Chrome extension 则展示了一个清晰的 builder 模式：把“稍后阅读”这种真实行为摩擦转成日历上的承诺，不上服务器、不建账号，先用低复杂度方案验证需求。",
        "更底层的长期变量来自 Intel CEO Lip-Bu Tan 在 No Priors 里谈半导体供应链重构。AI Builders 往往容易把算力当成云端抽象资源，但模型、agent 和企业部署背后仍然受制造、封装、资本开支和地缘供应链约束；未来 AI 产品竞争，很大一部分会间接受这些基础设施节奏影响。"
    ],
    "filteredNote": "过滤掉了 Swyx 的活动一句话/玩笑式 workshop 动态、Thibault Sottiaux 的 reset button 短评、Ryo Lu 的 app 宣传短句、Garry Tan 的空文本和 datacenter 口号、Matt Turck 与 Nikunj Kothari 的世界杯/日常内容、Peter Steinberger 的无上下文短评等低信号、非 AI 或缺少可执行洞察的内容。"
}

high = [
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月29日 · 周一",
        "actor": "Boris Cherny",
        "meta": "Claude Code · X 动态",
        "title": "后台 subagents 把 Claude Code 推向并行工作流",
        "summary": "Boris Cherny 预告下一版 Claude Code 会让 subagents 默认在后台运行，用户可以继续与 Claude 对话；如果需要前台执行，也可以直接告诉 Claude。这是 agent 产品形态的重要变化：从单线程对话助手，转向可同时委派、等待和继续协作的工作台。",
        "keyPoints": [
            "Claude Code 的 subagents 将默认在后台运行。",
            "用户可以一边等待子任务执行，一边继续和主 Claude 对话。",
            "前台/后台执行模式变成自然语言可控的产品行为。"
        ],
        "whyItMatters": "并行任务编排会成为 coding agent 的核心体验；真正高频的 agent 工具必须减少等待和上下文阻塞。",
        "tags": ["Agent", "产品", "工程"],
        "qualityScore": 94,
        "url": "https://x.com/bcherny/status/2071647677591466098"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月29日 · 周一",
        "actor": "Thibault Sottiaux",
        "meta": "Codex · X 动态",
        "title": "Codex 用量异常后的补偿机制仍是产品信任课",
        "summary": "Thibault Sottiaux 表示 Codex 用量限制会再次完全重置，并额外给用户一个未来 24 小时可用的 reset；团队调查后认为不是单一中心故障，而是几个小问题叠加导致消耗异常。这里的重点不是“送额度”，而是高频 AI 工具必须把计量、补偿和透明沟通产品化。",
        "keyPoints": [
            "Codex 对用户 usage limits 进行再次全量重置。",
            "团队额外发放一个可在 24 小时内使用的 reset。",
            "异常源不是单点故障，而是多个小问题复合。"
        ],
        "whyItMatters": "AI coding 工具一旦按用量和额度运行，计量准确性会直接影响信任与留存。",
        "tags": ["产品", "工程", "商业化"],
        "qualityScore": 92,
        "url": "https://x.com/thsottiaux/status/2071740419030053227"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月29日 · 周一",
        "actor": "Thibault Sottiaux",
        "meta": "Codex · X 动态",
        "title": "从粗粒度 sandbox 到可继承权限 profile",
        "summary": "Codex 面向高级用户推出替代粗粒度 sandbox modes 的机制：可复用、可继承的 permission profiles，把 OS 级文件读写/拒绝规则、按域名网络权限、Unix sockets 和 fail-closed admin allowlists 绑定起来。它把 coding agent 的安全边界从“能不能开沙箱”推进到“每个任务最小权限”。",
        "keyPoints": [
            "Permission profiles 支持复用和继承，替代粗粒度 sandbox 模式。",
            "规则覆盖文件读写/拒绝、网络域名、Unix sockets 等边界。",
            "Fail-closed allowlists 强调默认安全和任务级最小权限。"
        ],
        "whyItMatters": "企业采用 coding agents 的核心阻力之一是权限风险；更细的权限模型是走向生产环境的必要条件。",
        "tags": ["Agent", "安全", "工程"],
        "qualityScore": 91,
        "url": "https://x.com/thsottiaux/status/2071636285807059315"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月29日 · 周一",
        "actor": "Claude",
        "meta": "Anthropic / Microsoft Foundry · X 动态",
        "title": "Claude 进入 Microsoft Foundry，企业分发战线继续收缩到云平台",
        "summary": "Claude in Microsoft Foundry 已 GA，并托管在 Azure 上；Azure 客户可使用 Claude Opus 4.8 和 Claude Haiku 4.5，并接入 Azure authentication、billing 和 commitment retirement。后续补充说明显示推理由 Anthropic 运营在 Azure infra 上，支持 prompt caching 和 extended thinking。",
        "keyPoints": [
            "Claude in Microsoft Foundry 从预览走向一般可用。",
            "企业客户可通过 Azure 身份、账单和承诺消费体系采购 Claude。",
            "推理由 Anthropic 在 Azure 基础设施上运营，并支持缓存和 extended thinking。"
        ],
        "whyItMatters": "企业 AI 分发越来越依赖已有云采购与身份体系；模型公司的 go-to-market 会深度绑定 hyperscaler。",
        "tags": ["企业 AI", "云平台", "市场"],
        "qualityScore": 90,
        "url": "https://x.com/claudeai/status/2071653958905467027"
    },
    {
        "type": "blog",
        "typeLabel": "深度文章",
        "date": "7月1日 · 周三",
        "actor": "Anthropic Engineering",
        "meta": "Claude Code · 官方工程博客",
        "title": "Claude Code 质量报告背后的产品可观测性问题",
        "summary": "Anthropic Engineering 回应过去一个月部分用户反馈 Claude responses 变差的问题。对 AI Builders 来说，这类 postmortem 的价值在于：模型产品的质量不是静态 benchmark，而是跨模型、系统 prompt、工具调用、产品入口和用户任务分布共同形成的线上体验。",
        "keyPoints": [
            "Anthropic 正式调查并回应 Claude Code 近期质量反馈。",
            "用户感知质量可能来自多层系统变化，而不只是模型本身。",
            "AI 产品需要持续监控线上任务质量和用户反馈。"
        ],
        "whyItMatters": "当 AI 产品成为生产力工具，质量退化的解释、定位和沟通会成为工程能力的一部分。",
        "tags": ["质量", "工程", "Agent"],
        "qualityScore": 87,
        "url": "https://www.anthropic.com/engineering/april-23-postmortem"
    },
    {
        "type": "blog",
        "typeLabel": "深度文章",
        "date": "7月1日 · 周三",
        "actor": "Anthropic Engineering",
        "meta": "Managed Agents · 官方工程博客",
        "title": "Managed Agents 的关键架构：把 brain 和 hands 解耦",
        "summary": "Anthropic Engineering 的 Managed Agents 文章强调“decoupling the brain from the hands”：模型推理与执行环境需要分离扩展。这个框架对 builders 很重要，因为可靠 agent 不是单一模型 API，而是推理、工具、权限、环境、状态和失败恢复组成的系统。",
        "keyPoints": [
            "Managed Agents 的扩展问题被拆成推理层与执行层。",
            "执行环境需要能安全连接工具、文件系统和外部服务。",
            "Agent 平台化的难点在系统架构，而不只是模型调用。"
        ],
        "whyItMatters": "它给出了构建生产级 agent 平台的架构语言：模型是 brain，执行环境是 hands，两者要独立治理和扩展。",
        "tags": ["Agent", "架构", "工程"],
        "qualityScore": 89,
        "url": "https://www.anthropic.com/engineering/managed-agents"
    },
    {
        "type": "blog",
        "typeLabel": "深度文章",
        "date": "May 19, 20",
        "actor": "Claude Blog",
        "meta": "Managed Agents · 产品博客",
        "title": "自托管 sandbox 和 MCP tunnels 把企业私有工具接进 agent",
        "summary": "Claude Managed Agents 新增自托管 sandboxes 和 MCP tunnels，让 agent 可以在客户控制的 sandbox 中运行，并连接私有 MCP servers。它解决的是企业采用 agent 的关键问题：既要让 agent 接触真实系统，又要保留对网络、数据和执行环境的控制。",
        "keyPoints": [
            "企业可以把 Managed Agents 放进自己控制的 sandbox。",
            "MCP tunnels 允许连接私有 Model Context Protocol servers。",
            "产品方向从通用聊天入口转向企业内部工具编排。"
        ],
        "whyItMatters": "私有工具连接和自控执行环境是 agent 从个人效率工具进入企业系统的前置条件。",
        "tags": ["MCP", "企业 AI", "安全"],
        "qualityScore": 86,
        "url": "https://claude.com/blog/claude-managed-agents-updates"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月29日 · 周一",
        "actor": "Madhu Guru",
        "meta": "Open-weight models · X 动态",
        "title": "强 open-weight 模型可能反而加强云基础设施方",
        "summary": "Madhu Guru 认为 GLM 这类强 open-weight 模型的崛起会加强 Google 的位置，因为更多公司会实验微调 open-weight models，而价值会流向基础设施。企业想要开放模型的灵活性，但训练、微调、部署和运行仍然需要可靠云平台。",
        "keyPoints": [
            "强 open-weight models 会刺激企业微调和自部署实验。",
            "模型开放不等于价值只流向模型层，基础设施可能受益。",
            "Google 这类云与 AI infra 玩家可能从开放生态中获得增量需求。"
        ],
        "whyItMatters": "它提醒 builders 判断开源/闭源格局时，不要忽略 infra capture：价值可能沿着部署和运行链条重新分配。",
        "tags": ["开放模型", "基础设施", "云平台"],
        "qualityScore": 84,
        "url": "https://x.com/realmadhuguru/status/2071637885154148785"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "6月30日 · 周二",
        "actor": "Aaron Levie",
        "meta": "AI stack strategy · X 动态",
        "title": "闭源前沿如果不能长期领先，gatekeeping 会失效",
        "summary": "Aaron Levie 把 AI 的核心争论概括为：如果闭源 stack 能始终大幅领先，那么垂直整合和访问控制可以成立；但如果开源模型接近前沿，经济价值和控制力就会更难被少数平台锁住。这是对 AI stack 长期权力结构的判断。",
        "keyPoints": [
            "闭源 stack 的 gatekeeping 依赖长期保持明显 frontier advantage。",
            "开放模型接近前沿会削弱访问控制带来的战略价值。",
            "AI 技术栈的经济价值可能在开放生态中重新分布。"
        ],
        "whyItMatters": "这为 AI Builders 判断平台依赖、模型选择和长期议价能力提供了战略框架。",
        "tags": ["开放模型", "平台战略", "市场"],
        "qualityScore": 83,
        "url": "https://x.com/levie/status/2071775583072375214"
    },
    {
        "type": "podcast",
        "typeLabel": "播客摘录",
        "date": "6月18日 · 周四",
        "actor": "No Priors",
        "meta": "Intel CEO Lip-Bu Tan · YouTube / 播客",
        "title": "AI 时代的半导体供应链要重新工程化",
        "summary": "No Priors 对话 Intel CEO Lip-Bu Tan，核心 thesis 是半导体供应链不能只按旧周期优化，而要围绕 AI 需求、制造能力、封装、资本投入和生态合作重新工程化。对 AI Builders 来说，模型能力和 agent 产品背后的真实约束仍然是芯片供给、制造节奏与供应链韧性。",
        "keyPoints": [
            "AI 需求改变了半导体供应链的产能、节奏和资本配置。",
            "先进制造、封装和生态协作会影响未来 AI compute 供给。",
            "AI 产品公司的能力边界间接受到底层芯片与供应链约束。"
        ],
        "whyItMatters": "它把 AI 竞争从模型和应用拉回物理基础设施：没有稳定、可扩展的半导体供应链，软件层创新会被算力节奏卡住。",
        "tags": ["半导体", "基础设施", "供应链"],
        "qualityScore": 82,
        "url": "https://www.youtube.com/watch?v=asCgCv2XB4s"
    }
]

data["highSignalItems"] = high
# curated toplines for legacy surfaces
data["toplines"] = [
    {
        "title": item["title"],
        "source": item["meta"],
        "url": item["url"],
        "sourceDate": "2026-07-01" if item["type"] == "blog" else ("2026-06-18" if item["type"] == "podcast" else "2026-06-29"),
        "sourceDisplayDate": item["date"],
        "summary": item["summary"],
        "chineseTitle": item["title"],
        "tags": item["tags"],
        "score": item["qualityScore"]
    }
    for item in high[:5]
]

for path in (archive_path, latest_path):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

digests = json.loads(digests_path.read_text(encoding="utf-8"))
digests = [d for d in digests if d.get("date") != date]
digests.insert(0, data)
digests_path.write_text(json.dumps(digests, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"date": date, "highSignalItems": len(high), "archive": str(archive_path), "latest": str(latest_path), "digests": str(digests_path)}, ensure_ascii=False, indent=2))
