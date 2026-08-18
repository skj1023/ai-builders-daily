import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
date = "2026-08-19"
archive_path = root / "data" / "archive" / f"{date}.json"
data = json.loads(archive_path.read_text(encoding="utf-8"))

items = [
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Swyx", "meta": "Continual Learning · X 动态",
        "title": "持续学习的瓶颈在数据闭环，而不只是算法",
        "summary": "Swyx 转述 Trajectory 对 Continual Learning 的实践：剩下的核心问题是数据，单靠 GRPO 不够，还需要转向 on-policy，并处理后续修复环节。它说明持续学习真正难的不是把训练方法名换一遍，而是把真实使用反馈变成可持续的训练信号。",
        "keyPoints": ["Continual Learning 的主要瓶颈转向数据问题", "GRPO 不足以覆盖真实工作流，需要 on-policy 信号", "训练、反馈与修复必须形成闭环"],
        "whyItMatters": "对做 Agent 和模型产品的团队来说，数据闭环往往比再堆一个算法名更决定长期效果。",
        "tags": ["研究", "工程", "Agent"], "qualityScore": 84, "url": "https://x.com/swyx/status/2089393073327653344"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月18日 · 周二", "actor": "Josh Woodward", "meta": "Gemini · X 动态",
        "title": "模型升级之外，Agent 产品正在补齐工作区基础设施",
        "summary": "Josh Woodward 公布 Gemini 后续迭代：1–2 周内测试新版 Workspace 工具，Gemini 3.7 Flash 改进 tool calling，Projects 设计已完成并进入实现，同时连接器数量达到 49 个。路线很清楚：Agent 体验的竞争不只在模型能力，也在项目组织、工具调用和外部系统连接。",
        "keyPoints": ["新版 Workspace 工具进入测试", "Gemini 3.7 Flash 持续改进 tool calling", "Projects 与 49 个连接器强化工作流整合"],
        "whyItMatters": "这是一份很具体的 Agent 产品路线样本，提示 Builder 优先补齐工作流基础设施，而不是只追逐 benchmark。",
        "tags": ["Agent", "产品", "工程"], "qualityScore": 91, "url": "https://x.com/joshwoodward/status/2089520767281324112"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Madhu Guru", "meta": "AI evals · X 动态",
        "title": "把熟悉的工作流变成可测量的质量系统",
        "summary": "Madhu Guru 给出一套落地的 evals 方法：从自己熟悉的工作流开始，观察真实用户的 prompt 序列，定义每一步和端到端结果的好答案，再定位产品失败的位置。评估不是脱离产品的静态题库，而是对真实 trace 的结构化测量。",
        "keyPoints": ["从熟悉且真实的工作流切入评估", "分析用户 prompt 序列与每一步的质量标准", "同时关注局部步骤和端到端结果"],
        "whyItMatters": "这是把 Agent 评估从口号变成工程流程的实用框架，尤其适合早期产品建立第一版质量基线。",
        "tags": ["评估", "Agent", "产品"], "qualityScore": 94, "url": "https://x.com/realmadhuguru/status/2089480958571331623"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Thariq", "meta": "Claude Code · X 动态",
        "title": "代码模型正在侵入创意生产，而不只是软件开发",
        "summary": "Thariq 观察近期程序化艺术、视频编辑和 3D 游戏 demo 后，更新了判断：LLM coding models 在不少创意工作上可能优于 diffusion models。关键原因是代码更容易被编辑、微调，并能导出到现有工具链，创作者获得的是可控的迭代接口。",
        "keyPoints": ["创意工作成为 coding models 的新战场", "代码表示更容易编辑和定向微调", "输出可接入既有工具链，降低迁移成本"],
        "whyItMatters": "它揭示了创意 Agent 的产品机会：可控、可复用的生成过程，可能比一次性生成更有长期价值。",
        "tags": ["Agent", "工程", "创意工具"], "qualityScore": 88, "url": "https://x.com/trq212/status/2089415712007938315"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Amjad Masad", "meta": "AI 安全 · X 动态",
        "title": "漏洞扫描只是起点，真正的安全测试要主动攻破系统",
        "summary": "Amjad Masad 强调，扫描代码中的漏洞并不够，还必须通过 penetration testing 主动尝试攻破它们。对 AI 生成代码和 Agent 系统而言，静态检查只能覆盖已知模式，攻击性测试才能暴露组合漏洞、权限边界和真实运行时风险。",
        "keyPoints": ["静态漏洞扫描不能替代主动攻击测试", "Pen testing 更接近真实运行时风险", "AI 生成代码需要把安全验证纳入交付链路"],
        "whyItMatters": "随着 coding Agent 直接改代码、部署服务，安全能力必须从检查清单升级为持续的对抗性验证。",
        "tags": ["安全", "工程", "Agent"], "qualityScore": 90, "url": "https://x.com/amasad/status/2089435606338416884"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Guillermo Rauch", "meta": "Cursor Origin · X 动态",
        "title": "代码托管与部署开始收敛成一条 Agent 原生链路",
        "summary": "Guillermo Rauch 分享 Cursor Origin 的组合体验：代码仓库可以直接托管在 Cursor Origin，再通过 Cursor Origin 部署到 Vercel，而 Cursor Origin 本身也运行在 Vercel 上。这里的信号不是又多一个代码平台，而是开发、托管和部署之间的边界正在被 Agent 工作流重新压平。",
        "keyPoints": ["Cursor Origin 提供仓库托管", "可直接衔接 Vercel 部署", "开发到上线的路径更适合 Agent 自动化"],
        "whyItMatters": "对 Builder 来说，平台间的摩擦越少，Agent 越能从改代码走到可访问产品；部署链路会成为产品体验的一部分。",
        "tags": ["工程", "开发工具", "部署"], "qualityScore": 87, "url": "https://x.com/rauchg/status/2089409162270965858"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Aaron Levie", "meta": "AI 与数据资产 · X 动态",
        "title": "AI 让信息第一次像资产一样进入资产负债表",
        "summary": "Aaron Levie 认为，AI 对数据的需求正在让几乎所有形式的信息都具备经济价值，数据交易只是其中一个例子。更深层的判断是：在 AI 时代，企业知识、内容和行为数据不再只是运营副产品，而可能成为需要定价、管理和保护的资产。",
        "keyPoints": ["AI 对数据的需求扩展到几乎所有信息形态", "数据交易只是价值化的一个例子", "企业信息需要被当作可管理资产对待"],
        "whyItMatters": "这会影响数据采购、版权、隐私和企业知识库建设，是 AI 产品商业化的长期变量。",
        "tags": ["数据", "商业", "研究"], "qualityScore": 86, "url": "https://x.com/levie/status/2089499887905997272"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Garry Tan", "meta": "Personal AGI · X 动态",
        "title": "个人 Agent 的壁垒可能来自可迁移的技能库",
        "summary": "Garry Tan 开源了一个包含 70 个 skills 和知识 wiki 雏形的 GitHub repo，可配合现有 Claude Code 或 Codex 使用。这个实践把 Personal AGI 拆成了更具体的组件：可复用技能、个人知识结构，以及能被 Agent 直接消费的操作说明。",
        "keyPoints": ["以 skills 作为个人 Agent 的可复用能力单元", "知识 wiki 为长期上下文提供结构", "兼容现有 Claude Code 与 Codex 订阅"],
        "whyItMatters": "它提供了一个低成本实验路径，也说明个人 Agent 的差异化可能沉淀在用户自己的知识与工作方法中。",
        "tags": ["Agent", "知识管理", "开源"], "qualityScore": 82, "url": "https://x.com/garrytan/status/2089425134339961173"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Nikunj Kothari", "meta": "AI 产业判断 · X 动态",
        "title": "当模型、IDE 和 Agent harness 都趋于同质化，护城河转向分发",
        "summary": "Nikunj Kothari 逐层列举模型、IDE、harness、应用构建器、垂直 wrapper 和推理服务，判断这些层普遍缺乏稳定 moat。若能力快速扩散，真正能积累的优势就更可能来自分发、品牌、客户关系、专有数据和执行速度，而不是单一产品表面。",
        "keyPoints": ["模型到应用层的能力都在快速商品化", "单一技术层难以形成长期 moat", "分发、数据与客户关系成为更重要的积累项"],
        "whyItMatters": "这是评估 AI 创业机会时很有用的反幻觉框架：不要把暂时领先的功能误认成长期壁垒。",
        "tags": ["战略", "产品", "创业"], "qualityScore": 89, "url": "https://x.com/nikunj/status/2089486802356961364"
    },
    {
        "type": "post", "typeLabel": "观点动态", "date": "8月17日 · 周一", "actor": "Nikunj Kothari", "meta": "AI 产品营销 · X 动态",
        "title": "AI 产品的品牌价值建立在留存之上，而不是视觉噱头",
        "summary": "Nikunj Kothari 认为品牌营销会成为未来公司的主要差异化资产，但明确区分了品牌与烧钱做 launch video：先有 retention，再争取 attention。对 AI 产品而言，品牌不是包装层，而是把真实产品体验转化为记忆、信任和持续分发的机制。",
        "keyPoints": ["品牌可能成为 AI 产品的重要长期资产", "营销不能替代 retention", "品牌应建立在可重复的产品体验上"],
        "whyItMatters": "当底层能力越来越容易复制，可信认知与持续分发会变得更稀缺，但前提仍是产品真的留得住用户。",
        "tags": ["产品", "品牌", "增长"], "qualityScore": 85, "url": "https://x.com/nikunj/status/2089374392295842086"
    }
]

data["dailyInsight"] = {
    "paragraphs": [
        "今天最强的共同信号，是 AI 产品的竞争正在从单点模型能力转向完整工作流。Gemini 的 Workspace、Projects、tool calling 和连接器路线，与 Cursor Origin 打通代码托管和 Vercel 部署，本质上都在减少用户从意图到结果之间的摩擦。",
        "工程质量的重点也在变化：Madhu Guru 把 evals 拉回真实用户 trace，Swyx 转述的 Continual Learning 实践则强调数据闭环、on-policy 和修复流程；Amjad Masad 对 penetration testing 的提醒进一步说明，Agent 交付不能只看生成成功，还要能测量、验证并主动攻破失败路径。",
        "Thariq 对创意工作的观察和 Garry Tan 的 skills + knowledge wiki 实践，指向同一方向：Agent 的可持续价值来自可编辑、可复用、可迁移的过程资产，而不是一次性的生成结果。代码、技能库和个人知识都可能成为新的控制面。",
        "产业层面，Nikunj Kothari 判断从模型到 IDE、harness 和 wrapper 的多层能力都在商品化，因此真正的 moat 更可能来自分发、数据、客户关系和品牌；Aaron Levie 对数据资产化的判断，则提醒 Builder 提前处理数据权利、定价与治理。"
    ],
    "filteredNote": "过滤掉了纯情绪表达、单词式回复、无上下文转发、宣传导流和与 AI Builders 无关的内容，共保留 10 条高信号动态。"
}
data["highSignalItems"] = items

# Keep the source archive and the rendered latest snapshot identical.
for path in (archive_path, root / "data" / "latest.json"):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

digests_path = root / "data" / "digests.json"
digests = json.loads(digests_path.read_text(encoding="utf-8"))
digests = [d for d in digests if d.get("date") != date]
digests.insert(0, data)
digests_path.write_text(json.dumps(digests, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"date": date, "highSignalItems": len(items), "filesUpdated": 3}, ensure_ascii=False))
