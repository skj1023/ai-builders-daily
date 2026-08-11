import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-11"
archive_path = ROOT / "data" / "archive" / f"{DATE}.json"
with archive_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

items = [
    {
        "type": "blog", "typeLabel": "深度文章", "date": "8月11日 · 周二",
        "actor": "Anthropic Engineering", "meta": "Claude · Engineering Blog",
        "title": "从产品权限到纵深防御：Claude 的跨产品安全边界",
        "summary": "Anthropic 讨论如何在不同产品中约束 Claude：随着模型获得更强的工具调用和执行权限，安全边界不能只依赖单一提示词或单个沙箱。文章把权限控制、隔离、监测与产品级限制放进同一套纵深防御体系，反映出 Agent 产品的核心工程问题已从‘能不能完成任务’转向‘能否在可控边界内持续完成任务’。",
        "keyPoints": ["Agent 的权限设计必须按产品场景拆分，而不是一套规则覆盖全部入口", "单一隔离层不足以应对强模型，权限、执行环境和监控需要组合防御", "产品能力越强，安全控制越应成为默认架构而非上线后的补丁"],
        "whyItMatters": "这是构建可部署 Agent 时最容易被低估的基础设施问题：能力增长会同步扩大失误半径。",
        "tags": ["Agent", "安全", "工程"], "qualityScore": 95,
        "url": "https://www.anthropic.com/engineering/how-we-contain-claude"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月10日 · 周一",
        "actor": "Guillermo Rauch", "meta": "Vercel · X 动态",
        "title": "安全审查正在变成软件工厂里的 Agent 原语",
        "summary": "Guillermo Rauch 说，Vercel 内部已经把一项网络安全工具的名字动词化，用‘deepsec’来指代对代码进行安全审查，并将其视为软件工厂的必备环节。这个变化说明 Agent 不只是写代码，还会逐渐承担持续性的安全验证；安全检查若能嵌入开发流程，价值就从一次性审计变成每次变更都自动触发的生产能力。",
        "keyPoints": ["安全审查可以成为代码生成流程中的标准动作", "内部术语动词化通常意味着工具已经进入真实工作流", "Agent 软件工厂需要同时覆盖代码质量和安全质量"],
        "whyItMatters": "对 AI Builder 而言，‘生成后再检查’正在变成默认范式，安全 Agent 会和测试、部署一样成为流水线组件。",
        "tags": ["Agent", "安全", "开发工具"], "qualityScore": 91,
        "url": "https://x.com/rauchg/status/2086965425968148806"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月10日 · 周一",
        "actor": "Guillermo Rauch", "meta": "Vercel Sandbox · X 动态",
        "title": "Agent 沙箱不能只隔离计算，还必须隔离网络",
        "summary": "Guillermo Rauch 强调，Vercel Sandbox 同时隔离计算环境和网络；仅依赖容器隔离不足以应对 frontier models，网络路径本身也可能成为逃逸或数据外传的入口。对可执行 Agent 来说，沙箱的安全模型因此必须从‘限制进程’扩展到‘限制它能接触什么’。",
        "keyPoints": ["计算隔离与网络隔离是两个独立的安全维度", "强模型场景下，容器本身不能被视为完整边界", "默认限制 egress 能降低依赖下载、数据外传和供应链风险"],
        "whyItMatters": "任何让模型执行代码、访问依赖或调用外部服务的产品，都需要把网络权限当作一等配置。",
        "tags": ["Agent", "沙箱", "网络安全"], "qualityScore": 94,
        "url": "https://x.com/rauchg/status/2086946535716393209"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月10日 · 周一",
        "actor": "Aaron Levie", "meta": "Box · X 动态",
        "title": "Frontier 能力开始以 open weights 进入企业部署",
        "summary": "Aaron Levie 认为，Meta 将 Muse Spark 1.2 以 open weights 发布意义重大：具备 frontier-class 能力的模型不再只能通过封闭 API 使用。开放权重会扩大可私有化部署、云上自托管和针对特定任务继续训练的空间，也会进一步压低 intelligence 的单位成本。",
        "keyPoints": ["open weights 为 on-prem 和私有云部署打开空间", "企业可以围绕具体业务继续训练或改造模型", "模型可获得性提升会把竞争推向部署、数据和工作流整合"],
        "whyItMatters": "模型能力与部署控制权同时下沉，会显著改变企业采用 AI 的成本结构和供应商依赖。",
        "tags": ["模型", "open weights", "企业 AI"], "qualityScore": 92,
        "url": "https://x.com/levie/status/2086802472950239618"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月11日 · 周二",
        "actor": "Claude", "meta": "Anthropic · X 动态",
        "title": "Sonnet 5 的低价不再是发布期补贴，而是新基准",
        "summary": "Anthropic 宣布 Claude Sonnet 5 的 introductory pricing 永久保持不变：每百万 input tokens 2 美元、output tokens 10 美元。把发布期价格固定下来，意味着模型服务商正在用更激进的价格锚定扩大使用量，AI 产品的毛利和模型路由策略需要按长期价格而不是短期优惠重新设计。",
        "keyPoints": ["Sonnet 5 的 2/10 美元每百万 tokens 价格永久有效", "模型价格竞争从短期促销转向长期成本基线", "下游产品应重新评估调用频率、缓存和模型分层策略"],
        "whyItMatters": "价格是 AI 产品架构的一部分；永久降价会直接改变哪些工作流值得自动化。",
        "tags": ["模型定价", "产品", "市场"], "qualityScore": 90,
        "url": "https://x.com/claudeai/status/2086891169217122586"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月10日 · 周一",
        "actor": "Peter Yang", "meta": "Linear · X 动态",
        "title": "生产级 Agent 的第一步不是选模型，而是画出真实工作流",
        "summary": "Peter Yang 总结 Linear 团队构建 production agent 的方法：先梳理工作从哪里开始、上下文存在哪些系统、什么动作代表完成，以及哪些节点需要人审。这个顺序把 Agent 从聊天界面拉回业务流程，重点不在展示模型能力，而在定义可验证的任务边界和交接点。",
        "keyPoints": ["先映射实际工作流，再决定 Agent 的职责", "上下文来源、完成标准和人工审核点必须显式化", "生产 Agent 的质量取决于系统连接和流程闭环，而非单次回答"],
        "whyItMatters": "这是把 prototype 变成 production 的通用起点，尤其适合企业内部自动化项目。",
        "tags": ["Agent", "产品设计", "工作流"], "qualityScore": 93,
        "url": "https://x.com/petergyang/status/2086824976800436676"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月10日 · 周一",
        "actor": "Matt Turck", "meta": "Data Driven NYC · X 动态",
        "title": "Agent 的瓶颈仍然是数据，而不是聊天界面",
        "summary": "Matt Turck 用一句跨周期对照指出：从 Big Data 到 modern data stack，再到 Gen AI 和 agentic AI，团队往往先说模型、dashboard 或 chatbot 很好，最后发现问题在底层数据。Agent 能否可靠执行，取决于上下文是否完整、结构是否稳定、权限是否清晰，以及结果是否能回写系统。",
        "keyPoints": ["不同 AI 周期反复暴露同一个底层数据问题", "Agent 需要可访问、可解释、可回写的业务上下文", "数据治理和系统整合会比 UI 创新更决定生产效果"],
        "whyItMatters": "它提醒 Builder 不要把 Agent 失败简单归因于模型能力，先检查数据和工作流基础设施。",
        "tags": ["Agent", "数据", "基础设施"], "qualityScore": 89,
        "url": "https://x.com/mattturck/status/2086882606638153882"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月10日 · 周一",
        "actor": "Zara Zhang", "meta": "Codex · X 动态",
        "title": "用反向拆解把优秀设计变成 Agent 可学习的样本",
        "summary": "Zara Zhang 建议把一个设计优秀的网站交给 Codex：先让它分析设计为什么成立，再让它截取完整页面并在图像上加注释。这个方法把抽象的审美判断转成带有视觉证据和解释的训练材料，说明多模态 Agent 可以同时承担观察、归因和复现前的知识整理。",
        "keyPoints": ["从真实优秀案例学习，通常比只读设计理论更直接", "截图加标注能把视觉判断转成可讨论的结构化样本", "Agent 的价值不仅是生成，也包括把隐性知识显性化"],
        "whyItMatters": "对于做 AI 产品和界面的团队，这是一种低成本建立 design critique loop 的方法。",
        "tags": ["产品", "设计", "Codex"], "qualityScore": 88,
        "url": "https://x.com/zarazhangrui/status/2086758509979316423"
    },
    {
        "type": "podcast", "typeLabel": "播客摘录", "date": "7月31日 · 周五",
        "actor": "No Priors", "meta": "No Priors Podcast · Melisa Tokmak",
        "title": "现实服务业的自治化，关键是把 Agent 嵌入运营系统",
        "summary": "本期围绕 Netic 创始人 Melisa Tokmak 构建 autonomous enterprise for real-world services 展开，核心问题不是让模型在演示中完成一项任务，而是让 Agent 进入真实服务业的连续运营。可持续的自治需要把模型能力与现场流程、责任边界和业务系统结合起来，最终交付的是可重复的服务结果，而不是一次漂亮的 demo。",
        "keyPoints": ["现实世界服务的 Agent 必须处理连续流程和例外情况", "自治企业需要把模型、运营流程与责任机制一起设计", "衡量标准应从单次任务成功率转向长期服务质量和成本"],
        "whyItMatters": "它把 Agent 讨论从软件界面带到真实产业，适合思考 AI 如何承接有物理和组织约束的业务。",
        "tags": ["Agent", "企业自动化", "服务业"], "qualityScore": 86,
        "url": "https://www.youtube.com/@NoPriorsPodcast"
    }
]

data["dailyInsight"] = {
    "paragraphs": [
        "今天最清晰的主线是：Agent 正从‘会不会做’进入‘能不能被安全地放进生产系统’。Anthropic 的跨产品 containment 文章，以及 Guillermo Rauch 对 Vercel Sandbox 的补充，都把权限、计算隔离和网络 egress 放到同一张架构图里；强模型时代，安全边界不能只靠 prompt 或容器的单点承诺。",
        "第二条信号来自成本和供给侧。Claude Sonnet 5 将发布期价格永久固定，Meta 的 Muse Spark 1.2 则以 open weights 进入更广泛部署场景：模型能力越来越像基础设施，竞争会从‘谁能调用模型’转向‘谁能把模型以更低成本、更强控制力嵌入具体工作流’。",
        "产品方法论也在收敛。Linear 的 production agent 经验强调先画真实工作流，Matt Turck 则指出每一轮 AI 浪潮最终都会回到底层数据；两者共同说明，Agent 项目的第一性原理不是换一个更强模型，而是明确上下文在哪里、完成如何定义、哪些地方需要人审，以及结果如何回写系统。",
        "最后，Zara Zhang 的设计拆解方法和 No Priors 对现实服务自治化的讨论，分别展示了 Agent 的两种扩展方向：把隐性知识转成可学习样本，以及把模型嵌入连续的现实运营。前者提升个人和团队的认知杠杆，后者考验系统、流程与责任设计，都是比聊天 demo 更值得长期跟踪的建设方向。"
    ],
    "filteredNote": "过滤掉了纯离职感言、日常生活、玩笑、无上下文转发、单句评论和非 AI 话题等低信号内容"
}
data["highSignalItems"] = items

for path in [archive_path, ROOT / "data" / "latest.json"]:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

digests_path = ROOT / "data" / "digests.json"
with digests_path.open("r", encoding="utf-8") as f:
    digests = json.load(f)
if isinstance(digests, list):
    digests = [d for d in digests if d.get("date") != DATE]
    digests.insert(0, data)
else:
    raise TypeError("digests.json must contain a list")
with digests_path.open("w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(json.dumps({"date": DATE, "highSignalItems": len(items), "files": [str(archive_path), str(ROOT / 'data' / 'latest.json'), str(digests_path)]}, ensure_ascii=False))
