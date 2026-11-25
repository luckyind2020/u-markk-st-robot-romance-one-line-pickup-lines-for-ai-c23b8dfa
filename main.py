"""Robot Romance: one-line pickup line for AI.

Reads the line from output/entry.txt (next to this file's directory)
and prints it to stdout, exactly as the bounty harness expects.
"""

from pathlib import Path


def load_line() -> str:
    """Read the single pickup line, stripped of surrounding whitespace."""
    entry_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    line = entry_path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("entry.txt is empty")
    return line


def main() -> None:
    print(load_line())


if __name__ == "__main__":
    main()
