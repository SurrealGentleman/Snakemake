rule all:
    input:
        "results/output.txt"


rule process_text:
    input:
        "data/input.txt"
    output:
        "results/output.txt"
    shell:
        """
        py scripts/script.py {input} {output}
        """
