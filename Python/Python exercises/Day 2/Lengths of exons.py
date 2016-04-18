# lengths of exons
exon_lengths = open("E:\data files\exons.txt")

#Create new document
length_exons = open("length_exons.txt","w")
                    
#process one line at a time
for line in exon_lengths :
    split_line = line.split(",")
    start_site = int(split_line[0])
    stop_site = int(split_line[1])
    length = stop_site - start_site
    length_exons.write(str(length)+"\n")

#Close document
length_exons.close()
    
    
    
