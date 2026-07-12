import json

# Read the archive
with open('data/archive/2026-07-13.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build dailyInsight
dailyInsight = {
    "paragraphs": [
        "今天的信息密度集中在一个核心主题：GPT 5.6 Sol 的发布正在重塑 coding agent 的竞争格局。OpenAI Codex 负责人 Thibault Sottiaux 列出了这个版本逐项兑现的工程承诺——速度、token 效率、后端能力、前端质量，以及不再滥用 useEffect。这不是营销话术，而是直接回应了开发者社区过去几个月对 speed、code slop、frontend quality 的连续抱怨。一个产品负责人能精确复述用户的痛点并逐项打勾，说明 OpenAI 的反馈回路在缩短。",
        "Swyx 抛出了一个值得咀嚼的框架：Jevons Paradox 在 agentic engineering 时代的完整含义。当 coding agent 让软件生产的边际成本趋近于零时，需求不会饱和，反而会爆发。更关键的是他的第二层推论——如果人类学会了驾驭 coding agent，而 coding agent 又在向所有知识工作溢出，那么 Jevons Paradox 的冲击范围将远超「软件变多」，而是重新定义哪些工作值得人类做。",
        "Aaron Levie 从劳动力市场角度验证了同一个逻辑：AI 本该取代软件工程师，但软件岗位反而在增速上超过其他领域。他的解释和 Jevons Paradox 完全一致——生产成本下降 → 用例增加 → 需求扩大。这对所有担心「AI 抢饭碗」的 builder 来说是一个反直觉但有数据支撑的信号。",
        "Sam Altman 声称多个 benchmark 显示 5.6 Sol 是当前最强模型，并用「Elon 又开始 obsessed with me」作为最可靠的佐证。这句话的真实信息量不在 benchmark 本身，而在于它揭示了 OpenAI 与 xAI 之间的竞争张力仍在升级。模型能力的竞争已经不只是技术问题，而是创始人级别的注意力争夺。",
        "播客方面，No Priors 采访了 Booking.com CEO Glenn Fogel，标题直言「There is no such thing as a moat」。在一个 AI 正在瓦解传统壁垒的时代，旅行行业巨头选择主动拥抱这个判断，而不是防守，这本身就是一个信号。"
    ],
    "filteredNote": "过滤掉了 Peter Yang、Matt Turck、Nikunj Kothari 的足球评论，Guillermo Rauch 的生活日常，Garry Tan 的住房政策讨论，以及 Zara Zhang 的一句话评价等多条低信号内容。"
}

# Build highSignalItems
highSignalItems = [
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月12日 · 周日",
        "actor": "Swyx",
        "meta": "Latent Space · X 动态",
        "title": "Jevons Paradox 在 Agent 时代的完整推论",
        "summary": "Swyx 指出，如果你只在 agentic engineering 的语境下理解 Jevons Paradox（成本下降 → 需求增加），你可能还没有完全内化它的影响。两个被忽略的条件：一是人类学会驾驭 coding agent 后的效率乘数，二是 coding agent 正在突破软件边界向所有知识工作溢出。这意味着软件生产的爆发只是开始。",
        "keyPoints": [
            "Jevons Paradox 不只是「软件变多」，而是整个知识工作的成本结构被重写",
            "人类 + coding agent 的组合效率是被低估的变量",
            "当 agent 从代码溢出到其他知识工作，冲击范围将远超软件工程"
        ],
        "whyItMatters": "这是今天最有框架价值的一条推文。它把 Jevons Paradox 从经济学概念升级成了 AI builder 的战略推演工具。",
        "tags": ["Agent", "工程"],
        "qualityScore": 88,
        "url": "https://x.com/swyx/status/2076155833428431012"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月12日 · 周日",
        "actor": "Thibault Sottiaux",
        "meta": "OpenAI Codex · X 动态",
        "title": "GPT 5.6 Sol 逐项兑现开发者抱怨清单",
        "summary": "OpenAI Codex 负责人 Thibault Sottiaux 直接列出开发者过去几个月的核心抱怨——速度、code slop、前端质量——然后逐一说明 GPT 5.6 Sol 的改进：快速且 token 高效、后端硬核、前端优秀、不再到处使用 useEffect。最后反问「What is next?」，展示了一种罕见的产品迭代透明度。",
        "keyPoints": [
            "GPT 5.6 Sol 在速度和 token 效率上有显著提升",
            "前端质量被单独强调，回应了「code slop」批评",
            "「不再滥用 useEffect」是一个具体的工程改进信号",
            "产品负责人直接复述用户痛点并逐项回应，反馈回路在缩短"
        ],
        "whyItMatters": "这不是普通的产品更新公告，而是 OpenAI 在 coding agent 赛道上展示迭代速度的方式。对 builder 来说，选择工具时需要重新评估 5.6 Sol。",
        "tags": ["产品", "工程"],
        "qualityScore": 85,
        "url": "https://x.com/thsottiaux/status/2076145711922696371"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月12日 · 周日",
        "actor": "Aaron Levie",
        "meta": "Box CEO · X 动态",
        "title": "AI 没有消灭软件岗位，反而在加速需求",
        "summary": "Box CEO Aaron Levie 指出一个反直觉的现象：AI 本应取代的软件工程岗位，实际招聘增速反而超过了其他领域。他的解释是经典的 Jevons Paradox——当某种东西的生产成本下降，而它又有大量使用场景时，人们会想要更多。这在工业时代已经反复上演，现在轮到了软件。",
        "keyPoints": [
            "软件岗位增速超过其他领域，与「AI 取代程序员」的叙事矛盾",
            "核心逻辑：成本下降 → 用例增加 → 需求扩大（Jevons Paradox）",
            "工业时代的历史正在 AI 时代重演"
        ],
        "whyItMatters": "Aaron Levie 用劳动力市场数据验证了 Swyx 的 Jevons Paradox 框架。对 builder 来说，这意味着 AI 工具越强大，软件工程的市场需求可能越大，而不是越小。",
        "tags": ["产品", "Agent", "工程"],
        "qualityScore": 83,
        "url": "https://x.com/levie/status/2076116544980214164"
    },
    {
        "type": "post",
        "typeLabel": "观点动态",
        "date": "7月11日 · 周六",
        "actor": "Sam Altman",
        "meta": "OpenAI CEO · X 动态",
        "title": "5.6 Sol 的最强信号：Elon 又开始 obsessed",
        "summary": "Sam Altman 声称多个 benchmark 显示 GPT 5.6 Sol 是当前世界最强模型，但他认为「最可靠的判断方式」是 Elon Musk 又开始对他痴迷。这句话的真实信息量不在 benchmark 本身——benchmark 领先是预期内的——而在于它揭示了 OpenAI 与 xAI 之间的竞争张力仍在升级，模型能力的竞争已经演变为创始人级别的注意力争夺。",
        "keyPoints": [
            "5.6 Sol 在多个 benchmark 上领先，OpenAI 官方确认",
            "Altman 用 Elon 的反应作为「最可靠信号」，暗示 xAI 的竞争力构成实质压力",
            "模型竞争已超越技术层面，进入创始人叙事战争"
        ],
        "whyItMatters": "这条推文的价值不在于 benchmark 声明，而在于它暴露了 AI 头部竞争的真实动态。当 CEO 用竞争对手创始人的行为来证明产品力时，说明竞争已进入白热化。",
        "tags": ["研究"],
        "qualityScore": 78,
        "url": "https://x.com/sama/status/2075983427019612242"
    },
    {
        "type": "podcast",
        "typeLabel": "播客摘录",
        "date": "7月9日 · 周四",
        "actor": "No Priors × Booking.com CEO Glenn Fogel",
        "meta": "No Priors Podcast · 播客",
        "title": "「不存在护城河」—— Booking.com CEO 的 AI 时代生存逻辑",
        "summary": "Booking.com CEO Glenn Fogel 在 No Priors 播客中直言「不存在护城河」。在一个 AI 正在瓦解传统竞争壁垒的时代，旅行行业最大的玩家之一选择主动拥抱这个判断，而不是试图防守。这期播客的核心论点是：当 AI 让信息获取和个性化服务变得廉价时，传统的规模壁垒（库存、品牌、网络效应）正在被重新定义。",
        "keyPoints": [
            "传统护城河在 AI 时代正在被瓦解，没有任何壁垒是安全的",
            "Booking.com 选择主动拥抱变化而非防守，这本身是一个战略信号",
            "AI 让信息获取和个性化服务成本下降，重新定义了旅行行业的竞争维度"
        ],
        "whyItMatters": "一个传统行业的 CEO 公开说「不存在护城河」并主动拥抱 AI，比技术圈内的同类讨论更有说服力。这对所有在「护城河」思维下做产品的 builder 是一个提醒。",
        "tags": ["组织"],
        "qualityScore": 76,
        "url": "https://www.youtube.com/watch?v=8nj_0wZkbtA"
    }
]

# Update the archive JSON
data["dailyInsight"] = dailyInsight
data["highSignalItems"] = highSignalItems

# Write archive
with open("data/archive/2026-07-13.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Write latest
with open("data/latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Update digests.json
with open("data/digests.json", "r", encoding="utf-8") as f:
    digests = json.load(f)

# Remove existing entry for today if present
digests = [d for d in digests if d.get("date") != "2026-07-13"]
# Prepend new entry
digests.insert(0, data)

with open("data/digests.json", "w", encoding="utf-8") as f:
    json.dump(digests, f, ensure_ascii=False, indent=2)

print(f"Done. Items kept: {len(highSignalItems)}")
print("Filtered: football commentary (Peter Yang, Matt Turck, Nikunj Kothari), daily life (Guillermo Rauch), policy (Garry Tan CEQA), thin one-liners (Zara Zhang)")
