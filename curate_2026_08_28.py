import json
from pathlib import Path

root = Path.cwd()
date = '2026-08-28'
archive = root / 'data' / 'archive' / f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最强的产品信号是：AI 助手正在从“回答问题”进入“代替用户完成网页任务”。Claude 在 Cowork 中内置独立浏览器，能够导航网页、填写表单并完成任务，同时把浏览器环境与用户自己的登录态隔离；Claude in Chrome 则面向已经登录的真实浏览器流程。对 builders 来说，浏览器不再只是展示层，而是 Agent 执行、权限和失败恢复的工作现场。',
        '执行可靠性正在成为 Agent 产品的核心体验。Thariq 把 SendFeedback 做成 Claude 可调用的工具，让 Agent 起草反馈、由用户批准后提交；Guillermo Rauch 则展示 security check CLI，支持人工在环或定时运行，并把安全检查纳入可重复的工程流程。两者共同说明，Agent 不应只追求自动化率，还要把反馈、批准、审计和周期性运行设计成一等能力。',
        '基础设施和模型生态继续向“规模化可用”推进。Vercel 的全球计算能力覆盖多区域、故障转移和大规模并发 sandbox；Matt Turck 认为 NVIDIA、Nemotron 与 Hugging Face 的组合强化了开放 AI 的基础设施中心。与此同时，Aditya Agarwal 对 DeepCogito 的判断把竞争焦点放到 post-training、强化学习和递归自我改进。模型能力之外，算力调度、开放权重与后训练方法正在共同决定 builders 的实际选择空间。',
        '商业化信号也更具体了：Aaron Levie 分享 Box 季报时指出，企业 AI 需求正在转化为可量化的收入增长与指引上调。结合 Claude 将浏览器能力扩展到付费用户，可以看到 AI 产品的竞争已经从“是否有模型功能”转向“能否嵌入真实工作流并让组织持续付费”。快速发布固然重要，但真正的长期价值来自可靠执行、可治理反馈和可解释的商业结果。'
    ],
    'filteredNote': '过滤掉了纯情绪表达、日常闲聊、无上下文转发、单句评论、空内容及缺乏事实增量的自我宣传等低信号内容。'
}

def card(type_, label, date_, actor, meta, title, summary, points, why, tags, score, url):
    return {
        'type': type_, 'typeLabel': label, 'date': date_, 'actor': actor,
        'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points,
        'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url
    }

items = [
    card('post', '观点动态', '8月26日 · 周三', 'Claude', 'Claude · X 动态',
         '浏览器成为 Agent 的执行工作台',
         'Claude 宣布 Cowork 内置独立浏览器：当任务涉及网站时，浏览器会在侧边栏打开，由 Claude 导航、填写表单并完成任务。它与用户自己的浏览器和登录态保持分离，说明 Agent 浏览正在从简单网页访问走向有隔离边界的任务执行环境。',
         ['浏览器直接嵌入 Cowork 的任务流程', '支持导航、填写表单和完成网页工作', '独立于用户浏览器与登录态，降低权限耦合'],
         '网页是大量真实业务流程的入口；把浏览器做成受控执行环境，是 Agent 从聊天走向生产力工具的关键一步。',
         ['Agent', '浏览器', '产品'], 94, 'https://x.com/claudeai/status/2092755571455758427'),
    card('post', '观点动态', '8月26日 · 周三', 'Thariq', 'Claude Code · X 动态',
         '让 Agent 参与反馈闭环，但把提交权交给用户',
         'Thariq 介绍 Claude 的 SendFeedback tool：用户不必手动打开反馈入口和撰写报告，而是让 Claude 起草反馈，再由用户审阅和批准。这个设计把产品反馈变成 Agent 可调用的工作流，同时保留人类对外部提交的最终控制。',
         ['Agent 可以起草结构化反馈', '用户批准后才真正提交', '反馈入口从手动表单变成对话式工具'],
         '这是一个可复用的人机协作模式：让 Agent 降低记录和整理成本，但在会产生外部影响的动作前保留明确的 approval gate。',
         ['Agent', '反馈', '人机协作'], 92, 'https://x.com/trq212/status/2092696449616376140'),
    card('post', '观点动态', '8月26日 · 周三', 'Guillermo Rauch', 'Vercel · X 动态',
         '安全检查也应该成为可调度的 Agent 工作流',
         'Guillermo Rauch 分享 Vercel security check CLI 与安全 dashboard：用户可以让 Agent 在 human-in-the-loop 模式下改善安全状态，也可以安排 cron 定期运行。安全能力因此不再只是一次性扫描，而是可以被持续执行、复核和运营的工程流程。',
         ['CLI 与 dashboard 同时覆盖人工与自动流程', '支持 Agent 辅助改善 security posture', 'cron 让安全检查进入持续运营'],
         '对 AI 产品和基础设施团队而言，安全检查只有进入日常工作流并能持续复跑，才不会停留在发布前的合规仪式。',
         ['工程', '安全', 'Agent'], 91, 'https://x.com/rauchg/status/2092621371914482026'),
    card('post', '观点动态', '8月26日 · 周三', 'Guillermo Rauch', 'Vercel · X 动态',
         'Agent 基础设施开始按全球规模设计',
         'Guillermo Rauch 描述面向 Agent 的全球计算能力：多区域部署、故障转移、默认可 ramp 到 10,000 个并发 sandbox 和每分钟 5,000 个 vCPU，并计划继续扩展区域。这个信号表明，Agent 平台的关键指标正在从单次调用延迟扩展到突发任务、隔离环境和跨区域韧性。',
         ['多区域与 failover 面向持续运行的 Agent', '大规模并发 sandbox 成为平台能力', '容量 ramp 与区域扩展直接影响任务可靠性'],
         '当 Agent 能同时发起大量代码和工具任务时，调度、隔离、容量和故障转移会成为产品体验的一部分，而不是底层实现细节。',
         ['Agent', '基础设施', '弹性'], 90, 'https://x.com/rauchg/status/2092735785460277627'),
    card('post', '观点动态', '8月26日 · 周三', 'Aaron Levie', 'Box · X 动态',
         '企业 AI 需求开始反映在可量化的经营结果里',
         'Aaron Levie 分享 Box Q2 业绩：季度收入为 3.211 亿美元，同比增长 9%（按固定汇率为 11%），并将全年收入目标上调至 12.90 亿美元；他表示增长受到企业 AI 需求推动。相比只展示功能，这类经营数据提供了应用型 AI 进入企业预算后的真实验证。',
         ['Box Q2 收入 3.211 亿美元', '固定汇率增长率达到 11%', '企业 AI 需求被纳入增长与全年指引'],
         'builders 需要关注的不只是模型能力和用户热度，还要验证 AI 功能是否能进入客户预算、改善工作流并转化为持续收入。',
         ['企业 AI', '商业化', '产品'], 89, 'https://x.com/levie/status/2092702955292230100'),
    card('post', '观点动态', '8月27日 · 周四', 'Matt Turck', 'FirstMark · X 动态',
         '开放 AI 的新组合：算力、模型与分发平台彼此强化',
         'Matt Turck 认为 NVIDIA、Nemotron 与 Hugging Face 的组合形成了对开放源代码 AI 的多重利好：NVIDIA 强化其基础设施和模型中心角色，Hugging Face 获得更稳定的平台归属，开放模型生态则得到更强的分发与资源支持。这个判断把一次合作看成开放 AI 供应链的结构变化，而不只是单一产品发布。',
         ['NVIDIA 正同时靠近算力与开放模型生态', 'Hugging Face 获得更强的平台支持', '开放模型的分发、资源和商业基础更稳固'],
         '对 builders 来说，开放权重能否真正形成生产力，取决于模型、算力、工具链和分发渠道是否能一起降低采用成本。',
         ['开放模型', '生态', '基础设施'], 88, 'https://x.com/mattturck/status/2092808287280329097'),
    card('post', '观点动态', '8月26日 · 周三', 'Aditya Agarwal', 'DeepCogito · X 动态',
         '模型竞争的下一站是 post-training 与递归改进',
         'Aditya Agarwal 介绍 DeepCogito 完成 4,300 万美元 Series A，并将其定位为 post-training research lab，重点研究大规模强化学习、递归自我改进，以及 iterated distillation and amplification（IDA）。这代表模型进步的关注点继续从预训练规模扩展到如何通过训练后反馈持续放大能力。',
         ['DeepCogito 聚焦 post-training', '研究方向包含大规模强化学习与递归自我改进', 'IDA 试图迭代放大模型能力'],
         '如果 post-training 成为主要能力来源，builders 的模型选择会更关注可定制性、反馈数据和训练闭环，而不只是现成 benchmark。',
         ['研究', 'Post-training', '强化学习'], 90, 'https://x.com/adityaag/status/2092679288869019700'),
    card('blog', '深度文章', '8月26日 · 周三', 'Claude Blog', 'Anthropic · 产品博客',
         'Claude in Chrome 面向所有付费用户开放',
         'Claude in Chrome 正式面向所有付费 Claude 计划开放，让 Claude 可以在用户已经登录的浏览器环境中协助完成网页工作。与 Cowork 的独立浏览器并行存在，说明产品正在同时覆盖“隔离执行”和“沿用既有登录态”两种工作流，核心取舍是便利性、权限范围与安全边界。',
         ['面向所有付费计划开放', '支持在用户现有浏览器和登录态中工作', '与 Cowork 独立浏览器形成互补路径'],
         '浏览器 Agent 的普及会把身份、授权、敏感操作和可追踪性推到产品设计中心，值得所有做自动化工具的团队参考。',
         ['Agent', '浏览器', '身份'], 93, 'https://claude.com/blog/claude-in-chrome-generally-available'),
    card('blog', '深度文章', '8月26日 · 周三', 'Claude Blog', 'Anthropic · 产品博客',
         'Cowork 用独立浏览器降低网页自动化的权限耦合',
         'Claude Blog 介绍 Cowork 的内置浏览器：浏览器位于桌面应用侧边栏，无需额外安装，并与用户自己的浏览器和登录信息分离。产品把网页操作封装在独立环境中，让 Agent 能完成网站任务，同时避免直接继承个人浏览器的全部状态。',
         ['浏览器内置于桌面应用', '与个人浏览器和登录态保持分离', '以侧边栏形式嵌入任务执行体验'],
         '这是一种清晰的安全产品化范式：先用隔离环境控制 Agent 的权限面，再逐步扩展它能完成的网页任务。',
         ['Agent', '安全', '桌面应用'], 92, 'https://claude.com/blog/cowork-built-in-browser')
]

data['highSignalItems'] = items
data['headline'] = '今日聚焦浏览器 Agent、执行反馈、全球基础设施与开放模型：16 位 AI Builders、9 条高信号卡片。'
data['editorNote'] = '每日汇总一线 AI Builders 的观点、文章和播客，过滤低信号内容，优先保留可验证、可复用、对构建者有长期价值的判断。'

for path in (archive, root / 'data' / 'latest.json'):
    with path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

digests = root / 'data' / 'digests.json'
with digests.open(encoding='utf-8') as f:
    all_digests = json.load(f)
all_digests = [d for d in all_digests if d.get('date') != date]
all_digests.insert(0, data)
with digests.open('w', encoding='utf-8') as f:
    json.dump(all_digests, f, ensure_ascii=False, indent=2)

print(json.dumps({'date': date, 'highSignalItems': len(items), 'archive': str(archive), 'latest': str(root / 'data' / 'latest.json'), 'digestsUpdated': True}, ensure_ascii=False))
