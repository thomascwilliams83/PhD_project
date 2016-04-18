#Day 4 notes
#Paired day- "key" eg word, and "value" eg definition, or sample and coordinates.
#Only runs one say- keys go to values.
#In Python have "dicts" (Python for dictionary)
#To make a dict:

#Start and end with curly brackets
#separate keys and values with colons
#separate each pair (item) with a comma

#eg:
##enzymes = {"EcoRI" : "GAATTC" ,
##           "AvaII" : "GGACC",
##           "BisI" : "GCNGC",
##           }
##
##motif = enzymes ["BisI"]

#keys have to be unique

#can build up from an empty dict:

enzymes_1 ={}

enzymes_1["EcoRI"]="GAATTC"
enzymes_1["AvaII"]="GGACC"
enzymes_1["BisI"]="GCNCG"

                 
dna = "AATGATGAACGAC"
dinucleotides = ['AA','AT','AG','AC',
                'TA','TT','TG','TC',
                'GA','GT','GG','GC',
                'CA','CT','CG','CC']
all_counts = {}
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    if count > 0:
        all_counts[dinucleotide] = count

print all_counts['AA']

#get method- allows us to specify default value for keys that are missing
#eg all_counts.get("AG",0)
print all_counts.get("AT",0)
#to find out what keys are:
print all_counts.keys()

#to look for keys with a specific value
for dinucleotide in all_counts.keys():
    dinuc_count = all_counts.get(dinucleotide)
    
    if dinuc_count == 2:
        print(dinucleotide)
#shortcut
# can use "in" method

for dinucleotide, count in all_counts.items():
    if count == 2:
        print(dinucleotide)
        
#actually is position and comma that tells Python which is key and which is value, ie:

for key, value in all_counts.items():
    if value == 2:
        print(key)
#re are regular expression modules
#need to import re at the start of running functions

#to turn string into raw string add r at the beginning
# eg my_raw_string = r"hello\nworld\t!" eliminates new line and tab

#search() function finds a particular sequence and gives a true/false answer
#can search either for specific sequences:
re.search(r"GAA")
#or variations:
re.search(r"G(A|T)A")
re.search(r"G[AT]A")
#both above will search for same sequence

#stop sign can be any character

#? means value preceding it is optional

# + means value preceding it can be repeated more than once

# * is optional, but value preceding it can also be repeated

#can specify minimum and maximum number of repetitions
GCG{2,4}

#can use powerful combinations

^ATG[ATCG]{30,1000}A{5,10}$

#ie starts with ATG, followed by between 30 and 1000 base pairs, and finishes with between 5 and 10 consecutive As

#to extract a match with a match object

dna = "CGATNCGGAAYCGATC"
m = re.search(r"[^ATGC]", dna)

# m is now a match object
if m:
    print("ambiguous base found!")
    ambig = m.group()
    print("the base is " + ambig)

#can extract position of match use .start() method, but only finds first match

dna = "CGATCGGAAYCGATC"
m = re.search(r"[^ATGC]", dna)

# m is now a match object
if m:
    print("ambiguous base found!")
    ambig = m.group()
    print("the base is " + m.group())
    print("the base is at position " + str(m.start()))

#can also use re.findall method to keep non-matching sequences
