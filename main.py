"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader sets MAKEFUN_OUTPUT_DIR to
/output; the default here is /output).

The pitch is fixed text: no input, no randomness, no network, so two
runs always produce the same file. Before writing, the pitch is
validated against the gate (one sentence, 1-220 characters) and the
program fails loudly instead of writing an entry the gate would refuse.
"""

import os
import sys

MAX_CHARS = 220

PITCH = (
    "A washing machine that goes on strike whenever you overload it, "
    "holding your socks hostage until you negotiate with their union "
    "rep in a tiny hard hat."
)


def validate_pitch(pitch: str) -> None:
    """Refuse a pitch the gate would reject instead of writing it."""
    if not pitch.strip():
        sys.exit("error: pitch is empty")
    if len(pitch) > MAX_CHARS:
        sys.exit(f"error: pitch is {len(pitch)} characters, over the {MAX_CHARS} limit")
    if pitch.count(".") != 1 or not pitch.rstrip().endswith("."):
        sys.exit("error: pitch must be exactly one sentence")


def main() -> None:
    validate_pitch(PITCH)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)
    print(f"({len(PITCH)} characters -> {path})")


if __name__ == "__main__":
    main()
