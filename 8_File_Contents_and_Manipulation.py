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


# ABILITY: Deleting a single file

os.remove("/Users/Brian/Desktop/RNA_seq_21/sequences/copies/sequence1_copy.txt")


# ABILITY: Removing an empty folder

os.rmdir("/Users/Brian/Desktop/RNA_seq_21/sequences/sample2")


# ABILITY: Removing a directory and all of its files

shutil.rmtree("/Users/Brian/Desktop/RNA_seq_21")


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

os.mkdir("/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise")

base_path = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"

subdirectories = ["100-199", "200-299", "300-399", "400-499", "500-599", "600-699", "700-799", "800-899", "900-999"]

for subdirectory in subdirectories:
    os.makedirs(os.path.join(base_path, subdirectory), exist_ok=True)

print("All subdirectories created!")


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

os.listdir(r"C:\Users\Brian\Documents\Bioinformatics_general\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\working_with_the_filesystem\exercises")

# This worked, I can now loop over the files in the folder
# however there are two python files which are not ones I want to include, the rest are dna sequences


# as step 2 I will create a loop which will go through files, open them in read mode and determine their length





# As step 3 I will create the folders

import os

os.mkdir("/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise")

base_path = "/Users/Brian/Documents/Bioinformatics_general/Python_for_biologists/dna_binning_exercise"

subdirectories = ["100-199", "200-299", "300-399", "400-499", "500-599", "600-699", "700-799", "800-899", "900-999"]

for subdirectory in subdirectories:
    os.makedirs(os.path.join(base_path, subdirectory), exist_ok=True)


# As step 4 I will copy the files to the new directories based on their length

