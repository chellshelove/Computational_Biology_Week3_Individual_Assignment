# Define a dictionary mapping DNA codons to amino acids
codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

def translate_dna_to_protein(dna_sequence):
    # Initialize an empty mRNA and protein sequence
    mrna_sequence = ""
    protein_sequence = ""
    
    # Replace 'T' with 'U' to get the mRNA sequence
    mrna_sequence = dna_sequence.replace('T', 'U')
    
    # Translate the mRNA sequence into an amino acid sequence
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, 'X')  # 'X' represents an unknown codon
        protein_sequence += amino_acid
    
    return protein_sequence

# Example usage
dna_sequence = "TTACGA"
protein_sequence = translate_dna_to_protein(dna_sequence)
print("Input DNA =", dna_sequence)
print("Complement =", dna_sequence.translate(str.maketrans("ATCG", "TAGC")))
print("mRNA =", dna_sequence.replace('T', 'U'))
print("Aminoacid =", protein_sequence)