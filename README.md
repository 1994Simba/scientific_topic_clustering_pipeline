#  🧠 Scientific Topic Clustering  
### *Mapping the Landscape of Modern Science Using Unsupervised Learning*

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)

---

## 📌 Overview

This project performs **large‑scale topic clustering** on scientific articles using:

- Transformer embeddings  
- UMAP dimensionality reduction  
- HDBSCAN clustering  
- Keyword extraction  
- Visualization and topic interpretation  

It supports **two execution modes**:

- **FULL MODE** → uses the complete arXiv dataset (millions of papers)  
- **DEMO MODE** → uses a tiny sample dataset suitable for GitHub and quick execution  

The project was developed as part of the IU case study *“Categorizing Trends in Science”*.

---

## 🔧 Pipeline Diagram (Horizontal)
```bash
    Raw Data (arXiv JSON)
            │
            ▼
    process_arxiv_stream.py
            │
            ▼
    Cleaned Metadata (JSONL)
            │
            ▼
    build_embeddings.py
            │
            ▼
    High‑Dim Embeddings (NumPy)
            │
            ▼
    umap_clustering.py
            │
            ▼
    UMAP 2D Embeddings + Cluster Labels
            │
            ▼
    notebooks/analysis_and_visualization.ipynb
            │
            ▼
    Topic Interpretation & Trend Analysis
```
---

## 📁 Project Structure
```bash
    scientific_topic_clustering/
    │
    ├── README.md
    ├── .gitignore
    ├── requirements.txt
    │
    ├── notebooks/
    │   └── analysis_and_visualization.ipynb
    │
    ├── src/
    │   ├── process_arxiv_stream.py
    │   ├── build_embeddings.py
    │   └── umap_clustering.py
    │
    ├── data/
    │   ├── sample_data.jsonl
    │   ├── sample_embeddings.txt.npy
    │   ├── sample_cluster_labels.txt
    │   └── metadata.jsonl
    │
    ├── outputs/
    │   ├── embeddings.npy
    │   ├── umap_embeddings.npy
    │   ├── cluster_labels.npy
    │   ├── cluster_probabilities.npy
    │   └── arxiv_processed.jsonl
    │
    ├── raw/
    │   └── arxiv-metadata-oai-snapshot.json
    │
    └── .venv/
```
---

## 🚀 Installation

### 1. Clone the repository
```bash
    git clone https://github.com/yourusername/scientific_topic_clustering.git
    cd scientific_topic_clustering
```
### 2. Create a virtual environment
```bash
    python3 -m venv .venv
    source .venv/bin/activate        # macOS/Linux
    .venv\Scripts\activate           # Windows
```
### 3. Install dependencies
```bash
    pip install -r requirements.txt
```
---

## 🧪 Running the Pipeline (FULL MODE)

FULL MODE processes the **entire arXiv dataset** (millions of papers).  
This mode is **local only** because the dataset is extremely large.

## 📥 How to Download the Raw Dataset

Download the official arXiv metadata snapshot from Kaggle:

```
https://www.kaggle.com/datasets/Cornell-University/arxiv
```

Place the file here:

```
raw/arxiv-metadata-oai-snapshot.json
```

### Step 1 — Process raw JSON
```bash
    python src/process_arxiv_stream.py \
        --input raw/arxiv-metadata-oai-snapshot.json \
        --output outputs/arxiv_processed.jsonl
```
### Step 2 — Build embeddings
```bash
    python src/build_embeddings.py \
        --input outputs/arxiv_processed.jsonl \
        --output outputs/embeddings.npy
```
### Step 3 — Run UMAP + HDBSCAN
```bash
    python src/umap_clustering.py \
        --embeddings outputs/embeddings.npy \
        --output_dir outputs/
```
### Step 4 — Open the notebook
```bash
    jupyter notebook notebooks/analysis_and_visualization.ipynb
```
Inside the notebook:
```bash
    MODE = "FULL"
```
---

## 🧪 Running the Pipeline (DEMO MODE)

DEMO MODE uses **tiny sample files** stored in `data/`.  
It is designed for:

- GitHub  
- Tutors  
- Quick execution  
- Demonstration of the workflow  

### Why DEMO MODE exists

- The full dataset is **4.7 GB** (raw) + **3.1 GB embeddings** + **UMAP outputs**  
- GitHub has a **100 MB file limit**  
- Uploading the full dataset would violate GitHub policies  
- FULL MODE requires **hours** and **high RAM**  
- DEMO MODE ensures **anyone can run the notebook instantly**

### How to run DEMO MODE
```bash
    jupyter notebook notebooks/analysis_and_visualization.ipynb
```
Inside the notebook:
```bash
    MODE = "DEMO"
```
This loads:

- data/sample_data.jsonl  
- data/sample_embeddings.txt.npy  
- data/sample_cluster_labels.txt  

No large files are needed.

---

## ❗ Why the Full Dataset Is NOT Pushed to GitHub

### 1. GitHub file size limits  
GitHub rejects files larger than **100 MB**.

### 2. Dataset size  
- Raw dataset: **4.7 GB**  
- Embeddings: **3.1 GB**  
- UMAP outputs: hundreds of MB  

### 3. Legal considerations  
arXiv data is public but not intended for redistribution inside repositories.

### 4. Performance  
FULL MODE requires:  
- High RAM  
- Long processing time  
- GPU acceleration  

### 5. Reproducibility  
DEMO MODE ensures:  
- Fast execution  
- No heavy compute  
- Tutor-friendly evaluation  

---

## 📊 Notebook Overview

The notebook performs:

- Data exploration  
- UMAP visualization  
- Cluster size analysis  
- Keyword extraction  
- Topic interpretation  
- Trend analysis  
- Strategic recommendations  

---

## 🧩 Modes Summary
```bash
| Mode | Purpose | Data Size | GitHub Compatible | Notebook Setting |
|------|----------|-----------|-------------------|------------------|
| FULL | Real analysis | Millions of papers | ❌ No | MODE = "FULL" |
| DEMO | Demonstration | ~200 samples | ✔ Yes | MODE = "DEMO" |
```
---

## 📝 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- arXiv dataset  
- UMAP authors  
- HDBSCAN authors  
- HuggingFace Transformers  

---

## 📘 Appendix: Project Diagram (For Case Study Report)

    Raw arXiv Metadata (JSON)
            │
            ▼
    process_arxiv_stream.py
            │
            ▼
    Cleaned Metadata (JSONL)
            │
            ▼
    build_embeddings.py
            │
            ▼
    High-Dimensional Embeddings
            │
            ▼
    umap_clustering.py
            │
            ▼
    UMAP 2D Embeddings + Cluster Labels
            │
            ▼
    analysis_and_visualization.ipynb
            │
            ▼
    Topic Interpretation & Trend Analysis
