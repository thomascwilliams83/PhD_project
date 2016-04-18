#Day 5 notes

#os functions to work with operating system

#at start of file import os

#examples:
os.rename("old.txt","new.txt")

#moving a file is the same as renaming them

os.rename("biology/old.txt","python/old.txt"

#to created new folder - make directory
os.mkdir("C:/user/documents/python")

#copying and trees

#for this use shutil (shell utilities) module

#Copying is different for a file:
shutil.copy("original.txt","copy.txt"

#than for a folder:
shutil.copytree("original_folder","copy_folder"

#deleting files:
#Deleting a file:

os.remove("c:/martin/unwanted_file.txt")


#Deleting an empty folder:

os.rmdir("c:/martin/emtpy")


#Deleting a folder and all its contents:

shutil.rmtree("c:/martin/full")

#to list files and folders in the current working directory
for file_name in os.listdir("."):
    print("one file name is " + file_name
                
#to list them in a different directory
for file_name in os.listdir("E:/Python exercises/Day 1"):
    print("one file name is " + file_name

#using Python to run external program, eg analysis tool such as BLAST

#to run a program and display the output on the screen

import subprocess


# run a program with some options
subprocess.call("/bin/date +%B", shell=True)


#To run a program and capture the output in a string, use check_output:

cmd = "/bin/date +%B"
month = subprocess.check_output(cmd, shell=True)

# To get command line input
# e.g. python myscript apple banana
import sys
first = sys.argv[1] #apple
second = sys.argv[2] #banana


#Biopython

#Collection of related modules for working with biological data

from Bio.seq import Seq
