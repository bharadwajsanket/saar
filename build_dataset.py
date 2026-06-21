import json
from pathlib import Path

SOURCE = Path("../bhagavad-gita-data/slok")

verses = []

for file in SOURCE.glob("*.json"):
    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    translation = (
        data.get("prabhu", {}).get("et")
        or data.get("gambir", {}).get("et")
        or data.get("adi", {}).get("et")
        or data.get("siva", {}).get("et")
        or data.get("raman", {}).get("et")
        or data.get("purohit", {}).get("et")
        or data.get("san", {}).get("et")
        or data.get("abhinav", {}).get("et")
        or data.get("sankar", {}).get("et")
        or ""
    )

    verse = {
        "id": data["_id"],
        "chapter": data["chapter"],
        "verse": data["verse"],
        "speaker": data.get("speaker"),
        "slok": data.get("slok"),
        "transliteration": data.get("transliteration"),
        "translation": translation.strip()
    }

    verses.append(verse)

verses.sort(
    key=lambda x: (x["chapter"], x["verse"])
)

Path("data").mkdir(exist_ok=True)

with open(
    "data/verses.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        verses,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Saved {len(verses)} verses")