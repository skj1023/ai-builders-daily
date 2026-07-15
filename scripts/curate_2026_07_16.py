import json
from pathlib import Path

root = Path(r"C:/Users/PC/Documents/ai-builders-daily")
date = "2026-07-16"
archive = root / "data" / "archive" / f"{date}.json"
with archive.open(encoding="utf-8") as f:
    data = json.load(f)

insight = {
    "paragraphs": [
        "今天最强的信号不是又一个模型功能，而是 Codex/ChatGPT Work 的需求曲线开始反过来塑造产品运营。Sam Altman 说 GPT-5.6 Sol 的增长极快、推理团队正全力扩容且短期可能出现波动；Thibault Sottiaux 同时用 10,000 份 Codex credits 换取用户迁移原因与偏好。前者说明推理容量仍是产品上限，后者则把补贴、口碑和定性研究绑成一个快速学习闭环。",
        "Agent 能先在编程中爆发，Aaron Levie 给出了很朴素但关键的解释：代码的输出可以很快运行或测试，因而形成低成本、可自动化的验证回路。Thariq 用 Claude Code 拉取实时比赛数据、调用 npm 库并生成对局报告，是同一模式向垂直任务扩展的微型案例——有明确工具接口、可检验结果和结构化数据的领域，最适合先被 agent 化。",
        "产品接口的竞争正在从“模型能力”延展到“接入摩擦”。Vercel 将 Agentmail 放进 `vercel install`，把注册、初始化和计费都收敛到一个动作；Claude for Teachers 则把课程标准、优质教材、可编辑教案和 FERPA 隐私承诺做成一条端到端工作流。能否把能力嵌进用户已有的工具链与合规边界，正成为垂直 AI 产品的核心分水岭。",
        "与此同时，复杂度仍是 AI 产品的反作用力。Aditya Agarwal 指出新版 ChatGPT 的功能深度正在伤害自己每天 15–20 次的轻量查询体验；Nikunj Kothari 则观察到 agent 运行期间，工程师会出现新的等待与注意力切换行为。对 AI Builders 而言，自动化并不等于交互消失：产品需要同时照顾高频即时任务、长任务的可见进度，以及由此重构的人类工作节奏。"
    ],
    "filteredNote": "过滤掉了世界杯与日常生活内容、活动招募、表情/单句评论、无上下文自我宣传及纯转发式动态等 29 条低信号内容。"
}

items = [
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Sam Altman","meta":"OpenAI · X 动态","title":"GPT-5.6 Sol 的需求暴涨，把推理扩容推到产品前台","summary":"Sam Altman 表示 GPT-5.6 Sol 的增长极快，推理团队正全力支撑需求，但短期仍可能出现服务波动。这是来自产品负责人的直接信号：前沿模型的竞争已不仅是能力发布，能否持续把推理容量交付给用户同样决定体验。","keyPoints":["GPT-5.6 Sol 的使用增长显著","OpenAI 推理团队正在为需求扩容","短期容量压力可能带来服务 hiccups"],"whyItMatters":"对 AI Builders 来说，模型供应与容量管理是产品设计约束而非后台细节；高增长时必须为降级、排队和用户沟通预留机制。","tags":["推理基础设施","产品运营","规模化"],"qualityScore":88,"url":"https://x.com/sama/status/2077106587307798989"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Thibault Sottiaux","meta":"OpenAI Codex & ChatGPT · X 动态","title":"用 10,000 份 credits 把用户反馈变成 Codex 的增长研究","summary":"Thibault Sottiaux 邀请用户公开说明喜欢 GPT-5.6 Sol 或迁移的原因，前 10,000 人可领取 100 美元 Codex credits。这不是普通促销：它把使用激励、公开口碑与迁移原因收集压缩进同一个可快速迭代的产品研究动作。","keyPoints":["前 10,000 名参与者获得 100 美元 Codex credits","收集用户喜欢 GPT-5.6 Sol 或迁移的具体原因","将激励分发与定性反馈同时完成"],"whyItMatters":"当模型差异难以仅靠指标解释时，迁移叙事和真实工作流反馈是更高价值的产品信号。","tags":["Codex","用户研究","增长"],"qualityScore":82,"url":"https://x.com/thsottiaux/status/2077248807533003257"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Aaron Levie","meta":"Box · X 动态","title":"代码为何成为 Agent 最先规模化的工作对象","summary":"Aaron Levie 的判断是，代码天然适合 agent，因为结果可以快速通过运行应用或自动化测试验证；大多数工作领域没有同样廉价的反馈闭环。其核心不在于代码“更容易写”，而在于产出可被持续、客观地验收。","keyPoints":["代码可通过运行或测试快速验证","验证成本低让 agent 能够反复尝试","其他知识工作通常缺少同等强度的反馈回路"],"whyItMatters":"评估一个 agent 场景时，应先问验证器在哪里、反馈成本多高，而不是只问模型能否生成内容。","tags":["Agent","工程","验证"],"qualityScore":90,"url":"https://x.com/levie/status/2077201458546745553"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Thariq","meta":"Anthropic Claude Code · X 动态","title":"把实时数据、领域库和报告串起来：Claude Code 的垂直分析实验","summary":"Thariq 用 Claude Code 调用 Smogon 的 npm 库、拉取实时使用率，并输出对局、阈值和队伍构建报告来辅助 Pokémon Champions 分析。这个小案例展示了 coding agent 的价值正从“写代码”转向编排工具、数据和可读结论。","keyPoints":["调用领域 npm 库获取结构化能力","拉取实时使用数据","将分析结果输出为比赛决策报告"],"whyItMatters":"高价值 agent 往往不是聊天窗口，而是把现有 API、数据源和可验证分析串成一条可重复的工作流。","tags":["Claude Code","Agent","工具调用"],"qualityScore":84,"url":"https://x.com/trq212/status/2077051280267399550"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Guillermo Rauch","meta":"Vercel · X 动态","title":"Agentmail 进入 Vercel 安装流：Agent 服务开始被当作基础设施交付","summary":"Guillermo Rauch 宣布可直接通过 `vercel install agentmail` 为 agent 配置 Agentmail，无需单独注册，并自动完成设置和统一计费。信息本身很短，但产品选择很明确：把 agent 所需能力放进开发者已经信任的部署与计费平面。","keyPoints":["通过 Vercel 安装命令接入 Agentmail","免除单独注册与手动初始化","统一计费降低服务拼接摩擦"],"whyItMatters":"Agent 生态的护城河正在转向默认接入路径；最少的账号、配置和账单切换，往往比单点功能更能驱动采用。","tags":["Agent","开发者体验","基础设施"],"qualityScore":81,"url":"https://x.com/rauchg/status/2077154901013221444"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Guillermo Rauch","meta":"Vercel AI Gateway · X 动态","title":"开放 AI Gateway token flow 数据，为模型调用决策提供公共样本","summary":"Guillermo Rauch 宣布开放 Vercel AI Gateway 的 AI token flows 数据集，并称其中包含值得研究的使用洞察。模型与 provider 的流量数据很少被公开；即使该动态没有展开结论，数据集本身为观察真实生产调用结构提供了新的入口。","keyPoints":["Vercel 开放 AI Gateway token flow 数据集","数据覆盖实际网关调用的流量视角","可用于研究模型与 token 使用模式"],"whyItMatters":"AI Builders 需要用生产行为而非发布声量判断模型生态；开放流量数据是稀缺的外部校准来源。","tags":["AI Gateway","数据","模型生态"],"qualityScore":77,"url":"https://x.com/rauchg/status/2077176141790752798"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Claude","meta":"Anthropic · X 动态","title":"教育场景的 AI 工作流：从课程标准到可编辑课堂材料","summary":"Claude for Teachers 可通过 Learning Commons 连接州课程标准与高质量课程资料，生成教案和面向学生的材料，再由教师编辑带入课堂。Anthropic 同时强调不会用对话训练模型，并以符合 FERPA 的数据处理协议保护学生信息。","keyPoints":["以课程标准和优质教材作为生成上下文","输出教案与学生材料，并保留教师编辑权","针对 K-12 提供隐私与 FERPA 合规承诺"],"whyItMatters":"垂直 AI 的可用性来自领域上下文、人工审核和合规承诺的组合，而不是通用生成能力的简单包装。","tags":["教育 AI","工作流","隐私合规"],"qualityScore":86,"url":"https://x.com/claudeai/status/2077047279689535705"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Aditya Agarwal","meta":"产品观察 · X 动态","title":"功能越全，越可能失去高频查询的轻量入口","summary":"Aditya Agarwal 认可新版 ChatGPT 的功能深度，却指出它相较 Legacy 版本对每天 15–20 次的快速查询显得过重。这是一条具体的产品反例：扩展能力不应以牺牲高频、低意图任务的启动速度为代价。","keyPoints":["用户认可新版本的深度功能","高频轻量查询体验变得沉重","同一产品内存在复杂任务与即时任务的冲突"],"whyItMatters":"AI 产品应显式设计快路径与深路径；把所有能力堆进同一个入口，可能降低最常用场景的留存。","tags":["产品设计","用户体验","ChatGPT"],"qualityScore":83,"url":"https://x.com/adityaag/status/2077130899733553560"},
    {"type":"post","typeLabel":"观点动态","date":"7月16日 · 周四","actor":"Nikunj Kothari","meta":"工程组织观察 · X 动态","title":"当 Agent 在后台工作，工程师的等待时间成为新的组织变量","summary":"Nikunj Kothari 观察到，传统工程管理者可能难以理解最强工程师同时高度在线：当 agent 运行时，社交信息流成为等待期间的即时刺激。观点带有调侃，但指向一个真实的工作设计问题——自动化把连续专注改造成“发起—等待—审阅”的节奏。","keyPoints":["Agent 运行会制造新的等待间隙","工程师的注意力在执行与信息流间切换","传统以持续编码为中心的管理假设需要更新"],"whyItMatters":"团队采用 agent 后，除了吞吐量，还应设计任务可见性、审阅队列与并行工作，避免等待时间被无结构地消耗。","tags":["工程组织","Agent","工作流"],"qualityScore":72,"url":"https://x.com/nikunj/status/2077144910508257317"},
    {"type":"podcast","typeLabel":"播客摘录","date":"7月16日 · 周四","actor":"Training Data","meta":"Katelyn Lesse & Angela Jiang · 播客","title":"Anthropic 的生态策略：把协调层做成开放连接，而非围墙花园","summary":"Training Data 与 Anthropic 的 Katelyn Lesse、Angela Jiang 讨论的核心命题是：AI 产品的最后一层抽象更像协调层，而成功的生态不应是封闭花园。对开发者而言，模型公司竞争的不只是模型调用，而是谁能让工具、伙伴与用户工作流更容易互联并共同演化。","keyPoints":["将 AI 产品的高层抽象理解为协调层","主张建设生态而非封闭式平台","互操作与伙伴网络会影响长期开发者采用"],"whyItMatters":"平台策略会决定 agent 和工具能否跨边界组合；开放接口与协调能力正在成为模型公司长期分发的关键。","tags":["Anthropic","生态系统","平台策略"],"qualityScore":80,"url":"https://www.youtube.com/watch?v=vPnVTHYplrQ"}
]

data["headline"] = "今日聚焦推理扩容、可验证 Agent 工作流、低摩擦接入与 AI 产品复杂度：从 40 条源内容中筛选出 10 条高信号内容。"
data["editorNote"] = "本页只保留具备事实增量、观点密度、产品/工程 insight 或长期判断价值的 AI Builders 内容。"
data["dailyInsight"] = insight
data["highSignalItems"] = items
data["toplines"] = [{"title": i["title"], "source": i["meta"], "url": i["url"], "sourceDate": date, "sourceDisplayDate": i["date"], "summary": i["summary"], "chineseTitle": i["title"], "tags": i["tags"], "score": i["qualityScore"]} for i in items[:5]]

for path in (archive, root / "data" / "latest.json"):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

digest_path = root / "data" / "digests.json"
with digest_path.open(encoding="utf-8") as f:
    digests = json.load(f)
digests = [entry for entry in digests if entry.get("date") != date]
digests.insert(0, data)
with digest_path.open("w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"curated {date}: {len(items)} highSignalItems; archive/latest/digests synchronized")
