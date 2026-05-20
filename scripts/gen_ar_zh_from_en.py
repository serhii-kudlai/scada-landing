"""Generate src/i18n/{ar,zh}.json from en.json. Requires: pip install deep-translator"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

try:
    from deep_translator import GoogleTranslator
    from deep_translator.exceptions import TranslationNotFound
except ImportError:
    print("Install: pip install deep-translator", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "src" / "i18n" / "en.json"

_URL = re.compile(r"^https?://", re.I)
_CODE2 = re.compile(r"^[A-Z]{2}$")


def skip_value(s: str) -> bool:
    s = s.strip()
    if not s:
        return True
    if _URL.match(s):
        return True
    if _CODE2.match(s):
        return True
    return False


def main() -> int:
    if not EN_PATH.is_file():
        print(f"Missing {EN_PATH}", file=sys.stderr)
        return 1

    raw: object = json.loads(EN_PATH.read_text(encoding="utf-8-sig"))

    for dest, code in (("ar", "ar"), ("zh-CN", "zh")):
        cache: dict[str, str] = {}
        tr = GoogleTranslator(source="en", target=dest)

        def walk(obj: object) -> object:
            if isinstance(obj, dict):
                return {k: walk(v) for k, v in obj.items()}
            if isinstance(obj, list):
                return [walk(x) for x in obj]
            if isinstance(obj, str):
                if skip_value(obj):
                    return obj
                if obj in cache:
                    return cache[obj]
                try:
                    out = tr.translate(obj)
                except TranslationNotFound:
                    out = obj
                time.sleep(0.06)
                cache[obj] = out
                return out
            return obj

        data = walk(json.loads(json.dumps(raw)))
        if isinstance(data, dict) and "lang" in data and isinstance(data["lang"], dict):
            data["lang"]["ar"] = "العربية"
            data["lang"]["zh"] = "中文"

        out_path = ROOT / "src" / "i18n" / f"{code}.json"
        out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("Wrote", out_path.relative_to(ROOT))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
