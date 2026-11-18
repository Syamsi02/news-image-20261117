"""news-image-20261117 entry: copy the bundled front-page image to the output.

The image sums up Tuesday 17 November 2026 world news as a newspaper front
page: the Kerch Bridge struck again, Iran says tankers hit mines in Hormuz,
Trump lands in Manila, five EU states plan a Rwanda return hub, and JPMorgan
blames a software bug for its banking outage.

Standard library only, no network, deterministic: both runs write the same
bytes. The program checks the bundled file is a whole PNG (magic bytes and
size within the 1 MiB gate) before copying it, so a corrupt bundle fails
loudly instead of submitting a broken image.
"""

import os
import shutil

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    with open(SRC, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG file")
    if os.path.getsize(SRC) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB gate")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise SystemExit("copied entry.png size mismatch")


if __name__ == "__main__":
    main()
