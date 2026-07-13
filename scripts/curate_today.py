import json

with open('data/archive/2026-07-14.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build dailyInsight
data['dailyInsight'] = {
    'paragraphs': [
        '今日最显性的信号来自基础设施层的「算力让价」。Anthropic 将 Claude Fable 5 的付费用户开放期延长至 7 月 19 日，并维持 Claude Code 50% 的 rate limit 加成；OpenAI 的 Thibault Sottiaux 同步披露 GPT-5.6 Sol 完成推理优化，所有订阅层级获得约 10% 的用量提升，Codex 上下文窗口扩展至 372k。两大厂商在同一天释放「同等能力更便宜」的信号，说明推理成本的下降速度已超过模型能力的迭代速度，开发者议价权正在上升。',
        '架构层面的讨论集中在「谁拥有 AI 堆栈」。Guillermo Rauch 明确提出「Make the model a cog in a machine you own」——通过 AI SDK、Agent API、AI Gateway 三层开放架构，让创业公司和企业在数据、evals、模型选择上保持自主。Aaron Levie 从企业角度补充了另一个维度：当智力被打包进模型后，企业 IP（决策、工作流、最佳实践）如何不被 bitter lesson 吞没，是 21 世纪商业架构的核心问题。两个视角合在一起，指向一个判断：模型层的同质化正在加速，真正的壁垒在模型之上的数据飞轮和工作流编排。',
        '工程实践侧，Amjad Masad 分享了在 Replit 上用 Qwen-8b 微调国际象棋引擎的「Vibe Research」过程——并行跑 3 个实验分支，靠直觉引导模型做 ML。Zara Zhang 则展示了「会议录音即 PRD」的 Codex 工作流：和同事讨论实现细节，把 transcript 直接喂给 Codex 出原型。这两个案例的共同点是：人提供方向和判断，AI 负责执行和探索，这正是 Agent 时代的人机协作范式。',
        'FPV Ventures 的 Nikunj Kothari 提供了一个清醒的观察：旧金山很多人声称自己在 tokenmaxxing、跑 subagent 循环，但被问到「在为什么问题、为谁构建」时几乎答不上来。这揭示了一个行业噪音——工具使用的密度不等于产品方向的清晰度。在 Agent 基础设施快速商品化的当下，「做什么」比「怎么用」更重要。'
    ],
    'filteredNote': '过滤掉了 Matt Turck 的 meme 式吐槽、Dan Shipper 的短句感叹、Peter Steinberger 的硬件展示、Garry Tan 的政治评论、Nikunj 的日常提醒等低信号内容'
}

# Build highSignalItems
data['highSignalItems'] = [
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月12日 · 周六',
        'actor': 'Claude',
        'meta': 'Anthropic · 产品公告',
        'title': 'Claude Fable 5 延期开放，Code 限额持续加成',
        'summary': 'Anthropic 宣布将 Claude Fable 5 的付费用户访问权限延长至 7 月 19 日，同时维持 Claude Code 周限额 50% 的加成。付费用户可将最多一半的周限额用于 Fable 5，超出后可使用 credits 或切换模型。',
        'keyPoints': ['Fable 5 开放期延长一周', 'Claude Code rate limit 维持 +50%', '超额后支持 credits 或模型切换'],
        'whyItMatters': '推理成本下降的直接体现，开发者短期内获得更高的性价比窗口。',
        'tags': ['产品', '工程'],
        'qualityScore': 88,
        'url': 'https://x.com/claudeai/status/2076351399999557669'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月13日 · 周日',
        'actor': 'Thibault Sottiaux',
        'meta': 'OpenAI Codex · 工程更新',
        'title': 'GPT-5.6 Sol 推理优化落地，Codex 上下文扩至 372k',
        'summary': 'OpenAI Codex 负责人披露 GPT-5.6 Sol 完成推理优化，所有订阅层级获得约 10% 用量提升。同时将产品上下文限制调整为 372k，明确承诺不会 nerf 模型。',
        'keyPoints': ['推理优化带来 10% 用量提升', 'Codex 上下文窗口扩至 372k', '明确承诺 no nerfing'],
        'whyItMatters': '推理成本下降+上下文扩展，直接影响 Agent 类产品的架构决策和用户体验上限。',
        'tags': ['产品', 'Agent', '工程'],
        'qualityScore': 90,
        'url': 'https://x.com/thsottiaux/status/2076495156757577895'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月12日 · 周六',
        'actor': 'Guillermo Rauch',
        'meta': 'Vercel · 架构观点',
        'title': '把模型变成你自有机器里的齿轮',
        'summary': 'Rauch 提出三层开放架构主张：AI SDK（开放模型 API）→ Agent API（开放 Agent 接口）→ AI Gateway（开放 ZDR 推理）。核心论点是创业公司和企业必须掌控自己的数据、evals、模型选择和软件层，不要把大脑外包出去。',
        'keyPoints': ['三层开放架构：SDK → Agent API → Gateway', '企业必须拥有数据、evals、模型选择', "Don't outsource your brain"],
        'whyItMatters': '在模型层快速商品化的背景下，这是关于「价值在哪一层沉淀」的清晰判断框架。',
        'tags': ['Agent', '架构', '研究'],
        'qualityScore': 85,
        'url': 'https://x.com/rauchg/status/2076364176252191222'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月12日 · 周六',
        'actor': 'Aaron Levie',
        'meta': 'Box · 企业 AI 架构',
        'title': '模型同质化时代，企业 IP 如何不被 bitter lesson 吞没',
        'summary': 'Levie 提出 21 世纪商业的核心架构问题：当智力被打包进 AI 模型后，企业如何最大化自己的 IP（决策、洞察、工作流模式、最佳实践）？他暗示这些问题不能简单被 bitter lesson 解决。',
        'keyPoints': ['企业 IP 包括决策、洞察、工作流模式', '模型同质化不等于企业知识可替代', 'bitter lesson 不能解决所有问题'],
        'whyItMatters': '为企业 AI 架构提供了一个反向思考：不是「如何用模型」，而是「如何在模型之上保持壁垒」。',
        'tags': ['Agent', '研究', '企业'],
        'qualityScore': 82,
        'url': 'https://x.com/levie/status/2076338364635287637'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月12日 · 周六',
        'actor': 'Amjad Masad',
        'meta': 'Replit · Vibe Research',
        'title': 'Vibe Research：在 Replit 上微调 Qwen-8b 下国际象棋',
        'summary': 'Masad 分享了在 Replit 上用 Qwen-8b 微调国际象棋引擎的过程：并行跑 3 个实验分支，靠人的直觉引导模型做 ML。他指出模型在「做 ML」这件事上已经进步巨大，有良好直觉的人现在可以独立完成过去需要团队的工作。',
        'keyPoints': ['并行 3 个实验分支', '人提供直觉，模型执行 ML', '模型做 ML 的能力已大幅提升'],
        'whyItMatters': '「Vibe Research」是 Agent 时代人机协作的具体范式——人定方向，AI 执行和探索。',
        'tags': ['工程', '研究', '产品'],
        'qualityScore': 80,
        'url': 'https://x.com/amasad/status/2076227936202662357'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月12日 · 周六',
        'actor': 'Zara Zhang',
        'meta': 'follow-builders · 工作流实践',
        'title': '会议录音即 PRD：Codex 的新用法',
        'summary': 'Zhang 展示了一个高效工作流：和同事讨论功能实现细节，把会议 transcript 直接喂给 Codex，它就能按讨论内容构建原型。「会议本身就是 prompt」。',
        'keyPoints': ['会议 transcript 直接作为 PRD', 'Codex 能理解讨论上下文并出原型', '会议即 prompt'],
        'whyItMatters': '展示了 Agent 工具如何消除「讨论→文档→开发」的中间环节，是产品迭代效率的质变。',
        'tags': ['产品', '工程', '工作流'],
        'qualityScore': 78,
        'url': 'https://x.com/zarazhangrui/status/2076300222884626754'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月12日 · 周六',
        'actor': 'Swyx',
        'meta': 'Latent Space · 技术框架',
        'title': 'introspection 与 backpropagation：insanity 的定义',
        'summary': 'Swyx 引用爱因斯坦的名言重新定义了 Agent 的 introspection：如果多次 rollout 没有对 advantage 的预期，那就是 insanity。真正的区别在于 introspection/backpropagation——Agent 需要从自己的执行中学习，而不是盲目重复。',
        'keyPoints': ['introspection 是 Agent 的核心能力', '无预期的 rollout 就是 insanity', 'Agent 需要从执行中学习'],
        'whyItMatters': '为 Agent 架构设计提供了一个判断标准：是否有真正的 introspection 机制。',
        'tags': ['Agent', '研究', '框架'],
        'qualityScore': 76,
        'url': 'https://x.com/swyx/status/2076345087634620528'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月13日 · 周日',
        'actor': 'Nikunj Kothari',
        'meta': 'FPV Ventures · 行业观察',
        'title': 'tokenmaxxing 的幻觉：工具密度不等于产品方向',
        'summary': 'Kothari 观察到旧金山很多人声称自己在 tokenmaxxing、跑 subagent 循环，但被问到「在为什么问题、为谁构建」时几乎答不上来。他得出结论：即使在 AI 时代，简单性和方向感仍然比工具使用密度更重要。',
        'keyPoints': ['tokenmaxxing 不等于产品价值', '方向感比工具密度重要', '简单性仍是核心'],
        'whyItMatters': '在 Agent 工具快速商品化的当下，这是一个清醒的反噪音信号。',
        'tags': ['Agent', '市场', '判断'],
        'qualityScore': 83,
        'url': 'https://x.com/nikunj/status/2076458876816540144'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月13日 · 周日',
        'actor': 'Peter Yang',
        'meta': '社区观察 · 沟通策略',
        'title': 'Anthropic 的沟通困境：为什么不能像 OpenAI 那样做社区',
        'summary': 'Yang 指出 Anthropic 模型很好但沟通方式令人困惑，建议他们应该像 OpenAI 一样更直接地与社区互动。他观察到当社区情绪转向负面时，公司有 tendency 减少沟通并变得更 corporate，但这恰恰应该反向操作。',
        'keyPoints': ['Anthropic 沟通不够直接', '负面情绪时更应透明沟通', 'OpenAI 的社区互动是正面案例'],
        'whyItMatters': 'AI 公司的社区沟通策略正在成为产品竞争力的一部分。',
        'tags': ['产品', '组织', '沟通'],
        'qualityScore': 72,
        'url': 'https://x.com/petergyang/status/2076510899490480228'
    },
    {
        'type': 'podcast',
        'typeLabel': '播客摘录',
        'date': '7月2日 · 周三',
        'actor': 'No Priors',
        'meta': 'Valar Atomics Founder Isaiah Taylor',
        'title': '核能如何解锁能源充裕时代',
        'summary': 'Valar Atomics 创始人 Isaiah Taylor 讨论先进核反应堆如何为 AI 基础设施提供能源保障。核心论点是：AI 的算力瓶颈最终是能源瓶颈，核能是唯一能同时满足规模、稳定性和零碳要求的解决方案。',
        'keyPoints': ['AI 算力瓶颈本质是能源瓶颈', '核能是唯一同时满足规模+稳定+零碳的方案', '先进反应堆技术已接近商业化'],
        'whyItMatters': 'AI 基础设施的长期瓶颈不在芯片，而在能源。这是 builder 需要关注的底层约束。',
        'tags': ['工程', '能源', '基础设施'],
        'qualityScore': 75,
        'url': 'https://www.youtube.com/watch?v=5Xvbq_zvOQ4'
    }
]

# Save archive
with open('data/archive/2026-07-14.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Save latest
with open('data/latest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Update digests.json
try:
    with open('data/digests.json', 'r', encoding='utf-8') as f:
        digests = json.load(f)
except Exception:
    digests = []

# Remove existing entry for this date
digests = [d for d in digests if d.get('date') != '2026-07-14']
# Prepend new entry
digests.insert(0, data)

with open('data/digests.json', 'w', encoding='utf-8') as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print('Curated: 10 high-signal items, 4 paragraphs insight')
print('Files saved: archive/2026-07-14.json, latest.json, digests.json')
