#advanced version

import os

number = 100
copy_number = 0
file_number = 0 
for file_name in os.listdir("E:/data files/dna_files"):
    dna_seq = open("E:/data files/dna_files/" + file_name)
    for line in dna_seq:
        for number in range(100,1000,100):
            if len(line) >= number  and len(line) < number + 100:
                destination_folder = "E:/data files/dna_files/Processed data/" + str(number) + " to " + str(number+99)
                if not os.path.exists(destination_folder):
                    os.mkdir(destination_folder)
                destination_file = destination_folder +"/ID" + str(file_number)+ ",Sequence length " + str(len(line)) + " bases"
                if os.path.exists(destination_file + ".dna"):
                    new_file = open(destination_file + " copy number " + str(copy_number) + ".dna" , "w")
                    new_file.write(line)
                    new_file.close()
                else:
                    new_file = open(destination_file + ".dna" ,"w")
                    new_file.write(line)
                    new_file.close()
            file_number = file_number + 1

                
