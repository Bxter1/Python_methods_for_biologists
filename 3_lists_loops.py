#################### LISTS AND LOOPS #####################

# Lists denoted by square brackets
# Either "strings" or numbers 2, 5, 6

# calling on items in a list #
apes = ["homo sapiens", "organutan", "gorilla"]
print(apes[0])

# Assigning variables from a list #
second_animal = apes[2]
print(second_animal)

# Getting position from name #
gorilla_location = apes.index("gorilla")
print(gorilla_location)

# Putting a negative means python searches from the back of a list #
last_on_list = apes[-1]
print(last_on_list)

# getting multiple things from a list #
non_humans = apes[1:] # Doing [1:2] returned just orangutan
print(non_humans)

# Adding to a list
apes.append("monkeys")  #If you keep running this it will keep on adding to a list
print(apes)

# Get length of a list
print(len(apes))

# combining lists
insects = ["spider", "ladybug", "cricket"]
all_animals = apes + insects
print(all_animals)

print(str(len(all_animals)) + " alive things")  # Putting space here is needed to create space

# extend() adds a list to the end of a list whereas append() adds elements to the back of a list

# reverse() and sort() can change the order of a list

# of course can still only print strings so need print(str(VARIABLE))

ranks = ["kingdom", "phylum", "class", "order", "family"]
print(str(ranks))

ranks.reverse()
print("the ranks backwards are:", str(ranks))

#To store a reversed list in another variable rather than change the list itself it is good practice to make a copy of the list and then reverse it

original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(original_list, reversed_list)

ranks.sort()
print(ranks)


### Writing a loop ###

print(apes)

apes.append("monkey")

# If we want each line to be stated we create a loop

for apeType in apes:               # usually 'i' instead of words lin loops
    print(apeType + " is an ape")  #needed to highlight the whole thing for it to work


# loops with functions
# Figuring out name length of animal and the first letter

for apeType in apes:
    name_length = len(apeType)
    first_letter = apeType[0]
    print(apeType + " is an ape. It's name starts with a", first_letter)
    print("It's name has " + str(name_length) + " letters")

# In python we can treat characters in a string like a list where it iterates over each character
name = "ATCGCTAC"
for base in name:
        print("One base is " + base)


# Splitting a string to make a list
# It does this based on some indicator refered to as a delimiter
names = "fly,bird,duck,ferry"
species = names.split(",")
print(str(species))

# Iterating over lines of a file
# Like string characters become items in a list, each file line becomes an individual element
file = open("some_input.txt")
#for line in file:
     # Do something with the line

# This iterates over the file object, not over file contents
# To iterate over file objects see below
file1 = open("some_input.txt")
#contents = file.read()
#for line in file:
     # Lines are treated as a single character

# If you want the file contents as one big string, first read the file
# If you want line by line then it's goof to iterate over the file object as we've seen above


## Another common mistake is to iterate over the same file object twice ##
file2 = open("some_input.txt")

# print the length of each line
#for line in file:
     #print("the length is actually " + str(len(line)))

# print the first character of each line
for line in file:
     print("The first character is " + line[0])

# In this case the second for loop doesn't get executed
# This is because file objects are 'exhaustible' 
# After iterating over a file object you are at the end of the file
# You can overcome this by closing and reopening the file
# or

# Read the lines of the file into a list which we can then freely iterate over
# This is performed with the readlines() command
file = open("some_input.txt")
all_lines = file.readlines()

# Now we print the lengths
for line in all_lines:
     print("The length is " + str(len(line)))

# Now we can still print the first characters
for line in all_lines:
     print("The first character is " + line[0])


## Looping with Ranges ##
protein = "VSTLDTSLCDBSCSTYTSLCO"

# Now we want to print out increasingly long substrings starting from the 0'th position each time

# Bad solution
stop_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for stop in stop_positions:
     substring = protein[0:stop]
     print(substring)

# Better Solution - Using the built in range function
for i in range(0, len(protein)):
    print(protein[0:i])


##### EXCERCISES #####

## 1 ## remove initial 14 bp adapter sequeneces attached to each string. Then write the output to a new file

# Open input file
with open("dna_sequences/input.txt") as file_input:

# Open an output file
     with open("trimmed_dna.txt", "w") as output:

## This turned out to be unneccessary, because I can iterate over the file object directly
## I believe this turned out not to be neccessary because each dna sequence was already on a different line
#lines_in_file = file_input.readlines()
#print(lines_in_file) # Making sure I was ok up until here

# Trimming each sequence in the file
               for i in file_input:
                    trimmed_sequences = i[14:]
                    print(len(trimmed_sequences))
                    output.write(trimmed_sequences)

## This code above originally did not work until I opened files using the 'with' system. This could be for a number of reasons
#  One reason is without a file being closed properly it can lead to data not being written correctly or file locks
#  This could also be because of 'buffering' and 'flushing', data isn't immediately written to disk but kept in a buffer, this is flushed to the file when closed


### Removing multiple exons from a file ###

# Seeing first whether I'm dealing with a string or a list
with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/genomic_dna.txt") as input:

     with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as guide:
          
          with open("removed_exons.txt", "w") as output:
               print(type(input))
# I got back: "_io.TextIOWrapper" because it's a file object. 
# For a string I would have had to add a line below like "content = input.read()"
# For a list I would have added the line: "content = input.readlines()"


## My effort with a bunch of ChatGPT Help
## This didn't work because I didn't remove the newline tag in the exon file
with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/genomic_dna.txt") as input:
     dna = input.read()
     
     with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as guide:
          dividers = guide.read()
          exon_range = dividers.split(",")  # This operation returns the string to a list
          
          with open("removed_exons.txt", "w") as output:
               for i in range(0, len(exon_range), 2):
                    start = int(exon_range[i])
                    end = int(exon_range[i + 1])
                    exon_sequence = dna[start:end]
                    output.write(exon_sequence + "\n")


## Trying a fix for this
with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/genomic_dna.txt") as input:
     dna = input.read()
     
     with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as guide:
          dividers = guide.read()
          exon_range = dividers.split(",")  # This operation returns the string to a list
          # This is where the error was, splits the string at every comma not considering line breaks

          with open("removed_exons.txt", "w") as output:
               for i in range(0, len(exon_range), 2):
                    start = int(exon_range[i].strip())
                    end = int(exon_range[i + 1].strip())
                    exon_sequence = dna[start:end]
                    output.write(exon_sequence + "\n")
## After these changes I'm still seeing newline issues saying "58\n72" where these two should be on different lines


## ChatGPT fixed code considering line breaks
with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/genomic_dna.txt") as input:
     dna = input.read()
     
     with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as guide:
          for line in guide:
               start, end = line.split(',')
               start = int(start.strip())
               end = int(end.strip())

               exon_sequence = dna[start:end]
               with open("removed_exons.txt", "a") as output:
                    output.write(exon_sequence + "\n")
## I had a few fundamental mistakes in past attempts that this one fixed
## One mistake was because I opened the doc in "w" mode instead of "a", each time through the loop I wrote over what I previously wrote
## The key mistake was by splitting the doc without clarifying a start and end position it treated each element as separate rather than pairs
## Because I just opened the file it is a file object and observes each file line by line
## The split function then makes each side of a comma into it's own component which is seen as ['5' , '28']
## We also assigned known functions 'start' and 'end' to them, so start for this line is now '5' and end is now '58'
## Strip() now removes the newline function


## How the book solved this problem
exon_locations = open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt")
for line in exon_locations:
     print(line)
# Only printing the last two lines, probably just a bug but want to try opening the other way

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as exon_locations:
     for line in exon_locations:
          print(line)
# This one worked and just confirmed this buffering and flushing problem more, need to open files this way going forward

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as exon_locations:
     for line in exon_locations:
          positions = line.split(',')
          print(positions)
# By using this admitetly inefficient printing to check it at least showed me that the newline is here and causing an issue
# Breaking this up while less efficient would have saved me a lot of time

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as exon_locations:
     for line in exon_locations:
          positions = line.split(',')
          start = positions[0]
          stop = positions[1]
          print("start is " + start + " and is " + stop)
# The start and stop functions here are very similar to start and end used above, pretty key

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/genomic_dna.txt") as input:
     dna = input.read()  #By reading we now are processing the dna like a string which is okay, line by line functionality isn't needed here

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as exon_locations:
     for line in exon_locations:
          positions = line.split(',')
          start = positions[0]
          stop = positions[1]
          exon = dna[start:stop]
          print("The exon is: " + exon)
# This didn't work because of course the split function returns lists and we need intergers to find exact locations on a string

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/genomic_dna.txt") as input:
     dna = input.read()  #By reading we now are processing the dna like a string which is okay, line by line functionality isn't needed here

coding_sequence = ""

with open("c:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/lists_and_loops/exercises/exons.txt") as exon_locations:
     for line in exon_locations:
          positions = line.split(',')
          start = int(positions[0])
          stop = int(positions[1])
          exon = dna[start:stop]
          coding_sequence = coding_sequence + exon
          print("The coding sequence is: " + coding_sequence)
          
          with open("coding_sequence.txt", 'w') as output:
               output.write(coding_sequence)
# Now there's one other thing we were supposed to do which I did not in the previous attempt which is concatenate the exons together
# This is done by creating an empty variable and then adding to it in each round of the loop

print(coding_sequence)

## This monster worked, because I opened the output file in writing mode it wrote over the previous output each time around the loop
## Because each time around the loop it was just adding to the same things the final loop version is the inly one I care about