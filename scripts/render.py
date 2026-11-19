"""Render centralized book, ecosystem, case and resource metadata into Markdown."""
import argparse
import json
import re
from pathlib import Path

from render_cases import render_selected_cases

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true")
ARGS = parser.parse_args()
changed = []


def read(name):
    return json.loads((ROOT / name).read_text())


def put(name, content):
    content = content.rstrip() + "\n"
    path = ROOT / name
    if path.exists() and path.read_text() == content:
        return
    changed.append(name)
    if not ARGS.check:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


def block(name, tag, content):
    original = (ROOT / name).read_text()
    pattern = r"<!-- " + tag + r":start -->.*?<!-- " + tag + r":end -->"
    replacement = "<!-- " + tag + ":start -->\n\n" + content.strip() + "\n\n<!-- " + tag + ":end -->"
    if len(re.findall(pattern, original, re.S)) != 1:
        raise ValueError("Missing or duplicate generated block: " + name + "/" + tag)
    put(name, re.sub(pattern, lambda _: replacement, original, flags=re.S))


def cell(s):
    text = str(s).replace("|", "&#124;").replace("\n", " ")
    return re.sub(r'https?://[A-Za-z0-9./?=&_%:#~-]+', lambda m: '<' + m.group(0) + '>', text)


book = read("book/metadata.json")
chapters = read("book/chapters.json")
eco = read("community/ecosystem.json")
for name in ["README.md", "README_EN.md", "book/README.md"]:
    prefix = "../" if name.startswith("book/") else ""
    bp = "" if prefix else "book/"
    en = name == "README_EN.md"
    title = "Book and companion materials" if en else "图书与配套资料"
    byline = ("Author: " if en else "作者：") + book["author"] + " · " + book["publisher"]
    status = ("Published; more than 2,000 copies sold." if en else
              "正式出版，图书销量已突破2000册。")
    # Sales text is assembled from metadata to avoid a separate editable claim.
    status = status.replace("2,000", book["sales"].rstrip("+")).replace("2000", book["sales"].rstrip("+"))
    links = [("Publisher details" if en else "图书详情", book["publisherUrl"])]
    links += [(("Buy: " if en else "正版购买：") + x["name"], x["url"]) for x in book["purchases"]]
    links += [("Open-source companion materials" if en else "开源配套资料", book["companionUrl"]),
              ("Full contents" if en else "完整目录", bp + "table-of-contents.md"),
              ("Join the community" if en else "加入社区", "https://fdechina.ai/community/join"),
              ("Errata" if en else "勘误反馈", bp + "errata.md")]
    intro = ("A Chinese-language guide to FDE roles, business discovery, ontology, PoC, knowledge engineering, Agents, production delivery and industry practice." if en else
             "系统学习FDE定位与能力、业务调研、场景与本体建模、PoC、知识工程、Agent工程化、生产治理及制造、电商与出海实践。")
    content = ("## " + title + "\n\n" +
               '<img src="' + prefix + book["cover"] + '" width="220" alt="' + book["title"] + ' 正式封面">\n\n' +
               "### 《" + book["title"] + "》\n\n" + byline + " · " + book["publicationDate"] + " · ISBN " + book["isbn"] +
               "\n\n**" + status + "**\n\n" + intro + "\n\n" +
               " · ".join("[" + label + "](" + url + ")" for label, url in links) +
               "\n\n" + ("Metadata checked: " if en else "出版信息核验：") + book["verifiedAt"] + "。")
    block(name, "book", content)

for name in ["README.md", "README_EN.md", "community/README.md"]:
    en = name == "README_EN.md"
    content = "| " + ("Entry | Role" if en else "入口 | 定位") + " |\n| --- | --- |\n"
    content += "\n".join("| [" + x["name"] + "](" + x["url"] + ") | " + x["en" if en else "role"] + " |" for x in eco)
    block(name, "ecosystem", content)

chapter_rows = "| 章 | 正式章名 | 起始页 | 配套学习 |\n| --- | --- | ---: | --- |\n"
for c in chapters:
    cid = str(c["number"]).zfill(2)
    chapter_rows += f'| {c["number"]} | {c["title"]} | {c["page"]} | [进入](chapters/{cid}.md) |\n'
    block("book/chapters/" + cid + ".md", "chapter",
          "正式章名：**" + c["title"] + "**；纸书起始页：" + str(c["page"]) + "。章名与顺序依据[出版社正式目录](" + book["catalogUrl"] + ")。")
block("book/README.md", "chapters", chapter_rows)
toc = "# 图书完整目录\n\n章名、编号、顺序与页码已按[出版社正式目录](" + book["catalogUrl"] + ")核对（" + book["verifiedAt"] + "）。以下仅列目录，不包含正文。\n\n" + chapter_rows
for c in chapters:
    toc += "\n## 第" + str(c["number"]) + "章 " + c["title"] + "\n\n"
    toc += "| 节 | 标题 | 页码 |\n| --- | --- | ---: |\n"
    toc += "\n".join(f'| {s["number"]} | {s["title"]} | {s["page"]} |' for s in c["sections"]) + "\n"
put("book/table-of-contents.md", toc)

cases = read("cases/catalog.json")
categories = ["制造业", "跨境电商", "外贸出口", "连锁零售", "医药健康", "金融与保险", "企业服务", "物流与供应链", "营销与销售", "企业知识管理"]
content = "# FDE中国案例与实践文章索引\n\n来自本地社区快照的" + str(len(cases)) + "篇资料，仅保存摘要与链接。类型均为公开案例/实践文章（来源整理），不代表独立审计。原行业字段保留；通用电商不自动具备跨境部署证据。未披露的背景、架构、基线、验收或收益保持未知。\n\n"
content += " · ".join("[" + c + "](#" + c + ")" for c in categories) + "\n"
for category in categories:
    content += "\n## " + category + "\n\n"
    selected = [c for c in cases if c["category"] == category]
    if not selected:
        content += "当前快照暂无明确匹配条目。欢迎按[案例模板](case-template.md)补充可核验来源。\n"
        continue
    content += "| ID / 原行业 | 阅读条目与摘要 | 来源日期 |\n| --- | --- | --- |\n"
    for c in selected:
        content += "| " + c["id"] + " / " + c["originalIndustry"] + " | [" + cell(c["title"]) + "](" + c["url"] + ") — " + cell(c["summary"]) + " | " + c["publishedAt"][:10] + " |\n"
put("cases/catalog.md", content)

render_selected_cases(read, put, block, cell)

tools = read("resources/catalog.json")
content = "# 企业AI技术资源图谱\n\n重点项目逐条记录仓库、文档、定位、适用场景、技术特征、许可和企业注意事项。元数据核验不等于部署或安全认证。\n\n"
content += "## 工程层导航\n\n| 工程层 | 入口 |\n| --- | --- |\n"
layers = [
("大模型与推理", "../tools/model-serving.md"), ("Prompt与上下文", "prompt-and-context.md"),
("Agent框架与Workflow", "../cookbook/agent/README.md"), ("Agent Harness", "../cookbook/harness/README.md"),
("Multi-Agent", "../cookbook/multi-agent/README.md"), ("Skill", "../cookbook/skill/README.md"),
("MCP", "../cookbook/mcp/README.md"), ("RAG与知识库", "rag-and-knowledge.md"),
("文档解析", "rag-and-knowledge.md"), ("数据清洗与治理", "../toolkit/templates/data-governance.md"),
("向量数据库", "../tools/vector-databases.md"), ("知识图谱与本体", "../cookbook/ontology/README.md"),
("企业系统集成", "../delivery/implementation.md"), ("AI评测", "llmops-and-evaluation.md"),
("可观测性", "../tools/observability.md"), ("模型部署", "model-deployment.md"),
("AI安全与治理", "ai-security.md"), ("企业级AI应用", "../tools/application-platforms.md"),
("Vibe Coding", "../cookbook/llm/README.md"), ("模型网关", "../tools/ai-gateways.md")]
content += "\n".join("| " + a + " | [进入](" + b + ") |" for a, b in layers) + "\n"
for t in tools:
    content += "\n## " + t["name"] + "\n\n"
    fields = [("分类", t["category"]), ("官方仓库", "[GitHub](" + t["repository"] + ")"),
              ("官方文档", "[文档](" + t["docs"] + ")"), ("核心定位", t["purpose"]),
              ("适用场景", t["scenario"]), ("技术特点", t["features"]),
              ("许可证", t["license"] + "；[仓库许可说明](" + t["licenseUrl"] + ")"),
              ("企业注意事项", t["note"]), ("核验", t["verifiedAt"] + "；" + t["verification"])]
    content += "\n".join("- " + k + "：" + v for k, v in fields) + "\n"
content += "\n## 部署地区与采购判断\n\n大陆企业应实测模型和依赖下载可用性、私有化硬件资源、日志位置及数据出域路径。框架开源许可不涵盖模型权重和商业托管服务。按[选型矩阵](../toolkit/templates/technology-selection.md)记录结果。\n"
put("resources/frameworks.md", content)
if ARGS.check and changed:
    print("Generated files out of date: " + ", ".join(changed))
    raise SystemExit(1)
print(("Checked" if ARGS.check else "Rendered") + " metadata; changed=" + str(len(changed)))
