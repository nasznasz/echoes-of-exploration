#!/usr/bin/env python3
"""Pick one mission photo and one aesthetic photo per mission from the NASA Image and Video Library,
save them to data/image_pins.json and write docs/IMAGE_SOURCES.md. Needs internet. Standard library only."""
import json, os, re, sys, urllib.parse, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOOD = re.compile(r"panorama|sunset|sunrise|earthrise|crescent|horizon|selfie|view|rise|shadow|window|glow|sky|landscape|dust|surface|rings|flight", re.I)
BAD = re.compile(r"logo|patch|insignia|diagram|chart|graph|poster|schematic|table|team|portrait|press|briefing|conference|ceremony|crew photo", re.I)

def search(q):
    url = "https://images-api.nasa.gov/search?media_type=image&page_size=12&q=" + urllib.parse.quote(q)
    with urllib.request.urlopen(url, timeout=20) as r:
        items = json.load(r)["collection"]["items"]
    out = []
    for i in items:
        d = (i.get("data") or [{}])[0]
        if i.get("links") and d.get("nasa_id"):
            out.append({"id": d["nasa_id"], "t": d.get("title", ""), "u": i["links"][0]["href"],
                        "l": "https://images.nasa.gov/details/" + urllib.parse.quote(d["nasa_id"]),
                        "c": (d.get("secondary_creator") or d.get("center") or "NASA") + ((" · " + d["date_created"][:4]) if d.get("date_created") else "")})
    return out[:10]

def score(p, q):
    s = 0
    s += 2 if GOOD.search(p["t"]) else 0
    s -= 5 if BAD.search(p["t"]) else 0
    s += sum(1 for w in re.split(r"\W+", q.lower()) if len(w) > 3 and w in p["t"].lower())
    return s

def best(queries):
    for q in queries:
        try:
            items = search(q)
        except Exception as e:
            print("  search failed:", q, e); continue
        if items:
            return max(items, key=lambda p: score(p, q))
    return None

def main():
    M = json.load(open(os.path.join(ROOT, "data/missions.json")))
    pins, rows = {}, []
    for m in M:
        print(m["name"])
        a = best(m.get("nasaQueries") or [m["name"]]); b = best(m.get("scenic") or [])
        pins[m["id"]] = {k: v for k, v in (("main", a), ("scenic", b)) if v}
        for role, p in (("Mission photo", a), ("Aesthetic photo", b)):
            rows.append(f"| {m['name']} | {role} | {p['t'].replace('|','/') if p else 'none found'} | {p['id'] if p else ''} | {p['l'] if p else ''} | {p['c'] if p else ''} |")
    json.dump(pins, open(os.path.join(ROOT, "data/image_pins.json"), "w"), indent=1, ensure_ascii=False)
    head = "# Image sources (NASA)\n\nPictures from the NASA Image and Video Library (https://images.nasa.gov). Credit NASA and the creator shown. NASA does not endorse this project. Regenerate with `python3 scripts/pin_nasa_images.py`.\n\n| Mission | Role | Title | NASA ID | Link | Credit |\n|---|---|---|---|---|---|\n"
    open(os.path.join(ROOT, "docs/IMAGE_SOURCES.md"), "w").write(head + "\n".join(rows) + "\n")
    if "--download" in sys.argv:
        os.makedirs(os.path.join(ROOT, "data/img"), exist_ok=True)
        for mid, pr in pins.items():
            for role, name in (("main", mid), ("scenic", mid + "-scenic")):
                if role in pr:
                    try: urllib.request.urlretrieve(pr[role]["u"].replace("~thumb", "~medium"), os.path.join(ROOT, f"data/img/{name}.jpg"))
                    except Exception as e: print("  download failed", name, e)
    print("Wrote data/image_pins.json and docs/IMAGE_SOURCES.md")
main()
