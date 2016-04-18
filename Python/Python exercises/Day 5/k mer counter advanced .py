import os

### establish files to read
##for file_name in os.listdir("E:\data files\dna_files\Processed data"):
##    print (os.listdir(filename))
##
###create function to carry out task
##
##
##
##def kmer_calculator(seq,k,n):
##    #file to write into
##    kmer_file = open("E:/Python exercises/Day 5/kmer_file","w")
##    #create kmers in seq
##    for start in range(len(seq)):
##        kmer = seq[start:start+k]
##        kmer_count = seq.count(kmer)
##        kmer_file.write(kmer + "," + str(kmer_count) + "\n")
##        if kmer_count > n:
##            print (kmer,kmer_count)
##    return kmer_file.close()
##
##
##k= int(raw_input("Enter kmer length \n"))
##n= int(raw_input("Enter threshold \n"))
##

##def kmer_calculator(seq,k):
##    kmers = []
##    for start in range(0,len(seq)-(k-1),1):
##        kmer = seq[start:start+k]
##        kmers.append(kmer)
##    return kmers

seq= raw_input("Enter DNA sequence \n")
k = int(raw_input("Enter kmer length \n"))

kmer_counts= {}
for file_name in os.listdir("E:/data files/dna_files/Processed data"):
    if file_name.endswith((".dna"):
        dna_file = open("E:/data files/dna_files/Processed data/" + file_name)
        for line in dna_file:
            dna = line.rstrip("\n")
            for kmer in kmer_calculator(dna,k):
                current_count = kmer_counts.get(kmer,0)
                new_count = current_count + 1
                kmer_counts[kmer] = new count

print (kmer_counts)

        
