#original data
raw_data= ['atgctcgatcgctag','aag-tcgctcgct--','atcctc--tcgcggg']

sequence_1=raw_data[0]
sequence_2=raw_data[1]
sequence_3=raw_data[2]


for base in range(len(sequence_1)):
    alignment = (sequence_1[base]+ sequence_2[base]+sequence_3[base])
    print("Column "+ str(base) + ": " + alignment)
    
    
