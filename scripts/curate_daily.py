import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
date = "2026-09-02"
archive_path = root / "data" / "archive" / f"{date}.json"
latest_path = root / "data" / "latest.json"
digests_path = root / "data" / "digests.json"

data = json.loads(archive_path.read_text(encoding="utf-8"))

def item(type_, actor, meta, title, summary, key_points, why, tags, score, url, date_text):
    return {
        "type": type_,
        "typeLabel": {"post": "观点动态", "blog": "深度文章", "podcast": "播客摘录"}[type_],
        "date": date_text,
        "actor": actor,
        "meta": meta,
        "title": title,
        "summary": summary,
        "keyPoints": key_points,
        "whyItMatters": why,
        "tags": tags,
        "qualityScore": score,
        "url": url,
    }

high_signal = [
    item("post", "Thibault Sottiaux", "Codex · X 动态", "Codex 的真正阻力，可能不是能力而是迁移成本", "Thibault Sottiaux 直接询问：已经考虑过 Codex、却迟迟没有尝试的人，究竟被什么因素卡住。这个问题把 AI 编程产品的竞争从“模型能不能写代码”推进到采用障碍、工作流迁移和信任建立。", ["目标用户的未采用理由本身就是产品研究信号", "AI 编程工具的竞争包含工作流迁移成本", "能力宣传之外，降低首次尝试门槛同样关键"], "对正在做 AI 工具的人来说，用户为什么不用，往往比用户说喜欢什么更接近产品机会。", ["产品", "工程"], 82, "https://x.com/thsottiaux/status/2094588317245509959", "9月1日 · 周二"),
    item("post", "Peter Yang", "Personal agents · X 动态", "Personal agent 的规模化前提是可验证的信任", "Peter Yang 判断，信任会成为 Personal agent 采用的最大阻力，也会反过来成为最大驱动力。Agent 一旦触及个人数据、日程和外部操作，用户需要的不只是更强模型，还包括可解释边界、可控权限和稳定的行为预期。", ["信任是 Agent 采用的核心瓶颈", "权限、可解释性与可预测性是产品能力", "信任建立后会形成采用加速器"], "这为 Agent 产品定义了比“自动化更多任务”更重要的路线图：先让用户敢于授权，再扩大自治范围。", ["Agent", "产品"], 88, "https://x.com/petergyang/status/2094639655258091792", "9月1日 · 周二"),
    item("post", "Madhu Guru", "AI 产品 · X 动态", "PM 必须建立面向具体场景的模型能力地图", "Madhu Guru 认为，产品经理如果真正理解自己产品和用例对应的模型前沿，就能获得巨大的产品判断优势。关键不是背诵模型榜单，而是明确不同规模模型今天擅长什么、在哪里失败，以及这些差异如何改变产品设计。", ["按模型规模理解能力边界", "系统记录失败模式而非只看平均分", "产品决策需要连接模型前沿与具体用例"], "模型能力变化已经成为产品约束和机会来源；不会做场景化评测的 PM，很难持续做出高质量取舍。", ["产品", "研究"], 91, "https://x.com/realmadhuguru/status/2094591503981281503", "9月1日 · 周二"),
    item("post", "Guillermo Rauch", "DESIGN.md · X 动态", "把设计系统写成 Markdown，可能是治理 AI slop 的接口", "Guillermo Rauch 分享 DESIGN.md 的思路：用可读、可版本化的 Markdown 表达设计系统，从而在大组织里规模化传递设计品味。对 AI 生成界面而言，这类结构化规范不仅服务人类协作，也能成为模型生成与审查的共同上下文。", ["设计规则变成可版本控制的文本资产", "规范可同时服务人和生成模型", "规模化设计质量依赖共享上下文与审查机制"], "AI 生成速度越快，越需要把隐性的设计判断外显为机器可读、团队可协作的约束。", ["工程", "设计"], 90, "https://x.com/rauchg/status/2094541309579235680", "8月31日 · 周一"),
    item("post", "Guillermo Rauch", "AI 基础设施 · X 动态", "Coding tokens 需要像云资源一样被治理", "Guillermo Rauch 把 coding tokens 比作基础设施，并指出许多公司却只是把一把近似“无限额度”的钥匙交给团队。类比 AWS 的资源治理，AI 编程额度同样需要预算、权限、审计、配额和成本可见性，否则效率提升会转化为不可控支出。", ["Token 额度是可消耗的基础设施资源", "权限、预算、审计和配额应成为默认治理层", "Agent 编程成本需要产品化地暴露给团队"], "当 AI coding 从个人试验进入组织生产，成本控制和安全治理会成为基础设施，而不是财务补丁。", ["工程", "基础设施"], 92, "https://x.com/rauchg/status/2094523399280435630", "8月31日 · 周一"),
    item("post", "Aaron Levie", "开放权重模型 · X 动态", "数据优势正在从授权收入转向自有模型能力", "Aaron Levie 判断，开放权重基础模型变强、post-training 基础设施成熟并商业化后，拥有大量高质量数据的公司会出现新的模型化机会。数据拥有者不再只有把数据授权给外部实验室这一条路，也可以围绕自身场景训练和运营模型。", ["开放权重降低了定制模型的基础门槛", "post-training 基础设施正在商品化", "高质量专有数据可直接转化为模型能力"], "企业 AI 的护城河可能从“拥有数据”进一步升级为“能把数据持续训练成可用模型”。", ["研究", "工程", "Agent"], 91, "https://x.com/levie/status/2094650992818274514", "9月1日 · 周二"),
    item("post", "Aaron Levie", "AI 安全 · X 动态", "AI 安全攻防将成为 Agent 能力的高价值战场", "Aaron Levie 认为，随着 AI 安全事件增加，需要更先进的 AI Agent 来发现和阻止安全问题；目前 frontier models 在网络安全上领先，但开放模型正在快速追赶。这里的判断同时指向防御需求增长和模型能力扩散带来的攻防升级。", ["安全事件会推动 AI 安全 Agent 需求", "frontier models 当前仍有网络安全优势", "开放模型追赶会扩大安全能力的普及面"], "安全不是 Agent 的附属场景，而可能是最先证明高自治价值、也最需要严密评测的生产环境之一。", ["Agent", "研究", "安全"], 89, "https://x.com/levie/status/2094545525102235844", "8月31日 · 周一"),
    item("post", "Garry Tan", "GBrain · X 动态", "Agent 记忆的关键是检索评测，而不是把更多 LLM 塞进回路", "Garry Tan 分享了 GBrain 的新评测：针对无需 LLM-in-the-loop 的记忆回读，以及从 Agent transcript 保存和丰富记忆。这个方向把 Agent memory 从概念叙事拉回可测量的检索质量、写入策略和系统开销。", ["记忆回读可以在不调用 LLM 的情况下评测", "Agent transcript 是丰富长期记忆的重要输入", "memory-save 与 retrieval 应分别建立评测"], "Agent 是否真的“记得住”不能靠演示判断；可复现的读写评测会决定记忆系统能否进入生产。", ["Agent", "研究", "工程"], 93, "https://x.com/garrytan/status/2094462971598754010", "8月31日 · 周一"),
    item("post", "Dan Shipper", "AI 交互 · X 动态", "拟人化是交互工具，不应升级成事实判断", "Dan Shipper 区分了 AI 拟人化的有效与有害用法：当拟人化帮助用户理解、预测和使用 AI 时，它是有益的；当它制造恐慌，或诱导人们把模型与人类做不恰当比较时，就会误导产品和公共讨论。", ["拟人化可以降低复杂系统的理解成本", "产品隐喻必须服务可预测使用，而非制造情绪", "模型的道德与能力判断不能由拟人化替代"], "Agent 产品需要设计用户心智模型；好的隐喻能提升可用性，坏的隐喻则会放大错误授权和错误期待。", ["Agent", "产品", "交互"], 86, "https://x.com/danshipper/status/2094406185109647580", "8月31日 · 周一"),
    item("podcast", "Training Data", "Rich Sutton & Khurram Javed · 播客", "模型为何停止学习：从训练终点回到持续适应", "Rich Sutton 与 Khurram Javed 讨论 AI 模型为何会停止学习，以及如何让学习重新发生。核心问题不是一次性训练能否把知识压缩进去，而是模型在部署后如何继续从反馈、环境和任务中获得有效经验，同时避免灾难性遗忘与失控更新。", ["静态训练与持续学习之间存在结构性断层", "部署后的反馈和经验可能是下一阶段能力来源", "持续学习必须同时解决稳定性、评测与安全控制"], "如果模型只能在发布前学习，Agent 就很难真正适应长期任务；持续学习是从工具走向可靠协作者的基础议题。", ["研究", "模型", "Agent"], 88, "https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8", "8月18日 · 周二"),
]

data["headline"] = "今天的信息流集中在 Agent、工程、研究、产品：精选 10 条高信号内容。"
data["dailyInsight"] = {
    "paragraphs": [
        "今天最清晰的主线是：AI 产品的瓶颈正在从“模型能做什么”转向“用户敢不敢把真实工作交给它”。Peter Yang 把信任视为 Personal agent 采用的最大阻力与最大驱动力；Thibault Sottiaux 对 Codex 未采用原因的追问，则把问题落到了迁移成本、权限边界和首次体验上。",
        "工程侧的共识更具体：Agent 的资源和行为都需要治理。Guillermo Rauch 将 coding tokens 类比基础设施，意味着额度、预算、权限、审计和成本可见性要进入默认架构；Garry Tan 则用 GBrain 的 retrieval 与 memory-save evals 说明，记忆系统不能靠演示取信，必须拆成可复现的读写指标。",
        "模型能力的快速扩散正在重写企业 AI 的机会结构。Madhu Guru 建议 PM 建立面向具体用例的模型能力与失败地图；Aaron Levie 进一步指出，开放权重模型和 post-training 基础设施成熟后，拥有专有数据的企业可以从出售数据转向训练、部署自己的场景模型。",
        "最后两条信号分别指向质量与长期性：DESIGN.md 把设计品味变成可版本化、可供模型消费的文本规范，持续学习讨论则提醒我们，静态发布的模型距离长期可靠的 Agent 仍有距离。今天值得带走的判断是：下一轮竞争不只在模型参数，而在上下文、治理、评测和持续适应组成的系统能力。"
    ],
    "filteredNote": "过滤掉了寒暄、表情、无上下文短句、纯产品站队和无实质增量内容等低信号内容"
}
data["highSignalItems"] = high_signal

for path in (archive_path, latest_path):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

history = json.loads(digests_path.read_text(encoding="utf-8"))
history = [d for d in history if d.get("date") != date]
history.insert(0, data)
digests_path.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"date": date, "highSignalItems": len(high_signal), "paragraphs": len(data["dailyInsight"]["paragraphs"]), "files": [str(archive_path), str(latest_path), str(digests_path)]}, ensure_ascii=False))
