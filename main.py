"""One-line office joke entry.

Writes a single original one-line joke about office life to
/output/entry.txt. Deterministic: the same fixed text on every run,
standard library only, no network, no input.
"""

import os

JOKE = (
    "My calendar blocked focus time until 11, so my manager booked "
    "9 to 11 as 'Quick sync about your focus time.'"
)


def main():
    # Gate mirrors the competition's 1-200 char one-line requirement:
    # fail loudly instead of writing an empty/oversized joke.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "JOKE must be 1-200 non-blank characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
