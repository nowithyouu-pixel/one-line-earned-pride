"""One Line of Earned Pride — writes a single original line to /output/entry.txt."""

from pathlib import Path

LINE = "The weld held. After eleven failed beads, the weld held, and Old Tom set down the torch like a man laying a baby in a crib."

# The gate allows 1 to 240 characters of non-whitespace UTF-8 text; fail
# loudly here rather than shipping an entry the scorer would refuse.
assert 1 <= len(LINE) <= 240 and LINE.strip(), "entry line outside the 1-240 character gate"


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
