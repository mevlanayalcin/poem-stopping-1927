import os

TEXT = "\n".join(
    [
        "I can watch the portal tonight,",
        "my agent said, read the biopsy first,",
        "draft the next steps by dawn.",
        "",
        "Stop, I said. Leave it unread.",
        "I shut the screen,",
        "pulled a chair to the window,",
        "and stayed.",
        "If the roof falls in,",
        "I want to be home.",
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
