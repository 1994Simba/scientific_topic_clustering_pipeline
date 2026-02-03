# Scientific Topic Clustering  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen.svg)]()  
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()  
[![Jupyter](https://img.shields.io/badge/Notebook-UMAP%20Visualization-orange.svg)]()  
[![Reproducible](https://img.shields.io/badge/Mode-Demo%20Reproducible-success.svg)]()

A scalable, end‑to‑end pipeline for embedding, clustering, and visualizing scientific abstracts.

This project implements a complete workflow for processing scientific abstracts, generating high‑dimensional embeddings, clustering them into coherent topics, and visualizing the results using UMAP. The repository is structured for clarity, reproducibility, and ease of use, supporting both **demo mode** (lightweight, fast) and **full mode** (large‑scale, research‑grade). The full processing pipeline is implemented in `src/`, while the notebook in `notebooks/` provides an interactive exploration of the results.

---

# 📁 Project Structure

```
scientific_topic_clustering/
│
├── data/                     # Demo dataset (small, included in repo)
│   ├── sample_data.jsonl
│   ├── sample_embeddings.txt
│   └── sample_cluster_labels.txt
│
├── outputs/                  # Full dataset outputs (large, generated)
│   ├── arxiv_processed.jsonl
│   ├── embeddings.npy
│   ├── cluster_labels.npy
│   └── cluster_probabilities.npy
│
├── notebooks/
│   └── 01_umap_dimensionality_reduction.ipynb
│
├── src/                      # Processing pipeline
│   ├── 00_download_data.py
│   ├── 01_process_arxiv.py
│   ├── 02_generate_embeddings.py
│   ├── 03_cluster_embeddings.py
│   └── utils/
│
├── .gitignore
└── README.md
```

---

# 🔄 Pipeline Overview

```
                ┌────────────────────────┐
                │   00_download_data.py   │
                │  Download raw abstracts │
                └─────────────┬──────────┘
                              ▼
                ┌────────────────────────┐
                │   01_process_arxiv.py   │
                │  Clean + normalize JSON │
                │  → arxiv_processed.jsonl│
                └─────────────┬──────────┘
                              ▼
                ┌────────────────────────┐
                │ 02_generate_embeddings.py│
                │  Generate embeddings     │
                │  → embeddings.npy        │
                └─────────────┬──────────┘
                              ▼
                ┌────────────────────────┐
                │ 03_cluster_embeddings.py│
                │  Cluster + probabilities │
                │  → cluster_labels.npy    │
                │  → cluster_probabilities │
                └─────────────┬──────────┘
                              ▼
                ┌────────────────────────┐
                │  Notebook (UMAP + Viz) │
                │  01_umap_dimensional…  │
                └────────────────────────┘
```

---

# ▶️ Running the Full Python Pipeline

Activate your virtual environment:

```
source .venv/bin/activate
```

Run each script in order:

### 1. Download raw data
```
python src/00_download_data.py
```

### 2. Process and clean the dataset
```
python src/01_process_arxiv.py
```

This generates:
```
outputs/arxiv_processed.jsonl
```

### 3. Generate embeddings (large step)
```
python src/02_generate_embeddings.py
```

This generates:
```
outputs/embeddings.npy
```

### 4. Cluster embeddings
```
python src/03_cluster_embeddings.py
```

This generates:
```
outputs/cluster_labels.npy
outputs/cluster_probabilities.npy
```

Once these files exist, the notebook can run in **full mode**.

---

# 🚦 Demo Mode vs Full Mode

The notebook supports two execution modes, controlled by a single configuration variable:

```
MODE = "demo"   # or "full"
```

## Demo Mode
- Loads small sample files from `data/`
- Runs instantly
- Requires no preprocessing
- Ideal for:
  - reviewers  
  - tutors  
  - collaborators  
  - anyone cloning the repo  
- Guaranteed to execute end‑to‑end without errors

## Full Mode
- Loads the complete processed dataset from `outputs/`
- Requires running the full ETL pipeline in `src/`
- Uses multi‑gigabyte embeddings and clustering outputs
- Intended for full‑scale research and analysis

## Recommendation
For submissions and reproducibility, **demo mode is strongly recommended**.  
Full mode is optional and only needed for large‑scale experiments.

---

# 🧠 Notebook Workflow Summary

The notebook `01_umap_dimensionality_reduction.ipynb` follows a clear, reproducible workflow:

1. **Load Metadata**  
2. **Load Embeddings and Cluster Labels**  
3. **UMAP Dimensionality Reduction**  
4. **Visualization of Clusters**  
5. **Cluster Exploration**

This workflow allows users to explore clustering results without rerunning the full pipeline.

---

# ▶️ Running the Notebook

## Option A — Run in Demo Mode (recommended)

```
jupyter notebook notebooks/01_umap_dimensionality_reduction.ipynb
```

Ensure the configuration cell contains:

```
MODE = "demo"
```

Then run all cells.

---

## Option B — Execute from Terminal

```
jupyter nbconvert --to notebook --execute --inplace notebooks/01_umap_dimensionality_reduction.ipynb
```

---

## Option C — Run in Full Mode

Before switching to full mode, ensure you have generated:

- outputs/arxiv_processed.jsonl  
- outputs/embeddings.npy  
- outputs/cluster_labels.npy  
- outputs/cluster_probabilities.npy  

Then set:

```
MODE = "full"
```

---

# 🧹 Optional: Clear Notebook Outputs

To keep the notebook lightweight before committing:

```
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/01_umap_dimensionality_reduction.ipynb
```

---

# 🎯 Final Notes

- The project is fully reproducible in **demo mode**, making it ideal for submission.  
- Full mode is available for large‑scale experimentation.  
- The notebook has been validated structurally and executed successfully in demo mode.  
- The folder structure follows industry best practices for ML and data science projects.  
- The pipeline is modular, scalable, and ready for extension.
