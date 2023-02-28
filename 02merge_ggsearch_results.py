import pandas as pd
import csv, sys

# script to merge ggsearch result from  parse_ggsearch.py
# Usage: python parse_ggsearch.py list (tab-delim)
# list example (file name, species name):
# ggsearch_out_Caenorhabditis_elegans.WBcel235.txt.parsed.tsv	Cele
# ggsearch_out_Drosophila_melanogaster.BDGP6.32.txt.parsed.tsv	Dmel
# ggsearch_out_Homo_sapiens.GRCh38.txt.parsed.tsv	Hsap
# ggsearch_out_Mus_musculus.GRCm39.txt.parsed.tsv	Mmus

# python merge_ggsearch_results.py merge_ggsearch_list

list_in = sys.argv[1]

def make_df(gg_in, species):
    df = pd.read_table(gg_in)
    df = df.set_index('query')
    df = df.add_suffix('_' + species)
    df = df.iloc[:, [0, 1, 2]]
    return df

df_merge = pd.DataFrame()

with open(list_in, "r") as f:
    for line in f:
        line = line.split("\t")
        with open(line[0].rstrip(), "r") as g:
            df_tmp = make_df(g, line[1].rstrip())
            df_merge = df_merge.join([df_tmp], how = 'outer')

df_merge.to_csv("./merged_ggsearch_result.csv")