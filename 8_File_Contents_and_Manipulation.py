# TITLE: File Contents and Manipulation


# CHAPTER: Basic file manipulation



# ABILITY: rename an existing file

# requires os module

import os
os.rename("dna_sequences/old.txt", "dna_sequences/new.txt")

# This doesn't immediately work because
# this file is in a subfolder in the working directory

print(os.getcwd())

# this didn't work originally because I was working on files individually
# rather should be loading the folder as a workspace in VSCode
# as a result the default working directory was the app data download file


# ABILITY: Moving a file
# keep the same name but give a different directory path to move the file
# works on folders as well


# ABILITY: move and rename a file
# give a new filepath and rename at the same time


# NON-ABILITY: Moving a file while creating a director
# must create a new file first

os.mkdir("/Users/Brian/Desktop/RNA_seq_21")


# ABILITY: make multiple directories at once

os.makedirs("/Users/Brian/Desktop/RNA_seq_21/sequences/sample1")
# This will create the directories for RNA_seq_21, sequences, and sample1


# ABILITY: Make multiple subfolders at once using a FOR loop

import os

# Path to the main directory
base_path = "/Users/Brian/Desktop/RNA_seq_21/sequences"

# List of subdirectories to create under "sequences"
subdirectories = ["sample1", "sample2", "sample3", "experiment1", "experiment2"]

# Loop through the list and create each subdirectory
for subdirectory in subdirectories:
    os.makedirs(os.path.join(base_path, subdirectory), exist_ok=True)

print("All subdirectories created!")


# ABILITY: Copying a file
# do this with the shutil module

os.mkdir("/Users/Brian/Desktop/RNA_seq_21/sequences/copies")

import shutil
shutil.copy("/Users/Brian/Desktop/RNA_seq_21/sequences/sample1/sequence1.txt", "/Users/Brian/Desktop/RNA_seq_21/sequences/copies/sequence1_copy.txt")


# ABILITY: Copying a folder

shutil.copytree("/Users/Brian/Desktop/RNA_seq_21", "/Users/Brian/Desktop/RNA_seq_21_copy")


# Ability: Test whether a path exists

if os.path.exists("/Users/Brian/Desktop/RNA_seq_21/sequences/copies/sequence1_copy.txt"):
    print("The path exists")
else:
    print("The path does not exist")


# ABILITY: Deleting a single file

os.remove("/Users/Brian/Desktop/RNA_seq_21/sequences/copies/sequence1_copy.txt")


# ABILITY: Removing an empty folder

os.rmdir("/Users/Brian/Desktop/RNA_seq_21/sequences/sample2")


# ABILITY: Removing a directory and all of its files

shutil.rmtree("/Users/Brian/Desktop/RNA_seq_21")

shutil.rmtree("/Users/Brian/Desktop/RNA_seq_21_copy")


# ABILITY: Listing folder contents

for file_name in os.listdir("/Users/Brian/Desktop/RNA_seq_21_copy"):
    print("The file name is " + file_name)

for file_name in os.listdir("/Users/Brian/Desktop/RNA_seq_21_copy/sequences"):
    print("The file name is " + file_name)



# CHAPTER: Running external programs



# running a program is called a process
# running a program from another program is called a subprocess

import subprocess
subprocess.call("date /T", shell=True) # This didn't work

# going to try the preferred subprocess.run which is more modern

result = subprocess.run("date /T", shell=True, text=True, capture_output=True)
print(result.stdout) # This didn't work too

# troubleshooting now
# Ran in command line "date /T" and got the correct output
# Now trying a different subprocess to see if the subprocess works

import subprocess

result = subprocess.run("echo Hello", shell=True, text=True, capture_output=True)
print(result.stdout) # This didn't work too meaning there's something wrong with the subprocess

# Tried running vsCode as administrator to see if the issue was with permissions however it still didn't work
# Now updated python to most recent version but this isn't helping either
# I noticed things that previously worked then started not working like Import subprocess and then import os
# I restarted the vscode software and now suddenly its working


# ABILITY: Running a program and capturing the output

current_date = subprocess.run("date /T", shell=True, text=True, capture_output=True)
print(current_date.stdout)

# Subprocess.run appears to work a lot better than subprocess.call
# only use subprocess.run going forward


# ABILITY: Have user input rather than hard-coding data directly into the code

# The 'raw input' function is built for this function in python
# This is just input() for python 3

accession = input(" Enter an accession number name")

# The user input will always be returned as a string, might need to convert it
# User input ends with a newline so we might need to end it with a .rstrip()

# CAUTION
# If a long running program make sure:
# A. It is obvious to the user that they must enter input so they notice it and the program doesn't freeze unknowingly
# B. Make the data entry upfront so the program doesn't freeze waiting for user input

# CAUTION
# Input validation is also very important. eg. no ambiguous DNA bases entered, no non-numeric characters entered, name of a file must exist
# Do input validation immediately

answer = 0
while answer < 1 or answer > 10:
    try:
        answer = int(input("Enter a number between 1 and 10\n"))
    except ValueError:
        print("Please enter a valid integer")
        answer = 0  # reset the value and restart the loop

print("Final answer is " + str(answer))

# This code kept on running indefinitely

print(answer)

# This showed that the loop didn't reset and that the answer didn't reset to 0

answer = 0
while answer < 1 or answer > 10:
    try:
        answer = int(input("Enter a number between 1 and 10\n"))
    except ValueError:
        print("Please enter a valid integer")
        answer = 0  # reset the value and restart the loop
        continue

print("Final answer is " + str(answer))

# This works except that it only prints "please enter a valid integer after a correct integer is entered"
# Also gives "please enter a valid integer regardless of wrong input or a number out of range"

answer = 0
while answer < 1 or answer > 10:
    try:
        answer = int(input("Enter a number between 1 and 10\n"))
        if answer < 1 or answer > 10:
            print("please enter a number between 1 and 10")
    except ValueError:
        print("Please enter a valid integer")
        answer = 0  # reset the value and restart the loop
        continue

print("Final answer is " + str(answer))

# This now gives "please enter a valid integer" when entering a string or letter
# It now gives " Please enter a number between 1 and 10" when giving a value outside of the range
# However it still only prints these messages once a good answer is given

answer = None
while answer is None or answer < 1 or answer > 10:
    try:
        # prompt for user input
        answer = int(input("Enter a number between 1 and 10\n"))

        # Verifying right range of user input
        if answer < 1 or answer > 10:
            print("please enter a number between 1 and 10")
            answer = None

    except ValueError:
        # Checking for non-integer input
        print("Please enter a valid integer", flush=True)
        answer = None  # reset the value and restart the loop
        continue

print("Final answer is " + str(answer))

# switching to 'None' and trying flush did not help print error messages
# Now going to try a variation of the flush method

import sys
answer = None
while answer is None or answer < 1 or answer > 10:
    try:
        # prompt for user input
        answer = int(input("Enter a number between 1 and 10\n"))

        # Verifying right range of user input
        if answer < 1 or answer > 10:
            print("please enter a number between 1 and 10")
            sys.stdout.flush()
            answer = None

    except ValueError:
        # Checking for non-integer input
        print("Please enter a valid integer", flush=True)
        sys.stdout.flush()
        answer = None  # reset the value and restart the loop
        continue

print("Final answer is " + str(answer))

# Once again this did not work
# Might be how the terminal python REPL is buffering the output
# Going to save as a function in another file and try running in terminal

import sys

def Number_checker():

    answer = None
    while answer is None or answer < 1 or answer > 10:
        try:
            # prompt for user input
            answer = int(input("Enter a number between 1 and 10\n"))

        except ValueError:
            # Checking for non-integer input
            print("Please enter a valid integer", flush=True)
            sys.stdout.flush()
            continue

         # Verifying right range of user input
        if answer < 1 or answer > 10:
            print("please enter a number between 1 and 10")
            sys.stdout.flush()
            answer = None
            continue


    print("Final answer is " + str(answer))


if __name__ == "__main__":
    Number_checker()


# Made the number checker a function and ran in terminal
# This worked however gave both error messages each time
# This did not happen when running in vscode

# THING: command line arguments

# strings type in command line after the name of the program file
# These are inputs for the program
# "python myprogram.py one two three "
# one two and three are command line options
# to use command line arguments we import the sys module
# then use sys.argv to access the command line arguments


import sys
print(sys.argv) # lists program name and inputs

# Like input() sys.argv is a list of strings
# Might need to use int() if we want to use command line arguments as a number





# EXCERCISES!!!!!!!!!!!!!!!



# EXERCISE 1 - BINNING DNA SEQUENCES


# Objective: Create a program that:
    # Creates 9 new folders
    # 1 for sequences 100-199 bases long
    # 1 for sequences 200-299 bases long and so on..
    # Write out each DNA sequence in the input files to a seperate file in right folder

# Requirements:
    # Iterate over files in the folder
    # iterate over lines in each file
    # figure out which bin each DNA sequence should go in based on length
    # write outeach DNA sequence to new file in right folder



# MY_ATTEMPT

import os

os.mkdir("/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/8_dna_binning_exercise")

base_path = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/8_dna_binning_exercise"

subdirectories = ["100-199", "200-299", "300-399", "400-499", "500-599", "600-699", "700-799", "800-899", "900-999"]

for subdirectory in subdirectories:
    os.makedirs(os.path.join(base_path, subdirectory), exist_ok=True)

print("All subdirectories created!")


# deleting folder I made with an outdated naming convention

import shutil
shutil.rmtree("/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise")

def DNA_creator(dna_name, length):
    bases = ['A', 'T', 'C', 'G']
    dna_sequence = ""

    for base in bases in range(0, length, 1):
        dna.append(base)
        chain_length = len(dna)

        if chain_length > 99 and chain_length < 200:
            dna = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise/100-199"
        elif chain_length > 199 and chain_length <300:
            dna = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise/200-299"
        elif chain_length > 299 and chain_length <400:
            dna = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise/300-399"
        elif chain_length > 399 and chain_length <500:
            dna = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise/400-499"

# the file creation steps are well made
# It's wrong that I combined bases and range
# better -> for i in range(length):
# then -> dna_sequence += bases[i % len(bases)]
# The function is wrong because dna_name is not defined
# The function is also wrong because the dna.append is not appending to a growing chain but rewriting over the chain

# second attempt

def DNA_creator(dna_name, length):
    bases = ['A', 'T', 'C', 'G']
    dna_sequence = ""

    for i in range(length):
        dna_sequence += bases[i % len(bases)] # could also write 'i % 4', ensures cycle through bases

# '+=' is an operator function for adding a value to a variable and then assigning the result back to the variable
# it is known as teh addition assignment operator

    if 100 <= length < 200:
        folder = "100-199"
    elif 200 <= length < 300:
        folder = "200-299"
    elif 300 <= length < 400:
        folder = "300-399"
    elif 400 <= length < 500:
        folder = "400-499"
    elif 500 <= length < 600:
        folder = "500-599"
    elif 600 <= length < 700:
        folder = "600-699"
    elif 700 <= length < 800:
        folder = "700-799"
    elif 800 <= length < 900:
        folder = "800-899"
    elif 900 <= length < 1000:
        folder = "900-999"
    else:
        raise ValueError("DNA length must be between 100 and 1000 bases")

    # Save DNA sequence to the correct folder
    output_path = os.path.join(base_path, folder, f"{dna_name}.txt")
    with open(output_path, "w") as file:
        file.write(dna_sequence)


DNA_creator("short_sequence", 125)

# This works
# For a function make sure whatever I put after the definition are defined and used below
# For files again remember to open them as a writing file and then write in a seperate line


# we might also want the dna we create to be random
# similar to real life rather than ATCG in repition
# can use a random generator for this

import os
import random

def random_DNA_creator(dna_name, length):
    bases = ['A', 'T', 'C', 'G']

    dna_sequence = "".join(random.choices(bases, k=length))

# '+=' is an operator function for adding a value to a variable and then assigning the result back to the variable
# it is known as the addition assignment operator

    if 100 <= length < 200:
        folder = "100-199"
    elif 200 <= length < 300:
        folder = "200-299"
    elif 300 <= length < 400:
        folder = "300-399"
    elif 400 <= length < 500:
        folder = "400-499"
    elif 500 <= length < 600:
        folder = "500-599"
    elif 600 <= length < 700:
        folder = "600-699"
    elif 700 <= length < 800:
        folder = "700-799"
    elif 800 <= length < 900:
        folder = "800-899"
    elif 900 <= length < 1000:
        folder = "900-999"
    else:
        raise ValueError("DNA length must be between 100 and 1000 bases")

    # Save DNA sequence to the correct folder
    output_path = os.path.join(base_path, folder, f"{dna_name}.txt")
    with open(output_path, "w") as file:
        file.write(dna_sequence)


random_DNA_creator("2nd_short_sequence", 250)




# Now the books solution to this problem


# looks like I misunderstood the assignment
# There were given dna sequences which I needed to determine the lengths of
# After which I was then supposed to place them into the files I created
# I will now try and complete this task on my own



# plan

# As step 1: I will find out the names of the files in the folder
# Step 2: create a loop which will go through files, open them in read mode and determine their length
# step 3: create new files directories which I want the files to go to
# step 4: copy the files to the new directories based on their length





# As step 1 I will find out the names of the files in the folder
import os

os.listdir(r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises")

# This worked, I can now loop over the files in the folder
# however there are two python files which are not ones I want to include, the rest are dna sequences


# as step 2 I will create a loop which will go through files, open them in read mode and determine their length

for file in os.listdir(r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"):
    if file.endswith(".dna"):
        with open(file, "r") as f:  # This method automatically closes the file after use
            sequence = f.read()
            length = len(sequence)
            print(f"The length of {file} is {length} bases.") # This did not work!!!!

# It didn't work because list directory lists the files in the folders but does not make it the current working directory
# with open(file, "r") as f: reads from the current working directory

folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"

for file in os.listdir(folder):
    if file.endswith(".dna"):
        full_path = os.path.join(folder, file)
        with open(full_path, "r") as f:
            sequence = f.read()
            length = len(sequence)
            print(f"the length of {file} is {length} bases.")

# This worked!


# As step 3 I will create the folders

import os

os.mkdir("/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise")

base_path = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"

subdirectories = ["100-199", "200-299", "300-399", "400-499", "500-599", "600-699", "700-799", "800-899", "900-999"]

for subdirectory in subdirectories:
    os.makedirs(os.path.join(base_path, subdirectory), exist_ok=True)


# As step 4 I will copy the files to the new directories based on their length

import shutil

source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"

for file in os.listdir(source_folder):
    if file.endswith(".dna"):
        full_path = os.path.join(source_folder, file)
        with open(full_path, "r") as f:
            sequence = f.read()
            length = len(sequence)
            if 100 <= length < 999:
                shutil.copy(full_path, os.path.join(destination_folder, "100-199"))
            elif 1000 <= length < 1999:
                shutil.copy(full_path, os.path.join(destination_folder, "200-299"))
            elif 2000 <= length < 2999:
                shutil.copy(full_path, os.path.join(destination_folder, "300-399"))
            elif 3000 <= length < 3999:
                shutil.copy(full_path, os.path.join(destination_folder, "400-499"))
            elif 4000 <= length < 4999:
                shutil.copy(full_path, os.path.join(destination_folder, "500-599"))
            elif 5000 <= length < 5999:
                shutil.copy(full_path, os.path.join(destination_folder, "600-699"))
            elif 6000 <= length < 6999:
                shutil.copy(full_path, os.path.join(destination_folder, "700-799"))
            elif 7000 <= length < 7999:
                shutil.copy(full_path, os.path.join(destination_folder, "800-899"))
            elif 8000 <= length < 8999:
                shutil.copy(full_path, os.path.join(destination_folder, "900-999"))

# This worked!
# Files had a lot more characters than I expected so changed by a factor of 10
# The files are also shifted by one row but that's fine for the example
# A print statement after each saying how long the file is would have been nice

# Implementing now with print statements

import shutil

source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"

for file in os.listdir(source_folder):
    if file.endswith(".dna"):
        full_path = os.path.join(source_folder, file)
        with open(full_path, "r") as f:
            sequence = f.read()
            length = len(sequence)
            print(f"The length of {file} is {length} bases.")
            if 100 <= length < 999:
                shutil.copy(full_path, os.path.join(destination_folder, "100-199"))
            elif 1000 <= length < 1999:
                shutil.copy(full_path, os.path.join(destination_folder, "200-299"))
            elif 2000 <= length < 2999:
                shutil.copy(full_path, os.path.join(destination_folder, "300-399"))
            elif 3000 <= length < 3999:
                shutil.copy(full_path, os.path.join(destination_folder, "400-499"))
            elif 4000 <= length < 4999:
                shutil.copy(full_path, os.path.join(destination_folder, "500-599"))
            elif 5000 <= length < 5999:
                shutil.copy(full_path, os.path.join(destination_folder, "600-699"))
            elif 6000 <= length < 6999:
                shutil.copy(full_path, os.path.join(destination_folder, "700-799"))
            elif 7000 <= length < 7999:
                shutil.copy(full_path, os.path.join(destination_folder, "800-899"))



# While this worked *******

# We may have been including new line characters
# As well there were different sequences in each dna file which my method did not differentiate
# It treated each dna file as one sequence
# Here is the solution offered by the book

import os

source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"

for file_name in os.listdir(source_folder):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        full_path = os.path.join(source_folder, file_name)
        dna_file = open(full_path)

        # Look at each line
        for line in dna_file:
            dna = line.rstrip("\n")
            length = len(dna)
            print("found a dna sequence with a length of " + str(length))

        # This now lists each file and says how long each sequence is within each file
        # go through each bin and check if the sequence belongs in it

            for bin_lower in range(100, 1000, 100):
                bin_upper = bin_lower + 99
                if length >= bin_lower and length <= bin_upper:
                    print("bin is " + str(bin_lower) + " to " + str(bin_upper))


# Now that this works and lists which bin each dna fragment belongs to let's now create functions to clean the code


source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"


def process_sequence(line):
    dna = line.rstrip("\n")
    length = len(dna)
    print("sequence length is " + str(length))
    for bin_lower in range(100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length < bin_upper:
            print("bin is " + str(bin_lower) + " to " + str(bin_upper))

for file_name in os.listdir(source_folder):
    if file_name.endswith(".dna"):
        print("reading sequence from " + file_name)
        dna_file = open(file_name)
        for line in dna_file:
            process_sequence(line) # A recursive function!

# Now we create folders to add them too using our bin function

for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
    bin_folder_path = os.path.join(destination_folder, bin_folder_name)
    os.mkdir(bin_folder_name)

# This works out the folder naming scheme
# DNA file naming is not specified so we can name 1.dna, 2.dna and so on
# We need to create an extra variable to hold the number of dna sequences we've seen and
# increment after writing each dna sequence


# All together now

source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"


# Creating folders for each bin to go into

for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
    bin_folder_path = os.path.join(destination_folder, bin_folder_name)
    os.mkdir(bin_folder_path)


# A function to process each sequence
# This function analyses the length of the sequence and then writes it to the correct folder
# This top portion of the function describes where the function is written to
# I am creating one file per line of each .dna file
def process_sequence(line):
    dna = line.rstrip("\n")
    length = len(dna)
    print("sequence length is " + str(length))
    for bin_lower in range(100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length < bin_upper:
            print("bin is " + str(bin_lower) + " to " + str(bin_upper))
            bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
            bin_folder_path = os.path.join(destination_folder, bin_folder_name)
            output_path = bin_folder_path + '/' + str(seq_number) + '.dna'

            output = open(output_path, "w")
            output.write(dna)
            output.close()

# This bottom portion directs where the contents are taken from

seq_number = 1
for file_name in os.listdir(source_folder):
    if file_name.endswith(".dna"):
        print("reading sequence from " + file_name)
        full_path = os.path.join(source_folder, file_name)
        dna_file = open(full_path)
        for line in dna_file:
            process_sequence(line)
            seq_number = seq_number + 1

# This works!!



# EXERCISE 2  !!!!!!!!!!!!!!!!!!

# Kmer Counting

# Write a program which will calculate the amount of Kmers of a given length across all dna sequences in the input files
# Display only the ones that appear more than a given amount of times
# should take two arguments
# The Kmer length and the cut-off value


# Plan

# 1: Read the files out line by line
# 2: For each string break it into kmers of a given length
# 3: Search through the kmers and count them
# 4: Print the kmers that appear more than a given amount of times


# part 1: reading the files line by line and using the function "kmer_analyser" on each line

source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/kmer_exercise"

for file_name in os.listdir(source_folder):
    if file_name.endswith(".dna"):
        print("reading sequence from " + file_name)
        full_path = os.path.join(source_folder, file_name)
        dna_file = open(full_path)
        for line in dna_file:
            kmer_analyser(line)


# part 2: kmer_analyser function

def kmer_analyser(line, length):
    dna_file = line.rstrip("\n")
    kmer_list = []
    for i in range(len(dna_file) - length + 1):
        kmer = dna_file[i:i+length]
        kmer_list.append(kmer)
    kmer_counter = Counter(kmer_list)
    print(kmer_counter.most_common(10))


# The solution to the exercise

# It starts with a test sequence of DNA before looking through the files
# This is a good practice to start simple first

test_dna = "ACTGTAGCTGTACGTAGC"
print(test_dna)
kmer_size = 4
for start in range(0,len(test_dna) - kmer_size + 1,1):
    kmer = test_dna[start:start+kmer_size]
    print(kmer)

# With this range function we go though the dna increasing by 1 each time
# We also stop at the length with 1 kmer left rather than finishing with 3mers or less

# Turning it into a function

def kmer_analyser(given_dna, kmer_size):
    kmers = []
    for start in range(0, len(given_dna) - kmer_size + 1,1):
        kmer = given_dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

given_dna = "ACTGTAGCTGTACGTAGC"

kmer_analyser(given_dna, 4)
kmer_analyser(given_dna, 7)
kmer_analyser(given_dna, 2)


# Now combine with the looping through files
# We will create an empty dict
# Each kmer we find we will look up the current count for it in the dict
# If not in the dict, we say the current count is 0, add to the count, then store back in the dict


import os
kmer_size = 6
source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/kmer_exercise"



def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0, len(given_dna) - kmer_size + 1,1):
        kmer = given_dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

kmer_counts = {}
for file_name in os.listdir(source_folder):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        full_path = os.path.join(source_folder, file_name)
        dna_file = open(full_path)
        for line in dna_file:
            dna = line.rstrip("\n")
            for kmer in split_dna(dna, kmer_size):
                current_count = kmer_counts.get(kmer, 0)
                new_count = current_count + 1
                kmer_counts[kmer] = new_count

print(kmer_counts)

# This is just printing 100 for each which should not be the case

import os
kmer_size = 6
source_folder = r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises"
destination_folder = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/kmer_exercise"



def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0, len(given_dna) - kmer_size + 1,1):
        kmer = given_dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

kmer_counts = {}
for file_name in os.listdir(source_folder):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        full_path = os.path.join(source_folder, file_name)
        with open(full_path, 'r') as dna_file:
            line_number = 0
            for line in dna_file:
                line_number += 1
                print(f"File: {file_name}, Line: {line_number}")
                dna = line.rstrip("\n")
                for kmer in split_dna(dna, kmer_size):
                    current_count = kmer_counts.get(kmer, 0)
                    new_count = current_count + 1
                    kmer_counts[kmer] = new_count

print(kmer_counts)








