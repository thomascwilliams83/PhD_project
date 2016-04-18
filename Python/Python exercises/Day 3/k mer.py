# establish DNA sequence

seq = "ATGCATCATGATGCATCATGATGCATCATGATGCATCATGATGCATCATGATGCATCATGATGCATCATGATGCATCATGGGTTCCAATTCCGGAA"


#create function to carry out task



def kmer_calculator(seq,k,n):
    #file to write into
    kmer_file = open("kmer_file","w")
    #create kmers in seq
    for start in range(len(seq)):
        kmer = seq[start:start+k]
        kmer_count = seq.count(kmer)
        kmer_file.write(kmer +"," + str(kmer_count) + "\n")
        if kmer_count > n:
            print (kmer,kmer_count)
    return kmer_file.close()


k= int(raw_input("Enter kmer length \n"))
n= int(raw_input("Enter threshold \n"))

##print (kmer_calculator(seq,k,n))

        
