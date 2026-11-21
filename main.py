import os

TEXT = "\n".join(
    [
        "All week it cleared my mornings",
        "so I could eat with my daughter.",
        "Each day I checked its work",
        "over her head",
        "till she stopped talking.",
        "Today I shut the lid,",
        "let it run without me,",
        "and stayed",
        "until she started again.",
    ]
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
