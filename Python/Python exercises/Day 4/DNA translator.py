#define dictionary
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

###define DNA sequence
##
##dna_seq = "GTGGAATTGCCTGAGTCGTCCGGTAGGTCCGTAGCTGATGCTAGTAGCTAGTGGGGCCTTCGCTAGCGTCGACCTCGCGGTACCGTACCGTACGGTACGGTACGATCGATCGATCGATACGCTACG"
##
##def dna_translator():
##    protein_seq = ""
##    value = raw_input("Enter DNA sequence: \n")
##    for start in range(0,len(value),3):
##        codon = value[start:start+3]
##        for aa, protein in gencode.items():
##            if aa == codon:
##                protein_seq = protein_seq + protein
##        else:
##                protein_seq = protein_seq 
##    return protein_seq


def dna_translator():
    protein_seq = ""
    value = raw_input("Enter DNA sequence: \n")
    for start in range(0,len(value),3):
        codon = value[start:start+3]
        aa = gencode.get(codon, 'X')
        protein_seq = protein_seq + aa
    return protein_seq

  

        
        
        
    
