"""Advisory external-link check; never a blocking PR gate."""
import concurrent.futures
import argparse
import datetime
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--incremental', action='store_true', help='Reuse unchanged URL results from the last local run')
args = parser.parse_args()
urls = set()
for p in ROOT.rglob("*.md"):
    if any(x in p.parts for x in [".git", "node_modules", ".venv"]):
        continue
    text = re.sub(r"^```.*?^```[^\n]*", "", p.read_text(), flags=re.M | re.S)
    urls.update(re.findall(r'https?://[^\s<>"\)]+', text))
urls = sorted(u.rstrip(".,;") for u in urls if "example.com" not in u)


def check(url):
    code, final, detail = None, url, ""
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Awesome-FDE-LinkCheck/1.0"})
            with urllib.request.urlopen(req, timeout=12) as response:
                response.read(1024)
                code, final = response.status, response.url
            break
        except urllib.error.HTTPError as error:
            code, detail = error.code, str(error)
            if code not in {408, 429, 500, 502, 503, 504}:
                break
        except Exception as error:
            detail = str(error)
        if attempt == 0:
            time.sleep(1)
    status = "ok" if code and 200 <= code < 400 else (
        "access-limited-or-transient" if code in {401, 403, 408, 429, 500, 502, 503, 504} or code is None
        else "review")
    return {"url": url, "status": status, "http": code, "final_url": final, "detail": detail}


out = ROOT / "maintenance/external-links.json"
cache = {}
if args.incremental and out.exists():
    cache = {r['url']: r for r in json.loads(out.read_text())['results']}
pending = [u for u in urls if u not in cache]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    cache.update({r['url']: r for r in pool.map(check, pending)})
results = [cache[u] for u in urls]
out.write_text(json.dumps({"checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           "method": "GET, 12s timeout, max 2 attempts, 4 workers; unchanged URLs reused when incremental",
                           "fresh_checks": len(pending),
                           "results": results}, ensure_ascii=False, indent=2) + "\n")
summary = {s: sum(r["status"] == s for r in results) for s in ["ok", "review", "access-limited-or-transient"]}
print(json.dumps({"urls": len(results), **summary}, ensure_ascii=False))
