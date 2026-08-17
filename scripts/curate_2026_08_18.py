import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-18"
archive_path = ROOT / "data" / "archive" / f"{DATE}.json"
latest_path = ROOT / "data" / "latest.json"
digests_path = ROOT / "data" / "digests.json"

data = json.loads(archive_path.read_text(encoding="utf-8"))
display_date = data["displayDate"]

def card(type_, label, actor, meta, title, summary, key_points, why, tags, score, url, date=None):
    return {
        "type": type_, "typeLabel": label, "date": date or display_date,
        "actor": actor, "meta": meta, "title": title, "summary": summary,
        "keyPoints": key_points, "whyItMatters": why, "tags": tags,
        "qualityScore": score, "url": url,
    }

items = [
    card("post", "观点动态", "Thibault Sottiaux", "Codex · X 动态",
         "百万上下文不是越大越好：Agent 需要可控的记忆预算",
         "Thibault Sottiaux 公开了在 Codex 中启用 GPT-5.6 Sol 1M-token context window 的方式，同时强调默认上下文长度是经过性能与成本权衡的结果。更大的窗口能保留更多代码、工具输出和对话，但并不自动等于更好的 Agent；上下文容量本身也需要产品化治理。",
         ["Codex 可启用 1M-token context window", "更大上下文提升代码与工具历史的保留能力", "默认上限体现性能、成本与效果的平衡"],
         "长上下文正在从模型参数变成 Agent 产品设计问题：真正的竞争力是知道何时扩大上下文、如何控制成本，以及如何避免把无关历史一起塞进去。",
         ["Agent", "上下文", "Codex"], 94, "https://x.com/thsottiaux/status/2089082893804896524", "8月16日 · 周日"),
    card("post", "观点动态", "Thibault Sottiaux", "Codex · X 动态",
         "长上下文从 API 实验走向 ChatGPT 用户工作流",
         "GPT-5.6 Sol 的 1M context window 此前只对 API keys 开放，现在也能通过 ChatGPT 账号在 Codex 中使用。这个变化降低了长任务能力的使用门槛，但团队仍提醒用户，默认限制并非保守失误，而是对性能与成本的刻意调优。",
         ["1M context window 扩展到 ChatGPT 账号", "长上下文能力进入更广泛的产品工作流", "开放能力与默认成本控制并行存在"],
         "AI Builders 需要把高级模型能力设计成可渐进采用的产品，而不是只在设置里暴露一个更大的数字。",
         ["产品", "工程", "上下文"], 91, "https://x.com/thsottiaux/status/2089143488696705077", "8月17日 · 周一"),
    card("post", "观点动态", "Guillermo Rauch", "Vercel · X 动态",
         "低成本推理会把防御性安全带入高频评估时代",
         "Guillermo Rauch 分享了对 GLM 5.3 网络安全能力的评测，并判断其较低成本会推动防御性安全工作：同样的预算可以让团队至少多运行约 3 倍评测。重要变化不是单次 benchmark 更高，而是安全验证可以更频繁地嵌入开发和运营循环。",
         ["GLM 5.3 被用于网络安全能力评测", "更低成本意味着更高频的安全验证", "开放模型可能扩大防御性安全工具的可及性"],
         "当推理成本下降，评测从阶段性检查变成持续运行的基础设施，安全团队与 AI Builders 都应重新设计反馈频率。",
         ["研究", "安全", "模型"], 92, "https://x.com/rauchg/status/2089126690043916495", "8月16日 · 周日"),
    card("post", "观点动态", "Aaron Levie", "Box · X 动态",
         "AI 支出还没撞墙：便宜推理会扩大任务边界",
         "Aaron Levie 指出，AI 支出仍远未触顶；在偏工程型公司的样本中，最高 1% 的公司平均每位员工每月花费约 7,500 美元，前 10% 约 660 美元，而且各类企业都呈持续增长趋势。这个信号与模型降价形成组合：企业不是只用 AI 替代旧成本，而是在尝试此前因为不实用而被放弃的任务。",
         ["高使用企业的 AI 人均支出已达到较高水平", "增长趋势不只存在于工程公司", "成本下降会释放更多可自动化任务"],
         "对 Builders 来说，机会不只是降低单次调用价格，而是把新增推理预算转化为真实、连续且可衡量的工作流。",
         ["企业AI", "成本", "Agent"], 90, "https://x.com/levie/status/2088995821056659901", "8月16日 · 周日"),
    card("post", "观点动态", "Aaron Levie", "Box · X 动态",
         "Agent 的价值在于执行那些过去不值得做的工作",
         "Aaron Levie 认为，Agent 的上行空间来自持续完成那些人类并非不想做、而是过去完全不实际的任务。这个判断把产品机会从“替人完成一个明确动作”推进到“让大量低频、琐碎但有价值的工作第一次具备经济可行性”。",
         ["Agent 扩大可执行任务的边界", "价值来自持续而非一次性的自动化", "过去不经济的工作可能成为新产品入口"],
         "寻找 Agent 机会时，最值得问的不是哪项工作最热门，而是哪项工作长期有价值、过去却因频率或成本而无人处理。",
         ["Agent", "产品", "工作流"], 88, "https://x.com/levie/status/2089209131391729763", "8月17日 · 周一"),
    card("post", "观点动态", "Dan Shipper", "Fable · X 动态",
         "Vibe coding 正把客户研究变成可视化分析工具",
         "Dan Shipper 分享了用 Fable 快速构建应用的案例：把 Thesis 申请者可视化并按群体聚类。它说明 AI coding 的价值不只在生成页面，而在于让小团队可以低成本把客户数据转成探索性分析工具，从而更快获得对用户结构的细粒度理解。",
         ["Fable 可快速生成面向真实数据的应用", "申请者被可视化并按群体聚类", "客户理解与产品决策之间的反馈周期被压缩"],
         "当定制分析工具的边际成本下降，产品团队可以更频繁地用真实用户数据验证假设，而不是只依赖通用报表。",
         ["工程", "产品", "数据"], 87, "https://x.com/danshipper/status/2089121597017759800", "8月16日 · 周日"),
    card("post", "观点动态", "Thariq", "Claude Code · X 动态",
         "AI 正在成为成熟 Web 框架作者的第二增长曲线",
         "Thariq 观察到 Django、Flask 和 Rails 的创始人都很早就投入 AI，这不是简单的名人背书。熟悉框架演化的人更容易看出，AI 正在改变软件构建的抽象层：从手写每个实现细节，转向设计约束、工具链和可组合的系统。",
         ["多个主流 Web 框架创始人较早拥抱 AI", "框架经验有助于识别抽象层迁移", "AI coding 的长期影响可能类似新一代开发范式变化"],
         "对 Builders 而言，值得关注的不是短期工具热度，而是哪些新的工程抽象会像 Web framework 一样沉淀十年。",
         ["工程", "开发工具", "长期判断"], 85, "https://x.com/trq212/status/2089085004966207679", "8月16日 · 周日"),
    card("podcast", "播客摘录", "The MAD Podcast with Matt Turck", "Thomas Wolf · 播客",
         "模型会反过来改写产品团队的速度与组织方式",
         "Hugging Face 的 Thomas Wolf 在节目中讨论了 AI 模型如何从工具变成能影响产品开发节奏的参与者；核心不是单纯追求更快发布，而是当模型能力快速跃迁时，团队必须同时重做评测、协作和决策机制。模型进步带来的机会与组织风险会同步放大。",
         ["模型能力变化会直接影响产品节奏", "快速迭代需要新的评测与协作机制", "AI 组织要同时管理速度、可靠性与方向感"],
         "这期对 Builders 的价值在于把模型进步放回组织系统中看：真正难的不是得到一次能力跃升，而是让团队能持续吸收它。",
         ["研究", "组织", "Agent"], 89, "https://www.youtube.com/watch?v=FU9A481E2W8", "8月7日 · 周五"),
]

data["dailyInsight"] = {
    "paragraphs": [
        "今天最强的产品信号来自 Codex：1M-token context window 正从 API 能力扩展到 ChatGPT 账号用户。与此同时，团队仍强调默认上下文是性能与成本调优后的结果。长上下文因此不应被理解为越大越好，而应被视为 Agent 的记忆预算：何时加载、保留什么、如何控制噪声和成本，都会成为产品设计的一部分。",
        "模型成本下降正在把 AI 从“偶尔调用”推向“高频运行”。Guillermo Rauch 认为更低成本能让防御性安全评测运行得更频繁；Aaron Levie 则观察到企业 AI 支出仍在增长，并判断 Agent 的价值在于执行那些过去有价值却不具备经济可行性的工作。供给变便宜后，真正的瓶颈会转向能否找到足够多、足够具体的任务。",
        "应用层的工程闭环也在缩短。Dan Shipper 用 Fable 为 Thesis 申请者构建可视化聚类工具，说明 vibe coding 的高价值用法不是生成一个孤立 demo，而是快速把真实数据转成能帮助团队理解用户的工作界面。AI coding 的产出开始直接进入研究、决策和运营，而不只是停留在代码仓库里。",
        "长期看，成熟工程抽象与组织能力仍然重要。Thariq 注意到 Django、Flask 和 Rails 的创始人很早拥抱 AI；播客中 Thomas Wolf 讨论的重点也不是单次模型跃升，而是团队如何重做评测、协作和决策机制。对 AI Builders 来说，下一轮壁垒会是可控的上下文、可持续的执行循环，以及能吸收快速模型进步的组织系统。"
    ],
    "filteredNote": "过滤掉了个人搬家与生活感叹、泛泛鸡汤、无上下文短句、纯推广、单纯提问和没有 AI/工程增量的评论等低信号内容。"
}
data["highSignalItems"] = items

for path in (archive_path, latest_path):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

digests = json.loads(digests_path.read_text(encoding="utf-8"))
digests = [d for d in digests if d.get("date") != DATE]
digests.insert(0, data)
digests_path.write_text(json.dumps(digests, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"date": DATE, "highSignalItems": len(items), "dailyInsightParagraphs": len(data["dailyInsight"]["paragraphs"]), "files": [str(archive_path), str(latest_path), str(digests_path)]}, ensure_ascii=False))
