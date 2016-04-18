from __future__ import division
dna_sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#identify exons
exon_1 = dna_sequence[0:63]
exon_2 = dna_sequence[90:]
#stitch together coding DNA
coding_dna = (exon_1 + exon_2)
#intron
intron = dna_sequence[63:90]
#upper and lower case
dna_sequence_cases = (exon_1 + intron.lower() + exon_2)


#total length of DNA
total_length = len(dna_sequence)
#length of coding DNA
coding_length = len(coding_dna)
#percentage
percentage = (coding_length/total_length * 100)
#percentage coding
percentage_coding= ("The total percentage of coding DNA is " + str(percentage) + " percent ")

print ("The original DNA sequence is " + dna_sequence_cases )
print ("The coding sequences are " + coding_dna)
print (percentage_coding)





                    
                    
