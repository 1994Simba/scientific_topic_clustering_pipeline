Markdown
```markdown
# Scientific Topic Clustering on 2.16M arXiv Papers  
### Unsupervised Topic Discovery Using Sentence Embeddings, UMAP, HDBSCAN, and TF‑IDF

---

## 🧩 Abstract

This repository implements a scalable, end‑to‑end pipeline for unsupervised scientific topic discovery using the arXiv metadata corpus. The system processes **2.16 million** scientific abstracts, generates dense semantic embeddings, reduces dimensionality using UMAP, clusters documents with HDBSCAN, and extracts interpretable topic labels using TF‑IDF with reverse hashing.  
The project supports **demo mode** (instant, using included sample files) and **full mode** (processing the complete arXiv dataset). Large files are intentionally excluded from the repository to keep it lightweight and GitHub‑friendly.

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
│
├── process_arxiv_stream.py                # Streaming parser (demo + full mode)
├── build_embeddings.py                    # Embedding generator (demo + full mode)
│
├── 01_umap_dimensionality_reduction.ipynb # Full notebook pipeline
│
├── sample_data.jsonl                      # Demo dataset (5 records)
├── sample_embeddings.txt                  # Demo embeddings
├── sample_cluster_labels.txt              # Demo cluster labels
│
├── arxiv_processed.jsonl                  # (Generated) Processed dataset
├── embeddings.npy                         # (Generated) Full embeddings
├── cluster_labels.npy                     # (Generated) Full cluster labels
├── cluster_probabilities.npy              # (Generated) HDBSCAN probabilities
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

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🟢 Demo Mode (Instant, No Large Files Needed)

Demo mode uses the included sample files and runs in seconds.

### Process sample data

```
python process_arxiv_stream.py --demo
```

### Generate sample embeddings

```
python build_embeddings.py --demo
```

You can now open the notebook and run it in demo mode.

---

## 🔵 Full Mode (Full Dataset, Millions of Records)

### 1. Download the arXiv metadata snapshot  
Place it in the project folder as:

```
arxiv-metadata-oai-snapshot.json
```

### 2. Process the full dataset

```
python process_arxiv_stream.py
```

### 3. Generate full embeddings

```
python build_embeddings.py
```

You can now run the notebook in full mode.

---

## 📓 Notebook Overview

The notebook `01_umap_dimensionality_reduction.ipynb` performs:

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

## 🔧 ASCII Pipeline Diagram (Clean, GitHub‑Friendly)

```text
                 ┌────────────────────────────────────────┐
                 │   arXiv Metadata Snapshot (JSONL)       │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 1. Streaming Preprocessing              │
                 │    - Filter year >= 2015                │
                 │    - Normalize fields                   │
                 │    - Output: arxiv_processed.jsonl      │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 2. Embedding Generation                 │
                 │    - SentenceTransformers (MiniLM)      │
                 │    - Output: embeddings.npy             │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 3. UMAP Reduction (384 → 5 dims)        │
                 │    - metric: cosine                     │
                 │    - n_neighbors: 15                    │
                 │    - Output: reduced_embeddings         │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 4. HDBSCAN Clustering                   │
                 │    - min_cluster_size: 50               │
                 │    - min_samples: 10                    │
                 │    - Output: cluster_labels.npy         │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 5. TF-IDF Construction (30k features)   │
                 │    - HashingVectorizer (streaming)      │
                 │    - Manual IDF computation             │
                 │    - Output: tfidf_matrix               │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 6. Reverse Hashing Vocabulary           │
                 │    - CountVectorizer on 200k sample     │
                 │    - Output: vocab (30k words)          │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 7. Topic Labeling                       │
                 │    - Top TF-IDF keywords per cluster    │
                 │    - Human-readable labels              │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 8. Visualization (UMAP 2D)              │
                 │    - Cluster centroids                  │
                 │    - Top 50 labels on plot              │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
                 ┌────────────────────────────────────────┐
                 │ 9. Keyword Search Engine                │
                 │    - TF-IDF column lookup               │
                 │    - Returns top matching documents     │
                 └────────────────────────────────────────┘
```

---

## 🤝 Contributing

Contributions are welcome.  
You can contribute by:

- Improving documentation  
- Adding new visualizations  
- Enhancing clustering or labeling methods  
- Optimizing performance  
- Extending the notebook with new analyses  

To contribute:

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request  

Please ensure your code is clean, documented, and tested.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📦 requirements.txt

```
numpy
pandas
scikit-learn
scipy
umap-learn
hdbscan
sentence-transformers
tqdm
matplotlib
```

---

---

## 🙌 Acknowledgements

This project uses:

- arXiv metadata  
- SentenceTransformers  
- UMAP  
- HDBSCAN  
- scikit‑learn  
- NumPy / SciPy  
- pandas  

---
```

