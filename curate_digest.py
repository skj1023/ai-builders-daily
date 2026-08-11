import json, shutil
from pathlib import Path

root = Path.cwd()
date = '2026-08-12'
archive = root/'data/archive'/f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最重要的主线，是 AI 产品正在从“能不能调用模型”转向“能不能把模型安全地嵌入真实工作流”。Peter Yang 总结 Linear 的生产级 Agent 方法：先画清楚工作从哪里开始、上下文存在哪里、哪些动作算完成，以及何时必须由人复核；这说明 Agent 的核心难题不是再加一个 prompt，而是工作流建模、权限边界和可验证的完成定义。',
        '基础设施侧，Guillermo Rauch 提到 Vercel Sandbox 同时隔离计算与网络，并将 egress firewall 下放给更多用户；Anthropic 的工程文章也把“跨产品约束 Claude”作为系统工程问题来处理。两者共同指向一个判断：当 Agent 获得执行能力后，sandbox、网络出口、审计和恢复机制不再是附属安全层，而是产品体验本身的一部分。',
        '模型竞争继续向两个方向扩散：Claude Sonnet 5 将较低的 introductory pricing 永久化，Meta 的 Muse Spark 1.2 则以 open weights 方式释放 frontier-class 能力。前者压低了调用成本、加速应用试错，后者扩大了本地部署和后训练的空间；对 builders 来说，模型选择会越来越像成本、延迟、数据控制和可定制性的组合优化，而不是单纯追逐榜单第一。',
        '另一个值得注意的信号来自开发方法：Zara Zhang 建议让 Codex 对优秀网站做结构化拆解并在截图上标注设计理由，Swyx 的模型对比则显示“视觉复刻得像”和“理解用户意图”可能是两种不同能力。AI 辅助开发的杠杆正在从生成代码延伸到提炼范例、表达意图和评估结果；真正能拉开差距的团队，会把这些环节固化成可重复的反馈回路。'
    ],
    'filteredNote': '过滤掉了纯情绪表达、日常闲聊、无上下文转发、单句评论、空内容及缺乏事实增量的自我宣传等低信号内容。'
}

def post(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {'type':'post','typeLabel':'观点动态','date':date_,'actor':actor,'meta':meta,'title':title,'summary':summary,'keyPoints':points,'whyItMatters':why,'tags':tags,'qualityScore':score,'url':url}

def blog(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {'type':'blog','typeLabel':'深度文章','date':date_,'actor':actor,'meta':meta,'title':title,'summary':summary,'keyPoints':points,'whyItMatters':why,'tags':tags,'qualityScore':score,'url':url}

items = [
post('8月10日 · 周一','Peter Yang','Linear · X 动态','生产级 Agent 的第一步：先还原真实工作流','Peter Yang 总结了来自 Linear 团队的生产级 Agent 方法：不要从模型或 prompt 开始，而要先梳理工作如何启动、上下文在哪些系统里流动、哪些动作真正完成任务，以及哪些节点必须由人复核。这个框架把 Agent 开发从“做一个会聊天的功能”拉回到可观测、可验收的业务流程设计。',['先画出真实工作流，而不是先选模型','明确上下文来源、完成条件和人工复核点','生产质量来自流程建模与反馈闭环'], '它提供了一套可直接用于 Agent 项目评审的检查表，尤其适合避免 demo 成功、上线失控。',['Agent','产品','工程'],92,'https://x.com/petergyang/status/2086824976800436676'),
post('8月10日 · 周一','Guillermo Rauch','Vercel · X 动态','Agent 安全边界必须同时覆盖计算与网络','Guillermo Rauch 介绍 Vercel Sandbox 的双重隔离：既隔离计算环境，也隔离网络路径；他还指出仅靠 container isolation 不足以应对 frontier models，并提到 egress firewall 向所有用户开放。对 Agent 来说，阻止恶意或意外行为不仅是限制进程权限，也要控制它能访问和上传什么。',['microVM 用于强化计算隔离','网络出口控制是第二条关键安全边界','Sandbox 正从基础设施能力变成软件工厂的默认组件'], '它把 Agent 安全从抽象原则落到了可部署的架构边界：compute isolation 与 network isolation 缺一不可。',['Agent','工程','安全'],94,'https://x.com/rauchg/status/2086946535716393209'),
post('8月10日 · 周一','Matt Turck','MAD · X 动态','Agent 做得再好，数据底座坏了仍然无解','Matt Turck 用一条跨时代类比指出：从 Big Data、现代数据栈到 Gen AI，再到 Agentic AI，系统表面不断升级，但“底层数据有问题”始终是瓶颈。Agent 能调用更多工具只会放大错误、过期或不可追溯数据的影响，因此数据质量、权限和语义一致性依然是应用层竞争力。',['Agent 的可靠性受底层数据质量约束','工具数量不能替代上下文的准确性与可追溯性','数据治理是 Agent 产品的长期护城河'], '它提醒团队不要把 Agent 失败简单归因于模型能力，先检查数据和上下文供应链往往更有效。',['Agent','数据','研究'],89,'https://x.com/mattturck/status/2086882606638153882'),
post('8月10日 · 周一','Zara Zhang','Codex · X 动态','用可视化拆解把“审美”变成可学习的反馈','Zara Zhang 建议把优秀网站交给 Codex 分析，再让它截取完整页面并在图像上标注设计为何有效。这个方法把难以言传的设计判断转成具体范例、结构化解释和可复查产物，也适用于团队建立自己的设计评审语料。',['从真实范例而非抽象理论开始学习','让模型解释布局、层级与视觉决策','截图标注使设计反馈可共享、可复盘'], '这是一个低成本但高复用的 AI 辅助设计工作流，能缩短从参考到实现的距离。',['产品','设计','工程'],88,'https://x.com/zarazhangrui/status/2086758509979316423'),
post('8月11日 · 周二','Swyx','独立观察 · X 动态','模型评测正在分化为“像不像”与“懂不懂”','Swyx 用同一条指令让 GPT Luna Max 与 Claude Fable Ultracode 通过 fal 使用开放模型复刻 Grok Imagine，结果显示一个模型的视觉复刻更好，另一个对意图的理解更强。这个案例说明单一“最终效果”分数会掩盖不同能力维度，产品评测需要拆分视觉 fidelity、需求理解和执行可靠性。',['同一任务中不同模型的优势可能正交','视觉相似度不等于意图理解','复杂产品应建立多维评测而非单一榜单'], '它给 builders 一个实用提醒：选模型要按任务分解能力，不要把一次 demo 的观感当成通用结论。',['模型','评测','产品'],87,'https://x.com/swyx/status/2087045848022843451'),
post('8月10日 · 周一','Claude','Anthropic · X 动态','模型价格下探让更多 Agent 试验进入可行区','Claude 宣布 Claude Sonnet 5 的 introductory pricing 永久保持不变：每百万 input tokens 2 美元、output tokens 10 美元。价格承诺降低了高频 Agent 工作流的试错成本，也会迫使应用团队把注意力从“能否调用模型”转向单位任务成本、延迟和结果质量的综合优化。',['Sonnet 5 的试用价格转为长期价格','更低 token 成本扩大高频调用的可行场景','应用需要同时核算成本、延迟与成功率'], '模型价格是产品架构约束的一部分，永久价格信号会直接影响 Agent 的调用深度和商业模式。',['产品','市场','模型'],86,'https://x.com/claudeai/status/2086891169217122586'),
post('8月10日 · 周一','Aaron Levie','Box · X 动态','Frontier 能力开放权重，部署边界被重新画了一遍','Aaron Levie 认为 Meta 将 Muse Spark 1.2 以 open weights 发布意义重大：企业可以按自己的方式在本地或云端部署，并针对特定场景继续后训练。开放权重把模型竞争从 API 访问权扩展到部署控制、数据主权和定制能力，尤其会打开此前因合规或成本不可行的应用。',['open weights 降低企业部署依赖','本地部署与云部署可以按场景组合','后训练能力让垂直应用拥有更大控制权'], '对企业 builders 而言，模型可得性不只改变价格，也改变数据、合规和产品迭代的架构选择。',['模型','开源','企业'],90,'https://x.com/levie/status/2087009941806797206'),
post('8月10日 · 周一','Google Labs','Google Labs · X 动态','实验性 AI 产品的终点也可以是能力迁移','Google Labs 表示 Portraits experiment 将于 9 月 14 日结束，并计划把从 expert-grounded AI 中获得的经验融入其他 Google 产品。实验项目的价值不一定在于长期保留独立产品，也可能在于快速验证交互、收集反馈，再将成熟能力迁移到更大规模的产品体系。',['实验产品以快速反馈验证假设','结束实验不等于经验丢弃','专家知识 grounding 可迁移到其他产品'], '它提供了 AI 产品管理的另一种成功标准：实验的学习产出和能力迁移同样重要。',['产品','研究','实验'],82,'https://x.com/GoogleLabs/status/2086936798710923603'),
blog('8月12日 · 周三','Anthropic Engineering','Anthropic · Engineering Blog','把 Claude 约束在产品里：Agent 安全是持续演进的系统工程','Anthropic 回顾了如何在不同产品中逐步扩大 Claude 的操作权限，同时用隔离、权限、监控和恢复机制约束风险。文章的核心不是某一个安全开关，而是随着模型能力和工具范围增长，产品必须持续重做边界设计，让“能完成更多任务”和“无法造成不可接受的破坏”同时成立。',['权限要随产品场景和能力变化持续调整','隔离、监控、审计与恢复需要组合设计','安全边界必须进入产品架构而非上线前补丁'], '这是构建可执行 Agent 时最值得复用的工程视角：安全不是一次性审核，而是伴随能力增长的控制系统。',['Agent','安全','工程'],95,'https://www.anthropic.com/engineering/how-we-contain-claude'),
post('8月11日 · 周二','Thibault Sottiaux','Codex · X 动态','AI 编程产品的容量策略会直接影响开发者工作流','Thibault Sottiaux 宣布所有付费 ChatGPT Work 与 Codex 用户的 usage limits 已重置。虽然信息简短，但它反映出 coding agents 的产品体验越来越受配额、峰值容量和长任务连续性影响；对团队用户而言，限额策略本身已经是生产可用性的一部分。',['usage limits 是 coding agent 的核心产品变量','长任务需要稳定的容量与连续上下文','团队采购要评估配额策略而非只看模型名称'], '它是一个具体的产品运营信号：当 Agent 进入日常开发流程，容量管理会直接影响用户是否敢于把任务交给它。',['产品','工程','开发工具'],78,'https://x.com/thsottiaux/status/2086972933566857393')
]
data['highSignalItems'] = items
data['headline'] = '今日聚焦 Agent 工作流、安全边界、模型成本与开放权重：18 位 AI Builders、1 篇深度文章。'
data['editorNote'] = '每日汇总一线 AI Builders 的观点、文章和播客，过滤低信号内容，优先保留可验证、可复用、对构建者有长期价值的判断。'
for p in [archive, root/'data/latest.json']:
    with p.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

digests = root/'data/digests.json'
with digests.open(encoding='utf-8') as f:
    all_digests = json.load(f)
all_digests = [d for d in all_digests if d.get('date') != date]
all_digests.insert(0, data)
with digests.open('w', encoding='utf-8') as f:
    json.dump(all_digests, f, ensure_ascii=False, indent=2)
print(json.dumps({'date':date,'highSignalItems':len(items),'archive':str(archive),'latest':str(root/'data/latest.json'),'digestsUpdated':True}, ensure_ascii=False))
