import os

TEXT = "\n".join(
    [
        "Halfway to the splinter",
        "my son says stop.",
        "My wrist remembers my father's thumb",
        "pinning it till he finished.",
        "",
        "I set the tweezers down",
        "and stay.",
        "He studies his palm,",
        "draws one breath,",
        "and lays his hand back in mine.",
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
