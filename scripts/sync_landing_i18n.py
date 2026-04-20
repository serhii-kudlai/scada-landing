"""
Generate landing/src/i18n/{en,de,uk}.json from ru.json using deep_translator
(same library as backend/apps/core/management/commands/auto_translate.py).

Install the dependency with pip, NOT npm — the package is on PyPI only:
  pip install -r backend/requirements.txt
  # or: pip install deep-translator

Only strings containing Cyrillic are translated; Latin-only labels are kept.

Usage (from landing/):
  npm run i18n:sync
  # or: py -3 scripts/sync_landing_i18n.py
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

CYR = re.compile(r"[\u0400-\u04FF]")

ROOT = Path(__file__).resolve().parents[1]
RU_PATH = ROOT / "src" / "i18n" / "ru.json"

TARGETS = (
    ("en", "en"),
    ("de", "de"),
    ("uk", "uk"),
)


def main() -> int:
    try:
        from deep_translator import GoogleTranslator
    except ImportError:
        print("Install: pip install deep-translator", file=sys.stderr)
        return 1

    if not RU_PATH.is_file():
        print(f"Missing {RU_PATH}", file=sys.stderr)
        return 1

    data: object = json.loads(RU_PATH.read_text(encoding="utf-8"))
    cache: dict[tuple[str, str], str] = {}

    def translate_str(text: str, dest: str) -> str:
        if not text or not CYR.search(text):
            return text
        key = (text, dest)
        if key in cache:
            return cache[key]
        tr = GoogleTranslator(source="ru", target=dest).translate(text)
        time.sleep(0.08)
        cache[key] = tr
        return tr

    def walk(obj: object, dest: str) -> object:
        if isinstance(obj, dict):
            return {k: walk(v, dest) for k, v in obj.items()}
        if isinstance(obj, list):
            return [walk(x, dest) for x in obj]
        if isinstance(obj, str):
            return translate_str(obj, dest)
        return obj

    for filename, dest in TARGETS:
        out = walk(json.loads(json.dumps(data)), dest)
        path = ROOT / "src" / "i18n" / f"{filename}.json"
        path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("Wrote", path.relative_to(ROOT))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
