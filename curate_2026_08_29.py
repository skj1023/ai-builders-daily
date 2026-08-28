import json
from pathlib import Path

root = Path.cwd()
date = '2026-08-29'
archive = root / 'data' / 'archive' / f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最强的产品信号，是 AI 正从“提供答案”走向“在真实系统里代办任务”。Thibault Sottiaux 描述 ChatGPT 在不直接接触用户凭证的前提下完成购物、叫车和预约，Josh Woodward 则把书籍变成可调用的个人知识库。对 builders 来说，下一阶段的竞争不只是模型聪明，而是身份、权限、上下文和外部动作能否被安全地编排。',
        'Agent 的可靠性越来越依赖上下文与边界设计。Peter Yang 观察到用户已经习惯让 ChatGPT、Grok 等工具处理电脑和浏览器任务，却不愿为每个新产品重复注册、登录和交付上下文；Madhu Guru 则建议企业建设 model-agnostic 的 AI 栈，并先用覆盖业务结果的 eval suite 衡量系统。两条信号合起来说明，持久上下文、可替换模型和可验证结果会比单一模型品牌更接近生产级护城河。',
        '工程侧的关键变化是 Agent 正获得更强执行权限，但软件护栏必须同步升级。Guillermo Rauch 将新工具描述为 agent-native devtool，Aaron Levie 则强调软件在数据管理、业务逻辑、访问治理和数据保护方面提供不可替代的 guardrails；Sam Altman 对 AI 网络防御窗口的紧迫判断，也把安全从合规议题推成基础设施议题。能否让 Agent 做更多事，最终取决于隔离、审计、审批和恢复机制是否足够成熟。',
        '模型生态和组织采用也在进入规模化阶段。Claude 面向 10,000 名科学家推出带折扣的 Team 计划，说明 AI 厂商正在通过垂直人群和价格设计培育高价值使用场景；播客中围绕 2029 年超智能时间表的讨论，则提醒 builders：能力增长的速度与安全治理的速度可能不匹配。产品机会与系统性风险正在同一条曲线上加速，长期赢家需要同时建设交付能力和控制能力。'
    ],
    'filteredNote': '过滤掉了纯情绪表达、日常闲聊、无上下文转发、单句评论、非 AI 话题及缺乏事实增量的自我宣传等低信号内容。'
}

def card(type_, label, date_, actor, meta, title, summary, points, why, tags, score, url):
    return {
        'type': type_, 'typeLabel': label, 'date': date_, 'actor': actor,
        'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points,
        'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url
    }

items = [
    card('post', '观点动态', '8月27日 · 周四', 'Sam Altman', 'OpenAI · X 动态',
         'AI 网络防御进入必须立即行动的窗口期',
         'Sam Altman 判断，AI 网络防御正处在极其关键的时刻，留给行业采取行动的时间不多，并呼吁 OpenAI、竞争对手和合作伙伴共同应对。它把 AI 安全从单一公司的产品责任提升为需要集体响应的基础设施问题。',
         ['AI 正改变网络防御的攻防节奏', '安全准备不能等到能力完全成熟之后', '需要跨公司、跨生态的集体响应'],
         '对构建模型、Agent 和开发平台的团队而言，安全能力应被当作核心产品与基础设施，而不是发布后的附加项。',
         ['安全', '网络防御', '治理'], 94, 'https://x.com/sama/status/2093060670472241368'),
    card('post', '观点动态', '8月27日 · 周四', 'Claude', 'Anthropic · X 动态',
         '用科学家定价把 AI 推进专业工作流',
         'Claude 宣布面向各领域 10,000 名科学家提供 Team 计划：标准席位免费，premium 席位一年内以每月 15 美元、5 倍使用额度和 80% 折扣提供。这个方案不是单纯降价，而是在明确的专业人群中降低试用门槛、扩大高价值反馈来源。',
         ['目标用户覆盖数学、化学、物理等科学领域', '标准席位免费，premium 席位提供 5 倍用量', '通过一年期折扣培育专业场景采用'],
         '垂直用户、使用额度和反馈闭环正在成为 AI 产品商业化设计的组合变量，值得 builders 参考。',
         ['产品', '商业化', '科学计算'], 91, 'https://x.com/claudeai/status/2093059087298601113'),
    card('post', '观点动态', '8月27日 · 周四', 'Thibault Sottiaux', 'ChatGPT · X 动态',
         'Agent 代办现实任务的前提是凭证隔离',
         'ChatGPT 已能处理购物、叫车和预约等网页任务，同时不直接接触用户的实际凭证，并强调保持安全。这个产品信号说明，Agent 的价值正在从信息检索转向外部执行，而凭证、授权和风险隔离会决定用户是否敢把真实事务交给它。',
         ['任务从问答扩展到购物、叫车和预约', '执行流程不必暴露用户实际凭证', '安全授权是消费级 Agent 规模化的前提'],
         '一旦 Agent 开始代表用户行动，身份与权限架构就和模型能力同等重要。',
         ['Agent', '身份', '安全'], 92, 'https://x.com/thsottiaux/status/2093074717590921245'),
    card('post', '观点动态', '8月28日 · 周五', 'Peter Yang', 'AI 产品观察 · X 动态',
         '新 AI 产品首先要解决上下文迁移成本',
         'Peter Yang 说自己每天收到 3 至 5 个新 AI 产品测试请求，但几乎都要求重新注册账号并登录独立网站或应用；与此同时，他已经习惯让 ChatGPT、Grok 等工具处理电脑和浏览器任务。用户真正抗拒的不是尝试新模型，而是重复搬运身份、历史和工作上下文。',
         ['重复注册和登录是新产品的首要摩擦', '用户希望 Agent 直接利用已有上下文', '跨应用身份与上下文迁移是产品入口'],
         '对 builders 来说，减少 setup friction 可能比再增加一个模型功能更能决定产品是否进入日常工作流。',
         ['产品', 'Agent', '上下文'], 90, 'https://x.com/petergyang/status/2093126719888916616'),
    card('post', '观点动态', '8月28日 · 周五', 'Madhu Guru', 'Meta AI · X 动态',
         '企业 AI 栈应先追求模型无关与可评测',
         'Madhu Guru 建议企业 AI 负责人把最高杠杆放在 model-agnostic 的技术栈上，并优先建设完整覆盖业务用例和业务结果的 eval suite。核心判断是：企业不应把生产系统绑定在单一模型上，也不能只用通用 benchmark 代替真实结果评估。',
         ['先建设覆盖真实用例的 eval suite', '评测必须连接业务结果而非只看模型分数', '模型无关降低供应商切换与迭代风险'],
         '这是一条可直接落地的企业 AI 架构原则：先把结果定义清楚，再选择和替换模型。',
         ['工程', '评测', '企业 AI'], 93, 'https://x.com/realmadhuguru/status/2093143877087879377'),
    card('post', '观点动态', '8月27日 · 周四', 'Guillermo Rauch', 'Vercel · X 动态',
         'Agent-native 工具正在改变开发工具的设计起点',
         'Guillermo Rauch 表示，Vercel 的新工具源自内部 WebGPU 技术实践，并且从一开始就是为 agents 设计、而非只为人类设计。这个方向意味着开发工具的接口、可观察性和任务组织方式，可能会围绕机器执行重新设计，而不是简单把现有 IDE 接上模型。',
         ['产品从内部高置信技术实践中孵化', '工具以 agent-native 而非 human-only 为设计起点', '开发工具的交互和接口将面向机器执行重构'],
         '当 Agent 成为一等使用者，工具的可组合性、结构化输出和可验证状态会成为新的产品基本功。',
         ['Agent', '开发工具', '产品'], 89, 'https://x.com/rauchg/status/2093019310725951683'),
    card('post', '观点动态', '8月28日 · 周五', 'Aaron Levie', 'Box · X 动态',
         '企业软件的护栏决定 AI 能否真正进入业务',
         'Aaron Levie 认为，软件与 AI 的关系之所以重要，是因为软件负责数据管理、工作流业务逻辑、信息访问治理和数据保护。AI 可以增强执行能力，但企业真正依赖的是这些可控的系统边界。',
         ['软件承载数据管理与业务逻辑', '访问治理和数据保护是 AI 落地护栏', 'AI 应嵌入既有软件控制面而非脱离系统运行'],
         '这解释了为什么企业 AI 的长期价值往往属于拥有工作流和治理层的平台，而不只是模型提供商。',
         ['企业 AI', '工作流', '治理'], 90, 'https://x.com/levie/status/2093192697331011846'),
    card('post', '观点动态', '8月27日 · 周四', 'Josh Woodward', 'Google Notebook · X 动态',
         '把书本知识变成可调用的项目上下文',
         'Josh Woodward 介绍 Notebook 的新方式：购买书籍后放入 Notebook，把作者的经验应用到自己的项目；同时该计划与作者和出版商共同设计，以触达更投入的新读者。产品把静态内容转成围绕具体任务的个人知识库，也为内容版权方提供新的分发路径。',
         ['内容可以被导入个人项目上下文', 'AI 将阅读从消费转向任务应用', '作者和出版商参与设计商业分发模式'],
         '知识产品的机会不只是生成摘要，而是让高质量内容在用户真实项目中持续发挥作用。',
         ['知识库', '产品', '内容生态'], 87, 'https://x.com/joshwoodward/status/2093070717508296923'),
    card('blog', '深度文章', '8月29日 · 周六', 'Anthropic Engineering', 'Anthropic · Engineering Blog',
         'Agent 能力增长后，产品必须持续重做安全边界',
         'Anthropic 回顾了如何在不同产品中约束 Claude：随着模型从对话走向更强的工具调用和系统操作，原本不可接受的权限边界会被重新评估。文章的核心不是某个单一安全开关，而是通过隔离、权限控制、监控和恢复机制，让能力扩张与风险控制同步演进。',
         ['安全边界要随模型能力和产品场景持续调整', '隔离、权限、监控与恢复需要组合设计', 'Agent 安全是持续迭代的系统工程'],
         '这是构建可执行 Agent 时最值得复用的工程视角：安全不是上线前审核，而是伴随能力增长的控制系统。',
         ['Agent', '安全', '工程'], 95, 'https://www.anthropic.com/engineering/how-we-contain-claude'),
    card('blog', '深度文章', '6月18日 · 周四', 'Claude Blog', 'Anthropic · 产品博客',
         '让 Claude Code 的工作过程变成可分享的活文档',
         'Claude Code 支持把工作进展捕获为 artifact，并生成会随会话更新的可分享页面，例如 PR walkthrough、系统说明、dashboard 和 release checklist。它把 Agent 的中间产物从聊天记录提升为可复用、可审阅的工作界面。',
         ['artifact 可承载 PR walkthrough 和系统说明', '页面会随着工作会话持续更新', 'Agent 输出从文本答案扩展到可协作界面'],
         '可审阅、可分享、会更新的工作产物，有助于把 Agent 从个人助手接入团队协作和交付流程。',
         ['Agent', '开发工具', '协作'], 88, 'https://claude.com/blog/artifacts-in-claude-code')
]

data['highSignalItems'] = items
data['headline'] = '今日聚焦 Agent 执行边界、上下文迁移、企业护栏与安全工程：10 条高信号卡片。'
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
