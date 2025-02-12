####################  Conditional Tests  ####################

### Examples to verify truth in python

print(3 <=5)
print("ATGCTT".endswith("ATG"))
print("ATGCTT".startswith("ATG"))
print("V" in ["V", "L", "T"])
print("ATCG".isupper())
leg = 10
print(leg is 10)
print(leg is "10")   #False as this makes 10 a string not an integer


### Ex of IF statements in python

expression_level = 125
if expression_level > 100:
    print("positive hit")


accs = ['ab56', 'al32', 'bL32', 'ai34', 'tr27']
for accession in accs:
    if accession.startswith('a'):
        print(accession)


### Ex of ELSE statements in python
        
expression_level = 300
if expression_level > 500:
    print("The hit is in the top 5%")
else: 
    print("The hit is within 95% of data point")   # shows as blue due to text editor


file1 = open("one.txt", 'w')
file2 = open("two.txt", 'w')
file3 = open("three.txt", 'w')
file4 = open("four.txt", 'w')

accs = ['ab25', 'ac45', 'br21', 'tl56', 'ul56']

for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    else:
        file2.write(accession + "\n")


### Can have unlimited elif statements

for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    elif accession.startswith('t'):
        file3.write(accession + "\n")
    elif accession.startswith('u'):
        file4.write(accession + "\n")


## These were mutually exclusive, if they are not then we need a series of IF statements instead
        
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    if accession.endswith('b'):
        file2.write(accession + "\n")
    if len(accession) == 4:
        file3.write(accession + "\n")
    if accession.count('J') > 5:
        file4.write(accession + "\n")       


file1.close()
file2.close()
file3.close()
file4.close()    # Wasn't seeing the print until I closed the files, this causes issues with printing


## While Loops

count = 0
while count < 10:
    print(count)
    count = count + 1


## Building up complex conditions


# For two conditions one option is to nest two if statements together

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        if accession.endswith('3'):
            print(accession)

# instead better to use an 'and' connector
            
for accession in accs:
    if accession.startswith('a') and accession.endswith('7'):
        print(accession)      # This did not work but believe this to just be a bug

# There is an 'or' connector

for accession in accs:
    if accession.startswith('a') or accession.endswith('6'):
        print(accession)

# Can use 'and' with an 'or' connector as well

for accession in accs:
    if accession.startswith('a') and accession.endswith('7') or accession.startswith('b'):
        print(accession)   

# Better when doing the above though we use brackets for clarity
        
for accession in accs:
    if (accession.startswith('a') and accession.endswith('7')) or accession.startswith('b'):
        print(accession)  

# Not statements are also quite useful
        
for accession in accs:
    if accession.startswith('a') and not accession.endswith('6'):
        print(accession)


## While possible to use these when trying to identigy items in a list it is more useful to use the filter() function and/or list comprehension
## Filter and list comprehension in next book advanced python for biologists
        

## Writing true & false statments

# Function to determine if DNA is AT rich or not

def is_at_rich(DNA):
    length = len(DNA)
    a_count = DNA.upper().count('A')
    t_count = DNA.upper().count('T')
    at_amount = ((a_count + t_count) / length) * 100
    if at_amount > 65:
        print("DNA is AT rich")
    else:
        print("DNA is not AT rich")


print(is_at_rich("ATTATctacTA"))
print(is_at_rich("CGGCAGCGCT"))

# Can also implement the return function instead

def is_at_rich(DNA):
    length = len(DNA)
    a_count = DNA.upper().count('A')
    t_count = DNA.upper().count('T')
    at_amount = ((a_count + t_count) / length) * 100
    return at_amount > 65   # Should give 'true' if it's over 65%

print(is_at_rich("ATATATATATA"))



############################   EXERCISES  #################################

### Task 1 - print out gene names for all genes belonging to Drosophilia melanogaster or Drosophilia simulans


## First attempt

# Opening the file in read mode

data = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/conditional_tests/exercises/data.csv", "r")

for line in data:
    if column1 = Drosophilia melanogaster or column1 = Drosophilia simulans:
        print(DNA)

# This was wrong because the first step is to go through the csv file and assign each column a variable name

data = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/conditional_tests/exercises/data.csv")

for line in data:
    columns = line.rstrip("\n").split(",") # Split breaks a string into a list of substrings based on a separator
    species = columns[0]
    DNA = columns[1]
    name = columns[2]
    expression = columns[3]

    print(name)

    if species == "Drosophila melanogaster" or species == "Drosophila simulans":
        print(DNA)

# Important to know how to assign variables to columns CSV Files
# Conditionals can be embedded in loops
        
## Task 2 - Printing names of genes within a certain length

data = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/conditional_tests/exercises/data.csv")

for line in data:
    columns = line.rstrip("\n").split(",") # Split breaks a string into a list of substrings based on a separator
    species = columns[0]
    DNA = columns[1]
    name = columns[2]
    expression = columns[3]

    if len(str(DNA)) > 90 and len(str(DNA)) < 121:
        print(name) 

# This worked first go
# A useful check for length like this is    if 90 < len(sequence) < 100:  followed by print("yes")
        

## Task 3 - printing based on AT content and expression level

data = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/conditional_tests/exercises/data.csv")

for line in data:
    columns = line.rstrip("\n").split(",") # Split breaks a string into a list of substrings based on a separator
    species = columns[0]
    DNA = columns[1]
    name = columns[2]
    expression = columns[3]
   
    A_amount = DNA.upper().count('A')
    T_amount = DNA.upper().count('T')
    DNA_length = len(DNA)
    AT_percent = (A_amount + T_amount)/DNA_length

    if AT_percent > 0.5 and int(expression) > 200:
        print(name)     

# The only error was to be very careful on what number is recognized as a string such as expression level in this case
# I changed it in the if statement but could have done so when defining the variables as well
# Would have been more clever to use the function decided on above, I did recognize this but recreated it for practice


## Task 4 - print gene names that begin with 'k' or 'h' except those belonging to drosophila melanogaster

data = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/conditional_tests/exercises/data.csv")

for line in data:
    columns = line.rstrip("\n").split(",") # Split breaks a string into a list of substrings based on a separator
    species = columns[0]
    DNA = columns[1]
    name = columns[2]
    expression = columns[3]

    if name.startswith('h') or name.startswith('k') and species != "drosophila melanogaster":
        print(name)

# Got this right first try
        

## Task 5 - print mssage per gene saying AT content 'High' 'Low' or 'Medium'

def at_rating(DNA):
    length = len(DNA)
    A_amount = DNA.upper().count('A')
    T_amount = DNA.upper().count('T')
    AT_percent = (A_amount + T_amount)/DNA_length

    if AT_percent > 0.65:
        print("AT is High")
    elif AT_percent < 0.45:
        print("AT is low")
    else:
        print("AT is Medium")


data = open("C:/Users/Brian/Documents/Python_for_Biologists_files_all/p4b_exercises/exercises_and_examples/conditional_tests/exercises/data.csv")

for line in data:
    columns = line.rstrip("\n").split(",") # Split breaks a string into a list of substrings based on a separator
    species = columns[0]
    DNA = columns[1]
    name = columns[2]
    expression = columns[3]
    print(at_rating(DNA))

# Got it first try
    




