import pandas as pd
import sys

# script to merge blastp result from  parse_ggsearch.py
# Usage: python merge_blastp.py list (tab-delim)
# list example:
# blastp_out_Caenorhabditis_elegans.WBcel235.txt.parsed.txt   /work2/kataoka/fanflow_db/Caenorhabditis_elegans.WBcel235.pep.all.fa.gene_name_list   Cele
# blastp_out_Drosophila_melanogaster.BDGP6.32.txt.parsed.txt  /work2/kataoka/fanflow_db/Drosophila_melanogaster.BDGP6.32.pep.all.fa.gene_name_list  Dmel
# blastp_out_Homo_sapiens.GRCh38.txt.parsed.txt   /work2/kataoka/fanflow_db/Homo_sapiens.GRCh38.pep.all.fa.gene_name_list   Hsap
# blastp_out_Mus_musculus.GRCm39.txt.parsed.txt   /work2/kataoka/fanflow_db/Mus_musculus.GRCm39.pep.all.fa.gene_name_list   Mmus

# python merge_blastp.py merge_blastp_list

list_in = sys.argv[1]

def make_df_blastp_out(file_in):
    df = pd.read_table(file_in, names = ["query", "db"])
    return df

def make_df_blastp_db(file_in):
    df = pd.read_table(file_in, names = ["db", "gene_symbol", "description"])
    return df

df_out = pd.DataFrame()

with open(list_in, "r") as f:
    for line in f:
        line = line.split("\t")
        # print(line)
        with open(line[0].rstrip(), "r") as g:
            df_blastp_out = make_df_blastp_out(g)
        with open(line[1].rstrip(), "r") as h:
            df_blastp_db = make_df_blastp_db(h)

        species = line[2].rstrip()
        
        df_merge = pd.merge(df_blastp_out, df_blastp_db, on='db', how='inner')
        df_merge = df_merge.set_index('query')
        # print(df_merge)
        df_merge = df_merge.add_suffix('_' + species)
        # print(df_merge)
        df_out = df_out.join([df_merge], how = 'outer')
        # print(df_out)

df_out = df_out[~df_out.index.duplicated(keep='first')]

print(df_out)
df_out.to_csv("./merged_blastp_result.csv")