"""ai-happy-01 entry: copy the bundled happy image to the output path.

The image (assets/happy.jpg) is a pen-and-ink portrait of a laughing
woman holding sunflowers in warm morning light over a city skyline.
The program only copies it byte-for-byte, so two runs produce
byte-identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "happy.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # The file is a JPEG (told apart by its first bytes); the name stays
    # entry.png either way, per the competition rules. Verify the copy
    # is complete: JPEG magic bytes and under the 1 MiB cap.
    with open(dst, "rb") as f:
        head = f.read(3)
    size = os.path.getsize(dst)
    assert head[:2] == b"\xff\xd8", "not a JPEG"
    assert size <= 1048576, "entry over 1 MiB"
    print("wrote %s (%d bytes)" % (dst, size))


if __name__ == "__main__":
    main()
