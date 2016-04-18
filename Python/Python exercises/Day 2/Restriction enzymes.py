###select file
##fragment_DNA = open("fragment of DNA.txt").read()
##
###define sequence to find
##restriction_seq = "GAATTC"
##
###find position
##position = fragment_DNA.find(restriction_seq,)
##
##last_position = 0
##number = 0
##
##for i in range(fragment_DNA.count(restriction_seq)):
##    position = fragment_DNA.find(restriction_seq,last_position)
##    number = number + 1
##    print ("The length of fragment " + str(number) + " is " +str(position - last_position)+ " bases")
##    last_position= position + 1
##    
##print("The length of fragment " + str(number) + " is " + str(len(fragment_DNA)-last_position) + " bases")


#select file
fragment_DNA = open("E:\data files\ce1.txt").read()

#define sequence to find
restriction_seq = "GAATTC"

#find position
position = fragment_DNA.find(restriction_seq,)

#open new file
c_elegans = open("c_elegans.txt","w")

last_position = 0
number = 0


for i in range(fragment_DNA.count(restriction_seq)):
    position = fragment_DNA.find(restriction_seq,last_position)
    number = number + 1
    statement = ("The length of fragment " + str(number) + " is " +str(position - last_position)+ " bases")
    c_elegans.write(statement + "\n")
    print (statement)
    last_position= position + 1
    
    
print("The length of fragment " + str(number) + " is " + str(len(fragment_DNA)-last_position) + " bases")
