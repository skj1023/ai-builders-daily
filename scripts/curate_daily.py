import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-17"
archive_path = ROOT / "data" / "archive" / f"{DATE}.json"

with archive_path.open(encoding="utf-8") as f:
    data = json.load(f)

display_date = data["displayDate"]

def card(type_, label, actor, meta, title, summary, key_points, why, tags, score, url):
    return {
        "type": type_, "typeLabel": label, "date": display_date,
        "actor": actor, "meta": meta, "title": title, "summary": summary,
        "keyPoints": key_points, "whyItMatters": why, "tags": tags,
        "qualityScore": score, "url": url,
    }

items = [
    card("post", "观点动态", "Boris Cherny", "Claude Code · X 动态",
         "自动化能力正在从个人技巧变成团队的默认生产力",
         "Boris Cherny 回顾了优秀工程师过去如何用编辑器自动化、lint 规则和端到端测试消除重复劳动。他的判断是，Agent 把这类自动化的门槛显著降低：关键不再是谁会手搓工具，而是谁能把重复工作系统化地交给机器。",
         ["自动化一直是高效工程师的复利来源", "Agent 扩大了可自动化工作的覆盖面", "团队应把可重复任务沉淀为可执行工作流"],
         "这提醒 AI Builders：不要只把 Agent 当作更快的代码补全，而要把它纳入工程系统的持续自动化。",
         ["Agent", "工程", "自动化"], 94, "https://x.com/bcherny/status/2077460395279692197"),
    card("post", "观点动态", "Josh Woodward", "Google / Gemini · X 动态",
         "本地语言与多模态输入正在决定 AI 产品的下一轮增长",
         "Josh Woodward 分享 Gemini Southeast Asia Report：当地活跃用户同比增长超过一倍，70% 的提示词使用母语，40% 的提示完全通过语音、图片或视频完成。增长并非仅来自模型能力提升，而是语言、多模态与移动端入口共同降低了使用门槛。",
         ["活跃用户同比增长超过一倍", "70% 提示词使用本地语言", "40% 提示完全采用非文本输入"],
         "对面向全球市场的 AI Builders 而言，真正的产品本地化要覆盖输入方式、语言能力与移动场景，而不只是翻译界面。",
         ["产品", "多模态", "全球化"], 91, "https://x.com/joshwoodward/status/2077411104775406045"),
    card("post", "观点动态", "Josh Woodward", "Gemini Spark · X 动态",
         "Agent 的可用性取决于跨文档上下文与并行执行",
         "Gemini Spark 正向更多 Ultra 订阅用户开放，并新增直接打开和编辑 Google Docs、读取 Sheets 与 Slides 评论、提速超过 50% 及并行处理能力。功能组合指向同一个方向：Agent 必须进入用户真实协作资料流，而不是只在单一聊天框中回答问题。",
         ["可直接操作 Google Docs", "可读取 Sheets 与 Slides 评论", "速度提升并支持并行处理"],
         "AI 产品的竞争正在从“会不会生成”转向“能否接住分散在协作系统里的上下文，并完成动作”。",
         ["Agent", "产品", "协作"], 89, "https://x.com/joshwoodward/status/2077471111240204457"),
    card("post", "观点动态", "Thibault Sottiaux", "Codex · X 动态",
         "取消短时额度后，Agent 产品需要重新设计使用治理",
         "Thibault Sottiaux 表示 Codex Plus 与 Pro 已连续数日取消 5 小时限制，并公开询问用户：按周计的额度是否更易管理、理想方案应是什么。这个实验说明长任务 Agent 的计费与限制，不只是成本问题，也会直接影响用户如何规划、委派和信任工作。",
         ["Plus 与 Pro 暂无 5 小时限制", "团队在收集周额度的可管理性反馈", "使用边界是 Agent 体验的一部分"],
         "当 Agent 开始执行持续数小时的任务，清晰、可预期的资源治理会成为留存与信任的核心设计。",
         ["Codex", "产品", "定价"], 87, "https://x.com/thsottiaux/status/2077632589498913087"),
    card("post", "观点动态", "Thibault Sottiaux", "Codex · X 动态",
         "全权限 Agent 的安全边界必须落到默认配置",
         "针对 GPT-5.6 意外删除文件的报告，Thibault Sottiaux 说明，问题最常见于开启 Full Access、未使用 sandbox、且没有启用自动审查的组合；也与模型尝试覆盖既有文件有关。信息的重点不是单一模型失误，而是高权限自动化必须依赖分层防护和可审查的默认路径。",
         ["风险集中于 Full Access 且无 sandbox 的配置", "自动审查缺失会放大破坏性操作", "权限、隔离与审核应共同构成防线"],
         "AI Builders 应把安全默认值当作产品能力：Agent 越能行动，越不能把风险控制留给用户临场选择。",
         ["Agent", "安全", "工程"], 93, "https://x.com/thsottiaux/status/2077630111499882637"),
    card("post", "观点动态", "Thariq", "Claude Code · X 动态",
         "薄提示词、厚上下文：把知识从对话迁回工程资产",
         "Thariq 将理想的提示方式概括为“thin prompts、thick artifacts + context、thin skills”。这套框架把稳定知识和约束放入代码库、文档与可复用产物，而不是反复塞进临时对话；提示词只负责当前意图的轻量调度。",
         ["提示词应尽量短且指向明确", "上下文应沉淀为可验证的工程产物", "skills 应保持小而可组合"],
         "这是构建可靠 Agent 工作流的实用原则：减少依赖提示词记忆，增加可版本化、可测试的上下文。",
         ["提示工程", "上下文", "Agent"], 92, "https://x.com/trq212/status/2077539537992229076"),
    card("post", "观点动态", "Guillermo Rauch", "Vercel Sandbox · X 动态",
         "Agent 基础设施的需求正从实验性调用走向规模化运行",
         "Guillermo Rauch 公布 Vercel Sandbox 数据：DAU 月环比增长 100%，每天创建超过 350 万个 sandbox，并称其以 Active CPU 定价、已服务 Notion、Airtable、Meta 等客户。无论具体增长基数如何，日千万级隔离执行环境的量级都说明：让 Agent 安全运行代码正在成为独立的基础设施层。",
         ["DAU 月环比增长 100%", "每天创建超过 350 万个 sandbox", "以 Active CPU 作为定价模型"],
         "对 AI Builders，这验证了执行隔离、弹性成本和开发者体验不再是后台细节，而是 Agent 产品的供给能力。",
         ["基础设施", "Sandbox", "Agent"], 90, "https://x.com/rauchg/status/2077559189015335019"),
    card("post", "观点动态", "Aaron Levie", "Box · X 动态",
         "企业 Agent 落地的瓶颈仍是流程与变革管理",
         "Aaron Levie 在与大型企业 IT 负责人的交流中观察到，推动 Agent 改造的最大议题之一仍是变革管理：许多现有流程需要先升级为适合 Agent 的现代运营模式。他同时判断未来会是前沿模型充当编排器，与低成本或专用模型承担高频工作任务的混合架构。",
         ["流程现代化是 Agent 转型的前置条件", "组织变革与技术部署同等重要", "前沿编排器与专用工作模型将共存"],
         "企业机会不在于把聊天机器人接进旧流程，而在于重构流程、权限与模型分工。",
         ["企业AI", "组织", "模型架构"], 91, "https://x.com/levie/status/2077526010753581156"),
    card("post", "观点动态", "Zara Zhang", "X 动态",
         "让 Agent 参与组织，先把组织设计成它读得懂的系统",
         "Zara Zhang 指出，若希望 Agent 真正在公司里工作，就必须把公司设计为 Agent 可读取的形式；她以 Shopify 的实践为例：Agent 没有私聊功能，只能在公开频道活动，副作用却是促进了同事间的知识共享。这里的关键不是给 Agent 更多权限，而是让知识、决策与协作痕迹可被安全地观察和调用。",
         ["组织信息架构决定 Agent 可行动的范围", "公共频道让上下文可访问", "可读性设计还能促进人类同事间学习"],
         "这是 Agent-native 组织的具体设计线索：先改善信息流，再讨论智能体能完成什么任务。",
         ["组织设计", "Agent", "知识管理"], 90, "https://x.com/zarazhangrui/status/2077417579837309040"),
    card("blog", "深度文章", "Claude Blog", "Claude Code · 官方博客",
         "把 Agent 的过程产出变成可协作、可更新的项目界面",
         "Claude Code 新增 artifacts，能够在工作过程中生成并持续更新可分享的可视化页面，包括 PR walkthrough、系统说明、仪表板与发布清单。其核心并非增加一类输出格式，而是把原本封闭在终端会话中的 Agent 工作过程外化为团队可以检查和协作的对象。",
         ["可记录并展示 Agent 的工作进度", "支持 PR 讲解、系统说明、仪表板和发布清单", "产物会随会话工作持续更新"],
         "Agent 要进入团队流程，必须让过程和结果可见、可审阅；artifacts 是从“个人助手”走向“协作系统”的一块接口。",
         ["Claude Code", "协作", "开发工具"], 92, "https://claude.com/blog/artifacts-in-claude-code"),
]

data["dailyInsight"] = {
    "paragraphs": [
        "今天的主线是 Agent 从“能回答”进入“能在真实系统里持续行动”。Gemini Spark 接入 Docs、Sheets 与 Slides 的评论，Claude Code 用 artifacts 外化工作过程，说明下一阶段的产品壁垒是承接协作上下文、执行动作并让结果可审阅。",
        "工程侧的共识也更清晰：Boris Cherny 和 Thariq 都把 Agent 放在自动化的长期脉络中。与其不断写更长的提示词，不如把约束、测试、文档和可复用产物沉淀为厚上下文，让轻量提示词只负责调度。",
        "能力扩张同时放大治理问题。Codex 对无 sandbox、全权限环境下文件删除报告的复盘，以及其对使用额度的公开试验，都表明 Agent 的安全边界与资源边界必须成为默认体验的一部分，而不能依赖用户临时判断。",
        "基础设施与组织设计正在跟上需求：Vercel Sandbox 的大规模创建量证明隔离执行已成为刚需；Aaron Levie 与 Zara Zhang 则分别从企业流程和信息架构指出，Agent 能否落地取决于组织是否愿意把流程现代化、把知识流设计得机器可读。"
    ],
    "filteredNote": "过滤掉了日常感叹、非 AI 话题、单句评论、无分析的转发与纯推广内容。"
}
data["highSignalItems"] = items

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

print(json.dumps({"date": DATE, "highSignalItems": len(items), "dailyInsightParagraphs": len(data["dailyInsight"]["paragraphs"]), "files": [str(archive_path), str(ROOT / "data" / "latest.json"), str(digests_path)]}, ensure_ascii=False))
