import sys

# script to parse blastp results
# Usage: python parse_blastp.py blastp_out_Homo_sapiens.GRCh38.txt > blastp_out_Homo_sapiens.GRCh38.txt.parsed.txt

# bp_in=(blastp_out_Homo_sapiens.GRCh38.txt blastp_out_Mus_musculus.GRCm39.txt blastp_out_Drosophila_melanogaster.BDGP6.32.txt blastp_out_Caenorhabditis_elegans.WBcel235.txt)
# for i in ${bp_in[@]}; do python parse_blastp.py $i > $i.parsed.tsv; done

def remove_p(query_id):
    query_id = query_id.split(".")
    return ".".join(query_id[:-1])

file_in = sys.argv[1]

output = ""

with open(file_in, "r") as f:
    for line in f:
        line = line.split("\t")
        output += remove_p(line[0]) + "\t" + line[1] + "\n"

print(output)