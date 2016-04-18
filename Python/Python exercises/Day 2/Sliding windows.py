# create file
genomic_dna= open("E:\data files\genomic_dna2.txt","r").read()

#number
number = 0

#create new document
sliding_windows = open("sliding_windows.txt","w")

#create sliding window

for bases in genomic_dna:
    number = number + 1
    window = genomic_dna[number:number+4]
    A_content = window.count("A")
    T_content = window.count("T")
    AT_percentage = ((A_content + T_content)/0.04)
    message = (window + "(" + str(AT_percentage) + "%)")
    print(message)
    sliding_windows.write(message + "\n")

#close document
sliding_windows.close()

    
    

