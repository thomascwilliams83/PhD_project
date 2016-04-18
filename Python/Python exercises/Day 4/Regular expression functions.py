import re

dna = "ATCGATTTCAC"

if re.search(r"ATT",dna):
    print("restriction site found")
else:
    print("no restriction site found")

if re.search(r"AT(C|G)G",dna):
    print("restriction site found")
else:
    print("no restriction site found")
