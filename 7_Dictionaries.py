# Storing paired data

# Chapter talks about analyzing a 20bp sequence
# If we did count functions on the DNA for all different trinucleotides possibilities at least 46 of 64 would be 0 as there is only 18 overlapping trinucleotides
# Instead we can store hits in a list

dna = "ATGATCGATCGAGTGA"
dinucleotides = ['AA', 'AT', 'AG', 'AC', 'TA', "TT", 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

all_counts = []
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    print("The count is " + str(count) + " for " + dinucleotide)
    all_counts.append(count)
print(all_counts)

# Two issues
# 1 - Still many zeros being printed
# 2 - counts are disconnected from the dinucleotides. a.k.a the seventh list item has 3 instances of it

print("count for TG is " + str(all_counts[7]))

# To find position of 'TG' we can use the index function

i = dinucleotides.index('TG')
print(all_counts[i])

# This only works because both lists are the same length

# Still there are drawbacks to this strategy
# 1 - Still storing zeros
# 2 - Two lists to keep track of now
# 3 - If only one list is modified we will then get errors when checking the lists
# 4 - This method is computationally slow


## Key idea: we need to store pairs of data ##


## Examples of why we would need this
# Protein names and sequences
# RE and their motifs
# AA and their codons
# names and emails
# samples and coordinates
# words and definitions


## Creating a dictionary ##

# curly brackets
# key and value

enzymes = {
    'EcoRI' : r'GAATTC',
    'AvaII' : r'GG(A|T)CC',
    'BisI'  : r'GC[ATCG]GC' 
}

print(enzymes['BisI'])


# Dictionaries are only compatible with strings and numbers
# File objects are not possible with dictionaries
# Keys must also be uniques

# Often we build dictionaries slowly by creating an empty dictionary
# We can then add items to the dictionary using square brackets

enzymes2 = {}
enzymes2['EcoRI'] = r'GAATC'
print(enzymes2)

# We can remove items from a dictionary using the 'pop function

enzymes.pop('EcoRI')
print(enzymes)


dna = "ATGATCGATCGAGTGA"
dinucleotides = ['AA', 'AT', 'AG', 'AC', 'TA', "TT", 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

all_counts = {}
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    print("The count is " + str(count) + " for the dinucleotide " + dinucleotide)
    all_counts[dinucleotide] = count
print(all_counts)

# This has saved each dinucleotide with it's count data
# Looking up the count of a dinucleotide has become much simpler now too

print(all_counts['TA'])
print(all_counts['TG'])

# This is still saving information where the result is zero though
# To overcome this we can include an IF statement

dna = "ATGATCGATCGAGTGA"
dinucleotides = ['AA', 'AT', 'AG', 'AC', 'TA', "TT", 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

all_counts = {}
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    if count > 0:
        all_counts[dinucleotide] = count
print(all_counts)

# The remaining issue is if we look up a count that is zero we won't get an answer

print(all_counts['TA'])

# To overcome we can look for the existence of the key to see if it exists

if 'TA' in all_counts:
    print("TA is valid")
else:
    print("Invalid")

# Or we can use the 'get' method
# Both of the following are equivalent methods
    
print(all_counts['TA'])
print(all_counts.get('TA'))

# Alone this isn't enough however the get method allows for a second argument which returns a set value if the item is not present

print(all_counts.get('TA', 0))  # 0 is printed as there is no TA dinucleotides


##  Iterating over a dictionary  ##

# Let's say we want to print out all instances of dinucleotides that appear twice

for dinucleotide in dinucleotides:
    if all_counts.get(dinucleotide, 0) == 2:
        print(dinucleotide)

# Usually when creating a dict we'll do it in a way not needing an explicit key list
# Here we'll do a way to cover all dinculeotides using two nested 'for' loops

dna = "AATGATGAACGAC"
bases = ['A', 'T', 'C', 'G']
all_counts = {}
for base1 in bases:
    for base2 in bases:
        dinucleotide = base1 + base2
        count = dna.count(dinucleotide)
        if count > 0:
            all_counts[dinucleotide] = count
print(all_counts)

# This now will create a list of dinculeotide and then go through the DNA and count what is there
# Still storing the dinucleotide with the count data
            

##  Iterating over keys  ##

# Keys() function provides all the keys in a dictionary
            
print(all_counts.keys())

# Now to find all the dinucs that appear 2x we can iterate over the output of keys()

for dinucleotide in all_counts.keys():
    if all_counts.get(dinucleotide) == 2:
        print(dinucleotide)

# Note that dicts are inherently unordered
# Using keys() does not change this
        
# lists however always keep the same order when looping
# to implement order we can use the sorted() function

for dinucleotide in sorted(all_counts.keys()):
    if all_counts.get(dinucleotide) == 2:
        print(dinucleotide)


##  Iterating over items  ##
        
# previous example we looked up the value for the current key
# python has a function to do this called items()
        
# Instead of

for key in my_dict.keys():
    value = my_dict.get(key)
    # do something with key and value

# Do this
    
for key, value in my_dict.items():
    # Do something with key and vlaue

# This returns a list of pairs of values
    
    for dinucleotide, count in all_counts.items():
        if count == 2:
            print(dinucleotide)

# Needed the 'for' to be indented but otherwise worked well
# Prefered for simplicity and readability

## Note: Do not use .items() to look up a single value as that is wasteful  ##

# for looking up only instances of 'AT'
# Don't do

for dinucleotide in all_counts.items():
    if dinucleotide == 'AT':
        print(count)

# Instead do
        
print(all_counts.get('AT'))

## Final note: Dicts allow easy lookup of a value stored with a key, but not the other way around ##


##################   Exercises   ####################

## DNA Translation

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


## Tasks
# 1. Write a program that translates DNA into a protein
# 2. Split the DNA sequence into codons
# 3. Look up the amino acid residue for each codon
# 4. Join all the amino acids to give a protein

## Considerations
# a. How does the program deal with sequences that aren't multiples of 3
# b. How does it deal with sequences that have unknown bases


## My thoughts on initial task
# Need to loop through dna string in 3's from the start
# need it to search the 'gencode' dictionary for value pairs
# need to include an if statement for the end of the string if uneven possibly with .get()
# Need to set a replacement value for the codon if it's not known under .get()
# Need it to store the value in a new string called 'protein'


# To work with and test our code we will create a 3 codon long DNA string

dna = "ATGTTCGGT"

# split() only works if the things you want to separate are split by a delimeter

# Can do really basic however would be a bad idea for longer strings

codon1 = dna[0:3]
codon2 = dna[3:6]
codon3 = dna[6:9]
print(codon1, codon2, codon2)

# instead lets try and automate this

# The range functions role is to generate a sequence of number
# arguments are the start, stop (exclusive), and step size

dna = "ATGTTCGGT"
for start in range(0, 7, 3):
    codon = dna[start:start+3]
    print("one codon is " + codon)

# ^ This is how we turn DNA into codons
# Now we must turn the codons into amino acid sequences

for start in range(0, len(dna), 3):
    codon = dna[start:start+3]
    aa = gencode.get(codon)
    print("the codon is " + codon)
    print("the amino acid is " + aa)

# Now lets turn the amino acids into a protein sequence

protein = ""
for start in range(0, len(dna), 3):
    codon = dna[start:start+3]
    aa = gencode.get(codon)
    protein = protein + aa

# Let's now turn this into a function

def translate_dna(dna):
    protein = ""
    for start in range(0, len(dna), 3):
        codon = dna[start:start+3]
        aa = gencode.get(codon)
        protein = protein + aa
    return(protein)


translate_dna(dna)

dna = "TATCGTTAGCGTTA"

print(translate_dna("TATCGTTAGCGTTA"))

# Getting an error here because gencode.get(codon) is returning 'None' for some codons
# This means that the codon is not in the gencode dictionary
# We can confirm this by adding a line to print the codons

def translate_dna(dna):
    protein = ""
    for start in range(0, len(dna), 3):
        codon = dna[start:start+3]
        print("The codon is " + codon)
        aa = gencode.get(codon)
        protein = protein + aa
    return(protein)

print(translate_dna("CTATGTTAGCGTTA"))

# Here we see that the final codon is two values long causing the return to be invalid

# Need to use the second function of the 'get' command which puts a fill in when there is no dictionary match

def translate_dna(dna):
    protein = ""
    for start in range(0, len(dna), 3):
        codon = dna[start:start+3]
        aa = gencode.get(codon, 'N')
        protein = protein + aa
    return(protein)

translate_dna(dna)

# This worked I now got the answer with an 'N' put in
# I also see an underline as the 'TAG' codon returns a '_' as dichtated by the gencode


# This is now replacing non multiples of 3 at the end with N
# However we might prefer to leave N for when there is a codon triplicate not found
# We can overcome this by instead having the range  function stop reading two codons from the end
# This solution overcomes when DNA is not multiples of 3


def translate_dna(dna):
    last_codon_start = len(dna) - 2
    protein = ""
    for start in range(0, last_codon_start, 3):
        codon = dna[start:start+3]
        print("The codon is " + codon)
        aa = gencode.get(codon)
        protein = protein + aa
    return(protein)

print(translate_dna("CTATGTTAGCGTTA"))

# This worked because if there is a final complete last codon then stopping two codons from the end would still include the start of the last codon
# It only stop if the last codon is of length 1 or two bases


# Now we look at the situation where there is an undetermined base

print(translate_dna("ATGCTATNC"))

# We get an error, we can overcome this using a similar situation as above with the get function

def translate_dna(dna):
    last_codon_start = len(dna) - 2
    protein = ""
    for start in range(0, last_codon_start, 3):
        codon = dna[start:start+3]
        print("The codon is " + codon)
        aa = gencode.get(codon, 'X')
        protein = protein + aa
    return(protein)

print(translate_dna("ATGCTATNC"))

        













