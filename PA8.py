# Write a program that prompts the user for a DNA sequence and translates the DNA into protein.


def main():
    seq = get_valid_sequence("Enter a DNA sequence: ")
    codons = get_codons(seq.upper())
    new_codons = get_sets_three(codons)
    protein = get_protein_sequence(new_codons)
    print(protein)


def get_valid_sequence(prompt):
    seq = input(prompt)
    seq = seq.upper()
    nucleotides = "CATGX"
    for nucleotide in nucleotides:
        if nucleotide in seq:
            return seq
        else:
            print("Please enter a valid DNA sequence")
            return get_valid_sequence(prompt)


def get_codons(seq):
    codons = [seq[i: i + 3] for i in range(0, len(seq), 3)]
    return codons


def get_sets_three(codons):
    for item in codons:
        short = len(item) < 3
        if short:
            codons.remove(item)
    return codons


def get_protein_sequence(codons):
    gencode = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S',
               'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L',
               'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
               'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
               'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
               'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S',
               'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
               'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E',
               'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    stop_codons = {'TAA': '*', 'TAG': '*', 'TGA': '*'}
    protein = []
    for item in codons:
        if item in gencode:
            protein = protein + list(gencode[item])
        if item in stop_codons:
            protein = protein + list(stop_codons[item])
    return protein


main()
