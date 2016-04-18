from __future__ import division

sequence_1 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
total_content = len(sequence_1)
total_a = sequence_1.count('A')
total_t = sequence_1.count('T')
total_at = total_a + total_t
at_content = (total_at)/(total_content) * 100
percentage = str(at_content)
print ("AT content is " + percentage + "%")
       
