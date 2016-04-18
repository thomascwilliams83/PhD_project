dna_sequence_init = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# replace upper for lower case to avoid double replacement

# A to T
dna_sequence = dna_sequence_init.replace("A","t")
# T to A
dna_sequence = dna_sequence.replace("T","a")
# G to C
dna_sequence = dna_sequence.replace("G","c")
# C to G
dna_sequence = dna_sequence.replace("C","g")

print (dna_sequence_init)
print (dna_sequence.upper())

# or alternatively
dna_sequence = dna_sequence.replace("A","t") .replace ("T","a") .replace("G","c") .replace ("C","g")
dna_sequence_upper = dna_sequence.upper()
complementary_sequence_list = dna_sequence_upper.split()

reverse_sequence = complementary_sequence_list.reverse()


print (dna_sequence_init)
print (dna_sequence.upper())

print (reverse_sequence)

