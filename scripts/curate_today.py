import json

with open('data/archive/2026-07-10.json', 'r', encoding='utf-8') as f:
    archive = json.load(f)

archive['dailyInsight'] = {
    'paragraphs': [
        "今天的主线是 Agent 工具链的成熟度跃迁。Anthropic 的 Boris Cherny 发布 Claude Code /checkup 命令，一次性解决 context 膨胀、CLAUDE.md 冗余、hooks 性能等长期痛点；Cat Wu 则展示了从 single-player Claude Code 到 multi-player Claude Tag 的演进路径，Agent 正在从个人工具变成团队协作基础设施。",
        "工程范式层面出现两个重要判断。Thariq 指出 rewrites 在 AI 辅助下可以变得 cheap and fast，这颠覆了传统软件工程对重写的恐惧；Amjad Masad 则用编译器类比，认为我们不该再用手写代码的标准去衡量 agent 输出，这标志着 agent 正在获得独立的工程评价框架。",
        "组织层面，Zara Zhang 分享了一个 agent-pilled 创始人的案例：团队全员用 Codex Max 后，会议取消、协作减少、团队文化恶化。这揭示了 AI 工具普及的隐性成本——当每个人都和自己的 agent 对话时，人与人之间的知识共享和隐性协调也在消失。",
        "产品竞争格局上，Grok 4.5 成为今天的焦点：Cursor、Vercel、Box 同时接入，开发者在 Codex 和 Claude Code 之间来回切换。Swyx 指出 agent labs 在用中国模型时需要做宣传审查 eval 和 posttraining 校正，这揭示了模型供应链的隐性工程成本。",
        "深度内容方面，Anthropic 发布两篇工程博客：一篇关于 Claude Code 质量问题的 postmortem，另一篇关于 Managed Agents 的 brain-hands 解耦架构。播客则探讨作家如何在不失去个人声音的前提下使用 AI。"
    ],
    'filteredNote': '过滤掉了 Sam Altman 的无意义短评、Peter Yang 的 GTA 6 日常、Garry Tan 的旧金山政治评论、Matt Turck 的世界杯感慨、Dan Shipper 的无上下文兴奋帖等低信号内容'
}

archive['highSignalItems'] = [
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月8日 · 周三',
        'actor': 'Boris Cherny',
        'meta': 'Claude Code · X 动态',
        'title': 'Claude Code 发布 /checkup 命令，一键解决 context 膨胀',
        'summary': 'Boris Cherny 发布 Claude Code 的 /checkup 命令，可以自动清理未使用的 skills/MCPs/plugins、去重 CLAUDE.md、将根目录 CLAUDE.md 拆分为嵌套结构、关闭慢速 hooks、更新版本、启用 auto mode。这是一个针对长期使用者 context 管理痛点的系统性解决方案。',
        'keyPoints': [
            '清理未使用的 skills/MCPs/plugins 以节省 context',
            '自动去重本地和 checked-in 的 CLAUDE.md',
            '将根目录 CLAUDE.md 拆分为嵌套结构 + skills'
        ],
        'whyItMatters': 'Claude Code 正在从单次对话工具演进为需要长期维护的项目级工具，/checkup 是 context 管理的基础设施。',
        'tags': ['产品', '工程'],
        'qualityScore': 90,
        'url': 'https://x.com/bcherny/status/2074997570317779038'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月8日 · 周三',
        'actor': 'Cat Wu',
        'meta': 'Claude Code + Cowork · X 动态',
        'title': '从 single-player 到 multi-player：Claude Tag 的演进路径',
        'summary': 'Cat Wu 分享了从 single-player Claude Code 到 multi-player Claude Tag 的产品演进。Claude Tag 可以监控 channels、主动执行任务，AI 从完成句子到写完整功能，再到现在的主动协作。',
        'keyPoints': [
            '从 single-player 到 multi-player 的产品形态跃迁',
            'Claude Tag 可以监控 channels 并主动工作',
            'AI 角色从辅助到主动协作的演进'
        ],
        'whyItMatters': 'Agent 正在从个人工具变成团队协作基础设施，这改变了 AI 工具的产品边界。',
        'tags': ['产品', '工程', '组织'],
        'qualityScore': 85,
        'url': 'https://x.com/_catwu/status/2074925531519468012'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月8日 · 周三',
        'actor': 'Thariq',
        'meta': 'Claude Code · X 动态',
        'title': '重写可以又好又便宜又快：AI 时代的软件工程范式',
        'summary': 'Thariq 指出 rewrites 在 AI 辅助下可以变得 good, cheap and fast。虽然大多数应用不像 Bun 那样可测试和可验证，但模型在填补这些空白方面会持续进步。这是对传统软件工程重写恐惧的范式挑战。',
        'keyPoints': [
            '重写不再是禁忌，AI 让它变得可行',
            '可测试性和可验证性是关键差异',
            '模型能力会持续填补验证空白'
        ],
        'whyItMatters': '这代表工程范式的根本转变——当重写成本趋近于零时，架构决策的逻辑也会改变。',
        'tags': ['工程', '研究'],
        'qualityScore': 85,
        'url': 'https://x.com/trq212/status/2074993112217461020'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月9日 · 周四',
        'actor': 'Amjad Masad',
        'meta': 'Replit CEO · X 动态',
        'title': '停止用编译器的标准衡量工程师',
        'summary': 'Amjad Masad 提出一个类比：我们不会拿编译器和手写汇编的工程师比较，同样也不该用手写代码的标准去衡量 autonomous agents。这标志着 agent 需要独立的评价框架。',
        'keyPoints': [
            '编译器类比：不同层级的工具不该直接比较',
            'Agent 需要独立的评价标准',
            '手写代码和 agent 生成代码是不同范式'
        ],
        'whyItMatters': '这是 agent 工程化的重要认知转变——建立独立的评价框架是工具成熟的前提。',
        'tags': ['Agent', '工程'],
        'qualityScore': 82,
        'url': 'https://x.com/amasad/status/2075080984211624154'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月8日 · 周三',
        'actor': 'Zara Zhang',
        'meta': 'follow-builders · X 动态',
        'title': 'Agent-pilled 团队的隐性成本：当人们不再对话',
        'summary': 'Zara Zhang 分享了一个 agent-pilled 创始人的案例：团队全员购买 Codex Max 后，所有人通过和 Codex 对话完成工作。副作用是人与人之间的对话消失、会议取消、协作减少、团队文化恶化。这揭示了 AI 工具普及的组织层面隐性成本。',
        'keyPoints': [
            'Codex Max 让每个人都有自己的 agent',
            '副作用：会议取消、协作减少、文化恶化',
            '企业 AI 需要考虑组织层面的影响'
        ],
        'whyItMatters': 'AI 工具的组织影响常被忽视，这个案例提醒我们需要系统性地思考 AI 对团队协作的影响。',
        'tags': ['产品', 'Agent', '组织'],
        'qualityScore': 85,
        'url': 'https://x.com/zarazhangrui/status/2075004775436005687'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月8日 · 周三',
        'actor': 'Swyx',
        'meta': 'Cognition · X 动态',
        'title': 'Agent labs 使用中国模型的隐性工程成本',
        'summary': 'Swyx 指出大多数 agent labs 不愿承认使用中国模型，因为需要卖给政府/国防客户。Cog team 做了艰苦的工程工作：构建多语言宣传和审查 eval、在 posttraining 中成功校正、以 1000 tok/s 低成本服务。这揭示了模型供应链的隐性成本。',
        'keyPoints': [
            '政府/国防客户需要模型来源透明',
            '需要构建多语言宣传和审查 eval',
            'posttraining 校正是关键工程挑战'
        ],
        'whyItMatters': '模型选择不仅是技术决策，还涉及合规、客户信任和组织定位，这是 agent 商业化的重要约束。',
        'tags': ['产品', 'Agent', '组织'],
        'qualityScore': 80,
        'url': 'https://x.com/swyx/status/2074919183947808881'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月8日 · 周三',
        'actor': 'Aditya Agarwal',
        'meta': 'South Park Commons GP · X 动态',
        'title': '不要浪费这个时代：给创始人的建议',
        'summary': 'Aditya Agarwal 指出每个创始人都担心错过这个时代，但最好的创始人担心的是浪费它。浪费不是指没有行动，而是忽视世界已经改变的事实、用五年前的方式做纯软件、做小东西。他呼吁最大化雄心。',
        'keyPoints': [
            '担心错过 vs 担心浪费：两种不同心态',
            '浪费 = 忽视世界变化、用旧方式做小事',
            '现在是最大化雄心的时刻'
        ],
        'whyItMatters': '这是对创始人心态的重要校准——不是 FOMO，而是对时代变化的清醒认知和行动决心。',
        'tags': ['产品', '组织'],
        'qualityScore': 78,
        'url': 'https://x.com/adityaag/status/2074892507306238235'
    },
    {
        'type': 'blog',
        'typeLabel': '深度文章',
        'date': '7月10日 · 周五',
        'actor': 'Anthropic Engineering',
        'meta': 'Anthropic Engineering Blog',
        'title': 'Scaling Managed Agents：将大脑与双手解耦',
        'summary': 'Anthropic 工程博客发布关于 Managed Agents 架构的深度文章，核心思想是将 agent 的 brain（模型推理）和 hands（工具执行）解耦。这种架构支持 self-hosted sandboxes 和 MCP tunnels，让企业可以在自己的基础设施上运行 agent。',
        'keyPoints': [
            'Brain-hands 解耦是 managed agents 的核心架构',
            '支持 self-hosted sandboxes 满足企业安全需求',
            'MCP tunnels 连接私有工具服务器'
        ],
        'whyItMatters': '这是 agent 企业化的关键架构决策，解耦设计让 agent 可以适应不同的合规和安全要求。',
        'tags': ['产品', 'Agent', '工程'],
        'qualityScore': 88,
        'url': 'https://www.anthropic.com/engineering/managed-agents'
    },
    {
        'type': 'blog',
        'typeLabel': '深度文章',
        'date': '7月10日 · 周五',
        'actor': 'Anthropic Engineering',
        'meta': 'Anthropic Engineering Blog',
        'title': 'Claude Code 质量问题的 postmortem',
        'summary': 'Anthropic 工程博客发布关于 Claude Code 质量报告的 postmortem。过去一个月他们调查了用户反馈的 Claude 响应质量下降问题，并分享了调查过程和修复措施。这是工程透明度的体现。',
        'keyPoints': [
            '调查用户反馈的质量下降问题',
            '分享调查过程和根因分析',
            '工程透明度建立用户信任'
        ],
        'whyItMatters': '工程 postmortem 是建立用户信任的重要方式，也是团队学习和改进的机制。',
        'tags': ['产品', 'Agent', '工程'],
        'qualityScore': 82,
        'url': 'https://www.anthropic.com/engineering/april-23-postmortem'
    },
    {
        'type': 'podcast',
        'typeLabel': '播客摘录',
        'date': '7月8日 · 周三',
        'actor': 'AI & I by Every',
        'meta': '播客节目',
        'title': '作家如何在不失去声音的前提下使用 AI',
        'summary': '这期播客探讨作家如何在使用 AI 的同时保持个人声音。核心论点是 AI 应该辅助而非替代创作过程，作家需要建立清晰的工作流来区分 AI 辅助和原创内容。这对所有内容创作者都有参考价值。',
        'keyPoints': [
            'AI 辅助而非替代创作过程',
            '建立清晰的工作流区分 AI 和原创',
            '保持个人声音是关键挑战'
        ],
        'whyItMatters': '这是 AI 时代内容创作的核心问题，作家的实践经验对所有知识工作者都有参考价值。',
        'tags': ['Agent', '研究'],
        'qualityScore': 75,
        'url': 'https://www.youtube.com/watch?v=7ND0lQmLJlA'
    }
]

with open('data/archive/2026-07-10.json', 'w', encoding='utf-8') as f:
    json.dump(archive, f, ensure_ascii=False, indent=2)

with open('data/latest.json', 'w', encoding='utf-8') as f:
    json.dump(archive, f, ensure_ascii=False, indent=2)

with open('data/digests.json', 'r', encoding='utf-8') as f:
    digests = json.load(f)

digests = [d for d in digests if d.get('date') != '2026-07-10']
digests.insert(0, archive)

with open('data/digests.json', 'w', encoding='utf-8') as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print('Curated 10 high-signal items')
print('Updated archive, latest.json, and digests.json')
