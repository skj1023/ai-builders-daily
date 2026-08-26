import json
from pathlib import Path

root = Path.cwd()
date = '2026-08-27'
archive = root / 'data' / 'archive' / f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最清晰的主线，是 AI 产品正在从“模型能不能回答”进入“系统能不能可靠地完成工作”。Claude 把 Chat 与 Cowork 的记忆统一，并允许用户逐条查看、编辑和删除；Peter Yang 分享的 /fuck-cancer skill 则用一份持续更新的 brief 维护患者信息、下一步行动、术语解释和更新日志。两者共同说明，真正有用的 AI 产品不是一次性输出，而是围绕长期上下文建立可控、可修订的工作状态。',
        'Agent 工程的瓶颈继续从推理能力转向执行边界。Guillermo Rauch 一方面用 QuickJS secure context 为动态 Code Mode 提供比完整 sandbox 更轻量的运行路径，另一方面把安全连接服务与数据称为构建 Agent 最难的问题；Swyx 也提醒 Codex 的 locked-use 能力存在 macOS keychain 风险。对 builders 来说，隔离、网络出口、凭证和故障恢复已经是产品架构，而不是上线前的安全补丁。',
        '评测与产品化正在形成同一个反馈回路。Madhu Guru 强调 eval 不能是静态文档，必须随真实用户行为和产品路线演进；Google Labs 的 Play with Putty 把 vibe coding 做成多人实时协作实验；Aaron Levie 则指出企业真正需要的是解决问题和交付结果，而不是裸模型或孤立 Agent。换句话说，AI 产品的竞争单位正从“模型回答”转向“可观测的完整工作流”。',
        '成本与组织形态也在快速变化：OpenAI 面向团队的小企业方案把模型、Codex、外部 SaaS 连接、SSO/MFA 和集中管理打包，说明 AI 使用正在进入组织级采购；Nikunj Kothari 展示的 El Niño monitor 则体现了用 AI coding 工具把公共信息、区域影响、历史记录和 FAQ 组织成一个可用产品。低成本模型、快速构建工具和更强的企业治理，会同时扩大试验数量，也提高对数据来源与产品完成度的要求。'
    ],
    'filteredNote': '过滤掉了纯情绪表达、日常闲聊、无上下文转发、单句评论、空内容及缺乏事实增量的自我宣传等低信号内容。'
}

def post(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {'type': 'post', 'typeLabel': '观点动态', 'date': date_, 'actor': actor, 'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points, 'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url}

def podcast(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {'type': 'podcast', 'typeLabel': '播客摘录', 'date': date_, 'actor': actor, 'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points, 'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url}

items = [
    post('8月25日 · 周二', 'Claude', 'Claude · X 动态', '把跨产品记忆做成用户可控的工作上下文', 'Claude 宣布 Chat 与 Claude Cowork 共享同一套记忆：用户可以让 Claude 记住信息，Cowork 接手任务时直接使用既有项目、偏好和客户上下文。同时，记忆以主题列表呈现在 Settings 中，可查看、编辑和删除，敏感信息默认不纳入。它把“长期上下文”从隐形模型状态变成了可管理的产品对象。', ['Chat 与 Cowork 共享上下文，减少重复交代', '记忆可查看、编辑、删除，控制权回到用户', '健康和宗教等敏感主题默认排除'], '对构建个人助理和企业 Agent 很有参考价值：记忆的可解释性、可撤销性和隐私边界，决定用户是否敢把长期工作交给 AI。', ['产品', '记忆', '隐私'], 93, 'https://x.com/claudeai/status/2092299704864284888'),
    post('8月25日 · 周二', 'Guillermo Rauch', 'Vercel · X 动态', 'Agent 执行层需要更轻的安全运行时', 'Guillermo Rauch 介绍 Run SDK：Agent 生成代码时，不必每次都启动完整 sandbox，而可以在轻量的 QuickJS secure context 中执行，从而降低延迟和成本。这个设计把动态 Code Mode 拆成风险分层的执行路径：可信度较高、资源受限的任务走轻运行时，复杂任务再进入更强隔离环境。', ['QuickJS secure context 支持轻量代码执行', '不必为所有动态代码付出完整 sandbox 成本', '执行隔离应按任务风险与资源需求分层'], '它提供了 Agent 工具调用的实用架构方向：安全不只是“全部放进最重的沙箱”，而是把隔离强度、性能和成本做成可组合的策略。', ['Agent', '工程', '安全'], 94, 'https://x.com/rauchg/status/2092382653161107534'),
    post('8月25日 · 周二', 'Guillermo Rauch', 'Vercel · X 动态', 'Agent 的真正难题是安全地连接数据与服务', 'Guillermo Rauch 指出，构建 Agent 最难的问题是让它安全连接服务与数据，并介绍 Vercel Connect：通过认证用户获取可查询的 MCP client，例如代表用户访问 Notion。核心挑战不是再增加工具数量，而是让身份、权限、连接生命周期和审计能一起工作。', ['安全连接比工具数量更关键', 'MCP client 应代表已认证用户执行', '数据访问需要权限边界与可审计性'], '这是企业 Agent 从 demo 走向生产时必须面对的基础设施问题；连接层做不好，模型能力越强，潜在影响面越大。', ['Agent', 'MCP', '安全'], 93, 'https://x.com/rauchg/status/2092352411839193234'),
    post('8月26日 · 周三', 'Madhu Guru', 'Meta AI · X 动态', 'Eval 不能是静态表格，而要跟着产品一起进化', 'Madhu Guru 在 Eval 系列第 9 部分指出，很多 eval 失效，是因为团队把它们当成静态产物，而用户期望和行为已经变化。以金融研究 Agent 为例，评测需要随着真实用例、失败模式和产品路线更新，成为一份持续演进的 roadmap。', ['评测要反映真实使用模式', '产品变化会改变失败模式与质量标准', 'eval roadmap 应持续更新而非一次性交付'], '它把 eval 从发布前的验收表提升为产品运营系统，适合用来设计 Agent 的长期质量闭环。', ['评测', 'Agent', '研究'], 92, 'https://x.com/realmadhuguru/status/2092426017118028266'),
    post('8月25日 · 周二', 'Peter Yang', 'AI skill · X 动态', '高风险场景的 AI 助手，先建立一份可持续更新的事实底稿', 'Peter Yang 开源 /fuck-cancer skill，帮助患者和照护者理解诊断与治疗并进行沟通。它生成并持续更新一份 single source of truth brief，集中保存患者信息、下一步行动、医学术语解释和更新日志；这比让模型每次从零回答更适合高风险、长周期决策。', ['用单一事实底稿集中维护关键信息', '把下一步行动、术语和更新日志放在同一上下文', '高风险场景需要帮助用户提问和倡导，而非替代医生'], '这是一个很具体的工作流范式：在医疗、法律、财务等场景，状态管理、来源追踪和用户倡导能力往往比一次回答的流畅度更重要。', ['产品', '工作流', '高风险场景'], 91, 'https://x.com/petergyang/status/2092249012913258946'),
    post('8月25日 · 周二', 'Google Labs', 'Google Labs · X 动态', 'Vibe coding 正从单人试玩走向实时协作', 'Google Labs 发布 Play with Putty 实验：多人可以实时协作，用 vibe coding 一起构建工具和网站。它把生成式开发的交互单位从“一个人对一个 Agent”扩展为团队共同塑造产物，重点也从代码生成转向协作、反馈和即时可见的结果。', ['支持多人实时协作构建', '产物可以是工具和网站，而不只是代码片段', '协作反馈成为 vibe coding 的核心体验'], '如果这类交互成熟，AI 编程工具的竞争会从个人效率扩展到团队创意流和共同决策。', ['产品', '编程', '协作'], 86, 'https://x.com/GoogleLabs/status/2092293667688173593'),
    post('8月25日 · 周二', 'Aaron Levie', 'Box · X 动态', '企业 AI 的机会在结果交付，不在裸模型堆叠', 'Aaron Levie 认为，模型能力与企业底层工作流之间仍存在巨大鸿沟，应用型 AI 公司因此有大量机会。企业并不只是想要原始模型或孤立 Agent，而是希望问题被解决、结果被交付；这要求 builders 深入业务流程、数据和责任边界。', ['模型能力与企业工作流之间存在鸿沟', '客户购买的是解决问题和结果', '应用层机会来自流程、数据与责任整合'], '这是一条长期有效的产品判断：模型趋于普及后，最难复制的部分会是对具体业务流程的理解和交付能力。', ['企业 AI', 'Agent', '产品'], 90, 'https://x.com/levie/status/2092466424694649066'),
    post('8月25日 · 周二', 'Thibault Sottiaux', 'OpenAI · X 动态', 'AI 产品进入组织采购，治理能力成为套餐的一部分', 'Thibault Sottiaux 介绍面向团队和小公司的方案：覆盖 ChatGPT、ChatGPT Work 与 Codex，连接 Google Workspace、Slack、GitHub、Microsoft 365，并提供 SAML、SSO、MFA、集中计费和管理。产品边界从个人工具扩展到组织工作空间，身份、权限和采购管理与模型能力被打包在一起。', ['外部 SaaS 连接成为团队产品的标配', 'SAML、SSO、MFA 解决组织治理问题', '集中计费与管理降低团队采用成本'], '对做 B2B AI 的 builders 来说，企业愿意付费的不只是模型调用，而是安全接入、权限治理和可规模化管理。', ['产品', '企业', '组织'], 91, 'https://x.com/thsottiaux/status/2092345330272780499'),
    post('8月25日 · 周二', 'Nikunj Kothari', '独立产品 · X 动态', '把分散的公共信息组织成一个真正可用的主题监测器', 'Nikunj Kothari 展示 El Niño situation monitor：整合政府来源的实时更新、区域影响与成本、历史记录、重要性说明以及术语 FAQ，并说明它由 ChatGPT Codex 等工具辅助构建。价值不在“做了一个页面”，而在于把分散信息整理成可持续查询、可理解和可行动的主题产品。', ['优先使用政府来源并提供实时更新', '把影响、成本、历史和术语放进同一信息架构', 'AI coding 工具缩短从想法到可用产品的路径'], '它是 AI-native 产品的一种朴素但重要的形态：信息组织和决策辅助本身就是产品，不一定要先追求复杂 Agent。', ['产品', '信息服务', 'AI 编程'], 84, 'https://x.com/nikunj/status/2092383834470002922'),
    podcast('8月25日 · 周二', 'Training Data', 'Training Data · 播客摘录', '给 Agent 设计一张面向机器的新 Web', 'Parallel 的 Parag Agrawal 在节目中提出，传统 Web 依赖人类点击数据来优化搜索和交互，但对 Agent 来说，这类数据是偏差来源；更合理的方向是让 Agent 在完成任务的过程中产生反馈，并围绕机器可读、可验证和可执行的信息构建新的 Web。核心判断是：当用户从“亲自点击”转为“委托 Agent”，搜索质量和网站设计的反馈信号都必须重做。', ['人类点击数据不一定适合 Agent 时代', 'Agent 执行任务本身可以产生更直接的反馈', 'Web 内容需要更可读、可验证、可执行'], '它把 Agent 时代的基础设施问题上推到 Web 数据层：未来的产品不仅要服务人类阅读，也要服务机器完成任务。', ['Agent', '搜索', 'Web'], 92, 'https://www.youtube.com/playlist?list=PLOhHNjZItNnMm5tdW61JpnyxeYH5NDDx8')
]

data['highSignalItems'] = items
data['headline'] = '今日聚焦 Agent 工作流、执行安全、可演进评测与组织级 AI：17 位 AI Builders、9 条高信号卡片。'
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
