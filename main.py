#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line (max 200 characters) about my fridge to
/output/entry.txt. Pure standard library, no dependencies, no network.

The roast: a specific, recognisable detail (the fridge light nobody can
ever see working) with a twist that pays off in the last few words.
"""

import os

ROAST = (
    "My fridge has a light that only works when the door is closed, "
    "so the hardest-working thing in my kitchen is a magic trick "
    "nobody ever sees."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars, must be 1-200"
    assert ROAST.strip(), "roast must not be only whitespace"
    assert "\n" not in ROAST, "roast must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
