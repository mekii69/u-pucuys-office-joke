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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
