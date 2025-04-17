"""
First, download the OSCAR corpus from https://huggingface.co/datasets/oscar-corpus/OSCAR-2301.
"""


import gzip
import os
from pathlib import Path

# Input and output directories
corpus_dir = Path('/Users/skylorwong/Downloads/Princeton/COS484/cos484final/tokenizer-attack-main/data')
clean_dir = Path(str(corpus_dir) + "/local_data/oscar-mini")
clean_dir.mkdir(parents=True, exist_ok=True)

for gz_file in corpus_dir.glob("*.gz"):
    lang_code = gz_file.stem  # e.g., 'en' from 'en.gz'

    lang_output_dir = clean_dir / lang_code
    lang_output_dir.mkdir(parents=True, exist_ok=True)

    output_file = lang_output_dir / f"{lang_code}.txt"

    with gzip.open(gz_file, 'rt', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
        for line in fin:
            fout.write(line.strip() + "\n")

    print(f"Saved: {output_file}", flush=True)
