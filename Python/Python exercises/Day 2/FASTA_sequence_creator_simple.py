#FASTA sequence creator simple version

#create headers
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

#create sequences
sequence_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence_2_raw = "actgatcgacgatcgatcgatcacgact"
sequence_2 = sequence_2_raw.upper()
sequence_3_raw = "ACTGAC-ACTGT--ACTGTA----CATGTG"
sequence_3 = sequence_3_raw.replace("-","")

#create single FASTA file
FASTA_file_data = (">" + header_1 + "\n" + sequence_1 + "\n" + ">" + header_2 + "\n" + sequence_2 + "\n" + ">" + header_3 + "\n" + sequence_3)

#write file in .txt
FASTA_sequence = open("Fasta_sequence.txt","w")
FASTA_sequence.write(FASTA_file_data)
FASTA_sequence.close()

#write file in .fasta
FASTA_sequence = open("Fasta_sequence.fasta","w")
FASTA_sequence.write(FASTA_file_data)
FASTA_sequence.close()

#Create individual FASTA files
FASTA_file_data1 = (">" + header_1 + "\n" + sequence_1)
FASTA_file_data2 = ( ">" + header_2 + "\n" + sequence_2)
FASTA_file_data3 = (">" + header_3 + "\n" + sequence_3)


#write three files #1
FASTA_sequence1 = open("ABC123.fasta","w")
FASTA_sequence1.write(FASTA_file_data1)
FASTA_sequence1.close()

#write three files #2
FASTA_sequence2 = open("DEF456.fasta","w")
FASTA_sequence2.write(FASTA_file_data2)
FASTA_sequence2.close()

#write three files #3
FASTA_sequence3 = open("HIJ789.fasta","w")
FASTA_sequence3.write(FASTA_file_data3)
FASTA_sequence3.close()


 
