dna_sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
#total length of DNA strand
length = len(dna_sequence)
#identify insertion site
Eco_RI = dna_sequence.replace("GAATTC","G*AATTC")
#find position of insertion site
position = Eco_RI.find('*')
#lengths of different lengths
strand_1 = position
strand_2 = length - position 
#output
print (dna_sequence)
print ("Total strand length is " + str(length) + " nucleotides")
print ("Restriction fragment 1 length is " + str(strand_1) + " nucleotides")
print ("Restriction fragment 2 length is " + str(strand_2) + " nucleotides")

#alternatively
length = len(dna_sequence)

#identify insertion site - position of number given by Python + 1
position = dna_sequence.find("GAATTC")

print ("Total strand length is " + str(length) + " nucleotides")
print ("Restriction fragment 1 length is " + str(position + 1 ) + " nucleotides")
print ("Restriction fragment 2 length is " + str(length - position - 1) + " nucleotides")

#alternatively
length = len(dna_sequence)

#identify insertion site - position of number given by Python + 1
position = dna_sequence.find("GAATTC")+ 1

print ("Total strand length is " + str(length) + " nucleotides")
print ("Restriction fragment 1 length is " + str(position)  + " nucleotides")
print ("Restriction fragment 2 length is " + str(length - position - 2) + " nucleotides")
