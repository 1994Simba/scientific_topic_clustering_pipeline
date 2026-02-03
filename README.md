# Scientific Topic Clustering on 2.16M arXiv Papers  
### Unsupervised Topic Discovery Using Sentence Embeddings, UMAP, HDBSCAN, and TF‑IDF

---

## 🧩 Abstract

This repository implements a scalable, end‑to‑end pipeline for unsupervised scientific topic discovery using the arXiv metadata corpus. The system processes **2.16 million** scientific abstracts, generates dense semantic embeddings, reduces dimensionality using UMAP, clusters documents with HDBSCAN, and extracts interpretable topic labels using TF‑IDF with reverse hashing.

The project supports:

- **Demo mode** — instant, using included sample files  
- **Full mode** — processing the complete arXiv dataset  

Large files are intentionally excluded from the repository to keep it lightweight and GitHub‑friendly.

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![arXiv](https://img.shields.io/badge/Data-arXiv-red)

---

## 📁 Project Structure

```
scientific_topic_clustering/
├── src/
│   ├── process_arxiv_stream.py
│   ├── build_embeddings.py
│   └── ...
│
├── notebooks/
│   └── umap_dimensionality_reduction.ipynb
│
├── data/
│   ├── sample_data.jsonl
│   ├── sample_embeddings.txt
│   ├── sample_cluster_labels.txt
│   └── metadata.jsonl
│
├── outputs/
│   ├── arxiv_processed.jsonl
│   ├── embeddings.npy
│   ├── cluster_labels.npy
│   └── cluster_probabilities.npy
│
├── README.md
└── .venv/                                 # Local virtual environment (ignored)
```

### ❗ Large files NOT included in the repo

To keep the repository lightweight, the following files are excluded:

- `arxiv-metadata-oai-snapshot.json` (3+ GB)
- `arxiv_processed.jsonl` (2+ GB)
- `embeddings.npy`
- `cluster_labels.npy`
- `cluster_probabilities.npy`

These are generated locally when running in **full mode**.

---

## 🚀 Quick Start

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## ▶️ How to Run the Pipeline

This project supports **two execution modes**:

- **Demo Mode** — runs instantly using small sample files included in the repo  
- **Full Mode** — processes the complete arXiv dataset (millions of records)

Both modes use the same scripts.

---

## 🟢 Demo Mode (Instant, No Large Files Needed)

Demo mode uses the included sample files and runs in seconds.

### Process sample data

```bash
python src/process_arxiv_stream.py --demo
```

### Generate sample embeddings

```bash
python src/build_embeddings.py --demo
```

### Run the notebook in demo mode

Open:

```
notebooks/umap_dimensionality_reduction.ipynb
```

---

## 🔵 Full Mode (Full Dataset, Millions of Records)

### 1. Download the arXiv metadata snapshot  
Place it in the project folder as:

```
arxiv-metadata-oai-snapshot.json
```

### 2. Process the full dataset

```bash
python src/process_arxiv_stream.py
```

This generates:

```
outputs/arxiv_processed.jsonl
```

### 3. Generate full embeddings

```bash
python src/build_embeddings.py
```

This generates:

```
outputs/embeddings.npy
outputs/cluster_labels.npy
outputs/cluster_probabilities.npy
```

### 4. Run the notebook in full mode

Open:

```
notebooks/umap_dimensionality_reduction.ipynb
```

---

## ▶️ Running the Python Scripts (Detailed)

### 1. `process_arxiv_stream.py`

#### Demo Mode

```bash
python src/process_arxiv_stream.py --demo
```

#### Full Mode

```bash
python src/process_arxiv_stream.py
```

#### Custom paths

```bash
python src/process_arxiv_stream.py --input data/custom.jsonl --output outputs/custom_processed.jsonl
```

---

### 2. `build_embeddings.py`

#### Demo Mode

```bash
python src/build_embeddings.py --demo
```

#### Full Mode

```bash
python src/build_embeddings.py
```

#### Custom paths

```bash
python src/build_embeddings.py --input outputs/custom_processed.jsonl --output outputs/custom_embeddings.npy
```

---

### Script Arguments (Reference)

```
--demo        Run using sample files
--input       Path to input JSONL file
--output      Path to output file
```

---

## 📓 Notebook Overview

The notebook `umap_dimensionality_reduction.ipynb` performs:

1. Load metadata and embeddings  
2. UMAP reduction (384 → 5 → 2 dimensions)  
3. HDBSCAN clustering  
4. TF‑IDF construction (30,000 features)  
5. Reverse hashing to recover vocabulary  
6. Keyword extraction per cluster  
7. Topic label generation  
8. Cluster indexing for fast retrieval  
9. UMAP visualization with top 50 cluster labels  
10. Keyword search (e.g., “quantum”)  

Supports both **demo** and **full** datasets.

---

## 📊 Outputs (Full Mode)

- **2,166,782** processed records  
- **384‑dimensional embeddings**  
- **5‑dimensional UMAP reduction**  
- **2‑dimensional visualization**  
- **≈ 2,904 clusters** discovered  
- **TF‑IDF matrix:** `(2166782, 30000)`  
- **Recovered vocabulary:** 30,000 words  

---

## 🧠 Features

- Scalable streaming parser  
- SentenceTransformer embeddings  
- UMAP dimensionality reduction  
- HDBSCAN clustering  
- TF‑IDF keyword extraction  
- Reverse hashing vocabulary recovery  
- Keyword search  
- UMAP visualization with topic labels  

---

## 📜 License

MIT License — free for academic and research use.

