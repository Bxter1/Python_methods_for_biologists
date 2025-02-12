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


# Can also use other 'regular expression' functions, this is A or T

if re.search(r"GG(A|T)CC", dna):
    print("restriction sites found")


# This use case is not limited to only two options but will only be one of the four options

if re.search(r"GG(A|T|C|G)CC", dna):
    print("restriction sites found") 


# Square brackets serve the same role but a little more simple

if re.search(r"GG[ATCG]CC", dna):
    print("restriction sites found") 


# To have more freedom in the search criteria, a period would allow for any character between surrounding known characters

if re.search(r"GG.CC"):
    print("restriction sites found")   # This would print GG7CC, GGOCC, GG%CC


# We can also have searches with excluded characters

if re.search(r"GG[^NT]CC"):
    print("restriction sites found")  # Will print everything except GGNCC or GGTCC



## Quantifiers offers pattern searches with variable amounts of characters


# A question mark means the character is optional appearing 0 or 1 times

if re.search(r"GGA?CC"):
    print("restriction sites found")  # prints GGCC or GGACC


# Works with bracketed examples too

if re.search(r"GG(AAA)?CC"):
    print("restriction sites found")  # prints GGAAACC or GGCC


# A plus sign following a character means find all instances where the character appears one or more times between known characters

if re.search(r"GGA+CC"):
    print("restriction sites found") # This prints GGACC, GGAACC, GGAAAAAACC and so on, but not GGCC


# An asterix is the most flexible, it prints instances where the character dies not appear or appears any number of times

if re.search(r"GGA*CC"):
    print("restriction sites found") # prints GGCC GGACC GGAAAAAAAACC


# Curly brackets print an exact number of instances

if re.search(r"GGA{5}CC"):
    print("restriction sites found") # prints only GGAAAAACC


# Curly brackets with two numbers separated by a comma print instances where it appears between that range

if re.search(r"GGA{3,5}CC"):
    print("restriction sites found") # prints GGAAACC GGAAAACC GGAAAAACC


# Leaving out the first or second number means less than or greater than

if re.search(r"GGA{,3}CC"):
    print("restriction sites found") # prints GGACC GGAACC GGAAACC

if re.search(r"GGA{3,}CC"):
    print("restriction sites found") # prints GGAAACC GGAAAACC GGAAAAACC and so on



## Positions in the input strings


# ^ before characters searches for instances where that character appears at the start of a string, 
# $ does the same but for the end of a string

# ^AAA matches AAATTT not GGGAAATTT
# AAA$ matches TTTAAA not AAATTT


## These are most powerful when combined

if re.search(r"^AUG[AUGC]{3,10}A{5-10}$"):
    print("restriction sites found") # This prints only AUG followed by 3-10 characters that can be either A U G C followed by 5-10 bases poly A tail


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
# re.finditer() prints a list (actually iterator object) which can be processed with a loop

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


########### EXERCISES ##########


accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]



## print only ones containing the number 5 ##

five_containing = re.findall(r"(.+)5(.+)", accs)
print(five_containing)

# This didn't work because findall function expects a single string and not a list
# Always need to perform a loop through a list

for acc in accs:
    if re.search("5", acc):
        print(acc)

# Loop through a list is the way



## Contain the letter d or e ##
        
for acc in accs:
    if re.search("(d|e)", acc):
        print(acc)



## Contains the letters d and e in that order ##
        
for acc in accs:
    if re.search(r"d.*e", acc):
        print(acc)

# The '.' matches any single character
# The '*' is a quantifier matching zero or more of the preceeding element



## Conatin the letter d and e in that order with one letter bewteen them ##
        
for acc in accs:
    if re.search(r"d.{1}e", acc):
        print(acc)

# This worked but didn't need the bracketed one as a period is a standin for any character but only one


        
## Contains both d and e in any order ##
        
for acc in accs:
    if re.search(r"[d.*e|e.*d]", acc):
        print(acc)

# This didn't work matched expressions with either a d or an e
# This happened because of the use of square brackets
        
for acc in accs:
    if re.search(r"d.*e|e.*d", acc):
        print(acc)

# This worked

# Can also do this to make it more clear
        
for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print(acc)



## Starting with an X or Y ##
        
for acc in accs:
    if re.search(r"^[xy]", acc):
        print(acc)

# This worked



## Starting with x or y and ending with an e
        
for acc in accs:
    if re.search(r"^[xy].*(e)$", acc):
        print(acc)

# This worked



## Contain 3 or more digits in a row ##
        
for acc in accs:
    if re.search(r"(1|2|3|4|5|6|7|8|9)[3,]", acc):
        print(acc)

# This didn't work because the square brackets mean it's looking for a 3 or a comma

for acc in accs:
    if re.search(r"(1|2|3|4|5|6|7|8|9){3,}", acc):
        print(acc)

# This worked but is unneccesarily long
        
for acc in accs:
    if re.search(r"\d{3,}", acc):
        print(acc)



## End with a d followed by an a, r, or p ##
        
for acc in accs:
    if re.search(r"(d[a|r|p])$", acc):
        print(acc)

# This worked but I didn't need the rounded brackets
        
for acc in accs:
    if re.search(r"d[arp]$", acc):
        print(acc)
        


#### Exercise Number 2 ####
        
## Predict fragment length if dna.txt is digested with 2 restriction enzymes ##
## RE AbcI ANT/AAT and RE AbcII GCRW/TG
        
DNA_find = open(r"C:\Users\Brian\Documents\Python_for_Biologists_files_all\p4b_exercises\exercises_and_examples\regular_expressions\exercises\dna.txt")

opened_dna = DNA_find.read().rstrip("\n")

print(len(opened_dna))

cut_site_1 = re.finditer(r"A[ATCG]TAAT", opened_dna)
for site in cut_site_1:
    area = site.group()
    position = site.start()
    print(area + " at position " + str(position + 3))


cut_site_2 = re.finditer(r"GC[AG][AT]TG", opened_dna)
for site in cut_site_2:
    area = site.group()
    position = site.start()
    print(area + " at position " + str(position + 4))

# Figured out a way to find out where the cuts are 
# don't have an efficient way combine the cuts sites and measure length
# Rest of this is the books solutions
    
# Initialize a list of all the cut sites

all_cuts = [0]
for match in re.finditer(r"A[ATCG]TAAT", opened_dna):
    all_cuts.append(match.start() + 3)

all_cuts.append(len(opened_dna))
print(all_cuts)

# This works now for one enzyme we will loop through our cut positions to determine the length of each cut

for i in range(1, len(all_cuts)):
    this_cut_position = all_cuts[i]
    previous_cut_position = all_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("One fragment size is " + str(fragment_size))

# Now we want to alter the function so that is includes both restriction enzymes

all_cuts = [0]

# For AbcI
for match in re.finditer(r"A[ATCG]TAAT", opened_dna):
    all_cuts.append(match.start() + 3)

# For AbcII
for match in re.finditer(r"GC[AG][AT]TG", opened_dna):
    all_cuts.append(match.start() + 4)

all_cuts.append(len(opened_dna))
print(all_cuts)

# This issue here is it lists the first string followed by the second string
# To overcome this we can use the sort() function

all_cuts = [0]

# For AbcI
for match in re.finditer(r"A[ATCG]TAAT", opened_dna):
    all_cuts.append(match.start() + 3)

# For AbcII
for match in re.finditer(r"GC[AG][AT]TG", opened_dna):
    all_cuts.append(match.start() + 4)

all_cuts.append(len(opened_dna))
sorted_cuts = sorted(all_cuts)
print(sorted_cuts) 

for i in range(1, len(sorted_cuts)):
    this_cut_position = sorted_cuts[i]
    previous_cut_position = sorted_cuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("One fragment size is " + str(fragment_size))