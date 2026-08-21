import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
date = "2026-08-22"
archive_path = root / "data" / "archive" / f"{date}.json"
with archive_path.open(encoding="utf-8") as f:
    data = json.load(f)

insight = {
    "paragraphs": [
        "今天最强的信号是：AI 产品正在从“模型会不会回答”进入“能不能在真实约束下持续交付”。Anthropic 一侧同时推进 Claude Code 的质量复盘、企业级自托管 Agent 与 MCP 隧道，OpenAI 一侧则回应 Codex 使用额度被滥用的问题；产品能力和治理边界正在一起设计，而不是先上线、再补安全。",
        "企业 Agent 的基础设施正在拆成两个清晰层次：由模型负责推理的“脑”，与由沙箱、权限、数据驻留和工具连接组成的“手”。Managed Agents、Fable safeguards 以及 Mythos-class 模型的隐私合规设计都指向同一个判断：企业愿意采用 Agent 的前提，不是模型更聪明，而是组织能控制数据、执行环境和责任边界。",
        "工程方法上，Madhu Guru 对分层评测策略的总结很实用：不能用一个总分覆盖所有场景，而要针对独特工作流，在成本、真实性和迭代速度之间布置多级 eval。Aaron Levie 进一步指出，贴近企业底层流程的团队会用 post-training 把成本和准确率优化到具体任务上，未来的差异化将更多来自领域数据与流程理解。",
        "产品体验的另一条线是缩短从意图到可运行结果的距离：GPT-Image-2 已把透明图像能力同时带到 ChatGPT 和 API，ChatGPT Sites 让多人共同搭建小型产品，Replit 的 Free Mode 则强调交互速度。单个功能并不等于长期壁垒，但它们共同说明，AI Builder 的竞争焦点正在转向更短的反馈回路与更低的协作摩擦。"
    ],
    "filteredNote": "过滤掉了纯生活动态、情绪表达、无上下文短句、单纯宣传与转发、功能展示但缺乏工程含义的内容，以及无法还原核心论点的播客片段等低信号内容。"
}

def item(type_, type_label, date_text, actor, meta, title, summary, points, why, tags, score, url):
    return {
        "type": type_, "typeLabel": type_label, "date": date_text, "actor": actor,
        "meta": meta, "title": title, "summary": summary, "keyPoints": points,
        "whyItMatters": why, "tags": tags, "qualityScore": score, "url": url
    }

items = [
    item("post", "观点动态", "8月21日 · 周五", "Thibault Sottiaux", "Codex · X 动态", "订阅额度的公平使用需要透明的滥用边界", "Thibault Sottiaux 表示，团队调查了 Codex 使用额度差异的反馈，发现部分受影响用户在用 sub2api 把订阅额度转换成 API 流量再转售或共享。这个案例说明，AI 产品的额度设计不能只看单个用户体验，还要把转售、代理调用和社区沟通纳入系统治理。", ["调查发现部分额度异常与 sub2api 转换订阅流量有关", "额度调整需要与社区沟通并保持透明", "订阅产品与 API 产品之间的套利会持续制造治理压力"], "对做 AI SaaS 的团队而言，额度、身份和调用链路本身就是产品安全面。", ["产品", "工程", "治理"], 94, "https://x.com/thsottiaux/status/2090675027670978569"),
    item("post", "观点动态", "8月20日 · 周四", "Boris Cherny", "Claude Code · X 动态", "企业级模型的核心卖点转向数据主权", "Boris Cherny 透露，Anthropic 正为 Mythos-class models 增加额外安全措施，并让企业客户拥有和控制自己的数据，Anthropic 不保留这些数据。产品预计秋季推出，重点不是单纯提高模型能力，而是让高敏感场景获得可部署的合规边界。", ["高能力模型需要额外安全措施", "企业客户可控制自己的数据", "供应商不保留客户数据是采用门槛的一部分"], "这给企业 AI Builder 一个清晰信号：数据主权会与模型质量一样成为采购决策。", ["研究", "市场", "安全"], 92, "https://x.com/bcherny/status/2090537902912815536"),
    item("post", "观点动态", "8月21日 · 周五", "Madhu Guru", "AI 评测 · X 动态", "评测体系必须匹配具体工作流", "Madhu Guru 认为，企业难以构建可靠 AI 系统，常见根因不是缺少模型，而是没有 eval strategy。她建议围绕独特用例搭建分层评测，在成本与真实性的连续谱上组合多种 eval，而不是用单一基准分数做决策。", ["先为独特用例定义评测策略", "用多级 eval 覆盖不同成本和真实性要求", "评测应服务迭代与上线决策，而非只做展示"], "这是把“模型效果好不好”转成可执行工程流程的实用框架。", ["工程", "研究", "组织"], 91, "https://x.com/realmadhuguru/status/2090595384905113939"),
    item("post", "观点动态", "8月20日 · 周四", "Thariq", "Claude Code · X 动态", "企业 Agent 的安全控制应部署在客户自己的基础设施", "Thariq 介绍了新的 Fable safeguards：企业可以在自己的基础设施上运行，从而控制数据存放位置和访问者。该能力已与约 100 家公司共同开发，预计秋季扩大推出，说明企业 Agent 的部署环境正从厂商托管走向可控、可审计的执行层。", ["安全防护运行在企业自有基础设施", "控制数据驻留位置与访问权限", "与约 100 家公司共建后再扩大推广"], "Agent 一旦进入企业工作流，部署权和审计权会成为基础产品能力。", ["产品", "工程", "Agent"], 91, "https://x.com/trq212/status/2090569474139439335"),
    item("post", "观点动态", "8月21日 · 周五", "Aaron Levie", "Applied AI · X 动态", "领域理解会把 post-training 变成应用层护城河", "Aaron Levie 认为，针对应用 AI 场景的 post-training 可以降低成本并提升特定任务准确率；越接近企业底层工作流的公司，越有动力采用这条路线。价值因此不只在通用模型，而在于对领域、数据和任务反馈的持续理解。", ["post-training 可针对具体任务优化成本与准确率", "贴近企业工作流的公司拥有更强优化条件", "领域知识和反馈数据会形成应用层差异化"], "它把模型训练竞争连接到了真正的业务流程，而不是停留在通用 benchmark。", ["Agent", "研究", "组织"], 89, "https://x.com/levie/status/2090664811185205722"),
    item("post", "观点动态", "8月20日 · 周四", "Peter Yang", "Agent 工作流 · X 动态", "用管理 Agent 形成可迭代的输出审查环", "Peter Yang 提出，一个 manager agent 可以通过追问“这是最好的结果吗”“再仔细检查一次”等方式，驱动 worker agent 反复改进输出。虽然提示词本身很简单，但核心思路是把一次性生成改造成带审查、反馈和重试的工作流。", ["把 worker agent 与 manager agent 分工", "通过批评和重试提高输出质量", "质量提升来自流程闭环而非单次提示词魔法"], "这是构建 Agent 系统时最低成本、可快速验证的质量控制原语。", ["Agent", "工程", "产品"], 86, "https://x.com/petergyang/status/2090564541499498919"),
    item("blog", "深度文章", "8月22日 · 周六", "Anthropic Engineering", "Claude Code · 工程文章", "Claude Code 质量问题的复盘应落到可观测性", "Anthropic Engineering 更新了对近期 Claude Code 质量反馈的调查进展。文章的价值在于把用户感知到的“变差”转为可定位的质量问题：模型、工具链、上下文和发布变化必须被拆开观测，才能避免用单一主观印象做回滚或升级判断。", ["从用户报告反推可复现的质量指标", "区分模型变化与工具链、上下文变化", "质量复盘需要持续观测而不是一次性解释"], "所有做 AI coding 或 Agent 产品的团队都需要类似的质量回归机制。", ["产品", "Agent", "工程"], 90, "https://www.anthropic.com/engineering/april-23-postmortem"),
    item("blog", "深度文章", "8月22日 · 周六", "Anthropic Engineering", "Managed Agents · 工程文章", "把 Agent 的“脑”和“手”解耦，才能规模化管理", "Scaling Managed Agents 的核心是将负责推理的模型与执行动作的基础设施分离。这样可以独立管理沙箱、工具、权限、数据和运行生命周期，让 Agent 更容易迁移到不同环境，也让企业获得更清晰的控制面。", ["推理层与执行层解耦", "执行环境承载沙箱、工具和权限控制", "解耦有利于跨环境部署与生命周期管理"], "这是从聊天机器人走向可运营 Agent 平台时必须面对的架构分层。", ["Agent", "工程", "产品"], 93, "https://www.anthropic.com/engineering/managed-agents"),
    item("blog", "深度文章", "5月19日 · 周二", "Claude Blog", "Managed Agents · 产品文章", "自托管沙箱和 MCP 隧道把私有系统接入 Agent", "Claude Managed Agents 新增客户控制的 self-hosted sandboxes，以及连接私有 MCP servers 的 tunnels。它把 Agent 的执行环境和企业内部工具从厂商网络边界中解放出来，同时保留统一的模型调用与工具协议。", ["沙箱可以部署在客户控制的环境", "MCP tunnels 连接私有内部服务", "执行位置与工具访问边界可由企业管理"], "私有数据接入和可控执行环境，是 Agent 从 demo 进入生产的关键拼图。", ["Agent", "工程", "安全"], 92, "https://claude.com/blog/claude-managed-agents-updates"),
    item("podcast", "播客摘录", "8月20日 · 周四", "No Priors · Max Hodak", "No Priors · 播客摘录", "从修复视觉到重构神经接口：生物系统也可被工程化", "Max Hodak 在 No Priors 中把大脑视为一种计算系统，并从恢复视力谈到重新设计神经接口。核心判断不是简单地把 AI 套到医疗，而是通过理解神经编码、感知回路和硬件接口，把“治疗受损功能”逐步推进到“扩展或重构功能”。", ["神经系统可以用计算与工程视角拆解", "视觉恢复依赖模型、信号编码和硬件接口协同", "长期方向从治疗走向神经功能重构"], "它为 AI Builder 提供了跨模型、硬件与生物系统协同的长期技术视角。", ["研究", "工程", "产品"], 84, "https://www.youtube.com/watch?v=7HXqMepjvy8")
]

data["dailyInsight"] = insight
data["highSignalItems"] = items
# Keep the raw feed fields for traceability, while replacing the old low-signal editorial toplines.
data["toplines"] = [{
    "title": x["title"], "source": f'{x["actor"]} · {x["meta"]}', "url": x["url"],
    "sourceDate": date, "sourceDisplayDate": x["date"], "summary": x["summary"],
    "chineseTitle": x["title"], "tags": x["tags"], "score": x["qualityScore"]
} for x in items[:5]]

for path in [archive_path, root / "data" / "latest.json"]:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

digests_path = root / "data" / "digests.json"
with digests_path.open(encoding="utf-8") as f:
    digests = json.load(f)
digests = [d for d in digests if d.get("date") != date]
digests.insert(0, data)
with digests_path.open("w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(json.dumps({"date": date, "highSignalItems": len(items), "files": [str(archive_path), str(root / 'data/latest.json'), str(digests_path)]}, ensure_ascii=False))
