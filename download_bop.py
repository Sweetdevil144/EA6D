"""
Download BOP Linemod files for EA6D.
Run this on your local machine, then upload the zips to Kaggle.

Usage:
    pip install huggingface_hub
    python download_bop.py

    # If you get auth errors, first run:
    # pip install huggingface_hub[cli]
    # huggingface-cli login
    # (paste your HF token when prompted)
"""

import os

from huggingface_hub import hf_hub_download

OUTPUT = os.path.expanduser("~/Desktop/bop_downloads")
os.makedirs(OUTPUT, exist_ok=True)

for fname in ["lm_base.zip", "lm_test_bop19.zip"]:
    print(f"Downloading {fname}...")
    path = hf_hub_download(
        repo_id="bop-benchmark/lm",
        filename=fname,
        repo_type="dataset",
        local_dir=OUTPUT,
    )
    size_mb = os.path.getsize(path) / 1e6
    print(f"  -> {path} ({size_mb:.1f} MB)")

    if size_mb < 1:
        print(
            f"  WARNING: {fname} is only {size_mb:.1f} MB — likely a redirect page, not the real file."
        )
        print("  Run: huggingface-cli login   (then re-run this script)")
    else:
        print("  OK")

print(f"\nDone. Files are in: {OUTPUT}")
print("Upload both .zip files to Kaggle as a dataset.")
