import os

TEXT = "\n".join(
    [
        "At three the fare alert pinged",
        "and I booked the one-way out,",
        "packed one bag by the door,",
        "and left the receipt open.",
        "Twenty-four hours to cancel.",
        "I hit cancel before dawn.",
        "First time in six years",
        "staying wasn't an accident.",
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
