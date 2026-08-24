import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-25"
archive_path = ROOT / "data" / "archive" / f"{DATE}.json"
with archive_path.open(encoding="utf-8") as f:
    data = json.load(f)

cards = [
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Thibault Sottiaux", "meta": "Codex · X 动态",
        "title": "模型效率与可靠性将成为 AI 基础设施的核心指标",
        "summary": "Thibault Sottiaux 判断，2026 年企业会开始认真关注模型效率与可靠性，因为模型服务正在从实验性能力变成关键基础设施。对 AI 产品团队而言，单纯追求能力上限已经不够，成本、稳定性和可预期性会直接决定产品能否规模化。",
        "keyPoints": ["模型效率与可靠性正在从优化项变成基础设施要求", "推理成本、延迟和故障率会影响产品商业化", "AI 团队需要把模型运营纳入长期工程体系"],
        "whyItMatters": "这是一条对 AI 产品路线有长期影响的判断：当模型成为生产依赖，infra discipline 会和模型能力同等重要。",
        "tags": ["工程", "研究", "基础设施"], "qualityScore": 91,
        "url": "https://x.com/thsottiaux/status/2091581575108653374"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Peter Yang", "meta": "AI 产品实践 · X 动态",
        "title": "高质量 AI eval 需要上下两层同时测量",
        "summary": "Peter Yang 转述 Shreya 的框架：AI eval 一方面要从任务描述出发，做 top-down 的理想能力评估；另一方面要从大量真实交互和失败样本出发，做 bottom-up 的现实质量评估。前者帮助定义应该达到什么，后者揭示用户实际上会遇到什么。",
        "keyPoints": ["Top-down eval 从任务定义推导理想答案", "Bottom-up eval 依赖真实样本、轨迹和失败模式", "两类 eval 结合才能避免只测 benchmark 或只测局部体验"],
        "whyItMatters": "这是构建 Agent 评测体系时非常实用的分层方法，能把‘模型看起来会做’与‘产品在真实世界可靠’区分开。",
        "tags": ["评测", "Agent", "产品"], "qualityScore": 92,
        "url": "https://x.com/petergyang/status/2091586298779955512"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Madhu Guru", "meta": "Meta AI · X 动态",
        "title": "评测应对齐 Agent 的中间任务，而不只看最终答案",
        "summary": "Madhu Guru 提出构建 eval 的 Goldilocks principle：评测粒度应落在 Agent 实际要完成的各项工作上，而不是只检查最终输出。例如金融分析 Agent 不应只看最后的股票推荐，还要评估检索、数据分析、推理和证据组织等中间环节。这样才能定位能力瓶颈和错误来源。",
        "keyPoints": ["评测粒度要与具体 job-to-be-done 对齐", "最终答案正确不代表中间过程可靠", "拆解中间任务有助于定位 Agent 失败原因"],
        "whyItMatters": "对于复杂 Agent，端到端分数往往无法指导迭代；中间任务 eval 才能把质量问题转化为工程任务。",
        "tags": ["评测", "Agent", "工程"], "qualityScore": 94,
        "url": "https://x.com/realmadhuguru/status/2091684812012875981"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Guillermo Rauch", "meta": "Vercel · X 动态",
        "title": "Agent 扩展生态应回到开放协议与可组合工具",
        "summary": "Guillermo Rauch 分享了扩展 AI 产品的设计哲学：通过 MCP、Skills 和 Plugins 等开放协议连接能力，并借鉴 Unix 的两条原则——小程序做好一件事、通过组合完成复杂工作，以及提供可嵌入更大系统的 library。Agent 生态的关键不只是增加工具数量，而是让工具可发现、可组合、可嵌入。",
        "keyPoints": ["开放协议降低 Agent 与工具之间的耦合", "小而专一的工具更容易组合和复用", "library / embeddability 让能力进入更复杂的产品"],
        "whyItMatters": "这套思路直接影响 Agent 平台的架构选择：封闭能力堆叠不如开放、可组合的接口形成生态。",
        "tags": ["Agent", "开放协议", "工程"], "qualityScore": 93,
        "url": "https://x.com/rauchg/status/2091583525661384813"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Guillermo Rauch", "meta": "Vercel · X 动态",
        "title": "推理变便宜后，智能需求会呈现高弹性增长",
        "summary": "Guillermo Rauch 观察到，OpenAI Sol 的降价以及 Vercel AI Gateway 的折扣让 Sol 成为增长最快的 frontier model。这说明对智能的需求具有明显价格弹性：推理成本下降会迅速带来更多调用，也说明 gateway 能帮助团队更快捕捉成本变化和模型迁移机会。",
        "keyPoints": ["推理价格下降会显著放大使用量", "模型选择与成本管理需要动态化", "Gateway 是控制路由、价格和迁移成本的重要基础设施"],
        "whyItMatters": "AI 产品的市场规模不只取决于模型能力，也取决于单位智能的价格；成本下降可能创造全新的使用场景。",
        "tags": ["推理成本", "模型路由", "基础设施"], "qualityScore": 90,
        "url": "https://x.com/rauchg/status/2091671326897713424"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Garry Tan", "meta": "YC · X 动态",
        "title": "传统系统记录需要升级为 Agent 的执行中枢",
        "summary": "Garry Tan 预测，systems of record 如果不成为 AI harness，就可能被 Agent 取代。未来企业软件的价值不只是保存数据，还要围绕这些数据提供权限、上下文、动作和反馈，让 Agent 能在系统内完成工作。",
        "keyPoints": ["数据记录本身正在失去足够的产品护城河", "系统需要提供上下文、权限与可执行动作", "企业软件将从被动记录转向 Agent 工作编排"],
        "whyItMatters": "这为企业 AI 产品提供了清晰方向：最有价值的 AI 化不是外挂聊天框，而是重构核心工作流。",
        "tags": ["Agent", "企业软件", "产品"], "qualityScore": 89,
        "url": "https://x.com/garrytan/status/2091742825042030681"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Peter Yang", "meta": "AI 产品实践 · X 动态",
        "title": "高效的人类助手正在成为 AI Agent 的编排者",
        "summary": "Peter Yang 分享了与人类助手 Char 合作半年的经验：Char 使用 Claude Code 和 Codex 处理播客后期、show notes 和切片，并把 Peter 的 AI skills 复制、改造为适合自己工作流的版本。未来优秀的助手不只是执行任务，还要能够设计、调用和维护 Agent 工作流。",
        "keyPoints": ["人类助手可以通过 Agent 放大执行范围", "可复制、可定制的 skills 是工作流资产", "人与 Agent 的协作编排会成为新型岗位能力"],
        "whyItMatters": "它展示了 AI 落地的一个现实路径：不是立即替代完整岗位，而是先让熟悉业务的人掌握 Agent 编排。",
        "tags": ["Agent", "工作流", "组织"], "qualityScore": 87,
        "url": "https://x.com/petergyang/status/2091631590799737306"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Thibault Sottiaux", "meta": "Codex · X 动态",
        "title": "AI 产品质量需要持续修复与透明沟通",
        "summary": "Thibault Sottiaux 表示，针对前一天发现的使用问题，相关 reset 已经推送到账号，并完成了一批 usage 修复，后续还会继续迭代和沟通。这类更新说明 AI 产品的信任来自持续处理真实故障，而不是只发布能力演示。",
        "keyPoints": ["账号级配置和 usage 问题可以通过快速修复改善体验", "对已知问题的连续跟进比一次性发布更重要", "透明沟通是 AI 产品稳定运营的一部分"],
        "whyItMatters": "对 AI Builder 来说，可靠性不仅是模型指标，也是发现问题、修复问题并让用户感知改进的运营闭环。",
        "tags": ["可靠性", "产品运营", "工程"], "qualityScore": 84,
        "url": "https://x.com/thsottiaux/status/2091688655828246890"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": data["displayDate"],
        "actor": "Peter Steinberger", "meta": "AI 工具 · X 动态",
        "title": "Agent 接入现实世界需要把硬件协议变成可调用能力",
        "summary": "Peter Steinberger 提到，他为 Agent 增加旋转 USB 协议，并让 claw 控制 360 摄像头进行环境观察。这是一个小而具体的例子：当设备协议被封装成 Agent 可调用的工具后，Agent 就能从纯软件执行扩展到感知和操作现实世界。",
        "keyPoints": ["硬件协议可以作为 Agent tool 暴露", "视觉设备让 Agent 获得环境感知能力", "现实世界 Agent 依赖协议、权限和安全边界的工程化"],
        "whyItMatters": "它把 embodied Agent 的问题落到可执行的接口层：关键不是宏大叙事，而是把设备能力可靠地接入工具链。",
        "tags": ["Agent", "硬件", "工具协议"], "qualityScore": 82,
        "url": "https://x.com/steipete/status/2091639468935831910"
    },
    {
        "type": "blog", "typeLabel": "深度文章", "date": data["displayDate"],
        "actor": "Claude Blog", "meta": "Claude · 深度文章",
        "title": "在 Apple Foundation Models 中接入 Claude，构建更强的端侧智能应用",
        "summary": "Claude Blog 介绍了面向 Apple 平台的 Foundation Models framework 支持：开发者可以通过新的 Swift package 调用 Claude，把 Apple 的端侧模型能力与 Claude 组合到更复杂的工作流中。这个方向体现了端侧隐私、低延迟能力与云端 frontier model 的协同，而不是简单二选一。",
        "keyPoints": ["通过 Swift package 将 Claude 接入 Apple Foundation Models", "端侧模型适合隐私、响应速度和基础任务", "云端模型可承担更复杂的推理与工作流"],
        "whyItMatters": "对 Apple AI Builder 而言，这提供了一种混合架构：把端侧体验与云端智能组合起来，兼顾成本、隐私和能力上限。",
        "tags": ["Apple", "端侧 AI", "Agent"], "qualityScore": 88,
        "url": "https://claude.com/blog/claude-for-foundation-models"
    },
]

data["dailyInsight"] = {
    "paragraphs": [
        "今天最清晰的主线是：AI 正从能力展示进入基础设施竞争。Thibault Sottiaux 把模型效率与可靠性称为关键基础设施问题，Guillermo Rauch 则从 Sol 降价带来的增长观察到智能需求的价格弹性。对 Builder 来说，模型选型不能只看 benchmark，还要同时管理单位调用成本、延迟、稳定性和路由切换。",
        "评测方法正在变得更像产品工程，而不是发布前的单次考试。Peter Yang 转述的 top-down / bottom-up 框架，分别回答“理想情况下应该做到什么”和“真实用户到底遇到了什么”；Madhu Guru 进一步强调要按 Agent 的中间 job-to-be-done 拆解评测。只有把真实轨迹与中间环节纳入，eval 才能真正指导迭代。",
        "Agent 的产品边界也在外扩：Guillermo Rauch 倡导 MCP、Skills、Plugins 和 Unix 式组合，Garry Tan 预测 systems of record 必须升级为 AI harness，Peter Yang 展示了人类助手如何用 Claude Code 和 Codex 编排工作流。共同判断是，下一代软件价值不只是保存信息，而是让上下文、权限、工具和动作形成可组合的执行系统。",
        "从软件协议到 USB 摄像头，Peter Steinberger 的实践说明现实世界 Agent 的突破点往往很具体：先把设备能力封装为可靠工具，再逐步建立感知与操作闭环。与此同时，Thibault 对 usage 问题的持续修复提醒我们，AI 产品的可信度最终来自可观察、可修复、能被用户感知的运营质量。"
    ],
    "filteredNote": "过滤掉了 8 条低信号内容，包括纯生活分享、离题内容、缺乏上下文的一句话评论、诗性表达和单纯课程推广。"
}
data["highSignalItems"] = cards

for path in (archive_path, ROOT / "data" / "latest.json"):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

digests_path = ROOT / "data" / "digests.json"
with digests_path.open(encoding="utf-8") as f:
    digests = json.load(f)
digests = [d for d in digests if d.get("date") != DATE]
digests.insert(0, data)
with digests_path.open("w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(json.dumps({"date": DATE, "highSignalItems": len(cards), "filtered": 8, "files": 3}, ensure_ascii=False))
