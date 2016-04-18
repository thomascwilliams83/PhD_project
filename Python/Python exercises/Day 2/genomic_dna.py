genomic_dna_file = open("E:\data files\genomic_dna.txt")
genomic_dna_contents = genomic_dna_file.read()
my_dna = genomic_dna_contents.rstrip("\n")

#identify exons
exon_1 = my_dna[0:63]
exon_2 = my_dna[90:]
#stitch together coding DNA
coding_dna = (exon_1 + exon_2)
#intron
intron = my_dna[63:90]

#create new file for exons
coding_output_file = open("coding.txt","w")
coding_output_file.write(coding_dna)
coding_output_file.close()

#create new file for introns
non_coding_output_file = open("non_coding.txt","w")
non_coding_output_file.write(intron)
non_coding_output_file.close()





