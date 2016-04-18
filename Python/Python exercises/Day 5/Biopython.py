from Bio import Entrez, SeqIO
Entrez.email = "thomascwilliams83@googlemail.com"
my_search = Entrez.esearch(db= "nucleotide" , term = "COX1 or COI"  , retmax = 5)
result = Entrez.read(my_search)
for accession in result['IdList']:
    genbank = Entrez.efetch(db="nucleotide",id=accession,rettype="gb")
    record = SeqIO.read(genbank,"genbank")
    print len(record.seq)
    
    