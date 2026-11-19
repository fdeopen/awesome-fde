"""Render a compact public-case selection from the existing source catalog."""
from datetime import date
import re


INDUSTRIES = {
    "制造业与汽车": "Manufacturing and automotive",
    "电商与零售": "E-commerce and retail",
    "金融与保险": "Finance and insurance",
    "医疗健康": "Healthcare",
    "物流与供应链": "Logistics and supply chains",
    "互联网与媒体": "Internet and media",
    "专业服务": "Professional services",
}


def render_selected_cases(read, put, block, cell):
    selection = read("cases/selected.json")
    sources = {item["id"]: item for item in read("cases/catalog.json")}
    items = selection["items"]
    date.fromisoformat(selection["updatedAt"])
    if not 1 <= len(items) <= 30:
        raise ValueError("The homepage selection must contain 1–30 public cases")
    if len({item["id"] for item in items}) != len(items):
        raise ValueError("Duplicate selected case IDs")
    required = ("title", "titleEn", "focus", "focusEn", "problem", "approach", "evidence", "takeaway")
    urls = set()
    for item in items:
        source = sources.get(item["id"])
        if source is None or not source["url"].startswith("https://"):
            raise ValueError("Missing public source: " + item["id"])
        if source["url"] in urls:
            raise ValueError("Duplicate selected source URL: " + source["url"])
        urls.add(source["url"])
        if item["industry"] not in INDUSTRIES or any(not item.get(key, "").strip() for key in required):
            raise ValueError("Incomplete selected case: " + item["id"])
        snapshot = item["snapshot"]
        expected_path = "src/content/generated/cases-external/" + source["url"].rsplit("/", 1)[-1] + ".md"
        if (snapshot["repository"] != "fde-china" or snapshot["path"] != expected_path
                or not re.fullmatch(r"[0-9a-f]{64}", snapshot["sha256"])):
            raise ValueError("Invalid local source record: " + item["id"])

    ordered = sorted(items, key=lambda item: (list(INDUSTRIES).index(item["industry"]), item["id"]))
    count = len(items)
    industry_count = len({item["industry"] for item in items})
    for name in ("README.md", "README_EN.md", "cases/README.md"):
        en = name == "README_EN.md"
        prefix = "" if name.startswith("cases/") else "cases/"
        if en:
            content = f"## {count} public cases\n\n"
            content += f"Selected from public articles across **{industry_count} industry categories**. Case titles link to the source articles; summaries are curated for this guide.\n\n"
            content += f"[Case notes]({prefix}selected.md) · [Full reading index]({prefix}catalog.md)\n\n"
            content += "| Industry | Public case | What to study |\n| --- | --- | --- |\n"
        else:
            content = f"## {count} 个公开案例\n\n"
            content += f"从公开资料中精选，覆盖 **{industry_count} 个行业分类**。点击案例名称阅读来源文章；阅读重点由本项目整理。\n\n"
            content += f"[查看案例拆解]({prefix}selected.md) · [全部阅读资料]({prefix}catalog.md)\n\n"
            content += "| 行业 | 公开案例 | 阅读重点 |\n| --- | --- | --- |\n"
        for item in ordered:
            industry = INDUSTRIES[item["industry"]] if en else item["industry"]
            title = item["titleEn" if en else "title"]
            focus = item["focusEn" if en else "focus"]
            content += f'| {industry} | [{cell(title)}]({sources[item["id"]]["url"]}) | {cell(focus)} |\n'
        block(name, "public-cases", content)

    content = f"# {count} 个公开案例 · 阅读与交付拆解\n\n"
    content += f"整理日期：{selection['updatedAt']}。依据本地保存的公开文章整理，引用与日期回溯到来源。实施状态与效果按原文披露；“FDE 启发”为本项目的学习建议。\n\n"
    content += "本选集不收录本地项目或模拟教学案例；一篇多企业经验汇总计一条，同一企业不同工作流可分别收录。原始文章不在此转载。\n\n"
    content += "[返回案例索引](README.md) · [收录与维护](curation.md) · [原始资料目录](catalog.md)\n\n"
    content += "| 行业 | 数量 |\n| --- | ---: |\n"
    for industry in INDUSTRIES:
        subset = [item for item in ordered if item["industry"] == industry]
        if subset:
            content += f"| [{industry}](#{industry}) | {len(subset)} |\n"
    for industry in INDUSTRIES:
        subset = [item for item in ordered if item["industry"] == industry]
        if not subset:
            continue
        content += f"\n## {industry}\n"
        for item in subset:
            source = sources[item["id"]]
            content += f'\n<a id="{item["id"].lower()}"></a>\n\n### {item["id"]} · {item["title"]}\n\n'
            for label, key in (("业务问题", "problem"), ("实施做法", "approach"), ("公开资料范围", "evidence"), ("FDE 启发", "takeaway")):
                content += f'- **{label}**：{item[key]}\n'
            content += f'- **来源**：[{cell(source["title"])}]({source["url"]})；来源日期：{source["publishedAt"][:10]}。\n'
    content += "\n## 维护说明\n\n标题、分类与拆解维护在 [selected.json](selected.json)，来源链接与日期取自 [catalog.json](catalog.json)。本地文章文件的 SHA-256 记录在每条精选数据中，用于识别后续来源变动。生成方式见[维护说明](curation.md)。\n"
    put("cases/selected.md", content)
