#processing tabular data

#to make division work!
from __future__ import division

#input data
raw_data = open("E:\data files\data.csv","r")

#species name
for line in raw_data:
    row = line.split(",")
    species_name = row[0]
    dna_seq = row[1]
    gene_name = row[2]
    expression_level = row[3]
    if species_name == "Drosophila melanogaster" or species_name == "Drosophila simulans":
        print ("Gene " + gene_name + " belongs to Drosophila melanogaster or Drosophila simulans")

#new line
print("\n")

#add in data again
raw_data = open("E:\data files\data.csv","r")              

#gene length
for line in raw_data:
    row = line.split(",")
    species_name = row[0]
    dna_seq = row[1]
    gene_name = row[2]
    expression_level = row[3]
    if len(dna_seq)>90 and len(dna_seq)<110:
        print ("Gene " + gene_name + " in " + species_name + " is between 90 and 110 bp long ")

#new line
print("\n")

#and again
raw_data = open("E:\data files\data.csv","r")  

#calculate AT content
for line in raw_data:
    row = line.split(",")
    species_name = row[0]
    dna_seq = row[1]
    gene_name = row[2]
    expression_level = row[3]
    total_content = len(dna_seq)
    total_at = dna_seq.count("a")+dna_seq.count("t")
    at_content = (total_at)/(total_content)
    if at_content < 0.5 and int(expression_level)> 200:
        print ("The AT content of gene " + gene_name + " is <0.5 and its expression level is >200 ")

#new line
print("\n")

#and again
raw_data = open("E:\data files\data.csv","r")

#gene names beginning with h or t except those belonging to Drosophila melanogaster

for line in raw_data:
    row = line.split(",")
    species_name = row[0]
    dna_seq = row[1]
    gene_name = row[2]
    expression_level = row[3]
    if (gene_name.startswith("h") or gene_name.startswith("t")) and species_name != "Drosophila melanogaster":
        print ("Gene " + gene_name + "starts with h or t but does not belong to Drosophila melanogaster ")

#new line
print("\n")

#and again
raw_data = open("E:\data files\data.csv","r")        


for line in raw_data:
    row = line.split(",")
    species_name = row[0]
    dna_seq = row[1]
    gene_name = row[2]
    expression_level = row[3]
    total_content = len(dna_seq)
    total_at = dna_seq.count("a")+dna_seq.count("t")
    at_content = (total_at)/(total_content)
    if at_content > 0.65 :
        print (gene_name + " has a high AT content")
    elif at_content <0.65 and at_content >0.45:
        print (gene_name + " has a medium AT content")
    else:
        print (gene_name + " has a low AT content")
                             
