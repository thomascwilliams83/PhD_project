#input initial data
raw_data= ['atgctcgatcgctag','aag-tcgctcgct--','atcctc--tcgcggg']

#length sequence
length = len(raw_data[1])

for column_number in range(length):
    column_string = ''
    for sequence in raw_data:
        column_string = column_string + sequence[column_number]
    print ("Column" + str(column_number) + " : " + column_string)
    
    
