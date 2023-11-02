import json
from datasets import load_dataset

# Load the answersumm dataset
dataset = load_dataset("alexfabbri/answersumm")

# Save each split to a separate JSON file as a list of records
for split, data in dataset.items():
    records = data.to_list()

    filename = f"answersumm_{split}.json"
    with open(filename, "w") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)
