import sys, re

# script to parse ggsearch result to tab-delim format (ggsearch results based on evm gene model)
# Usage: python parse_ggsearch.py input > output

# gg_in=(ggsearch_out_Homo_sapiens.GRCh38.txt ggsearch_out_Mus_musculus.GRCm39.txt ggsearch_out_Drosophila_melanogaster.BDGP6.32.txt ggsearch_out_Caenorhabditis_elegans.WBcel235.txt)
# for i in ${gg_in[@]}; do python parse_ggsearch.py $i > $i.parsed.tsv; done

def remove_p(query_id):
    query_id = query_id.split(".")
    return ".".join(query_id[:-1])

gg_in = sys.argv[1]

header = "query\tdbdesc\tdbhit\tdbgsymbol\tgnw_frame\tgnw_expect\tgnw_score\tgnw_ident\tgnw_sim"
print(header)

with open(gg_in, "r") as f:
    output_tmp = []
    for line in f:
        if line[0:3] == ">>>" and line[0:6] != ">>><<<":
            line = line.split(",")
            query = line[0][3:].rstrip()
            # query = remove_p(query) # for evm gene model e.g., evm.model.jcf7180000001939.498
            output_tmp.append(query) # 1
        elif line[0:2] == ">>" and line[0:6] != ">>><<<":
            if "description:" in line:
                idx = line.find("description:")
                dbdesc = line[idx + 12:].rstrip()
                output_tmp.append(dbdesc) # 2
            else:
                dbdesc = "No description"
                output_tmp.append(dbdesc) # 2
            line = line.split(" ")
            dbhit = line[0][2:].rstrip()
            output_tmp.append(dbhit) # 3
            if "gene_symbol:" in line:
                for l in line:
                    if l[0:11] == "gene_symbol":
                        dbgsymbol = l[12:].rstrip()
                        output_tmp.append(dbgsymbol) # 4
            else:
                dbgsymbol = "No gene_symbol"
                output_tmp.append(dbgsymbol) # 4
        elif line[0:11] == "; gnw_frame":
            line = line.split(":")
            gnw_frame = line[1][1:].rstrip()
            output_tmp.append(gnw_frame) # 5
        elif line[0:12] == "; gnw_expect":
            line = line.split(":")
            gnw_expect = line[1][1:].rstrip().lstrip()
            output_tmp.append(gnw_expect) # 6
        elif line[0:11] == "; gnw_score":
            line = line.split(":")
            gnw_score = line[1][1:].rstrip()
            output_tmp.append(gnw_score) # 7
        elif line[0:11] == "; gnw_ident":
            line = line.split(":")
            gnw_ident = line[1][1:].rstrip()
            output_tmp.append(gnw_ident) # 8
        elif line[0:9] == "; gnw_sim":
            line = line.split(":")
            gnw_sim = line[1][1:].rstrip()
            output_tmp.append(gnw_sim) # 9
        elif line[0:6] == ">>><<<" and len(output_tmp) == 9:
            print("\t".join(output_tmp))
            output_tmp = []
        # elif line[0:6] == ">>><<<" and len(output_tmp) != 0:
        #     print(output_tmp)
        #     # print("\t".join(output_tmp))
        #     output_tmp = []

        