"""Validate every card in data/cards against the schema and sourcing rules.

Usage: python3 scripts/validate_cards.py [slug ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "data" / "cards"

ARCHETYPES = {
    "marketplace", "saas_subscription", "usage_based_api", "advertising",
    "payments_take_rate", "freemium_plg", "hardware_services", "licensing_ip",
    "d2c_ecommerce", "b2b_services", "infrastructure_energy", "fintech_lending_float",
}
STATUSES = {"public", "private", "defunct"}
SOURCE_TYPES = {"filing", "company", "press", "research", "estimate"}
REQUIRED = {
    "name": str, "slug": str, "archetype": str, "status": str, "cautionary": bool,
    "hq": str, "founded": str, "one_liner": str, "customer": str,
    "revenue_streams": list, "unit_economics": str, "key_figures": list,
    "moat": str, "pivots": list, "weak_points": list, "lesson": str,
    "last_verified": str,
}


def check(card, fname):
    errs = []
    for key, typ in REQUIRED.items():
        if key not in card:
            errs.append(f"missing {key}")
        elif not isinstance(card[key], typ):
            errs.append(f"{key} should be {typ.__name__}")
    if errs:
        return errs
    if card["slug"] + ".json" != fname:
        errs.append("slug does not match filename")
    if card["archetype"] not in ARCHETYPES:
        errs.append(f"bad archetype {card['archetype']}")
    sec = card.get("secondary_archetype")
    if sec is not None and sec not in ARCHETYPES:
        errs.append(f"bad secondary_archetype {sec}")
    if card["status"] not in STATUSES:
        errs.append(f"bad status {card['status']}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", card["last_verified"]):
        errs.append("last_verified must be YYYY-MM-DD")
    for i, rs in enumerate(card["revenue_streams"]):
        if not rs.get("stream") or not rs.get("pricing_mechanic"):
            errs.append(f"revenue_streams[{i}] incomplete")
        sp = rs.get("share_pct")
        if sp is not None and not (isinstance(sp, (int, float)) and 0 <= sp <= 100):
            errs.append(f"revenue_streams[{i}].share_pct out of range")
    if len(card["key_figures"]) < 3:
        errs.append("fewer than 3 key_figures")
    for i, kf in enumerate(card["key_figures"]):
        for k in ("metric", "value", "period", "source_url", "source_type"):
            if not kf.get(k):
                errs.append(f"key_figures[{i}] missing {k}")
        if kf.get("source_url") and not kf["source_url"].startswith("http"):
            errs.append(f"key_figures[{i}] source_url not a URL")
        if kf.get("source_type") and kf["source_type"] not in SOURCE_TYPES:
            errs.append(f"key_figures[{i}] bad source_type")
    if len(card["weak_points"]) < 2:
        errs.append("fewer than 2 weak_points")
    return errs


def main(argv):
    files = sorted(CARDS.glob("*.json"))
    if argv:
        files = [CARDS / f"{s}.json" for s in argv]
    bad = 0
    for f in files:
        try:
            card = json.loads(f.read_text())
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {f.name}: invalid JSON ({e})")
            bad += 1
            continue
        errs = check(card, f.name)
        if errs:
            bad += 1
            print(f"FAIL {f.name}: " + "; ".join(errs))
    print(f"{len(files) - bad}/{len(files)} cards valid")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
