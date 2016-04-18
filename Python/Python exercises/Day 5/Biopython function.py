from __future__ import division

from Bio import Entrez, SeqIO

Entrez.email = "thomascwilliams83@googlemail.com"

def mean_length_calculator(search_term, retmax=5):
   
    #create protein list
    protein_list = []
    #search ncbi
    my_search = Entrez.esearch(db= "protein" , term = search_term , retmax = retmax)
    # creates 100 results
    result = Entrez.read(my_search)
    #loops through 100 results
    for accession in result['IdList']:
        print(str(len(protein_list)) + '/' + str(retmax)) 
        genbank = Entrez.efetch(db="protein",id=accession,rettype="gb")
        record = SeqIO.read(genbank,"genbank")
        protein = record.seq
        protein_list.append(len(protein))
    mean_length = sum(protein_list)/len(protein_list)
    return (mean_length)

#input data
search_term = raw_input("Enter search term: \n")   
retmax = int(raw_input("Enter sample size: \n"))   
output = open("E:/Python exercises/Day 5/result" + search_term + ".txt", "w")
mean = mean_length_calculator(search_term, retmax)
output.write(str(mean))
output.close()
print mean

    
 
    