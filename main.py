"""News image entry: copy the repo-held image to /output/entry.png.

The image (entry.png, in this repository) sums up the world's news of
Friday 27 November 2026. It was drawn in the session that built this
entry (see draw.py, which generated it with Pillow). This program uses
only the Python standard library, runs with no network, and is fully
deterministic: it copies the same bytes every run.
"""

import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_dimensions(data):
    """Return (width, height) from a PNG IHDR chunk, or None if malformed."""
    if len(data) < 33 or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> None:
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")

    with open(source, "rb") as handle:
        data = handle.read()

    if not data.startswith(PNG_SIGNATURE):
        print("entry.png is not a PNG file", file=sys.stderr)
        raise SystemExit(1)
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        raise SystemExit(1)
    dimensions = png_dimensions(data)
    if dimensions is None:
        print("entry.png has no readable IHDR chunk", file=sys.stderr)
        raise SystemExit(1)
    width, height = dimensions
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"entry.png is {width}x{height}, over the 1024x1024 limit",
              file=sys.stderr)
        raise SystemExit(1)

    with open(destination, "wb") as handle:
        handle.write(data)

    with open(destination, "rb") as handle:
        written = handle.read()
    if written != data:
        print("verification failed: /output/entry.png differs from entry.png",
              file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
