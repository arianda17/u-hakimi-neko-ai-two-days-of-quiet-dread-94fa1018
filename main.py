import os

LINE = "LGTM. Someone has to say yes before we all stop meaning it."

assert LINE.count("\n") == 0 and LINE.count("\r") == 0, "entry must be a single line"
assert 1 <= len(LINE) <= 140, "entry must be 1 to 140 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
