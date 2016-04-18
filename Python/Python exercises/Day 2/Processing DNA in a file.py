#Processing DNA in a file

#create file that contains data
dna_sequence = open("E:\data files\input.txt")
dna = dna_sequence.read()

#break up into strings
dna_strings = dna.split("\n")

#Create new document
Clean_sequence = open("Clean_dna.txt","w")

#trim out adaptor
for string in dna_strings:
    clean_dna = string[14:]
    Clean_sequence.write(clean_dna + "\n")

#Close document
Clean_sequence.close()




    



