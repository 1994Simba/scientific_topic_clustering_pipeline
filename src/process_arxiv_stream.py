# process_arxiv_stream.py
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Run pipeline in demo mode using sample data")
args = parser.parse_args()

# -----------------------------
# DEMO MODE vs FULL MODE SETUP
# -----------------------------
if args.demo:
    print("Running in DEMO MODE!")
    INPUT_FILE = "data/sample_data.jsonl"
    OUTPUT_FILE = "arxiv_processed.jsonl"
    MIN_YEAR = 0   # keep all demo records
else:
    INPUT_FILE = "arxiv-metadata-oai-snapshot.json"
    OUTPUT_FILE = "arxiv_processed.jsonl"
    MIN_YEAR = 2015


# -----------------------------
# STREAMING JSONL READER
# -----------------------------
def stream_arxiv_records(path):
    """Generator that yields one JSON record per line."""
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


# -----------------------------
# YEAR EXTRACTION
# -----------------------------
def extract_year(record):
    """Extracts year from update_date or created."""
    date_str = record.get("update_date") or record.get("created") or ""
    if len(date_str) >= 4 and date_str[:4].isdigit():
        return int(date_str[:4])
    return None


# -----------------------------
# MAIN PROCESSING LOOP
# -----------------------------
def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    count_in = 0
    count_out = 0

    with open(OUTPUT_FILE, "w") as out_f:
        for rec in stream_arxiv_records(INPUT_FILE):
            count_in += 1

            # Extract year
            year = extract_year(rec)

            # Apply filter ONLY in full mode
            if not args.demo:
                if year is None or year < MIN_YEAR:
                    continue

            # Build cleaned record
            processed = {
                "id": rec.get("id"),
                "title": rec.get("title"),
                "abstract": rec.get("abstract"),
                "categories": rec.get("categories"),
                "year": year,
            }

            out_f.write(json.dumps(processed) + "\n")
            count_out += 1

    print(f"Done. Read {count_in} records total, wrote {count_out} filtered records to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
