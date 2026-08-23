import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
date = '2026-08-24'
archive = root / 'data' / 'archive' / f'{date}.json'
with archive.open(encoding='utf-8') as f:
    data = json.load(f)

data['dailyInsight'] = {
    'paragraphs': [
        '今天最明确的工程信号，是 AI coding agent 的瓶颈正在从模型能力转向系统效率与容量管理。Thibault Sottiaux 说明 Codex 的 rate limits 受到长会话图片处理、多次 compaction、Computer History 的高 p95 用量，以及对话标题生成等环节的额外消耗影响；这意味着长任务的连续性、缓存效率和后台功能都已经是开发者体验的一部分。',
        '评测是另一条主线。Madhu Guru 把 eval 的 hill climbing 解释为：选择真正重要的维度，依据生产数据持续优化；Aaron Levie 则指出，AI diffusion 更受“针对具体业务场景的好评测”限制，而不是受模型发布时的通用 benchmark 限制。对 builders 来说，eval 不应只是发布前的分数，而应连接高价值用户旅程、相邻用例、成本和可靠性。',
        'Agent 产品的价值还在于把能力嵌入可执行的用户流程。Peter Yang 分享了用 Codex 或 Claude Code 清理浏览器中外部应用访问 Google 数据的做法，展示了“发现权限—选择目标—执行撤销”的低摩擦工作流；这类体验的关键不是一次性的模型回答，而是让用户能看见范围、保留选择权，并完成可验证的动作。',
        '组织层面，Zara Zhang 观察到个人使用 AI 时的生产力增幅可能远高于大型组织中的增幅，核心差异在于个人可以直接改变流程，而组织会被审批、协作和既有系统稀释。这个判断对 AI Builders 的启发是：产品设计和内部落地都要优先寻找能缩短决策链、减少交接、允许快速反馈的工作单元，而不是只增加一个 AI 入口。'
    ],
    'filteredNote': '过滤掉了纯生活动态、情绪表达、表情包、无上下文短句、单纯宣传或转发、非 AI 话题，以及无法从现有文本还原核心论点的播客片段等低信号内容。'
}

def item(type_, label, date_, actor, meta, title, summary, points, why, tags, score, url):
    return {
        'type': type_, 'typeLabel': label, 'date': date_, 'actor': actor,
        'meta': meta, 'title': title, 'summary': summary, 'keyPoints': points,
        'whyItMatters': why, 'tags': tags, 'qualityScore': score, 'url': url
    }

items = [
    item('post', '观点动态', '8月23日 · 周日', 'Thibault Sottiaux', 'Codex · X 动态',
         'Coding agent 的限额，本质是系统效率问题',
         'Thibault Sottiaux 解释 Codex rate limits 的几个真实消耗源：长会话中的图片处理与多次 compaction、Computer History 的高 p95 用量，以及对话标题生成特性产生的额外开销。团队正在用专项小组排查这些问题，说明 coding agent 的容量体验不仅由模型推理决定，也由上下文管理和后台产品逻辑共同决定。',
         ['长会话与多模态输入会放大用量低效', '高 p95 的后台功能会侵蚀用户可用额度', '容量、缓存与上下文连续性已成为 coding agent 的产品质量指标'],
         '这是少见的产品内部信号：当开发者把 agent 用于长任务时，限额策略和系统效率会直接决定他们是否敢把工作流交出去。',
         ['产品', '工程', '开发工具'], 95, 'https://x.com/thsottiaux/status/2091407991736332689'),
    item('post', '观点动态', '8月22日 · 周六', 'Madhu Guru', 'AI evaluation · X 动态',
         'Eval 不只是打分：用生产反馈持续爬坡',
         'Madhu Guru 将 eval 上的 hill climbing 解释为一个持续优化循环：先挑选真正重要的维度，再结合生产数据提升已有高价值功能、扩展相邻用例，或降低成本。这个框架把评测从发布前的验收表，变成连接用户价值、产品迭代和资源效率的控制面。',
         ['评测维度必须对应真实用户价值', '生产数据应驱动已有功能和相邻用例的优化', '质量提升、覆盖扩展与成本下降都可以成为 eval 目标'],
         '它给 Agent 团队提供了可执行的评测方法：不要追求一个漂亮总分，而要围绕关键旅程建立可反复优化的指标。',
         ['评测', 'Agent', '工程'], 93, 'https://x.com/realmadhuguru/status/2091278653435072523'),
    item('post', '观点动态', '8月23日 · 周日', 'Aaron Levie', 'Box · X 动态',
         'AI 普及的真正瓶颈，是业务场景的好评测',
         'Aaron Levie 认为，模型发布时的通用 eval 很有帮助，但它们主要描述总体能力形状和相对水平；真正限制 AI 在组织内扩散的，是覆盖各类业务场景的具体评测。换句话说，企业需要衡量模型在自己的数据、流程和风险边界内是否可靠，而不是只看通用 benchmark。',
         ['通用 benchmark 不能代表企业工作流表现', '场景化 eval 是 AI diffusion 的关键基础设施', '评测应覆盖业务结果、风险和长期稳定性'],
         '这把企业 AI 的竞争焦点从“选哪个模型”转向“能否建立自己的验证系统”，对产品采购和内部落地都很关键。',
         ['评测', '企业 AI', 'Agent'], 94, 'https://x.com/levie/status/2091359223368315050'),
    item('post', '观点动态', '8月23日 · 周日', 'Peter Yang', 'Codex / Claude Code · X 动态',
         '让 AI 直接治理第三方数据权限',
         'Peter Yang 分享了一条具体的隐私工作流：让 Codex 或 Claude Code 识别浏览器中的开放页面，再由用户挑选要删除的外部应用连接，最后执行撤销。他实际清理了多条不再需要的 Google 数据访问，体现出 AI 工具正在从“告诉用户去哪里设置”走向“在用户确认后完成权限治理”。',
         ['先发现外部应用与数据范围', '用户保留逐项选择和最终确认权', 'Agent 的价值在于完成可验证的权限变更'],
         '这是一个可复用的 Agent 产品范式：把复杂设置流程变成可检查、可授权、可回滚的动作链，而不是只生成说明文字。',
         ['隐私', 'Agent', '产品'], 88, 'https://x.com/petergyang/status/2091331251211059468'),
    item('post', '观点动态', '8月23日 · 周日', 'Zara Zhang', 'AI productivity · X 动态',
         'AI 的个人杠杆，为什么在组织里会被稀释',
         'Zara Zhang 观察到，擅长使用 AI 的个人在做自己的事情时可能获得接近 10 倍的潜力提升，但进入大型组织后增幅可能只有约 20%，甚至下降。关键不一定是模型能力差异，而是组织中的审批、交接、工具边界和既有流程会吞掉个人获得的速度优势。',
         ['个人项目可以直接重构工作流', '组织摩擦会稀释 AI 带来的局部效率', '落地应优先选择决策链短、反馈快的工作单元'],
         '它提醒 builders，AI 产品的 adoption 难点往往是组织设计而非功能缺失；减少交接和等待，可能比再加一个模型入口更有价值。',
         ['组织', '产品', 'AI productivity'], 86, 'https://x.com/zarazhangrui/status/2091379220257603593')
]
data['highSignalItems'] = items
data['headline'] = '今日聚焦 coding agent 效率、场景化评测、权限治理与组织杠杆：5 条高信号内容。'
data['editorNote'] = '每日汇总一线 AI Builders 的观点、文章和播客，过滤低信号内容，优先保留可验证、可复用、对构建者有长期价值的判断。'

for path in [archive, root / 'data' / 'latest.json']:
    with path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

digests_path = root / 'data' / 'digests.json'
with digests_path.open(encoding='utf-8') as f:
    digests = json.load(f)
digests = [d for d in digests if d.get('date') != date]
digests.insert(0, data)
with digests_path.open('w', encoding='utf-8') as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print(json.dumps({'date': date, 'highSignalItems': len(items), 'archive': str(archive), 'latest': str(root / 'data' / 'latest.json'), 'digestsUpdated': True}, ensure_ascii=False))
