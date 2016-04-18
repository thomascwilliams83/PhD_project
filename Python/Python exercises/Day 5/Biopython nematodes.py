from __future__ import division

from Bio import Entrez, SeqIO

protein_list = []
Entrez.email = "thomascwilliams83@googlemail.com"
my_search = Entrez.esearch(db= "protein" , term = '"Nematoda"[Organism] and cox1',retmax = 10)
result = Entrez.read(my_search)
for accession in result['IdList']:
    print(str(len(protein_list)) + '/100') 
    genbank = Entrez.efetch(db="protein",id=accession,rettype="gb")
    record = SeqIO.read(genbank,"genbank")
    
    protein = record.seq
    protein_list.append(len(protein))
mean_length = sum(protein_list)/len(protein_list)
print mean_length

    
    
 
    