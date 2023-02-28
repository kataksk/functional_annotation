import pandas as pd
import sys

# script to merge ggsearch and blastp result from parse_ggsearch.py and parse_blastp.py respectively
# Usage: python merge_ggsearch_and_blastp.py ggsearch_result blastp_result

# python merge_ggsearch_and_blastp.py merged_ggsearch_result.csv merged_blastp_result.csv

ggsearch_in = sys.argv[1]
blastp_in = sys.argv[2]

df_gg = pd.read_csv(ggsearch_in)
df_bp = pd.read_csv(blastp_in)

df_gg = df_gg.set_index('query')
df_bp = df_bp.set_index('query')

df_gg = df_gg.add_prefix("ggsearch:")
df_bp = df_bp.add_prefix("blastp:")

# print(df_gg)
# print(df_bp)

df_merge = pd.merge(df_gg, df_bp, on='query', how='inner')

df_merge = df_merge[~df_merge.index.duplicated(keep='first')]

print(df_merge)
df_merge.to_csv("./annotated_all.csv")
