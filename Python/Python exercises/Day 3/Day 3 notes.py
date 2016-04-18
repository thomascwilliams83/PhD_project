from __future__ import division

### to write programs that follow sets of rules need conditions
##
### a condition is a short segment of code that Python can make a true/false call on
##
### == means equals
##
### > greater than
##
### <= less than or equal to
##
##>>> print(len("ATGC") > 5)
##False
##
##>>> print("GAATTC".count("T") > 1)
##True
##
##>>> print("ATGCTT".startswith("ATG"))
##True
##
##>>> print("ATCCTT".endswith("TTT"))
##False
##
##>>> print("V" in ["V","W","U","Z"])
##True
##
###how to use conditions in script? simplest thing to do is execute a code if it is true
##
##>>> expression_level = 125
##>>> if expression_level > 100:
##	print ("length is over 100")

##
##accs = ["ab56","bh84","hv76","ay93"]
##
##print accs
##for accession in accs:
##    if accession.count("b") > 0:
##        print (accession + " contains a b")
##
##accs = ["ab56","bh84","hv76","ay93"]
##print( "Total number of accessions is " + str(len(accs))+ "\n")
##for accession in accs:
##    if accession.startswith("a"):
##        print(accession + " starts with a")
##    else:
##        print(accession + " does not start with a")
##
##accs = ["ab56","bh84","hv76","ay93","ap97","bd72"]
##
##print( "Total number of accessions is " + str(len(accs))+ "\n")
##for accession in accs:
##    if accession.startswith("a"):
##        print(accession + " starts with a")
##    else:
##        if accession.startswith("b"):
##            print (accession + " starts with b")
##        else:
##            print (accession + " does not start with a or b")

#elif function - 
##
##accs = ["ab56","bh84","hv76","ay93","ap97","bd72","c76","c89","d87","d89","e76"]
##
##print( "Total number of accessions is " + str(len(accs))+ "\n")
##print (" The following accessions start with a or b ")
##
##for accession in accs:
##    if accession.startswith("a"):
##        print(accession + " starts with a")
##    elif accession.startswith("b"):
##        print (accession + " starts with b")
##    elif accession.startswith("c"):
##        print (accession + " starts with c")
##    elif accession.startswith("d"):
##        print (accession + " starts with d")       
##    else:
##        print (accession + " does not start with a,b,c or d")
##
##
###bit more complicated
##        
##accs = ["ab56","bh84","hv76","ay93","ap97","bd72","c76","c89","d87","d89","e76"]
##
##print( "Total number of accessions is " + str(len(accs))+ "\n")
##print ("The following accessions start with a or b: \n ")
##
##for accession in accs:
##    if accession.startswith("a"):
##        print(accession)
##    if accession.startswith("b"):
##        print (accession )      
    

### and function
##accs = ["ab56","bh84","hv76","ay93","ap97","bd72","c76","c89","d87","d89","e76"]
##
##for a in accs:
##    if a.startswith("a") and a.endswith("6"):
##        print (a + " starts with a and ends with 6")
##
###or function
##
##for a in accs:
##    if a.startswith("a") or a.endswith("6"):
##        print ("at least once condition is true for " + a)
##
##for pos in range(len(accs)):
##    a = accs[pos]
##    if a.startswith("a") or a.endswith("3"):
##        print ("at least one condition is true for accession " + a + " at position " + str(pos))
##
##accs = ["ab56","bh84","hv76","ay93","ap97","bd72","c76","c89","d87","d89","e76"]
##
##accs = ["ab54","bh84","hv74","ay93","ap97","bd72","c76","c89","d87","d89","e76"]
##for a in accs:
##    if (
##        # does the accession start with a?
##        (a.startswith("a")
##        # does the accession start with h?
##        or a.startswith("h"))
##        and a.endswith("4")
##        ):
##            print("accession " + a + " starts with a or h and ends with 4")

#can turn line of code into function by using def


#define a new function
def get_at_content(dna):
    length= len(dna)
    a_count = dna.count("A")
    t_count = dna.count("T")
    at_content = (a_count + t_count) / length
    return at_content

#call the function

dna="AAATTGGGCCCGGTTAAGCGATAGACGTAGGAA"

at = get_at_content(dna)

print at

#when write a function don't need to worry about how it will be used - only need to know input and output


# how to round off answer
round function eg. round(number,2) for two decimal places

#define a new function
def get_at_content(dna,sig_figs):
    length= len(dna)
    a_count = dna.count("A")
    t_count = dna.count("T")
    at_content = (a_count + t_count) / length
    rounded_at_content = round(at_content,sig_figs)
    return rounded_at_content        

#assert function - if an assert give a false answer will stop and give an error message
# use this to test functions
