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

for apeType in apes:
    name_length = len(apeType)
    first_letter = apeType[0]
    print("the name has a length of", name_length, "the animals name starts with a", first_letter)




