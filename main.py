import os

TEXT = "\n".join(
    [
        "Halfway up the stairs my mother",
        "grips the rail and whispers",
        "stop, don't lift me.",
        "",
        "I lower my hands",
        "and stay one step below",
        "while she finds her breath.",
        "",
        "Then she climbs the rest herself,",
        "still the one who leads me up.",
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
