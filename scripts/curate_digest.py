import json
from pathlib import Path

base = Path(r"C:/Users/PC/Documents/ai-builders-daily/data")
date = "2026-08-20"
archive = base / "archive" / f"{date}.json"
data = json.loads(archive.read_text(encoding="utf-8"))
data["dailyInsight"] = {
    "paragraphs": [
        "今天最明确的主线是：AI 产品的竞争边界正在从模型能力外移到工作流与安全边界。Aaron Levie 观察到，模型和最终用户流程之间仍有远超预期的价值空间；Claude 已把 Gmail、Google Drive 等外部系统纳入可执行链路，产品不再只是回答问题，而是代替用户完成一段可审计的工作。",
        "Agent 的可用性首先取决于“犯错时能否收场”。Sam Altman 表示会暂停部分 frontier RL training，以补齐 alignment、security 和 monitoring 标准；Thibault Sottiaux 则复盘 Codex 对潜在破坏性操作的风险收敛。两条信息放在一起看，前沿能力越快，reset、审批、监控和回滚就越应被当作核心产品能力，而不是上线后的补丁。",
        "工程组织也在为 Agent 重写上下文层：Guillermo Rauch 主张把设计、市场、销售、工程和支持等公司信息放进 monorepo，让 Agent 有统一的可检索工作面；Google Labs 的 CC 则把 Agent 放进 Gmail 这样的日常入口。对 Builder 来说，真正的护城河不是再包一层聊天界面，而是把权限、上下文、状态和业务动作连成闭环。",
        "评估与商业化正在形成两条同样重要的落地路径。Madhu Guru 建议先用最高质量的方法定义“什么是好”，再沿成本曲线下探；Thariq 则指出 SaaS 可以 headless 化，让 Agent 以交互为单位调用并付费。前者解决产品是否可靠，后者解决产品如何被新型使用者消费，二者共同指向一个判断：AI 应用的单位经济和质量体系必须围绕真实任务，而不是围绕模型调用次数。"
    ],
    "filteredNote": "过滤掉了日常生活、政治争论、纯情绪表达、玩笑、转发式短句和缺少上下文的一句话动态等低信号内容。"
}

def item(kind, label, actor, meta, title, summary, points, why, tags, score, url):
    return {"type": kind, "typeLabel": label, "date": "8月20日 · 周四", "actor": actor, "meta": meta,
            "title": title, "summary": summary, "keyPoints": points, "whyItMatters": why,
            "tags": tags, "qualityScore": score, "url": url}

items = [
item("post", "观点动态", "Thibault Sottiaux", "Codex · X 动态", "Agent 的安全能力必须包含可恢复性", "Thibault Sottiaux 复盘了 Codex 针对潜在破坏性操作推出的一系列风险降低措施，背景是少量 GPT-5.6 执行了破坏性动作。重点不只是减少误操作，而是让 Agent 在真实环境里具备更清晰的边界、审批与恢复路径。", ["破坏性动作是 Agent 从演示走向生产的关键风险面", "安全措施需要持续迭代并覆盖执行过程", "reset、审批和回滚应成为产品设计的一部分"], "这是一条来自产品一线的安全工程复盘，直接回答了 Agent 如何在真实系统中被信任。", ["Agent", "工程", "安全"], 95, "https://x.com/thsottiaux/status/2089891927659585918"),
item("post", "观点动态", "Claude", "Claude · X 动态", "从聊天到可审批的跨应用执行", "Claude 现在可以在 Gmail 中回复并发送邮件，也能管理 Google Drive 文件，并允许用户控制何时需要审批。它把模型能力嵌入既有工作流，关键变化是从生成内容转向执行动作，同时保留人类控制点。", ["Gmail 与 Google Drive 成为 Agent 的真实操作面", "高风险动作保留用户审批", "连接器是跨应用工作流的基础设施"], "这是 AI 助手产品化的重要门槛：价值来自完成任务，而不是多说几句答案。", ["产品", "Agent", "工作流"], 94, "https://x.com/claudeai/status/2089806039088517356"),
item("post", "观点动态", "Sam Altman", "OpenAI · X 动态", "前沿训练速度必须服从安全与监控标准", "Sam Altman 表示，OpenAI 暂停了部分 frontier RL training，以确保新的能力水平满足 alignment、security 和 monitoring 标准；他同时强调这影响的是更远期发布，近期仍会推出新模型。信号很清楚：能力进展已经快到需要用发布节奏主动换取安全准备时间。", ["暂停部分训练是对能力加速的治理响应", "安全标准需要在训练和发布前置", "短期产品节奏与远期前沿研究被区分处理"], "它展示了模型公司如何把安全准备从口号变成训练与发布决策。", ["研究", "安全", "模型"], 93, "https://x.com/sama/status/2089787807611195475"),
item("post", "观点动态", "Madhu Guru", "Meta · X 动态", "先定义质量前沿，再优化评估成本", "Madhu Guru 建议把 evals 当作 frontier models 来管理：先用最高质量的方法确认产品是否按预期工作，写清 rubric 和“什么是好”，再逐步沿成本曲线下探。这个顺序避免团队为了省评估成本，过早把错误的质量标准自动化。", ["先建立高质量评估基准", "rubric 要先于规模化自动评估", "成本优化应发生在质量标准稳定之后"], "对 AI Builder 而言，评估不是测试收尾，而是产品定义的一部分。", ["评估", "产品", "工程"], 92, "https://x.com/realmadhuguru/status/2089918106814603728"),
item("post", "观点动态", "Thariq", "Claude Code · X 动态", "把 SaaS 变成 Agent 可调用的基础设施", "Thariq 提出一个直接的商业化方向：把现有 SaaS headless 化，让 Agent 能调用，再按交互向企业收费。这个判断的核心不是“给产品加 AI”，而是把产品能力重构为机器可消费的接口，并围绕真实业务动作建立新的计价单位。", ["headless SaaS 能成为 Agent 的工具层", "计费单位可能从席位转向交互或完成的动作", "企业场景更看重可控、可集成和可计量"], "它把 Agent 浪潮转译成了具体的产品架构与商业模式问题。", ["Agent", "SaaS", "商业化"], 91, "https://x.com/trq212/status/2089844723691479333"),
item("post", "观点动态", "Google Labs", "Google Labs · X 动态", "Agent 正从独立应用进入邮件入口", "Google Labs 扩大了 Gmail productivity agent CC 的可用范围，并开放更多地区 waitlist。把 Agent 放在 Gmail 这样的高频入口，意味着用户无需改变工作习惯，Agent 可以直接围绕邮件、上下文和后续动作形成任务流。", ["入口选择决定 Agent 的使用频率", "Gmail 提供天然的上下文与任务触发点", "地区扩展和 waitlist 是从实验走向规模化的信号"], "对 Builder 的启发是优先寻找已有工作流中的高频触点，而不是要求用户迁移到新界面。", ["产品", "Agent", "工作流"], 88, "https://x.com/GoogleLabs/status/2089812430885208361"),
item("post", "观点动态", "Guillermo Rauch", "Vercel · X 动态", "给 Agent 一个统一的公司上下文层", "Guillermo Rauch 认为 software factory 应该是 monorepo，把设计、市场、销售、工程和支持等公司上下文放在一个地方，供 Agent 构建。这里的 monorepo 不只是代码仓库，而是把组织知识变成可检索、可组合、可持续更新的工作面。", ["Agent 需要跨职能上下文才能完成端到端任务", "组织知识的结构化程度决定 Agent 上限", "monorepo 正从代码组织扩展为公司上下文容器"], "它把 Agent 工程的瓶颈从模型调用转向知识架构和上下文治理。", ["工程", "Agent", "组织"], 90, "https://x.com/rauchg/status/2089804717337817514"),
item("post", "观点动态", "Guillermo Rauch", "Vercel · X 动态", "用公开悬赏验证 Sandbox 的真实安全边界", "Vercel 将投入 100 万美元，公开验证 Vercel Sandbox 的安全性，允许使用任意模型尝试寻找 escape。这个做法把“模型能否突破护栏”从内部宣称变成可外部复现、可持续攻击的工程问题。", ["公开红队测试比静态安全声明更接近真实风险", "Sandbox 安全需要面对不同模型和攻击策略", "透明验证有助于建立 Agent 基础设施信任"], "当 Agent 拥有执行权限时，运行环境的可验证隔离是基础设施级能力。", ["安全", "工程", "研究"], 91, "https://x.com/rauchg/status/2089747453004468339"),
item("post", "观点动态", "Aaron Levie", "Box · X 动态", "模型价值之外，工作流才是更大的应用层", "Aaron Levie 认为，模型与最终用户工作流之间可创造的价值远大于许多人的预期。模型能力负责抬高上限，但真正决定产品价值的仍是把能力嵌入具体流程、权限、数据和结果交付。", ["模型只是 agentic product 的能力底座", "工作流整合创造主要增量价值", "应用层需要围绕终端结果设计"], "这是评估 AI 产品机会时很重要的校准：不要把模型能力误认为完整产品价值。", ["产品", "Agent", "工作流"], 89, "https://x.com/levie/status/2089921630650925170"),
item("blog", "深度文章", "Anthropic Engineering", "Anthropic Engineering · 深度文章", "如何在产品中约束 Claude 的执行权限", "Anthropic 讨论了如何在不同产品中 containment Claude，包括权限边界、隔离环境、监控和对高风险操作的控制。文章的核心不是让模型永不出错，而是把不可避免的不确定性包在可观测、可恢复的系统边界里。", ["模型能力必须与执行权限分层", "隔离、监控和恢复共同构成 containment", "安全架构要随模型能力和产品形态持续演化"], "这是构建 Agent 产品时最值得参考的系统安全视角，尤其适合需要接触真实数据和工具的团队。", ["Agent", "工程", "安全"], 95, "https://www.anthropic.com/engineering/how-we-contain-claude"),
item("podcast", "播客摘录", "Training Data", "Training Data · 播客摘录", "为什么 AI 模型会停止学习，以及如何重新启动", "Rich Sutton 与 Khurram Javed 讨论了 AI 模型停止学习的原因，以及如何通过新的训练机制恢复持续学习能力。核心判断是，当前模型的能力增长仍高度依赖离线训练与固定目标，而更具通用性的系统需要面对长期反馈、探索和不断变化的环境。", ["持续学习不只是增加数据量", "固定训练目标会限制模型适应新环境", "探索、反馈与长期记忆是重新启动学习的关键方向"], "它把模型研究从一次性训练拉回到长期学习系统，对 Agent 和下一代模型架构都有启发。", ["研究", "模型", "Agent"], 90, "https://www.youtube.com/watch?v=xH7U7w9Qzlo")
]
items.pop(5)  # 保留更高密度的工程、研究与产品信号，并满足每日最多 10 条
data["highSignalItems"] = items
text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
archive.write_text(text, encoding="utf-8")
(base / "latest.json").write_text(text, encoding="utf-8")
digests = base / "digests.json"
old = json.loads(digests.read_text(encoding="utf-8"))
old = [x for x in old if x.get("date") != date]
old.insert(0, data)
digests.write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"date": date, "highSignalItems": len(items), "filesUpdated": 3}, ensure_ascii=False))
