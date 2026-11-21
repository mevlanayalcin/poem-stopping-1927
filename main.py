import os

TEXT = "\n".join(
    [
        "My mother caught every cup",
        "before I could spill it.",
        "Now my son crosses the kitchen",
        "with a full bowl,",
        "both hands shaking.",
        "Broth wets his thumb.",
        "My knees lift to save it.",
        "I stop. Sit back and stay.",
        "He sets it down himself,",
        "one drop gone.",
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
