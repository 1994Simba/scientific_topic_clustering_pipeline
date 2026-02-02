# build_embeddings.py
import json
import numpy as np
import argparse
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Run embedding generation in demo mode")
args = parser.parse_args()

# -----------------------------
# DEMO vs FULL MODE SETUP
# -----------------------------
if args.demo:
    print("Running in DEMO MODE!")
    INPUT_FILE = "arxiv_processed.jsonl"   # contains 5 records in demo mode
    OUTPUT_FILE = "sample_embeddings.txt"
else:
    INPUT_FILE = "arxiv_processed.jsonl"   # full dataset (2.1M+ records)
    OUTPUT_FILE = "embeddings.npy"

# -----------------------------
# LOAD MODEL
# -----------------------------
print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# -----------------------------
# READ INPUT RECORDS
# -----------------------------
texts = []
with open(INPUT_FILE, "r") as f:
    for line in f:
        rec = json.loads(line)
        text = (rec.get("title") or "") + " " + (rec.get("abstract") or "")
        texts.append(text)

print(f"Loaded {len(texts)} texts for embedding.")

# -----------------------------
# GENERATE EMBEDDINGS
# -----------------------------
print("Generating embeddings...")
embeddings = model.encode(texts, batch_size=64, show_progress_bar=True)

# -----------------------------
# SAVE OUTPUT
# -----------------------------
if args.demo:
    # Save as readable text for demo mode
    with open(OUTPUT_FILE, "w") as f:
        for emb in embeddings:
            f.write(" ".join(map(str, emb)) + "\n")
else:
    # Save as binary .npy for full mode
    np.save(OUTPUT_FILE, embeddings)

print(f"Done. Saved embeddings to {OUTPUT_FILE}.")
