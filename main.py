import os

TEXT = "\n".join(
    [
        "When the swarm settled on my wrist,",
        "my grandfather stepped back",
        "so the stillness was mine.",
        "Ten minutes I held my arm",
        "level while bees walked my knuckles",
        "and rose without a sting.",
        "Nothing in me wanted to stay.",
        "That was how I knew",
        "it was my hand.",
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
