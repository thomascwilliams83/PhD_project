#open file

data_file = open("E:/data files/names.txt")
dictionary = {}
dictionary_common_to_scientific = {}
dictionary_common_name_count = {}

for line in data_file:
    row= line.rstrip("\n").split(",")
    scientific_name = row[0]
    common_name = row [1]
    dictionary[scientific_name] = common_name
    if common_name not in dictionary_common_name_count:
        dictionary_common_name_count[common_name] = 1
    else:
        current_count = dictionary_common_name_count[common_name]
        current_count = current_count + 1
        dictionary_common_name_count[common_name] =  current_count
    dictionary_common_to_scientific[common_name]= scientific_name


def dictionary_reader():
    value = raw_input("Enter scientific name \n")
    return dictionary[value]
   
def common_name_counter():
    value = raw_input("Enter common name \n")
    return dictionary_common_name_count[value.rstrip("\n")]

##for common_name, count in dictionary_common_name_count.items():
##    if count > 1:
##        print(common_name, count)


number = 0
frog_list =[]
for scientific_name , common_name in dictionary.items():
    if "frog" in common_name:
        number = number + 1
        frog_list.append(scientific_name)

print ("The number of frog species is: " + str(number))
print ("Their scientific species names are: \n " + str(frog_list))

