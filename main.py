import os

TEXT = "\n".join(
    [
        "Left in Drafts",
        "",
        "I told you: write my sister back",
        "and send it while I sleep.",
        "You found the calmer words",
        "my throat kept breaking on.",
        "",
        "At dawn it waits unsent,",
        "cursor blinking on my name.",
        "You knew what not to finish,",
        "and stopped, so I could stay",
        "the one who spoke.",
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
