import json
from pathlib import Path

root = Path(r"C:/Users/PC/Documents/ai-builders-daily")
date = "2026-07-03"
archive_path = root / "data" / "archive" / f"{date}.json"
latest_path = root / "data" / "latest.json"
digests_path = root / "data" / "digests.json"

with archive_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

items = [
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Claude / Anthropic",
        "meta": "Claude 官方 · X 动态",
        "title": "Fable 5 限时回归：强模型正在变成受控资源",
        "summary": "Claude 宣布付费套餐用户可在 7 月 7 日前访问 Fable 5，但最多只能使用到每周额度的 50%，之后需切换到其他模型，也可继续通过 usage credits 使用。它不是一次普通的模型开放，而是把高能力模型当作稀缺、需要分层调度的资源来管理。对 AI Builders 来说，这意味着产品体验、成本控制和模型路由会更深地绑定在一起。",
        "keyPoints": ["Fable 5 对含用量的付费计划限时开放至 7 月 7 日", "使用上限为每周用量额度的 50%，之后需切换模型或使用 credits", "高能力模型的可用性开始被额度、风险和成本共同约束", "模型产品不再只是能力发布，也是在设计供给策略"],
        "whyItMatters": "这为 AI 产品提供了一个现实信号：顶级模型能力可能长期处于“可访问但受控”的状态，Builders 需要提前设计降级路径、模型路由和用户预期管理。",
        "tags": ["产品", "模型", "商业化"],
        "qualityScore": 90,
        "url": "https://x.com/claudeai/status/2072402639644766602"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月2日 · 周四",
        "actor": "Aaron Levie",
        "meta": "Box CEO · X 动态",
        "title": "Agentic MapReduce：推理需求的下一次放大器",
        "summary": "Aaron Levie 用 Devin 的 agentic mapreduce 作为例子解释为什么未来 AI 推理需求可能需要 100 倍增长：不再是单个 Agent 处理一个请求，而是一群 Agent 并行处理大量数据或代码。这个范式把传统分布式计算的 map/reduce 思路迁移到 Agent 系统中，任务被拆分、分发、汇总，推理调用自然呈指数级放大。",
        "keyPoints": ["Agentic mapreduce 让多个 Agent 并行处理大规模代码或数据", "推理需求增长来自工作流结构变化，而不只是用户数增长", "Agent swarm 会把一次任务拆成大量模型调用", "基础设施瓶颈会从单次响应延迟转向吞吐、调度和成本控制"],
        "whyItMatters": "如果 Agent 工作流走向并行化，AI Builders 的架构重点会从“调用一个模型”转向“管理一群模型工人”：队列、缓存、预算、评测和失败恢复都变成一等公民。",
        "tags": ["Agent", "工程", "基础设施"],
        "qualityScore": 88,
        "url": "https://x.com/levie/status/2072519377371459836"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Guillermo Rauch",
        "meta": "Vercel CEO · X 动态",
        "title": "Agentic 部署需要 dry-run：让 Agent 先检查再推送",
        "summary": "Guillermo Rauch 指出，Agent 在推送前天然会运行 node --check、tsc --noEmit、next build 等自检步骤；Vercel 因此推出面向 agentic deployments 的 dry-run step，以降低成本和风险。这个改动把人类开发者熟悉的 CI 前置检查，产品化为 Agent 工作流中的默认安全阀。",
        "keyPoints": ["Agent 会主动在推送前运行类型检查、构建检查和其他验证命令", "Vercel 将 dry-run 加入部署流程以减少错误部署和无效成本", "Agentic 部署需要“先模拟、再执行”的产品护栏", "平台正在为自动化开发者而非只为人类开发者重新设计流程"],
        "whyItMatters": "AI Builders 在接入 coding agent 时，不能只关注生成能力，还要设计验证层。dry-run、预检和回滚会成为 Agent 产品可靠性的基础设施。",
        "tags": ["Agent", "工程", "部署"],
        "qualityScore": 86,
        "url": "https://x.com/rauchg/status/2072398926175404250"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Guillermo Rauch",
        "meta": "Vercel CEO · X 动态",
        "title": "单个 Dockerfile 跑 WordPress：云平台继续吸收传统运维复杂度",
        "summary": "Rauch 展示了用单个 Dockerfile.vercel 在 Vercel Fluid 上运行 WordPress，配合 PlanetScale MySQL，并把包含 docker build 的云端部署压到约 30 秒。它说明现代云平台正在把历史包袱很重的应用形态也纳入统一部署体验，而不仅服务新式前端项目。",
        "keyPoints": ["WordPress 可通过单个 Dockerfile.vercel 部署到 Vercel Fluid", "数据库层使用 PlanetScale MySQL，部署流程约 30 秒", "Docker build 被放入云端部署路径，降低本地环境依赖", "传统应用也能进入更快、更声明式的平台工作流"],
        "whyItMatters": "很多 AI 产品最终要接入旧系统和内容基础设施。平台若能吸收传统应用复杂度，AI Builders 就能把更多精力放在智能层，而非遗留运维。",
        "tags": ["工程", "云平台", "部署"],
        "qualityScore": 80,
        "url": "https://x.com/rauchg/status/2072463293654942090"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Amjad Masad",
        "meta": "Replit CEO · X 动态",
        "title": "从“能做出来”到“能卖出去”：AI 编程平台开始补商业闭环",
        "summary": "Amjad Masad 说，当构建软件变得容易后，Replit 正更关注帮创业者进入市场、拿到第一个客户和第一美元，并宣布 Replit apps 可以在 Whop 上销售。这里的核心不是又多一个分发渠道，而是 AI 编程工具正从生产力工具走向创业操作系统。",
        "keyPoints": ["Replit 将重点从“帮助构建”延展到“帮助变现”", "Replit apps 现在可以通过 Whop 销售", "AI 降低构建门槛后，市场进入和支付转化成为新瓶颈", "开发平台正在补齐从 idea 到 revenue 的路径"],
        "whyItMatters": "AI Builders 的竞争不再只在生成代码速度，而在能否把用户从原型带到收入。分发、支付、模板和市场教育会成为产品护城河的一部分。",
        "tags": ["产品", "市场", "商业化"],
        "qualityScore": 84,
        "url": "https://x.com/amasad/status/2072385092824260748"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Nikunj Kothari",
        "meta": "FPV Ventures Partner · X 动态",
        "title": "OpenAI 与 Anthropic 的人才漩涡正在改写创业生态",
        "summary": "Nikunj Kothari 观察到，过去两个月里有多位朋友从非常成熟的职位离开，加入 OpenAI 或 Anthropic。他认为吸引力来自两点叠加：参与建设最重要公司的使命感，以及 pre-IPO 阶段仍可能带来的流动性。这意味着顶级人才市场会继续向前沿实验室集中，创业公司和大厂都要面对更贵、更稀缺的人才供给。",
        "keyPoints": ["OpenAI 与 Anthropic 正从成熟公司吸走高质量人才", "使命感与 pre-IPO 流动性共同形成强吸引力", "前沿实验室的人才优势可能进一步强化模型领先", "其他 AI 公司需要重新设计招聘叙事和激励结构"],
        "whyItMatters": "模型竞争不仅是算力和数据竞争，也是人才资本竞争。AI Builders 在组队时需要面对一个现实：最强候选人可能正在被实验室级别的叙事和权益包围。",
        "tags": ["组织", "人才", "市场"],
        "qualityScore": 82,
        "url": "https://x.com/nikunj/status/2072344802570756121"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Claude / Anthropic",
        "meta": "Claude Code · X 动态",
        "title": "误报反馈进入产品闭环：安全分类器也需要运营机制",
        "summary": "Claude 提醒用户，如果 Claude Code 请求被错误标记，可以通过 /feedback 提交报告；在其他产品中也可用 thumbs 按钮反馈。这说明安全分类器不是一次性规则，而是持续调优的产品系统，需要把误报样本从用户侧重新纳入训练和校准循环。",
        "keyPoints": ["Claude Code 用户可用 /feedback 报告误报", "Claude 与 Cowork 也通过 thumbs 收集反馈", "反馈会用于调优分类器、减少 false positives", "安全产品化需要明确的申诉和样本回流通道"],
        "whyItMatters": "任何有权限、代码或敏感能力的 AI 产品都会遇到误报问题。Builders 需要把“反馈—标注—调优—解释”做成系统，而不是只写一套安全规则。",
        "tags": ["安全", "产品", "工程"],
        "qualityScore": 79,
        "url": "https://x.com/claudeai/status/2072402640907162072"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月1日 · 周三",
        "actor": "Zara Zhang",
        "meta": "Builder · X 动态",
        "title": "Skill 不是起点，而是工作流成熟后的封装",
        "summary": "Zara Zhang 给出一个很实用的 Agent 构建原则：不要从写 skill 开始，而要以 skill 结束；skill 是工作流被验证后的最后一步，而不是第一步。换句话说，先跑通真实任务、沉淀步骤和边界，再把可复用部分封装成工具能力。",
        "keyPoints": ["不要先抽象 skill，再寻找使用场景", "先通过真实工作流验证任务结构和边界条件", "skill 应是可复用流程的产品化结果", "过早封装会放大错误抽象和维护成本"],
        "whyItMatters": "对做 Agent 工具链的 AI Builders 来说，这是一条反过度工程的原则：先观察工作，再固化能力。",
        "tags": ["Agent", "工程", "方法论"],
        "qualityScore": 78,
        "url": "https://x.com/zarazhangrui/status/2072381929366987087"
    },
    {
        "type": "podcast",
        "typeLabel": "播客摘录",
        "date": "7月1日 · 周三",
        "actor": "AI & I by Every",
        "meta": "Every · Podcast / YouTube",
        "title": "Every 咨询团队的 AI 工作流：从教学到交付的可复制系统",
        "summary": "这一期围绕 Every 咨询团队如何把 AI 工作流带进企业：核心不是向高管演示几个提示词，而是把 AI 嵌入真实业务流程、培训团队形成可持续使用习惯，并把咨询经验反哺为可复用方法论。它反映了 AI 服务市场的一个变化：客户买的不是“会用 AI 的人”，而是能迁移到组织内部的流程设计。",
        "keyPoints": ["企业 AI 咨询的价值从工具教学转向工作流改造", "高管和团队都需要理解 AI 如何嵌入日常决策与执行", "可复制的方法论比一次性 prompt demo 更重要", "咨询团队的交付经验可以沉淀为产品、模板和训练体系"],
        "whyItMatters": "很多 AI Builders 会以服务、咨询或内部 enablement 进入企业市场。这期的信号是：真正可规模化的交付，来自流程迁移能力，而不是单点模型能力。",
        "tags": ["产品", "组织", "Agent"],
        "qualityScore": 77,
        "url": "https://www.youtube.com/playlist?list=PLuMcoKK9mKgHtW_o9h5sGO2vXrffKHwJL"
    }
]

insight = {
    "paragraphs": [
        "今天的主线不是某个模型单点能力爆炸，而是“高能力 AI 如何被产品化地控制”。Fable 5 限时回归且设置每周额度 50% 的使用上限，说明前沿模型正在从“能力发布”进入“供给管理”：安全、成本、容量和用户体验会一起决定模型是否可用。对 AI Builders 来说，默认永远能调用最强模型已经不是稳健假设，模型路由、降级路径和额度叙事都要成为产品设计的一部分。",
        "Agent 工程的信号更清晰：系统正在从单 Agent 请求变成并行、可验证、可回滚的任务网络。Aaron Levie 提到 Devin 的 agentic mapreduce，指向未来一项工作会被拆给一群 Agent 并行处理；Guillermo Rauch 则从部署侧补上 dry-run，让 Agent 在真正推送前先自检。一个负责放大吞吐，一个负责控制风险，合起来就是 Agent 基础设施的下一阶段：调度、验证和成本预算会比 prompt 本身更重要。",
        "平台层也在补齐从构建到交付的闭环。Vercel 展示用单个 Dockerfile 跑 WordPress，继续把传统运维复杂度吸进云平台；Replit 则通过 Whop 把“写出 app”延伸到“卖出 app”。当 AI 让构建成本下降，新的瓶颈会自然转向部署、分发、支付、获客和信任，这些看起来不如模型酷，但更接近真实收入。",
        "组织与市场层面，前沿实验室的人才吸力仍在增强。Nikunj Kothari 提到 OpenAI 与 Anthropic 正从成熟职位中吸走高质量人才，背后是使命叙事和 pre-IPO 流动性的叠加。与此同时，Claude Code 把误报反馈显式接入 /feedback，也提醒我们：有能力的 AI 产品必须同时建设运营机制，尤其是安全分类器、申诉通道和持续调优循环。",
        "今天过滤掉的大量高互动内容其实很能说明问题：社区对 Fable 回归、Anthropic 招人、会议现场很兴奋，但真正值得 Builders 留下的是可迁移判断——强模型会受控开放，Agent 会并行化，部署会前置验证，AI 编程平台会向商业闭环延伸。热闹是信号源，不是结论。"
    ],
    "filteredNote": "过滤掉了 Garry Tan 的短句转述、Thariq 的 one-liner、Dan Shipper 的兴奋表达、Peter Steinberger 找场地 / 感叹、Matt Turck 的非 AI IPO 评论、Nikunj 的体育内容、空文本和纯链接等低信号内容；最终保留 9 条具备事实增量、工程/产品 insight 或长期判断价值的内容。"
}

data["headline"] = "今天的信息流集中在 Fable 5 受控回归、Agentic MapReduce、agentic 部署 dry-run、AI 编程平台商业闭环与前沿实验室人才竞争：已筛选出 9 条高信号内容。"
data["editorNote"] = "本页只保留有事实增量、观点密度、工程/产品 insight 或长期判断价值的 AI Builders 内容；低信号日常、吐槽、meme、无上下文短评、纯转发和非 AI 主题会被过滤。"
data["dailyInsight"] = insight
data["highSignalItems"] = items
data["toplines"] = [{"title": f"{i['actor']} · {i['title']}", "source": i["meta"], "url": i["url"], "sourceDate": "2026-07-02" if "7月2日" in i["date"] else "2026-07-01", "sourceDisplayDate": i["date"], "summary": i["summary"], "chineseTitle": i["title"], "tags": i["tags"], "score": i["qualityScore"]} for i in items[:5]]

for path in (archive_path, latest_path):
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

with digests_path.open("r", encoding="utf-8") as f:
    digests = json.load(f)
digests = [d for d in digests if d.get("date") != date]
digests.insert(0, data)
with digests_path.open("w", encoding="utf-8", newline="\n") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"curated {date}: {len(items)} highSignalItems")
