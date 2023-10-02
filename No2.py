# Define a dictionary mapping DNA codons to amino acids
codon_table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

def calculate_codon_frequency(dna_sequence, amino_acid):
    rna_sequence = dna_sequence.replace('T', 'U')
    codon_frequency = {}
    amino_acid_codons = [codon for codon, aa in codon_table.items() if aa == amino_acid]
    
    for codon in amino_acid_codons:
        codon_frequency[codon] = rna_sequence.count(codon)
            
    return codon_frequency

# Example usage
dna_sequence = "AAUGCUAAU"
target_amino_acid = "N"
amino_acid_sequence = "NNA"
codon_frequency = calculate_codon_frequency(dna_sequence, target_amino_acid)

print("Input Aminoacid =", amino_acid_sequence)
print("mRNA =", dna_sequence)
for codon, frequency in codon_frequency.items():
    print(f"{codon} = {frequency}")