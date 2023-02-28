import pandas as pd
import sys

# script to add functional annotation to result of deseq2 based on output from merge_ggsearch_and_blastp.py
# Usage: python add_annotation.py result_padj_ordered_transcript.csv annotated_all.csv

# python add_annotation.py result_padj_ordered_transcript.csv /work2/kataoka/madarasuzu/rnaseq/masurca405_ph_hirise/fanflow/annotated_all.csv

# result_padj_ordered_transcript.csv
deseq_out = sys.argv[1]

# annotated_all.csv
ann_all = sys.argv[2]

df_deseq = pd.read_csv(deseq_out)
df_deseq = df_deseq.rename(columns={'Unnamed: 0': 'query'})
df_deseq = df_deseq.set_index("query")

# print(df_deseq)

df_ann_all = pd.read_csv(ann_all)
df_ann_all = df_ann_all.set_index("query")

# print(df_ann_all)

# df_merge = pd.merge(df_deseq, df_ann_all, on='query', how='inner')
df_merge = df_deseq.join([df_ann_all], how = 'outer')

# print(df_merge)

df_merge = df_merge.dropna(subset=['baseMean'])

# print(df_merge)
# df_merge.to_csv("./result_padj_ordered_transcript_annotantion_added.csv")

# python add_annotation.py result_padj_ordered.csv /work2/kataoka/madarasuzu/rnaseq/masurca405_ph_hirise/fanflow/annotated_all_gene.csv
# python ../deseq_brain/add_annotation.py result_padj_ordered.csv /work2/kataoka/madarasuzu/rnaseq/masurca405_ph_hirise/fanflow/annotated_all_gene.csv
df_merge.to_csv("./result_padj_ordered_annotantion_added.csv")
