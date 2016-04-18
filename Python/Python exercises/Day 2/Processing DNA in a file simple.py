
#Simpler alternative for processing DNA in a file

#create file that contains data
dna_sequence = open("E:\data files\input.txt")

#don't need to create list of strings as Python does this automatically for files

#Create new document
Clean_sequence = open("Clean_dna_simple.txt","w")

#trim out adaptor
for string in dna_sequence:
    clean_dna = string[14:]
    Clean_sequence.write(clean_dna)
    print (int(len(clean_dna) )- 1)

#Close document
Clean_sequence.close()
