import pandas as pd
import sys

# python transcript2gene.py annotated_all.csv

def remove_iso(query_id):
    query_id = query_id.split(".")
    return ".".join(query_id[:-1])

annotated_all = sys.argv[1]

df = pd.read_csv(annotated_all)
df['query'] = df['query'].map(remove_iso)
df = df.set_index('query')
df = df[~df.index.duplicated(keep='first')]

df.to_csv("./annotated_all_gene.csv")
