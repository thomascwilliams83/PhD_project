from __future__ import division

def _my_subsid_function(protein, aa_list):
    number = 0
    for aa in aa_list:
        aa_upper = aa.upper()
        protein.count(aa)
        number = number + protein.count(aa)
    return number


def my_function(protein, aa_list = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
    number = _my_subsid_function(protein,aa_list)
    length = len(protein)
    aa_content = number/length * 100
    rounded_aa_content = round(aa_content,0)
    return rounded_aa_content

assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65

