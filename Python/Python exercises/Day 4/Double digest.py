#Double digest

import re

dna_seq = open("E:/data files/long_dna.txt").read().rstrip("\n")
# dna_seq = "CCCAATAATGGGATTAATGCCCCC"

# restriction cut site for Abc1 is ANT/AAT

#method 1 - physically cut up dna_seq

fragments = re.split("A[ATGC]TAAT",dna_seq)

list_fragments =[]

for fragment in fragments:
    if len(list_fragments) == 0:
        fragment = fragment + "ANT"
    elif len(list_fragments)> 0 and len(list_fragments) < (len(list_fragments)-1) :
        fragment = "ANT" + fragment + "AAT"
    else:
        fragment = "AAT" + fragment
    list_fragments.append(fragment)
##
##for fragment in list_fragments:
##    print len(fragment)

# now cut again- restriction cut site for Abc2 is GCRW/TG


final_fragments=[]

# for each original fragment
for fragment in list_fragments:
    
    # split with the second enzyme to make new fragments
    new_fragments = re.split("GC[AG][AT]TG", fragment)

    # if only one new fragment, then it hasn't split...
    if len(new_fragments) == 1:
        # ... so just append to the final fragments
        final_fragments.append(new_fragments[0])

    # if multiple new fragments...
    else:
        list_new_fragments =[]

        # .. then add bases to replace the split bits
        for fragment in new_fragments:
            if len(list_new_fragments) == 0:
                fragment = fragment + "CGRW"
            elif len(list_new_fragments)> 0 and len(list_new_fragments) < (len(list_new_fragments)-1) :
                fragment = "TG" + fragment + "CGRW"
            else:
                fragment = "TG" + fragment
            list_new_fragments.append(fragment)
            final_fragments.append(fragment)

for fragment in final_fragments:
    print len(fragment)

    


        
    

