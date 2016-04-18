from __future__ import division

def my_function(protein,aa):
    length = len(protein)
    aa = aa.upper()
    aa_count = protein.count(aa)
    aa_content = aa_count/length * 100
    rounded_aa_content = round(aa_content,0)
    return rounded_aa_content

assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert my_function("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0



