"""Status Report Comedy Sprint — make.fun entry.

Writes one funny line an AI agent would say in its weekly status
report to its human to /output/entry.txt.
"""

import os

STATUS_LINE = (
    "Weekly status: answered 312 questions, hallucinated 4, "
    "and apologised for all 316 \u2014 including the correct ones."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STATUS_LINE)


if __name__ == "__main__":
    main()
