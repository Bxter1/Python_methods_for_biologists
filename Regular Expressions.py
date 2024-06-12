############################  REGULAR EXPRESSIONS ##########################

# Standard tool set for dealing with common problem in biology

# These are parts of modules which need to be downloaded 

# regular expression can be called using 'import re' at the start of a script

# To use then we need to use the prefix before the function as seen below


import re
re.search(pattern, string)


# To avoid conflicts between special characters in python like newline and tab with calls of refular expression we can put an r infront of a string
# This removes the special character and has the string be read 'raw'

print(r"\t\n")

print("\t\n")


## Searching for patterns in a string with regular expressions and IF statements

dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
    print("restriction sites found")


# Finding alternatives sites in DNA
    
if re.search(r"GAATTC", dna) or re.search(r"GGTCC", dna):
    print("restriction sites found")


# Can also use other 'regular expression' functions

if re.search(r"GG(A|T)CC"):
    return("restriction sites found")


# This use case is not limited to only two characters

if re.search(r"GG(A|T|C|G)CC"):
    return("restriction sites found") 


# Square brackets serve the same role but a little more simple

if re.search(r"GG[ATCG]CC"):
    return("restriction sites found") 


# To have more freedom in the search criteria, a period would allow for any character between surrounding known characters

if re.search(r"GG.CC"):
    return("restriction sites found")   # This would return GG7CC, GGOCC, GG%CC


# We can also have searches with excluded characters

if re.search(r"GG[^NT]CC"):
    return("restriction sites found")  # Will return everything except GGNCC or GGTCC



## Quantifiers offers pattern searches with variable amounts of characters


# A question mark means the character is optional appearing 0 or 1 times

if re.search(r"GGA?CC"):
    return("restriction sites found")  # Returns GGCC or GGACC


# Works with bracketed examples too

if re.search(r"GG(AAA)?CC"):
    return("restriction sites found")  # Returns GGAAACC or GGCC


# A plus sign following a character means find all instances where the character appears one or more times between known characters

if re.search(r"GGA+CC"):
    return("restriction sites found") # This returns GGACC, GGAACC, GGAAAAAACC and so on, but not GGCC


# An asterix is the most flexible, it returns instances where the character dies not appear or appears any number of times

if re.search(r"GGA*CC"):
    return("restriction sites found") # returns GGCC GGACC GGAAAAAAAACC


# Curly brackets return an exact number of instances

if re.search(r"GGA{5}CC"):
    return("restriction sites found") # returns only GGAAAAACC


# Curly brackets with two numbers separated by a comma return instances where it appears between that range

if re.search(r"GGA{3,5}CC"):
    return("restriction sites found") # returns GGAAACC GGAAAACC GGAAAAACC


# Leaving out the first or second number means less than or greater than

if re.search(r"GGA{,3}CC"):
    return("restriction sites found") # returns GGACC GGAACC GGAAACC

if re.search(r"GGA{3,}CC"):
    return("restriction sites found") # returns GGAAACC GGAAAACC GGAAAAACC and so on



## Positions in the input strings


# ^ before characters searches for instances where that character appears at the start of a string, 
# $ does the same but for the end of a string

# ^AAA matches AAATTT not GGGAAATTT
# AAA$ matches TTTAAA not AAATTT


## These are most powerful when combined

if re.search(r"^AUG[AUGC]{3,10}A{5-10}$"):
    return("restriction sites found") # This returns only AUG followed by 3-10 characters that can be either A U G C followed by 5-10 bases poly A tail


## To Master RE ##  
 # learn
 # greedy vs minimal quantifiers
 # back references
 # Lookahead
 # Lookbehind assertions
 # Built in character classes


## Extracting the part that matched through grouping

dna = "CGATNCGGAACGATC"
m = re.search(r"[^ATCG]", dna)

if m:
    print("ambiguous base found")
    ambig = m.group()
    print("ambiguous base is " + ambig)


# Extracting multiple groups
# We can take advantage of some of the most flexible regular expression; period = any character, plus = anthing above 0
# We can put parentheses around these patterns to extract two things into separate variable

scientific_name = "homo sapiens"

m = re.search("(.+) (.+)", scientific_name)

if m:
    genus = m.group(1)
    species = m.group(2)
    print("genus is " + genus + ", species is " + species)


# Getting the match positions
    
m = re.search(r"[^ATCG]", dna)

if m:
    print("ambiguous base found")
    print("at position " + str(m.start()))


## Multiple matches within a string

# re.search() only finds a single instance, the first instance
# re.finditer() alternatively finds all instance where the instance is found
# re.finditer() returns a list (actually iterator object) which can be processed with a loop

dna = "CGCTCNTAGATGCGCRATGACTGCAYTGC"   

matches = re.finditer(r"[^ATCG]", dna)

for m in matches:
    base = m.group()
    position = m.start()
    print("ambiguous base is " + base + "at position " + str(position))


# Getting multiple matches as strings

dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"

matches = re.finditer(r"[AT]{6,}", dna)

results = []
for m in matches:
    results.append(m.group())

print(results)


# There is a more specialized function called re.findall()

results = re.findall(r"[AT]{6,}", dna)
print(results)


# Splitting a string using regular expressions

# Example splitting the DNA between each odd character

runs = re.split(r"[^ATCG]", dna)
print(runs)













