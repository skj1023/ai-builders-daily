import json
from pathlib import Path

root = Path.cwd()
date = '2026-09-03'
archive = root / 'data' / 'archive' / f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最强的产品信号，是 AI 正在从“回答问题”进入“完成工作”。Fable 5.1 的企业评测、代码生成视频和更长任务能力，说明模型进步的价值越来越通过完整工作流体现，而不是单次对话的惊艳效果；Box 的实测也把模型能力直接放进真实的非结构化企业任务中衡量。',
        'Agent 的体验瓶颈正在转向“少打扰但不失控”。Nan Yu 把减少烦人交互视为重要机会，Peter Yang 则展示了通过 prompt-audit 清理旧 skill、删除冗余规则的实践。两条信号共同说明，Agent 产品需要同时优化对话修辞、上下文负担和可维护性，否则能力越强，用户越容易在长流程中退出。',
        '工程基础设施的竞争继续围绕执行边界展开：Thariq 提到 effort 切换不再破坏 prompt cache，Guillermo Rauch 则把统一的 Dockerfile、网络、文件系统和安全边界带入不同计算产品。对 builders 来说，模型路由、缓存、沙箱和网络出口并非底层细节，而是决定 Agent 成本、延迟、可靠性和安全性的产品架构。',
        '安全与自我改进正在成为生产系统的闭环能力。Claude 和 Boris Cherny 给出了降低误拦截的具体比例，Madhu Guru 强调企业应建设自己的 post-training、eval 和数据飞轮，Sam Altman 也将能力与 safeguards 的同步推进放在下一模型发布之前。值得关注的方向不是单纯追逐更强模型，而是建立可度量、可反馈、可持续迭代的系统。'
    ],
    'filteredNote': '过滤掉了 merch、Bullish、日常闲聊、纯宣传、无上下文评论、空内容及缺乏事实增量的低信号内容。'
}

def post(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {'type': 'post', 'typeLabel': '观点动态', 'date': date_, 'actor': actor, 'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points, 'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url}

def podcast(date_, actor, meta, title, summary, points, why, tags, score, url):
    return {'type': 'podcast', 'typeLabel': '播客摘录', 'date': date_, 'actor': actor, 'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points, 'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url}

items = [
    post('9月1日 · 周二', 'Boris Cherny', 'Claude Code · X 动态', '模型降价正在重塑长任务 Agent 的成本曲线', 'Boris Cherny 表示，Fable 5.1 的 cache reads 已从每百万 token 1 美元降至 0.25 美元，典型 Claude Code 会话最高便宜 38%，Enterprise、API 和 SDK 客户也同步受益。对 coding agent 来说，缓存价格会直接影响上下文长度、任务连续性和团队是否敢于运行更复杂的自动化。', ['cache reads 降至每百万 token 0.25 美元', '典型 Claude Code 会话最高便宜 38%', '成本下降扩大长上下文与持续执行的可行空间'], '它是一个明确的基础设施产品信号：Agent 的竞争不仅是模型质量，也包括把重复上下文变成可负担的计算成本。', ['模型成本', 'Agent', '开发工具'], 91, 'https://x.com/bcherny/status/2094864062186426373'),
    post('9月1日 · 周二', 'Boris Cherny', 'Claude Code · X 动态', '安全护栏的价值也要用误拦截率衡量', 'Boris Cherny 分享了 Fable 5.1 的安全改进：生物学护栏对良性请求的误干预减少 85%，Claude Code 用户每次会话预计少遇到约 60% 的网络安全干预。这个变化把安全从“拦得更多”推进到“在保持防护的同时减少无谓摩擦”。', ['良性生物学请求的误干预减少 85%', 'Claude Code 网络安全干预预计减少约 60%', '安全质量需要同时关注拦截能力与误报成本'], 'Agent 一旦进入真实开发和研究流程，误拦截会直接侵蚀信任；把安全体验纳入可量化产品指标，是生产化的必要条件。', ['安全', '产品', '模型'], 92, 'https://x.com/bcherny/status/2094864063478276288'),
    post('9月2日 · 周三', 'Peter Yang', 'AI skill · X 动态', '模型升级后，skill 也需要做一次 prompt 资产审计', 'Peter Yang 建议 Fable 5.1 用户运行 /claude-api prompt-audit，找出 skill 中已经冗余或应删除的规则，并表示正在为自己的 skills 批量清理。它揭示了一个常被忽视的维护问题：模型能力变化后，旧 prompt 可能不再提供增益，反而增加上下文噪声和行为约束。', ['用 prompt-audit 找出冗余规则', '模型升级会改变旧 skill 的最优提示结构', 'skill 需要像代码一样持续重构与删除'], '对使用本地或团队 skill 的 builders 来说，提示词不是一次性配置，而是需要版本化、评测和定期清理的产品资产。', ['Prompt Engineering', 'Skill', '开发工具'], 90, 'https://x.com/petergyang/status/2094987791566622971'),
    post('9月1日 · 周二', 'Nan Yu', 'OpenAI · X 动态', 'Agent UX 的关键指标可能是：让用户少一次“烦了退出”', 'Nan Yu 认为，让 Agent 变得 less annoying 仍有大量未开发价值；用户只有在不频繁 rage-quit 的情况下，才会真正走到价值交付，并建议 UX 设计师重视 conversation/rhetoric design。这里的重点不是让 Agent 更会聊天，而是把措辞、节奏、追问和打断设计成降低认知摩擦的交互系统。', ['减少烦人交互是提升价值到达率的杠杆', 'rage-quit 可视为 Agent UX 的失败信号', 'UX 设计需要覆盖对话修辞与行为节奏'], '许多 Agent 失败并非能力不足，而是用户在完成任务前被交互摩擦消耗；这条判断适用于任何长流程 AI 产品。', ['Agent', '产品体验', 'UX'], 91, 'https://x.com/thenanyu/status/2094928205753040999'),
    post('9月1日 · 周二', 'Madhu Guru', 'Meta AI · X 动态', '自我改进产品需要指标、策略和知识库组成闭环', 'Madhu Guru 认为 self-improving products 应成为每家公司都要实施的 meta idea，并列出清晰的 primary、secondary、guardrail metrics，以及策略、路线图和知识库等基础组件。核心不是让模型神秘地“自我进化”，而是把产品目标、反馈数据和改进动作连接成可治理的循环。', ['明确 primary、secondary 与 guardrail metrics', '把策略、路线图和指标放进同一改进框架', '知识库是持续反馈和学习的基础设施'], '它提供了一套比“加一个 Agent”更稳健的 AI 产品进化视角：先定义什么叫变好，再让系统围绕指标持续学习。', ['评测', 'Agent', '产品'], 93, 'https://x.com/realmadhuguru/status/2094817857821704659'),
    post('9月2日 · 周三', 'Thariq', 'Claude Code · X 动态', '可切换推理 effort，且不破坏缓存，意味着成本策略更可编排', 'Thariq 分享了对 Fable 5.1 的观察：对于需要较少验证或边界情况较少的任务，可以使用 lower effort；同时，切换 effort 不再破坏 prompt cache。模型质量、推理预算和缓存复用因此可以被放进同一任务路由策略，而不必在速度与上下文效率之间做粗糙的二选一。', ['低风险任务可使用 lower effort', '切换 effort 不再破坏 prompt cache', '任务路由可以同时优化质量、延迟和成本'], '这是 Agent 运行时的重要能力：不同任务应使用不同推理预算，且预算调整不应带来上下文缓存的惩罚。', ['推理', '缓存', 'Agent'], 92, 'https://x.com/trq212/status/2094945951865520458'),
    post('9月1日 · 周二', 'Guillermo Rauch', 'Vercel · X 动态', '统一计算抽象正在成为 Agent 基础设施的 DX 核心', 'Guillermo Rauch 介绍 Fluid 如何统一 Vercel 的构建、Sandbox 和长时函数能力：共享 Dockerfile、安全边界、网络和文件系统，并支持更长的函数执行时间。对 Agent 应用而言，这种统一让不同计算形态能够复用相同的开发与安全模型，降低从原型到生产迁移时的系统割裂。', ['统一 Dockerfile、网络、文件系统和安全边界', '覆盖构建、Sandbox 与长时函数等计算形态', '一致的计算抽象改善开发体验与迁移成本'], 'Agent 需要频繁跨越异步任务、沙箱和服务端执行；基础设施的一致性会直接决定 builders 能否稳定扩展。', ['基础设施', 'Sandbox', 'Agent'], 90, 'https://x.com/rauchg/status/2094831747037085978'),
    post('9月1日 · 周二', 'Alex Albert', 'Anthropic · X 动态', '代码生成正在把 3D 场景从设计任务变成可编排流水线', 'Alex Albert 展示了 Fable 5.1 的一条完整链路：输入一张地块图片，模型设计房屋、渲染场景并生成电影感的 walkthrough，而且使用的是 headless Blender。价值不只是生成一段视频，而是把视觉规划、程序化建模、渲染和输出串成可自动执行的工程流程。', ['从地块图片生成房屋设计与渲染结果', '通过 headless Blender 接入自动化流程', '多步骤视觉产出可由代码和模型共同编排'], '它展示了 multimodal Agent 的实际方向：模型负责规划与生成，成熟工具链负责确定性执行和交付。', ['多模态', '代码生成', '3D'], 91, 'https://x.com/alexalbert__/status/2094860187743986169'),
    post('9月1日 · 周二', 'Aaron Levie', 'Box · X 动态', '企业 Agent 的竞争要落到真实非结构化任务的评测分数', 'Aaron Levie 表示，Box 用复杂的 enterprise work eval 测试 Fable 5.1，在非结构化数据任务上相较 Fable 5 提升 7 个百分点，并由 Box Agent 执行一系列真实企业工作。这个例子把“模型更强”转换成了业务场景中可复现、可比较的结果指标。', ['真实企业工作 eval 提升 7 个百分点', '评测覆盖非结构化数据任务', '模型价值通过 Box Agent 的完整工作流体现'], '企业采购最终关心的是任务完成质量，而不是 benchmark 排名；场景化 eval 是连接模型能力与商业结果的关键。', ['企业 AI', '评测', 'Agent'], 94, 'https://x.com/levie/status/2094851976769257770'),
    post('9月1日 · 周二', 'Nikunj Kothari', '独立产品 · X 动态', 'WebMCP 让网站从被浏览对象变成 Agent 的可调用界面', 'Nikunj Kothari 认为 WebMCP 被低估：Agent 可以原生调用网站工具，并获得完整 UI/UX 与交互元素来构建自己的视图。他展示的 El Niño demo 暗示，网站未来不必只为人类点击设计，也可以提供机器可读、可执行且保留交互语义的能力层。', ['Agent 可原生调用网站工具', '支持 UI/UX 与交互元素的机器构建视图', 'Web 需要同时面向人类使用与 Agent 执行'], '这条信号把 Agent 生态的入口从独立插件推进到网站本身：产品是否可被可靠调用，可能成为下一代 Web 的基础能力。', ['WebMCP', 'Web', 'Agent'], 90, 'https://x.com/nikunj/status/2094922789128196314')
]

data['highSignalItems'] = items
data['headline'] = '今日聚焦 Agent 体验、推理成本、企业评测与执行基础设施：16 位 AI Builders、10 条高信号卡片。'
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
