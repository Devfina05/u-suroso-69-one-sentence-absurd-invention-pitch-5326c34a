"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention to
$MAKEFUN_OUTPUT_DIR/entry.txt (the grader sets MAKEFUN_OUTPUT_DIR to
/output; the default here is /output).

The pitch is fixed text: no input, no randomness, no network, so two
runs always produce the same file.
"""

import os

PITCH = (
    "A washing machine that goes on strike whenever you overload it, "
    "holding your socks hostage until you negotiate their release "
    "with a union rep in a tiny hard hat."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)
    print(f"({len(PITCH)} characters -> {path})")


if __name__ == "__main__":
    main()
