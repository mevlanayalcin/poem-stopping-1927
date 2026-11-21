import os

TEXT = "\n".join(
    [
        "When voices rose, my father",
        "took his keys and drove till dark.",
        "Tonight my son slams his door.",
        "My hand is already on my coat.",
        "I stop. Leave it on the peg.",
        "Sit on the bottom stair and stay.",
        "Ten minutes.",
        "His door opens",
        "an inch.",
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
