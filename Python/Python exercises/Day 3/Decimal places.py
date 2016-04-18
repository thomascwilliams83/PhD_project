from __future__ import division

def get_at_content(dna,dp=2):
    length= len(dna)
    a_count = dna.count("A")
    t_count = dna.count("T")
    at_content = (a_count + t_count) / length
    rounded_at_content = round(at_content,dp)
    return rounded_at_content

assert get_at_content("A")==1
assert get_at_content("G")==0

assert get_at_content("ATGC")==0.5

assert get_at_content("AGG")== 0.33

assert get_at_content("AGG",1)==0.3
assert get_at_content("AGG",5)==0.33333

