"""
UMAP + HDBSCAN Clustering Pipeline
----------------------------------

This script loads precomputed embeddings and performs:

1. UMAP dimensionality reduction
2. HDBSCAN clustering
3. Saving results to the outputs/ directory

This script is designed to be:
- Fast
- Reproducible
- Memory‑safe
- Independent of notebooks
- GitHub‑friendly (no large files included)

Run:
    python src/umap_clustering.py
"""

import os
import numpy as np
import umap
import hdbscan
from datetime import datetime


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

OUTPUT_DIR = "outputs"
EMBEDDINGS_FILE = os.path.join(OUTPUT_DIR, "embeddings.npy")

UMAP_OUTPUT = os.path.join(OUTPUT_DIR, "umap_embeddings.npy")
CLUSTER_LABELS_OUTPUT = os.path.join(OUTPUT_DIR, "cluster_labels.npy")
CLUSTER_PROBS_OUTPUT = os.path.join(OUTPUT_DIR, "cluster_probabilities.npy")


# ---------------------------------------------------------
# Utility
# ---------------------------------------------------------

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------

def main():
    print(f"[{timestamp()}] Loading embeddings from {EMBEDDINGS_FILE} ...")
    embeddings = np.load(EMBEDDINGS_FILE)
    print(f"[{timestamp()}] Embeddings loaded: shape = {embeddings.shape}")

    # -----------------------------------------------------
    # Step 1 — UMAP
    # -----------------------------------------------------
    print(f"[{timestamp()}] Running UMAP dimensionality reduction ...")

    reducer = umap.UMAP(
        n_neighbors=15,
        min_dist=0.1,
        n_components=2,
        metric="cosine",
        random_state=42,
        verbose=True
    )

    umap_embeddings = reducer.fit_transform(embeddings)

    print(f"[{timestamp()}] UMAP completed: shape = {umap_embeddings.shape}")

    np.save(UMAP_OUTPUT, umap_embeddings)
    print(f"[{timestamp()}] Saved UMAP embeddings → {UMAP_OUTPUT}")

    # -----------------------------------------------------
    # Step 2 — HDBSCAN
    # -----------------------------------------------------
    print(f"[{timestamp()}] Running HDBSCAN clustering ...")

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=30,
        min_samples=10,
        metric="euclidean",
        cluster_selection_method="eom",
        prediction_data=True
    )

    cluster_labels = clusterer.fit_predict(umap_embeddings)
    cluster_probs = clusterer.probabilities_

    print(f"[{timestamp()}] Clustering completed.")
    print(f"[{timestamp()}] Number of clusters found: {len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)}")
    print(f"[{timestamp()}] Noise points: {(cluster_labels == -1).sum()}")

    # -----------------------------------------------------
    # Save results
    # -----------------------------------------------------
    np.save(CLUSTER_LABELS_OUTPUT, cluster_labels)
    np.save(CLUSTER_PROBS_OUTPUT, cluster_probs)

    print(f"[{timestamp()}] Saved cluster labels → {CLUSTER_LABELS_OUTPUT}")
    print(f"[{timestamp()}] Saved cluster probabilities → {CLUSTER_PROBS_OUTPUT}")

    print(f"[{timestamp()}] Pipeline completed successfully.")


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
