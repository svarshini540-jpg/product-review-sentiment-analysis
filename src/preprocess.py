import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    df = pd.read_csv("../data/raw/reviews.csv")

    df["clean_review"] = df["review"].apply(clean_text)

    df.to_csv("../data/processed/clean_reviews.csv", index=False)
    print("Preprocessing completed.")
