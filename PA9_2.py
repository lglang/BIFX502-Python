#  program that predicts the fragment lengths that we will get if we digest the
# sequence with the following made up restriction enzyme AbcI, whose recognition site
# is ANT/AAT

import re


def main():
    dna = get_valid_file("Enter file name: ")
    if re.search(r"A.TAAT", dna):
        print("Restriction site found.")


def get_valid_file(prompt):
    try:
        file_input = input(prompt)
        file_name = open(file_input, 'r')
        dna = file_name.readline()
        dna_list = []
        for line in dna:
            dna_list.append(line)
        file_name.close()
        return dna_list
    except IOError:
        print("An error occurred retrieving the file list; please try again")
        return get_valid_file(prompt)


main()
