from __future__ import division

#create data series
dna_seq1 = "AGTTCGGTTNNNNNNNGGTTTCGGCGG----ATTT---GTTC---SSS"
dna_seq2 = "AAGGGTT---NNNNNNNSSSSGGTTT----AACCCTTTCCCSSSNNNN"
dna_seq3 = "AAACCCCGGTGATGCTGATGCCCGTAGTCATAGCTGGGTACG---SSS"
dna_seq4 = "AAACCCTTTCCCGGGGCAGTAGTATGATGCTGGTGGCCCTAGATGCTG"

###create function
##def my_function(dna_seq,threshold):
##    number = 0
##    number = number + dna_seq.count("A")
##    number = number + dna_seq.count("T")
##    number = number + dna_seq.count("C")
##    number = number + dna_seq.count("G")
##    percentage_pre_rounding = 100 - ((number / len(dna_seq)) * 100)
##    percentage = round(percentage_pre_rounding,0)
##    if percentage > threshold:
##        return( dna_seq + ":\nTrue: percentage of undetermined bases is " + str(percentage)+ "% ; threshold is " + str(threshold)+ " %")
##    else:
##        return (dna_seq + ":\nFalse: number of undetermined bases is " + str(percentage)+ "% ; threshold is " + str(threshold)+ " %")

#create function
def my_function(dna_seq,threshold):
    number = 0
    for base in ["A","T","C","G"]:
        number = number + dna_seq.count(base)
    percentage_pre_rounding = 100 - ((number / len(dna_seq)) * 100)
    percentage = round(percentage_pre_rounding,0)
    if percentage > threshold:
        return( dna_seq + ":\nTrue: percentage of undetermined bases is " + str(percentage)+ "% ; threshold is " + str(threshold)+ " %")
    else:
        return (dna_seq + ":\nFalse: number of undetermined bases is " + str(percentage)+ "% ; threshold is " + str(threshold)+ " %")

###test data
##threshold = 20
##
##dna_seq = dna_seq1
##
##print my_function(dna_seq,threshold)
##
##print("\n")
##
##dna_seq = dna_seq2
##
##print my_function(dna_seq,threshold)
##
##print("\n")
##
##dna_seq = dna_seq3
##
##print my_function(dna_seq,threshold)
##
##print("\n")
##
##dna_seq = dna_seq4
##
##print my_function(dna_seq,threshold)





#test data
threshold = 20

for seq in [dna_seq1,dna_seq2,dna_seq3,dna_seq4]:
    print my_function(seq,threshold)
