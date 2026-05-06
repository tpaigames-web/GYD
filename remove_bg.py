"""
Batch-remove white background from all cow_NN.png frames.

Pure-white pixels (R/G/B > WHITE_HARD) -> fully transparent.
Near-white pixels -> feathered alpha for clean anti-aliased edges.
Bull's natural cream / fur colors are preserved (they fall under the threshold).

Usage:
    python remove_bg.py

Inputs:  ./Cow/cow_00.png .. cow_54.png
Outputs: ./Cow_transparent/cow_00.png .. cow_54.png
"""
import os
import sys
from pathlib import Path

try:
    from PIL import Image
    import numpy as np
except ImportError:
    print("Installing pillow + numpy...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "numpy", "--quiet"])
    from PIL import Image
    import numpy as np

ROOT       = Path(__file__).parent
SRC_DIR    = ROOT / "Cow"
DST_DIR    = ROOT / "Cow_transparent"
WHITE_HARD = 248   # min(R,G,B) >= this  -> alpha 0  (pure white background)
WHITE_SOFT = 225   # min(R,G,B) <= this  -> alpha 255 (clearly not white)
# Pixels in (WHITE_SOFT, WHITE_HARD) get a feathered alpha for smooth edges.

DST_DIR.mkdir(exist_ok=True)

png_files = sorted(SRC_DIR.glob("cow_*.png"))
if not png_files:
    print(f"No frames found in {SRC_DIR}")
    sys.exit(1)

print(f"Processing {len(png_files)} frames -> {DST_DIR}")

for i, src in enumerate(png_files):
    img = Image.open(src).convert("RGBA")
    arr = np.array(img)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    minimum = np.minimum(np.minimum(r, g), b).astype(np.float32)

    # alpha curve: 0 above WHITE_HARD, 255 below WHITE_SOFT, linear feather between
    alpha = np.clip(
        (WHITE_HARD - minimum) * 255.0 / (WHITE_HARD - WHITE_SOFT),
        0, 255
    ).astype(np.uint8)

    arr[..., 3] = alpha
    Image.fromarray(arr).save(DST_DIR / src.name, optimize=True)

    if (i + 1) % 10 == 0 or i == len(png_files) - 1:
        print(f"  [{i+1:>3}/{len(png_files)}] {src.name}")

print("Done.")
