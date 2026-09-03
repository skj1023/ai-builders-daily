import json
from pathlib import Path

root = Path.cwd()
date = '2026-09-04'
archive = root / 'data' / 'archive' / f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最明确的产品信号，是 AI 正在从“回答”转向“代办”。Claude 已能在 Claude Cowork 和 Claude Code 中后台操作电脑，点击、输入并打开应用；Zara Zhang 则指出，会议转录的主要消费者可能不再是人，而是后续要执行任务的 Agent。两者共同指向一种新的产品范式：界面和记录系统的价值，越来越取决于能否成为可靠的执行输入。',
        '模型能力商品化后，产品层需要替用户隐藏复杂度。Madhu Guru 认为 AI 产品应逐步抽象掉模型选择，让用户只关心任务是否完成；Thariq 关于 effort 切换不再破坏 prompt cache 的说明，则让后台可以按任务风险动态分配推理预算。前者降低用户认知负担，后者降低系统调度成本，二者都是 Agent 从“能用”走向“愿意长期用”的基础。',
        '企业 AI 的竞争也正在从模型发布转向真实工作流验证。Boris Cherny 展示 Claude Tag 从 Slack 和指标表中生成管理层材料，并主动发现供应商报告与内部数据不一致；Aaron Levie 则强调非结构化企业任务的评测提升。对于 builders 来说，真正有壁垒的不是再包一层聊天框，而是把数据接入、事实核验、权限边界和结果交付做成可重复评测的闭环。',
        '组织和模型生态的信号显示，速度与开放性仍在同时加速。Thibault Sottiaux 将 OpenAI 描述为强调 ownership、care 和 pace 的“mega startup”；Aaron Levie 认为如果 Muse 的新能力以 open weights 发布，将改变美国开放权重模型的竞争格局。与此同时，今天的信息流中也有大量日常闲聊、活动宣传和口号式表达，说明在高噪声环境里，持续筛选事实增量与长期判断本身就是信息产品的核心能力。'
    ],
    'filteredNote': '过滤掉了校园大使招募、活动宣传、日常闲聊、政治话题、纯口号、单句评论、无上下文互动及正文不足以支撑核心观点的播客摘录。'
}

def post(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {
        'type': 'post', 'typeLabel': '观点动态', 'date': date_, 'actor': actor,
        'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points,
        'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url
    }

items = [
    post('9月2日 · 周三', 'Claude', 'Claude · X 动态', 'AI 助手开始在后台直接操作电脑',
         'Claude 宣布，Claude Cowork 和 Claude Code 现在可以在后台使用电脑：点击、输入并打开应用，同时让用户继续处理其他工作。这使 Agent 从提供建议进一步走向代替用户完成桌面流程，也把任务隔离、权限控制和可观察性推到产品设计的中心。',
         ['支持后台点击、输入和打开应用', '用户可在 Agent 执行期间继续工作', '桌面自动化需要同步考虑权限与安全边界'],
         '后台 computer use 把 Agent 的价值从“生成答案”扩展到“持续完成任务”，是交互范式的重要变化。',
         ['Agent', 'Computer Use', '自动化'], 95, 'https://x.com/claudeai/status/2095226833293685100'),
    post('9月2日 · 周三', 'Boris Cherny', 'Claude Code · X 动态', '企业 Agent 的关键能力是发现数据之间的矛盾',
         'Boris Cherny 展示 Claude Tag 使用 Slack 和指标表等多源数据制作临时管理层演示，并发现供应商报告与内部数字不一致后主动标记。这个案例说明企业 Agent 的价值不只是汇总内容，而是跨来源核验事实、暴露冲突并在交付前阻止错误继续传播。',
         ['跨 Slack、指标表等来源组织材料', '识别供应商报告与内部数据的不一致', '事实核验应成为工作流中的主动步骤'],
         '企业场景最难的往往不是生成文本，而是保证结论可追溯、冲突可见、错误不会静默进入决策材料。',
         ['企业 AI', '数据核验', 'Agent'], 94, 'https://x.com/bcherny/status/2095276133214491086'),
    post('9月2日 · 周三', 'Madhu Guru', 'Meta AI · X 动态', 'AI 产品应把模型选择藏到任务完成之后',
         'Madhu Guru 认为，AI 产品应持续抽象模型选择，因为用户真正关心的是事情是否完成，而不是底层使用哪个模型。让用户频繁挑模型会增加认知负担；更成熟的产品应根据任务、质量要求和成本在后台完成路由，并用结果质量承担选择责任。',
         ['用户关心任务结果而非模型名称', '模型选择会带来额外认知负担', '智能路由应由产品承担而不是转嫁给用户'],
         '模型菜单适合专家调试，却未必适合大众产品；把复杂性留在系统内部，是 AI 产品体验成熟的重要标志。',
         ['产品设计', '模型路由', 'Agent'], 92, 'https://x.com/realmadhuguru/status/2095174463696589223'),
    post('9月3日 · 周四', 'Thariq', 'Claude Code · X 动态', '推理预算可以动态切换而不牺牲上下文缓存',
         'Thariq 说明，effort levels 在 API 上线后，切换推理强度将不再破坏 prompt cache，Claude Code 预计随后支持。这样一来，系统可以针对低风险任务使用较低 effort、针对复杂任务提高预算，同时继续复用已有上下文，不必在质量、延迟和缓存效率之间做粗糙取舍。',
         ['低风险任务可使用更低推理强度', '切换 effort 不再破坏 prompt cache', '任务路由可同时优化质量、延迟与成本'],
         '这是 Agent runtime 的关键基础能力：推理深度应成为可编排的运行时参数，而不是固定的全局设置。',
         ['推理', 'Prompt Cache', '运行时'], 93, 'https://x.com/trq212/status/2095367584489038044'),
    post('9月3日 · 周四', 'Zara Zhang', '独立 Builder · X 动态', '会议记录的下一位读者可能是 Agent',
         'Zara Zhang 观察到，人们既不读 AI 会议摘要，也很少回听录音，团队真正保留下来的可能是供 Agent 消费的转录文本。这个转变意味着记录系统的评价标准会从“人读起来是否漂亮”转向“机器能否准确提取状态、决策、责任人与下一步动作”。',
         ['转录内容可作为 Agent 的长期输入', '摘要不应只服务于会后人工阅读', '记录格式需要支持状态与行动的可靠提取'],
         '它提示 builders 重新思考知识管理：最有价值的内容不一定是给人看的总结，而可能是能驱动后续执行的结构化上下文。',
         ['Agent', '知识管理', '工作流'], 91, 'https://x.com/zarazhangrui/status/2095375073381318656'),
    post('9月2日 · 周三', 'Aaron Levie', 'Box · X 动态', '模型进步必须在非结构化企业工作中兑现',
         'Aaron Levie 认为，近期 AI 发布速度正在明显加快，并指出如果 Muse 的新模型以 open weights 发布，将改变美国开放权重模型的竞争格局。这里的判断同时包含两层信号：能力进步正在加速，而开放权重的可获得性会进一步改变部署、成本和生态竞争的结构。',
         ['模型能力发布节奏正在加快', 'open weights 会影响生态与竞争格局', '开放性将联动部署成本和开发者选择'],
         '对 builders 而言，模型能力本身只是变量；是否开放、能否部署以及由此形成的生态才决定长期产品机会。',
         ['模型生态', 'Open Weights', '竞争格局'], 88, 'https://x.com/levie/status/2095234253613359200'),
    post('9月3日 · 周四', 'Thibault Sottiaux', 'OpenAI · X 动态', '高速度组织文化正在成为 AI 公司的产品能力',
         'Thibault Sottiaux 将 OpenAI 描述为“mega startup”，并强调 extreme ownership、care 和 pace。虽然这是内部观察而非量化研究，但它提供了一个有用的组织判断：在模型和产品快速迭代的环境中，责任边界清晰、对结果负责与高执行速度可能共同构成竞争优势。',
         ['强调 extreme ownership', '速度与对工作质量的 care 同时存在', '组织节奏会影响模型产品迭代速度'],
         'AI 产品的竞争不只发生在模型和代码层；能否持续把研究、工程与产品决策快速闭环，同样决定长期产出。',
         ['组织', '产品开发', 'AI 公司'], 84, 'https://x.com/thsottiaux/status/2095369901137654271'),
    post('9月2日 · 周三', 'Aditya Agarwal', 'AI 创业与研究 · X 动态', '不要只为今天的模型能力创业',
         'Aditya Agarwal 认为，很多创业公司只围绕当前模型的问题或能力设计产品，更有价值的做法是对一年后的能力边界形成明确判断。这个观点把产品机会从“模型现在能做什么”推进到“能力进步后哪些工作流会被重新定义”，要求团队把技术趋势转化为具体的长期产品假设。',
         ['避免只针对当前模型缺陷做产品', '对一年后的能力边界形成 POV', '技术判断需要转化为产品与工作流假设'],
         '模型快速迭代会压缩跟随式产品的窗口；对未来能力的判断，可能比今天的功能拼装更能形成持久差异化。',
         ['AI 创业', '产品战略', '模型演进'], 92, 'https://x.com/adityaag/status/2095192873973301601')
]

data['highSignalItems'] = items
data['headline'] = '今日聚焦后台 Agent、企业事实核验、模型路由与开放权重：15 位 AI Builders、8 条高信号卡片。'
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

print(json.dumps({'date': date, 'highSignalItems': len(items), 'archive': str(archive), 'latest': str(root / 'data/latest.json'), 'digestsUpdated': True}, ensure_ascii=False))
