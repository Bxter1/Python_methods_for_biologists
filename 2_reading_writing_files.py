### Opening Files of DNA ###
dna_file = open("dna.txt")  #can sometimes want to store the file in a string before 'opening' it as an object under a name
dna = dna_file.read()


#The file, open on the file, and read on the file are 3 different things

### counting the length of the DNA from the file directly ###

dna_length = len(dna)

print("my dna is " +  dna + "with a length of " +  str(dna_length))

### Removing the newline characteristic ###

dna_cleaned = dna.rstrip("\n")
dna_length = len(dna_cleaned)
print("my dna is " +  dna_cleaned + "with a length of " +  str(dna_length))

# Or

DNA = dna_file.read().rstrip("\n")


### Missing Files ###
myfile = open("non_existant.txt")

### Closing the File ###
dna_file.close()


### Writing text to files ###
my_file = open("out.txt", "w")
my_file.write("Hello World")
file = open("out.txt")
file_read = file.read()
print(file_read)


# Another writing example #
 
my_file.write("abc" + "def")  #write abcdef
file2 = open(my_file) 
print(file2)
my_file.write(str(len('AGTGCTAG')))  #write "8"
my_file.write("ATGC".replace('A', 'T')) #write "TTGC"
my_file.write("ATGC".lower())  #write atgc

# It is good practice to close files after writing to them for ressource management
# Then Open the file under reading
# read it under a different vairable name
# close the reading file and then print under the variable

my_file.close()


### Paths and Folders ###
my_file_3 = open("C:\\Users\\Brian\\Documents\\Python_for_Biologists_files_all\\p4b_exercises\\exercises_and_examples\\reading_files\\examples\\out_2.txt")


# had an escape error because it viewed one of the backslashes as an escape function
# using two backslashes solved this 
# also could have put an 'r' infront of the quotations or used front slashes. Actually this didn't seem to work the first time



############################### Excercises ###############################

### Spliting Genomic DNA Into Two Files Is the Goal ###
genomic_dna_file = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/reading_files/exercises/genomic_dna.txt", "r")
genomic_dna_file_cleaned = genomic_dna_file.read().rstrip("\n")
print(genomic_dna_file_cleaned)

dna_length = len(genomic_dna_file_cleaned)
print(str(dna_length))  #After this I opened the file and turns out there's nothing in it. I might have written over it? Now fixed it

exon_1 = genomic_dna_file_cleaned[0:30]
intron_1 = genomic_dna_file_cleaned[30:100]
exon_2 = genomic_dna_file_cleaned[100:]

print(str(len(exon_1)))  #checking if I did the brackets right for 1-30, I didn't originally but now its good
print(str(len(intron_1)))
print(str(len(exon_2)))

exons = exon_1 + exon_2

new_file_exons = open("exons.txt", "w")
new_file_exons.write(exons)
new_file_exons.close()

reading_exons = open("exons.txt")
see_exons = reading_exons.read()
print(see_exons)

new_file_introns = open("introns.txt", "w")
new_file_introns.write(intron_1)
new_file_introns.close()

introns_open = open("introns.txt")
see_introns = introns_open.read()
print(see_introns)


### Same thing as above but more concise without the checking of each step ###

# open the file and read its contents
dna_file = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/reading_files/exercises/genomic_dna.txt")
my_dna = dna_file.read()

# extract the different bits of DNA sequence
exon1 = my_dna[0:63]
intron = my_dna[63:90]
exon2 = my_dna[90:]

# open the two output files
coding_file = open("coding_dna.txt", "w")
noncoding_file = open("noncoding_dna.txt", "w")

# write the sequences to the output files
coding_file.write(exon1 + exon2)
noncoding_file.write(intron)


### Writing a FASTA File ###

# One file, 3 sequences with three headers
abc_sequence = "ATCGCTAGCTAGCTAGCTAGCTTCGCTAGGCGATCG"
def_sequence = "atcgctagctatatagcccgatatagcgctagctag"
hij_sequence = "ATCGATCH--ATCGCTAGC-ATCCGCTAG----CATCGTAG"

ABC123 = abc_sequence
DEF456 = def_sequence.upper()
HIJ789 = hij_sequence.replace("-","" )

# checking if it worked
print(str(DEF456))
print(str(HIJ789))  #it worked

# creating the FASTA file
fasta_1 = open("fasta.txt", "w+")
fasta_1.write(ABC123 + DEF456 + HIJ789)
fasta_1.seek(0)
fasta_see = fasta_1.read()
print(str(fasta_see))     # This succeeded at combining everything into one file but that wasn't the goal

# Write the headers
header_1 = "abc123" 
header_2 = "def456" 
header_3 = "hij789" 

# Adding a 'new line' 
print('>' + header_1 + '\n' + ABC123)  #worked nice

# Adding it all together
print('>' + header_1 + '\n' + ABC123 + '\n' + '>' + header_2 + '\n' + DEF456 + '\n' + '>' + header_3 + '\n' + HIJ789)  #Success now turn this into a file

combined_fasta = open("Combined_Sequences", "w+")
combined_fasta.write('>' + header_1 + '\n' + ABC123 + '\n' + '>' + header_2 + '\n' + DEF456 + '\n' + '>' + header_3 + '\n' + HIJ789)  #Could have written these in 3 lines too for code clarity
combined_fasta.close()

combined_fasta_see = open("Combined_Sequences", "r")
see_sequences = combined_fasta_see.read()
print(see_sequences)   #BIG SUCCESS#


### Writing multiple FASTA Files ###

ABC123_create = open("ABC123", "w")
ABC123_create.write('>' + "ABC123" + "\n" + ABC123)
ABC123_create.close()

DEF456_create = open("DEF456", "w")
DEF456_create.write('>' + "DEF456" + "\n" + DEF456)
DEF456_create.close()

HIJ789_create = open("HIJ789", "w")
HIJ789_create.write('>' + "HIJ789" + "\n" + HIJ789)
HIJ789_create.close()

# An alternative way is to use our header variable as the name
# ABC_create = open(header_1 + ".fasta", "w")




