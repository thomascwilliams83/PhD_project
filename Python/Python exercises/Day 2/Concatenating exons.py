# lengths of exons
exon_lengths = open("E:\data files\exons.txt")

#genomic dna data
genomic_dna = open("E:\data files\genomic_dna2.txt").read()

#create new document
concatenated_exons = open("concatenated_exons.txt","w")

#number
number = 0 
                    
#process one line at a time
for line in exon_lengths :
    split_line = line.split(",")
    name = split_line[0]
    start_site = int(split_line[1])
    stop_site = int(split_line[2])
    exon_length = stop_site - start_site
    number = number + 1 
    print(name + " is number " + str(number) + " and it is " + str(exon_length)+ " nucleotides long")
    concatenated_exons.write(genomic_dna[start_site:stop_site])

#Close document
concatenated_exons.close()

final_data= open("E:\Python exercises\Day 2\concatenated_exons.txt")
final_data_read = final_data.read()

print("The coding sequence is : " + final_data_read)

    
    
    
