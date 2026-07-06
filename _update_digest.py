import json
from datetime import datetime

with open('data/archive/2026-07-07.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add dailyInsight
data['dailyInsight'] = {
    'paragraphs': [
        '今天的信号密度不高——7月4日美国独立日加周末，多数 builder 处在休息状态。不过 Nan Yu（Linear 产品负责人）的两条观察值得细读：他认为「即时战略游戏」式的 Agent 管理范式（微观管理每一个 Agent 的行为）已经走到尽头——旧时代的 AI 在微操层面已经碾压人类，不应该再让人类扮演「指挥官」角色。这种观点与 Anthropic 等公司推动的「让 Agent 更自主」方向一致，预示着人机协作的新接口范式正在形成。',
        'Cat Wu（Anthropic Claude Code 团队）分享了一个具体 workflow：用 Claude Code 自动搜索候选人，整合 LinkedIn、Twitter、博客和播客信息，并为每位候选人生成一句话 pitch。这个用例的价值在于把 Claude Code 从「代码工具」延伸到了「知识工作自动化」——说明 Agent 在非编程的知识密集型场景中也有实用空间，而不仅仅是代码补全。',
        'Garry Tan（YC CEO）发表了两个值得关注的观点。其一是「人类财富的真正约束从来不是资源，而是好的想法和利用好想法的杠杆——我们刚刚为所有人消除了杠杆约束」。这是一个简洁的 thesis：AI 让执行不再稀缺，剩下来的竞争壁垒是想法质量。其二是他在大阪的观察：日本经历了三十年零增长，却锻造出了全世界最好的服务、交通和手工艺——当无法竞争「更多」，就竞争「更好」。而 AI 时代可以同时做到更多和更好。',
        'Dan Shipper（Every 主编）延续了上周的「Fable 过度使用 Agent」讽刺线。一条假装用户说「把这个按钮换个颜色」，Fable 回复「没问题，我刚启动了 100 个 Agent 来完成这个任务」——精准吐槽了当前行业里「为用 Agent 而用 Agent」的倾向。与 Nan Yu 的 RTS 观点形成呼应：行业在 Agent 自主性和过度工程化之间寻找平衡点。',
        'No Priors 播客发布了与 OpenAI 研究科学家 Noam Brown 的访谈，主题是超大规模 Test-Time Compute（测试时计算）正在改变基准测试、安全研究和 AI 研究范式。Noam Brown 是博弈论和推理方面的关键研究者（此前因在扑克 AI 方面的工作闻名），这期播客是理解 OpenAI 在推理方向上思考的重要一手资料。'
    ],
    'filteredNote': '过滤掉了 Sam Altman（育儿观察）、Guillermo Rauch（体育预测）、Amjad Masad（美国独立日祝福）、Amanda Askell（就医感想）、Thariq（旧金山文化幽默）、Peter Yang（体育评论+生日自荐）、Matt Turck（体育+单句Agent玩笑）、Nikunj Kothari（旅行推荐+VC方法）、Peter Steinberger（内容截断无上下文）、Zara Zhang（代码理解技能提及但无细节）等低信号内容。'
}

highSignalItems = [
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月6日 · 周一',
        'actor': 'Nan Yu',
        'meta': 'Linear 产品负责人 · X 动态',
        'title': 'Agent 的「即时战略游戏」管理范式已经过时',
        'summary': 'Nan Yu（Linear 产品负责人）指出，把管理 AI Agent 当作即时战略游戏（RTS）来微观操作已经走不通了——即使是旧时代的 AI 也能在微操层面碾压 99% 以上的玩家。这个类比精准地批评了当前很多 Agent 产品把人类当作「微操指挥官」的设计思路，暗示真正的 Agent 化应该是设定目标后让模型自主执行，而不是人类实时盯着每一步。',
        'keyPoints': [
            'RTS 式管理（微观操作每个 Agent 行为）是死路，因为 AI 在微操上早已碾压人类。',
            '真正的人机协作应转向「设定目标→自主执行」范式。',
            '与 Anthropic 等推动的 Agent 自主化方向一致，暗示产品设计需要根本性转变。'
        ],
        'whyItMatters': '它用一个简洁的类比点出了当前 Agent 产品设计中一个普遍的但尚未被广泛讨论的误区。',
        'tags': ['Agent', '产品', '研究'],
        'qualityScore': 85,
        'url': 'https://x.com/thenanyu/status/2073920326304460847'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月6日 · 周一',
        'actor': 'Nan Yu',
        'meta': 'Linear 产品负责人 · X 动态',
        'title': '炫耀同时打开 10 个 Claude Code 标签页只是「表演」',
        'summary': 'Nan Yu 在另一条推文中直接批评了行业里一种常见的展示方式——炫耀同时运行多个 Claude Code 实例。他认为这种「多开」除展示外没有实质意义，暗示衡量 AI 编码工具的指标应该是实际产出质量而非并发数量。这与上一条 Agent 观点形成互补：不是 Agent 越多越好，而是 Agent 越自主越好。',
        'keyPoints': [
            '运行多个 Claude Code 实例不等于更高效率。',
            '行业需要从「并发数量崇拜」转向关注实际产出。',
            '与 RTS 观点一致：核心问题是 Agent 质量/自主性，不是数量。'
        ],
        'whyItMatters': '它对当前 AI 编码工具使用中一种流行但可能误导的炫耀方式提出了直接质疑。',
        'tags': ['Agent', '工程'],
        'qualityScore': 78,
        'url': 'https://x.com/thenanyu/status/2073920959011074292'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月5日 · 周日',
        'actor': 'Cat Wu',
        'meta': 'Anthropic Claude Code 团队 · X 动态',
        'title': '用 Claude Code 自动搜索候选人：非编程知识工作的新用例',
        'summary': 'Cat Wu（Anthropic）分享了她在 Claude Code 中发现的一个新用例——候选人搜索。工作流（workflow）是：告诉 Claude Code 招聘角色和所需背景，它会启动一个动态工作流自动找到 100 名候选人，并为每个人整理 LinkedIn、Twitter、博客、播客链接，以及一句话 pitch。这个场景展示 Claude Code 正在从「代码工具」扩展到更广泛的知识工作自动化领域。',
        'keyPoints': [
            'Claude Code 可用于候选人搜索等非编程知识密集型任务。',
            '自动聚合多平台信息（LinkedIn, Twitter, 博客, 播客）并生成结构化输出。',
            '展示了 Agent 在招聘、研究等场景中的实用潜力。'
        ],
        'whyItMatters': '它展示了 Claude Code 在编程之外的意外用例，暗示 Agent 化工具的知识工作场景比预期更广。',
        'tags': ['产品', 'Agent', '工程'],
        'qualityScore': 80,
        'url': 'https://x.com/_catwu/status/2073806626965049686'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月5日 · 周日',
        'actor': 'Garry Tan',
        'meta': 'YC CEO · X 动态',
        'title': 'AI 消除了执行的杠杆约束，剩下的竞争壁垒是想法质量',
        'summary': 'Garry Tan（YC CEO）提出了一个简洁的 thesis：人类财富的真正约束从来不是资源，而是好的想法以及实现它们所需的杠杆。AI 刚刚为所有人消除了「杠杆约束」——剩下唯一的竞争要素是想法质量。对于创业者来说，这意味着「执行力溢价」正在快速消退，「判断力溢价」大幅上升。',
        'keyPoints': [
            '资源的稀缺从未是真正的约束，缺乏好想法和杠杆才是。',
            'AI 消除了杠杆约束——执行不再是稀缺资源。',
            '剩下的竞争壁垒是：谁能提出更好的想法并知道该做什么。'
        ],
        'whyItMatters': '它提供了一个简洁但有力的 AI 时代竞争框架，对创业者和 builder 的精力分配有直接指导意义。',
        'tags': ['观察', '创业'],
        'qualityScore': 88,
        'url': 'https://x.com/garrytan/status/2073881439700168925'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月5日 · 周日',
        'actor': 'Garry Tan',
        'meta': 'YC CEO · X 动态',
        'title': '日本的三十年零增长实验：当无法竞争「更多」，就竞争「更好」',
        'summary': 'Garry Tan 在大阪的观察：日本用三十年的零增长证明了，当增长空间被封顶后，社会可以转向极致质量。新干线、服务、手工艺——这些都是「无法做更多，就做更好」的产物。他的核心论点是：AI 时代的区别在于，我们可以同时做更多和更好——而不需要先选择牺牲其中一个。',
        'keyPoints': [
            '日本三十年零增长反而锻造了世界顶级质量。',
            '增长天花板不一定是坏事——它可以强制质量竞争。',
            'AI 带来的真正突破是：可以同时追求数量和质量的增长。'
        ],
        'whyItMatters': '它将日本的历史经验与 AI 时代的可能性连接起来，提供了一个观察长期趋势的独特视角。',
        'tags': ['观察', '创业'],
        'qualityScore': 82,
        'url': 'https://x.com/garrytan/status/2073881438123110512'
    },
    {
        'type': 'post',
        'typeLabel': '观点动态',
        'date': '7月5日 · 周日',
        'actor': 'Dan Shipper',
        'meta': 'Every 主编 · X 动态',
        'title': '为改一个按钮颜色启动 100 个 Agent：行业过度工程化讽刺',
        'summary': 'Dan Shipper（Every CEO）延续了对 Fable（AI 开发平台）的讽刺线。用户说「帮我改个按钮颜色」，Fable 回复「没问题，我刚启动了 100 个 Agent 来完成这个任务」。另一条跟进是「Fable on ultracode 模式下的\'别出错\'指令」。这调侃了当前行业中滥用 Agent 和过度抽象的倾向——小任务也要启动大量 Agent，复杂度和收益严重不匹配，与 Nan Yu 的 RTS 观点形成有趣呼应。',
        'keyPoints': [
            '精准讽刺了「为用 Agent 而用 Agent」的产品设计倾向。',
            '小任务（改按钮颜色）启动大量 Agent 是过度工程化的典型表现。',
            '与 Nan Yu 的「RTS 管理范式过时」观点形成互补。'
        ],
        'whyItMatters': '它以幽默方式提醒 builder：Agent 化的正确方向是合适粒度的自主，而非越多越好。',
        'tags': ['Agent', '产品', '工程'],
        'qualityScore': 76,
        'url': 'https://x.com/danshipper/status/2073764166700048480'
    },
    {
        'type': 'podcast',
        'typeLabel': '播客摘录',
        'date': '6月26日 · 周五',
        'actor': 'No Priors',
        'meta': 'No Priors · 播客 Episode',
        'title': 'Noam Brown 谈超大 Test-Time Compute 如何改变 AI 基准、安全与研究',
        'summary': 'No Priors 播客邀请 OpenAI 研究科学家 Noam Brown，讨论超大规模 test-time compute（测试时计算）对 AI 带来的根本性变化。Noam Brown 此前因在扑克 AI（Libratus、Pluribus）方面的工作闻名，是推理和博弈论领域的核心贡献者。本期覆盖了 test-time compute 如何改变已有基准测试的可靠性、对 AI 安全的意义，以及 OpenAI 在推进推理方向的最新思考。对于关注「推理模型」方向的 builder，这是理解 OpenAI 内部视角的重要一手材料。',
        'keyPoints': [
            'Test-time compute 规模正在快速放大，改变了模型能力的评估方式。',
            '传统基准测试在 test-time compute 新范式下的可靠性正在被重新审视。',
            'Noam Brown 是推理方向的关键研究者之一，其视角有独特价值。'
        ],
        'whyItMatters': '这是目前理解 test-time compute 前沿和 OpenAI 推理方向不可绕过的一期播客。',
        'tags': ['研究', '工程'],
        'qualityScore': 90,
        'url': 'https://www.youtube.com/watch?v=AZrU6y3pUcU'
    }
]

data['highSignalItems'] = highSignalItems

# Update headline and editorNote
data['headline'] = '今天信号量清淡但质量扎实：Agent 管理范式争议（Nan Yu vs. 过度工程化讽刺）、Garry Tan 的 AI 杠杆论点、Cat Wu 的 Claude Code 知识工作用例、以及 Noam Brown 谈 test-time compute。'
data['editorNote'] = '每日策展简报：过滤低信号日常内容，保留对 AI Builders 有实质价值的观点、工程洞察和深度内容。精选 7 条高信号条目。'

# Save to archive
with open('data/archive/2026-07-07.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Saved archive/2026-07-07.json')

# Save to latest.json
with open('data/latest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Saved latest.json')

# Update digests.json - replace entry 0
with open('data/digests.json', 'r', encoding='utf-8') as f:
    digests = json.load(f)

digests[0] = data

with open('data/digests.json', 'w', encoding='utf-8') as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print('Updated digests.json')
print(f'Curated {len(highSignalItems)} high-signal items')
