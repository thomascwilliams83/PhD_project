#pairwise distance
from __future__ import division

#data
dna_frag = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']


dna_a= dna_frag[0]
dna_b= dna_frag[1]

#to start counter
number = 0


for pos in range(len(dna_a)):
    #looking at pos within dna string
    base_a = dna_a[pos]
    base_b = dna_b[pos]
    if base_a == base_b:
    #if they are equal add 1 to counter
        number=number+1

percentage = number/len(dna_a)*100
print(str(percentage) + " % of bases are identical in dna_a and dna_b")



#data
dna_frag = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']



for dna_a_pos in range(len(dna_frag)):
    dna_a = dna_frag[dna_a_pos]

    for dna_b_pos in range(len(dna_frag)):
        dna_b = dna_frag[dna_b_pos]

        if dna_a != dna_b:

            #to start counter
            number = 0

            for pos in range(len(dna_a)):
                #looking at pos within dna string
                base_a = dna_a[pos]
                base_b = dna_b[pos]
                if base_a == base_b:
                #if they are equal add 1 to counter
                    number=number+1

            percentage = number/len(dna_a)*100
            print(dna_a_pos, dna_b_pos, str(percentage) + " % of bases are identical")

