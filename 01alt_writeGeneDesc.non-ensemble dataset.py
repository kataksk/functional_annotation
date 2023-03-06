import pandas as pd
import sys, csv

# Modify parsed ggsearch tsv file based on non-ensemble dataset

# python 01_2writeGeneDesc.py protein.fa ggsearch_out_parsed.tsv > ggsearch_out_parsed.mod.tsv
# Can be used for protein.fa with header below:
# >NP_001014455.1 phosphatase 1 nuclear targeting subunit, isoform B [Drosophila melanogaster]

# python 01_2writeGeneDesc.py Drosophila_melanogaster_GCF_000001215.4_Release_6_plus_ISO1_MT_protein.faa ggsearch_out_Drosophila_melanogaster_GCF_000001215.4_Release_6_plus_ISO1_MT_protein.txt.parsed.tsv > ggsearch_out_Drosophila_melanogaster_GCF_000001215.4_Release_6_plus_ISO1_MT_protein.txt.parsed.tsv

db_in = sys.argv[1]
parsed_tsv = sys.argv[2]

def split_desc(header):
    header = header.split(" ")
    id_out = header[0][1:]
    desc_out = " ".join(header[1:]).rstrip()
    return id_out, desc_out

db_dict = {}

with open(db_in, "r") as f:
    for line in f:
        if line[0] == ">":
            db_dict[split_desc(line)[0]] = split_desc(line)[1]

# print(db_dict)
print("query\tdbdesc\tdbhit\tdbgsymbol\tgnw_frame\tgnw_expect\tgnw_score\tgnw_ident\tgnw_sim")

with open(parsed_tsv, "r") as f:
    for line in f:
        reader = csv.reader(f, delimiter = "\t")
        header = next(reader)
        for cols in reader:
            # print(cols[2])
            # output = cols[0] + "\t" + db_dict(cols[2]) + "\t" + "\t".join(cols[2:])
            output = cols[0] + "\t" +  db_dict[cols[2]] + "\t" + "\t".join(cols[2:])
            print(output)

