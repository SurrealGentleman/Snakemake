import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f:
    content = f.read().strip()

with open(output_file, "w") as f:
    f.write(content + "\n")
    f.write("Processed by Snakemake workflow.\n")
