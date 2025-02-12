####################  Writing Functions  ####################

## Abstracting code blocks into a 'function'

# Before making a function define the inputs and outputs
# Creating an DNA AT_Calculator function
# Input is DNA output is a decimal
# In python terms input is string and output is type 'number'

# Creating the code that will fit into the A_T_Calculator

dna_input = "ATCGTAGCTAGCTAGCGTAGCGATGCGGCTAFCGCTAGCGGCGCTACGTA"

def get_at_content(dna_input):
    dna_input = dna_input.upper()
    dna_length = len(str(dna_input))
    a_counter = dna_input.count('A')
    t_counter = dna_input.count('T')
    a_t_percent = (a_counter + t_counter) / len(dna_input)
    return(a_t_percent)

dna_2 = "ATTCGGGTCGGCTAGCGATGCTACTAGCGCTGCATCGCGTCG"

# Testing the function
get_at_content(dna_2)

# To keep the answer from the function we need to store the result of the function in a variable
ecoli_promoter_a15_ATpercent = get_at_content(dna_2)
print(ecoli_promoter_a15_ATpercent)

## Note: variable defined inside the function are not recognized outside of the function. Like a_counter doesn't exist ##

## If two many decimals are produced python has a .round() function which takes two inputs, number to round and sig figs
def get_at_content(dna_input):
    dna_input = dna_input.upper()
    dna_length = len(str(dna_input))
    a_counter = dna_input.count('A')
    t_counter = dna_input.count('T')
    a_t_percent = (a_counter + t_counter) / len(dna_input)
    return round(a_t_percent, 2)

## We can add another variable if we like
## We might want the amount of sig figs to change depending on input
def get_at_content(dna_input, sig_figs):
    dna_input = dna_input.upper()
    dna_length = len(str(dna_input))
    a_counter = dna_input.count('A')
    t_counter = dna_input.count('T')
    a_t_percent = (a_counter + t_counter) / len(dna_input)
    return round(a_t_percent, sig_figs)

## In this case we don't need to define sig figs
## This is because the round() function takes two arguments, we're pretty much saying in our function we made we'll tell you each time how man sig_figs we want
## It's only like this because we applied the 'round' function at the return stage, so it's constant or we define as we go
test_dna = "ACTGCTAGCTGATCGGGCTATGC"
print(get_at_content(test_dna, 4))


## Try hard not to 'overwork' a function
## Make them flexible as possible
## Consider them like building blocks, you always want to be able to reuse the block
## Maximum compatibility is key


## Keyword arguments are another thing in functions that let's us call them in a different way
## Maybe useful if we don't rememebr the order of arguments in a function
get_at_content("ATCGCTAGCTCG", 2)
# OR
get_at_content(dna_input="ATCGATCGTACG", sig_figs=5)
# OR
get_at_content(sig_figs=4, dna_input="ATCGATCGTAGCTGAC")
## If we didn't put the function calls first we can't put these out of order
## Makes the code clearer too if code is being shared
## Can do not **keyword arguments** for the second call in a function but not the first
## If you do it for the first one though then you need to do it for the next

### Defaults in Functions ###
## Like how opening a file defaults to read mode
def get_at_content(dna_input, sig_figs=2):  # by putting '=2' here we set the default
    dna_input = dna_input.upper()
    dna_length = len(str(dna_input))
    a_counter = dna_input.count('A')
    t_counter = dna_input.count('T')
    a_t_percent = (a_counter + t_counter) / len(dna_input)
    return round(a_t_percent, sig_figs)
# Can still specify a different number of sig figs

### Testing Functions ###

# In some examples we use very short fake test sequences to see if our code is working before
# Not always practical to test with our real sequences
# Python has a built in tool for this called *** assert ***
assert get_at_content("ATCG", 3) == 0.5  # Couldn't let default sig figs had issues with previous default setting
# If wrong we would have seen "assertion error"

# Assertions can help distinguish between an error with a function and the code that calls the function
# Good to try after modifying a function as well
# Can also be useful for documentation to make the expected output clear

assert get_at_content("ATCGNNNNNNNNNNN", 2) == 0.5  # Returns assertion error

# 'N' is often used to represent unknown bases in sequencing

def get_at_content(dna_input, sig_figs=2):  
    dna_input = dna_input.upper()
    dna_input = dna_input.replace('N', '')
    dna_length = len(str(dna_input))
    a_counter = dna_input.count('A')
    t_counter = dna_input.count('T')
    a_t_percent = (a_counter + t_counter) / len(dna_input)
    return round(a_t_percent, sig_figs)

assert get_at_content("ATCGNNNNNNNNNNN", 2) == 0.5  # Now this should be fine

# Grouping assetions together can help test the resilience of a function

assert get_at_content("A") == 1
assert get_at_content("T") == 1
assert get_at_content("G") == 0
assert get_at_content("ATCG") == 0.5
assert get_at_content("AGC") == 0.33
assert get_at_content("AGC", 1) == 0.3


################## EXERCISES ##################

### Percent of amino acid residues part 1 ###
 
def amino_acid_tracker(protein_sequence, amino_acid):
    protein_sequence = protein_sequence.upper()
    amino_acid_number = protein_sequence.count(amino_acid)
    protein_length = len(protein_sequence)
    amino_acid_percent = (amino_acid_number/protein_length) * 100
    return round(amino_acid_percent, 4)

amino_acid_tracker("MLNO", "L")

assert amino_acid_tracker("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_tracker("MSRSLLLRFLLFLLLLPPLP", "r") == 10  # Only one that didn't work
assert amino_acid_tracker("msrslllrfllfllllpplp", "L") == 50
assert amino_acid_tracker("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


### Percent of amino acid residues part 2 ###

## Goal is to accept a list of amino acids instead of a single one
## If no list is given it returns the percent of hydrophobic amino acids

## First Attempt ##  No Bueno ##

amino_list = [given_list]
given_list = ["A", "L", "I"]


def nucleotide_checker_function(protein_entry, amino_list):
    protein_entry.UPPER()
    protein_entry.count()
    protein_total = len(protein_entry)
    given_list.UPPER()
    given_list.count()
    amino_acid_constituents = ()
    return(amino_list.count() / protein_entry.count())


## Going through with the book ##


# Two ways 
# Loop through each of the given amino acids in turn counting the number of times they appear
# or
# Treat the protein sequence string as a list, then ask for each position if the character there is a part of the list of amino acids we're searching for


## The first way is the way we're going with for now ## 

# To keep count of matches we create a variable outside of the loop which gets updated each time through the loop

protein = "MSRSLLLRFLLFLLLLPPLP"
aa_list = ['M', 'L', 'F']

# The variable 'total' will keep track of the total number of instances

total = 0 

for aa in aa_list:
    print("counting number of " + aa)
    aa = aa.upper()
    aa_count = protein.count(aa)

    # Adding to the total count
    total = total + aa_count
    print("the running count is " + str(total))

percentage = (total * 100) / len(protein)
print("the final percentage is " + str(percentage))


## Now just like before turn the protein string and amino acid list into arguments to create a function ##

def get_aa_percentage(protein, aa_list):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
    percentage = (total * 100)/ protein_length
    return percentage

# This passes all the tests except for the one that it returns all the hydrophobic amino acids when no list is given
# Without setting the default here we get an error back if we try an run without giving two inputs

def get_aa_percentage(protein, aa_list=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    protein = protein.upper()
    protein_length = len(protein)
    total = 0
    for aa in aa_list:
        aa = aa.upper()
        aa_count = protein.count(aa)
        total = total + aa_count
    percentage = (total * 100)/ protein_length
    return percentage

assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65


