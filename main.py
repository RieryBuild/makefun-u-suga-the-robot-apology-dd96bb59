"""The Robot Apology — two-line robot confession.

A robot set the alarm for 7 p.m. instead of 7 a.m. and let its person sleep
through an interview. The lesson follows from that exact slip: it now reads
the time back out loud before it sets an alarm, so an a.m./p.m. mix-up gets
caught before it costs anyone a morning.
"""

import os

ENTRY = (
    "I'm sorry I set your alarm for 7 p.m. instead of 7 a.m. "
    "and let you sleep through your interview.\n"
    "I have learned to read the time back to you out loud before I set it."
)


def write_entry(entry, output_dir):
    """Write the two-line entry, guarding the gate before touching disk."""
    text = entry.strip("\n")
    if not text or len(text) > 400:
        raise ValueError("entry must be 1-400 non-whitespace characters")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY, output_dir)


if __name__ == "__main__":
    main()
