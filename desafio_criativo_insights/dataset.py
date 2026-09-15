from datasets import load_dataset
import pandas as pd

DATASET_NAME = "claritystorm/cfpb-consumer-complaints"
OUTPUT_CSV = "desafio_criativo_insights/cfpb_consumer_complaints.csv"

ds = load_dataset(DATASET_NAME, split="train")
df = ds.to_pandas()

print(f"Dataset carregado: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(df.head())

df.to_csv(OUTPUT_CSV, index=False)
print(f"Arquivo salvo em: {OUTPUT_CSV}")