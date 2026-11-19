"""Generate public contributor names from Git history, without email addresses."""
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
names = subprocess.check_output(["git", "log", "--format=%aN"], cwd=root, text=True).splitlines()
unique = sorted(set(n.strip() for n in names if n.strip()), key=str.casefold)
content = "# 贡献者\n\n依据当前Git历史生成，只展示公开作者名，不公开邮箱。资源作者与仓库贡献者分别记录。\n\n"
content += "\n".join("- " + n.replace("<", "&lt;").replace(">", "&gt;") for n in unique)
content += "\n\n[完整贡献历史](https://github.com/fdeopen/awesome-fde/graphs/contributors) · [参与贡献](../CONTRIBUTING.md)\n\n维护命令：`python3 scripts/update_contributors.py`。定时任务生成更新草稿供维护者审阅，不自动向主分支写入。\n"
(root / "community/contributors.md").write_text(content)
print("Contributors:", len(unique))
