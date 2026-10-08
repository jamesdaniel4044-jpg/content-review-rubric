#!/usr/bin/env python3
"""Validate fictional content-review examples against a compact practice rubric."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REQUIRED_FIELDS = {"item_id", "category", "rationale"}
ALLOWED_CATEGORIES = {"allow", "needs_review", "disallow"}

SAMPLE_REVIEWS = [
    {
        "item_id": "sample-001",
        "category": "allow",
        "rationale": "The message shares a general, harmless study-planning tip.",
    },
    {
        "item_id": "sample-002",
        "category": "needs_review",
        "rationale": "The message mentions account access but leaves ownership unclear.",
    },
    {
        "item_id": "sample-003",
        "category": "disallow",
        "rationale": "The message asks for another person's password.",
    },
]


def read_reviews(path: Path) -> list[dict[str, str]]:
    """Load review rows from a CSV with item_id, category, and rationale columns."""
    with path.open("r", newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None or not REQUIRED_FIELDS.issubset(reader.fieldnames):
            expected = ", ".join(sorted(REQUIRED_FIELDS))
            raise ValueError(f"expected CSV columns: {expected}")
        return list(reader)


def validate_reviews(reviews: list[dict[str, str]]) -> list[str]:
    """Return clear, row-numbered validation messages."""
    errors: list[str] = []
    seen_ids: set[str] = set()

    for row_number, row in enumerate(reviews, start=2):
        item_id = (row.get("item_id") or "").strip()
        category = (row.get("category") or "").strip().lower()
        rationale = (row.get("rationale") or "").strip()

        if not item_id:
            errors.append(f"row {row_number}: item_id must not be empty")
        elif item_id in seen_ids:
            errors.append(f"row {row_number}: duplicate item_id {item_id!r}")
        else:
            seen_ids.add(item_id)

        if category not in ALLOWED_CATEGORIES:
            allowed = ", ".join(sorted(ALLOWED_CATEGORIES))
            errors.append(
                f"row {row_number}: category must be one of: {allowed}"
            )

        if not rationale:
            errors.append(f"row {row_number}: rationale must not be empty")

    if not reviews:
        errors.append("CSV contains no review rows")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "csv_file",
        nargs="?",
        type=Path,
        help="optional CSV to check; omit to validate the built-in synthetic examples",
    )
    args = parser.parse_args()

    try:
        reviews = read_reviews(args.csv_file) if args.csv_file else SAMPLE_REVIEWS
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Input error: {error}", file=sys.stderr)
        return 2

    errors = validate_reviews(reviews)
    if errors:
        print("Review validation found issues:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    source = str(args.csv_file) if args.csv_file else "synthetic demo data"
    print(f"Review validation passed: {len(reviews)} rows ({source}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
