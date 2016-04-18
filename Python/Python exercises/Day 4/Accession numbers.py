#Accession numbers
import re

raw_data = "xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp"
proteins = raw_data.split(", ")

print("\nThe following accession numbers contain a 5:")
for protein in proteins:
    if re.search("5", protein):
        print protein

print("\nThe following accession numbers contain a \'d\' or an \'e\':")
for protein in proteins:
    if re.search("[de]", protein):
        print protein

    
print("\nThe following accession numbers contain a \'d\' and an \'e\' in that order:")
for protein in proteins:
    if re.search("d.*e", protein):
        print protein

print("\nThe following accession numbers contain a \'d\' and an \'e\' in any order")
for protein in proteins:
    if re.search("d", protein)and re.search("e", protein):
        print protein

print("\nThe following accession numbers start with an \'x\' or a \'y\'")
for protein in proteins:
    if re.search("^x", protein)or re.search("^y",protein):
        print protein

print("\nThe following accession numbers start with an \'x\' or a \'y\' and end with an \'e\'")
for protein in proteins:
    if (re.search("^x", protein) or re.search("^y",protein)) and (re.search("e$",protein)):
        print protein

print("\nThe following accession numbers contain three or more numbers in a row")
for protein in proteins:
    if re.search("[1234567890]{3,}",protein):
        print protein

print("\nThe following accession numbers end with \'d\' followed by either \'a\', \'r\' or \'p\'")
for protein in proteins:
    if re.search("d[arp]$", protein):
        print protein
