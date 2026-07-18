import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
date = "2026-07-19"
display_date = "7月19日 · 周日"
archive_path = ROOT / "data" / "archive" / f"{date}.json"
latest_path = ROOT / "data" / "latest.json"
digests_path = ROOT / "data" / "digests.json"

with archive_path.open(encoding="utf-8") as f:
    digest = json.load(f)

digest["dailyInsight"] = {
    "paragraphs": [
        "今天最明确的产品信号不是又一个模型分数，而是供给约束正在直接重塑产品套餐。Claude 将 Fable 5 纳入 Max 和 Team Premium、同时把高强度使用的标准访问设为 50% 限额，说明前沿能力的商业化仍要在可预测的用户体验与瞬时算力成本之间做精细配给。对 AI Builders 而言，定价、额度和容量不再是后台运营问题，而是产品承诺的一部分。",
        "Agent 从“能不能跑”转向“如何稳定地跑在企业系统里”。Madhu Guru 把企业停留在聊天机器人的原因指向 harness 与 offline/online evals 的人才缺口；Anthropic 对 Managed Agents 的更新则把推理层与执行环境拆开，并将自托管 sandbox、私有 MCP 连接纳入部署路径。真正的门槛正在从调用模型，移动到定义任务、测量质量、隔离权限和接入私有系统。",
        "工程摩擦依旧决定 Agent 的实际产能。Peter Steinberger 记录了 Agent 为上传一张图片而绕行浏览器和系统选择器，也因此把 Codex 放进 VM 避免抢占前台；Thariq 则建议先让模型生成 mockup、schema、数据模型和 POC，再投入长链路执行。两者共同指向同一原则：先压缩交互与返工，再扩大自治范围。",
        "成本下降带来的并非简单的价格战，而是可部署工作负载的边界扩张。Aaron Levie 认为，只要成本继续下降，总使用量就会上升；Swyx 已把这种廉价智能用于每周自动研究 SEO/AEO。下一阶段的差异化更可能来自把低成本推理嵌入持续循环、并用评估与分发反馈把循环跑起来，而不是一次性的聊天界面。"
    ],
    "filteredNote": "过滤掉了“still true”、产品预告、纯转发、日常感叹、无上下文的一句话评论等低信号内容。"
}

def card(type_, label, actor, meta, title, summary, points, why, tags, score, url):
    return {
        "type": type_, "typeLabel": label, "date": display_date,
        "actor": actor, "meta": meta, "title": title, "summary": summary,
        "keyPoints": points, "whyItMatters": why, "tags": tags,
        "qualityScore": score, "url": url
    }

digest["highSignalItems"] = [
    card("post", "观点动态", "Claude", "Claude · X 动态", "前沿模型套餐进入“容量配给”阶段", "Claude 表示，从 7 月 20 日起，Fable 5 将进入 Max 和 Team Premium，但仅提供 50% 的使用限额；Pro 和 Team Standard 则通过 usage credits 获得访问及一次性 $100 credit。官方同时承认需求难以预测，并承诺继续扩容。", ["高价值模型能力被纳入现有订阅层级", "不同套餐以额度与 credits 分流", "需求预测与容量建设仍是核心约束"], "这揭示了 AI 产品的现实：模型能力、算力容量与定价承诺必须被同时设计，额度机制会直接影响留存与信任。", ["产品", "商业化", "基础设施"], 92, "https://x.com/claudeai/status/2078302415804379218"),
    card("post", "观点动态", "Madhu Guru", "Meta AI · X 动态", "企业 Agent 的短板不是模型，而是 harness 与 evals", "Madhu Guru 认为，企业难以从基础聊天机器人走向更复杂的 Agent，关键障碍是缺少构建 harness 和评估体系的人才。评估既要清晰复现业务场景，也要同时覆盖离线和在线环节，并以足够高的标准推动模型能力边界。", ["先把业务用例编码为可重复评估", "offline 与 online evals 缺一不可", "评估标准决定 Agent 能被推进到什么程度"], "对团队来说，采购更强模型不能替代评估工程；没有任务 harness，能力提升很难转化为可靠的业务结果。", ["Agent", "评估", "企业AI"], 94, "https://x.com/realmadhuguru/status/2078131628262752550"),
    card("blog", "深度文章", "Anthropic Engineering", "Anthropic Engineering · 博客", "Managed Agents 将“大脑”与“手”拆开扩展", "Anthropic Engineering 发布了关于 Scaling Managed Agents 的文章，核心是将 Agent 的推理决策与执行环境解耦。与同日的产品更新结合看，Managed Agents 正沿着可控 sandbox 和私有工具接入的方向，降低把 Agent 接入真实系统时的运行与权限复杂度。", ["推理层与执行层解耦", "执行环境成为独立的扩展与治理单元", "面向真实系统的部署需要隔离和连接能力"], "Agent 的扩展瓶颈常在执行环境而非单次推理；这种架构使团队能分别演进模型策略、工具权限与运行基础设施。", ["Agent", "架构", "基础设施"], 91, "https://www.anthropic.com/engineering/managed-agents"),
    card("blog", "深度文章", "Claude Blog", "Claude · 博客", "自托管 sandbox 与 MCP 隧道补齐企业接入", "Claude Managed Agents 新增可由用户控制的 sandbox，并支持连接私有 MCP 服务器。这个组合让 Agent 可以在受控执行环境中调用企业内部工具，而不是把运行边界和工具访问完全交给外部托管环境。", ["sandbox 可由用户自行控制", "可接入私有 MCP 服务器", "执行隔离与内部工具连接同时推进"], "企业 Agent 落地的难点是权限、网络和数据边界；可控 sandbox 与 MCP 连接是把原型推进到生产的关键拼图。", ["Agent", "MCP", "安全"], 90, "https://claude.com/blog/claude-managed-agents-updates"),
    card("post", "观点动态", "Peter Steinberger", "Codex · X 动态", "浏览器自动化暴露出 Agent 的最后一公里摩擦", "Peter Steinberger 观察到 Codex 为给 GitHub PR 上传一张图片，需要操控 Chrome、定位评论框并处理 macOS 文件选择器；即使 GitHub 没有合适 API，Agent 仍会以 GUI 路径完成任务。他同时把 Codex 放在 VM 中运行，避免其抢占前台焦点。", ["缺失 API 会把 Agent 推向脆弱的 GUI 自动化", "桌面控制存在焦点与环境隔离问题", "VM 是当前降低干扰的实用边界"], "这不是模型“会不会点击”的问题，而是工具接口、隔离环境和失败恢复共同决定自动化是否可用。", ["Agent", "浏览器自动化", "工程"], 89, "https://x.com/steipete/status/2078318731785359634"),
    card("post", "观点动态", "Thariq", "Claude Code · X 动态", "先让 Agent 产出原型，再为长链路执行付费", "Thariq 建议，在生成最终结果前，先让模型构建 mockup、schema、数据模型或 POC。这样能更早发现目标并不值得继续投入，避免在错误方向上消耗大量 tokens。", ["先验证输出形态与约束", "用 schema 和 POC 暴露歧义", "把 token 预算投入已验证的路径"], "这是一条直接可执行的 Agent 工作流原则：把昂贵的自治执行拆成廉价、可审阅的中间产物。", ["Agent", "原型", "工作流"], 88, "https://x.com/trq212/status/2078189833445654714"),
    card("post", "观点动态", "Aaron Levie", "Box · X 动态", "更便宜的 AI 会扩大可部署工作负载", "Aaron Levie 的判断是，AI 成本下降会让整个生态系统、尤其终端客户受益，并带动总使用量增长；当前真正的瓶颈在于能否以成功且有成本效益的方式把 AI 部署到真实工作负载。", ["成本下降会放大需求而非只压缩价格", "部署成功率与单位经济性仍是瓶颈", "真实工作负载决定价值释放"], "这提醒 AI Builders 不要只看单位 token 价格：成本曲线的价值要通过可靠部署转化为新增任务和更高频使用。", ["市场", "部署", "成本"], 90, "https://x.com/levie/status/2078139206946459853"),
    card("post", "观点动态", "Swyx", "X 动态", "把 SEO/AEO 研究变成每周运行的 Agent 循环", "Swyx 建议将 Codex、Claude、Gemini 或 Devin 配置为每周自动研究 SEO/AEO 改进机会，并进一步追问：针对某个模型优化 AEO，是否会在该模型上产生不成比例的收益。观点的重点不是一次性生成内容，而是建立持续研究和验证的增长循环。", ["用 Agent 固化周期性研究任务", "区分通用 AEO 与模型特定优化", "将低成本推理接入增长反馈回路"], "可复用的 Agent 价值常来自持续运行的闭环；增长、内容与产品团队都可以把这类研究从临时项目改为常规基础设施。", ["AEO", "Agent", "增长"], 86, "https://x.com/swyx/status/2078244735794413786"),
    card("post", "观点动态", "Madhu Guru", "Meta AI · X 动态", "企业买的不是模型 API，而是合规交付能力", "谈及 Kimi 与 Google 的竞争时，Madhu Guru 指出，许多企业不会直接消费模型，而会经由 Google Cloud 获取服务，因为它们仍需要安全、数据驻留、合规以及芯片等保障。模型收入因此可能在云平台体系内重新分配，而非简单地从既有云厂商流失。", ["企业采购路径受安全与合规约束", "数据驻留和芯片供给属于产品的一部分", "模型竞争可被云平台的交付层吸收"], "对做企业 AI 的团队，模型能力只是供应链的一层；可销售性取决于能否满足组织级的基础设施与治理要求。", ["企业AI", "云", "合规"], 87, "https://x.com/realmadhuguru/status/2078210889778708744")
]

# Keep the archive and latest byte-for-byte equivalent in data terms.
for path in (archive_path, latest_path):
    with path.open("w", encoding="utf-8") as f:
        json.dump(digest, f, ensure_ascii=False, indent=2)
        f.write("\n")

with digests_path.open(encoding="utf-8") as f:
    digests = json.load(f)
digests = [d for d in digests if d.get("date") != date]
digests.insert(0, digest)
with digests_path.open("w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(json.dumps({"date": date, "items": len(digest["highSignalItems"]), "paragraphs": len(digest["dailyInsight"]["paragraphs"]), "digests": len(digests)}, ensure_ascii=False))
