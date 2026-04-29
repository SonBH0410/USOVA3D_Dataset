import json
import cv2
import numpy as np
from pathlib import Path
from tqdm import tqdm

# ── CONFIG ───────────────────────────────────────────────────────
JSON_PATH    = Path(__file__).resolve().parent / "split.json"
DATASET_ROOT = JSON_PATH.parent

# Pick which annotation to pair with the images.
#   ANNOTATOR ∈ {"follicle_r1", "follicle_r2", "ovary_r1", "ovary_r2"}
#   VARIANT   ∈ {"binary", "color", "instance"}   (ovary only has "binary")
ANNOTATOR = "ovary_r2"
VARIANT   = "binary"

# ── LOAD JSON ────────────────────────────────────────────────────
with open(JSON_PATH, encoding="utf-8") as f:
    split = json.load(f)

def get_split(split_name, annotator=ANNOTATOR, variant=VARIANT):
    imgs, masks = [], []
    for vol, data in split["split"][split_name].items():
        for img_rel in data["images"]:
            imgs.append(DATASET_ROOT / img_rel)
        for mask_rel in data["labels"][annotator][variant]:
            masks.append(DATASET_ROOT / mask_rel)
    return imgs, masks

def count_masks(mask_paths, desc=""):
    fg = black = 0
    for mp in tqdm(mask_paths, desc=f"  counting {desc}", leave=False):
        m = cv2.imread(str(mp), cv2.IMREAD_GRAYSCALE)
        if m is not None and m.max() > 0:
            fg += 1
        else:
            black += 1
    return fg, black

# ── LOAD & COUNT ─────────────────────────────────────────────────
image_train, mask_train = get_split("train")
image_valid, mask_valid = get_split("val")
image_test,  mask_test  = get_split("test")

fg_train, bk_train = count_masks(mask_train, "train")
fg_valid, bk_valid = count_masks(mask_valid, "val")
fg_test,  bk_test  = count_masks(mask_test,  "test")

print(f"annotator={ANNOTATOR}  variant={VARIANT}")
print(f"train: {len(image_train):4d} images / {len(mask_train):4d} masks  "
      f"foreground={fg_train}  black={bk_train}")
print(f"valid: {len(image_valid):4d} images / {len(mask_valid):4d} masks  "
      f"foreground={fg_valid}  black={bk_valid}")
print(f"test : {len(image_test):4d} images / {len(mask_test):4d} masks  "
      f"foreground={fg_test}  black={bk_test}")
