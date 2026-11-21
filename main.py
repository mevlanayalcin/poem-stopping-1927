import os

TEXT = "\n".join(
    [
        "Two blocks from school my son",
        "stops and looks at his hand in mine.",
        "From here, he says.",
        "",
        "My grip tightens once,",
        "the way my mother did.",
        "Then I let his fingers slip free,",
        "stay at the corner,",
        "and watch him cross alone.",
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
