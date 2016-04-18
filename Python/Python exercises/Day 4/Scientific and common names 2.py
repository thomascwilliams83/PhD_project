#initially create dictionary mapping common names to sequence counts

data_file1 = open("E:/data files/names.txt")
data_file2 = open("E:/data files/seq_counts.csv")
dictionary2 = {}

for line in data_file2: 
    row= line.rstrip("\n").split(",")
    common_name = row[0]
    seq_count = row [1]
    dictionary2[common_name] = seq_count

#iterate over names file
    
for line in data_file1:
    row= line.rstrip("\n").split(",")
    scientific_name = row[0]
    common_name = row [1]

    seq_count = dictionary2[common_name]
    print(common_name,scientific_name,seq_count)

