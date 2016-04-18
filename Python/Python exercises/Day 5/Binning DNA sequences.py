#binning dna sequences

import os
import shutil

#list files in folder
##
##for file_name in os.listdir("E:/data files/dna_files"):
##    dna_seq = open("E:/data files/dna_files/" + file_name)
##    number = 0
##    for line in dna_seq:
##        if len(line) > 100 and len(line) < 200:
##            if number == 0:
##                number = number + 1
##                os.mkdir("E:/data files/dna_files/100 to 200")
##                new_file = open("E:/data files/dna_files/100 to 200/" + str(len(line)),"w")
##                new_file.write(line)
##                new_file.close()

            
            
    
    
##
##for file_name in os.listdir("E:/data files/dna_files"):
##    dna_seq = open("E:/data files/dna_files/" + file_name)
##    for line in dna_seq:
##        if len(line) > 100 and len(line) < 200:
##            if os.path.exists("E:/data files/dna_files/100 to 199"):
##                new_file = open("E:/data files/dna_files/100 to 199/" + str(len(line)),"w")
##                new_file.write(line)
##                new_file.close()  
##            else:
##                os.mkdir("E:/data files/dna_files/100 to 199")
##                new_file = open("E:/data files/dna_files/100 to 199/" + str(len(line)),"w")
##                new_file.write(line)
##                new_file.close()
##

for file_name in os.listdir("E:/data files/dna_files"):
    dna_seq = open("E:/data files/dna_files/" + file_name)
    for line in dna_seq:
        for number in range(100,1000,100):
            if len(line) >= number  and len(line) < number + 100:
                destination_folder = "E:/data files/dna_files/" + str(number) + " to " + str(number+99)
                if not os.path.exists(destination_folder):
                    os.mkdir(destination_folder)
                new_file = open(destination_folder +"/" + "Sequence length " + str(len(line)) + " bases.dna","w")
                new_file.write(line)
                new_file.close()  
               
                
       



##def file_creator():
##    number = 100
##    value = raw_input("Enter folder directory: \")
##    for file_name in os.listdir("E:/data files/dna_files"):
##    dna_seq = open("E:/data files/dna_files/" + file_name)
##    for line in dna_seq:
##        if len(line) > number  and len(line) < number + 100:
##            if os.path.exists("E:/data files/dna_files/"+str(number) + " to " + str(number+99)):
##                new_file = open("E:/data files/dna_files/"+str(number) + " to " + str(number+99)+"/" + str(len(line)),"w")
##                return new_file.write(line)
##                return new_file.close()  
##            else:
##                os.mkdir("E:/data files/dna_files/"+ str(number) + " to " + str(number+99))
##                new_file = open("E:/data files/dna_files/"+str(number) + " to " + str(number+99)+"/" + str(len(line)),"w")
##                return new_file.write(line)
##                return new_file.close()
##        else:
##            return number = number + 100
            
    
##
##            if len(line) > number  and len(line) < number + 100:
##                if os.path.exists("E:/data files/dna_files/"+str(number) + " to " + str(number+99)):
##                    new_file = open("E:/data files/dna_files/"+str(number) + " to " + str(number+99)+"/" + str(len(line)),"w")
##                    new_file.write(line)
##                    new_file.close()  
##                else:
##                    os.mkdir("E:/data files/dna_files/"+ str(number) + " to " + str(number+99))
##                    new_file = open("E:/data files/dna_files/"+str(number) + " to " + str(number+99)+"/" + str(len(line)),"w")
##                    new_file.write(line)
##                    new_file.close()
##            else:
##                number = number + 100
##                if len(line) > number  and len(line) < number + 100:
##                    if os.path.exists("E:/data files/dna_files/"+str(number) + " to " + str(number+99)):
##                        new_file = open("E:/data files/dna_files/"+str(number) + " to " + str(number+99)+"/" + str(len(line)),"w")
##                        new_file.write(line)
##                        new_file.close()  
##                    else:
##                        os.mkdir("E:/data files/dna_files/"+ str(number) + " to " + str(number+99))
##                        new_file = open("E:/data files/dna_files/"+str(number) + " to " + str(number+99)+"/" + str(len(line)),"w")
##                        new_file.write(line)
##                        new_file.close()
##
