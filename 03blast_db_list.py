import sys

# First step only
# script to extract gene id and name from databse fasta file
# Usage: python blast_db_list.py Homo_sapiens.GRCh38.pep.all.fa > Homo_sapiens.GRCh38.pep.all.fa.gene_name_list

file_in = sys.argv[1]

with open(file_in, "r") as f:
    for line in f:
        if line[0] == ">":
            output_tmp = []

            idx_end = line.find(" ")
            db_id = line[1 : idx_end].rstrip()
            output_tmp.append(db_id)

            if "gene_symbol:" in line:
                idx = line.find("gene_symbol:")
                gene_symbol = line[idx + 12:].rstrip()
                gene_symbol = gene_symbol.split(" ")
                output_tmp.append(gene_symbol[0])
            else:
                gene_symbol = "No gene_symbol"
                output_tmp.append(gene_symbol)

            if "description:" in line:
                idx = line.find("description:")
                dbdesc = line[idx + 12:].rstrip()
                output_tmp.append(dbdesc)
            else:
                dbdesc = "No description"
                output_tmp.append(dbdesc)
            
            print("\t".join(output_tmp))