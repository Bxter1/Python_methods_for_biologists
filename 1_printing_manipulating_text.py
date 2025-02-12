### Counting AT Content ### 
my_dna = "ACTGATCGATTACGTATAGAATTCTGCTATCATACATATATATCGATGCGTTCAT"
print(my_dna)

a_content = my_dna.count("A")
print(a_content)

t_content = my_dna.count("T")
print(t_content)

at_content = (a_content + t_content) / len(my_dna)
print("AT content is", at_content)

### Complementing DNA Above ###
reverse_dna1 = my_dna.replace("A", "t")
reverse_dna2 = reverse_dna1.replace("T", "a")
reverse_dna3 = reverse_dna2.replace("C", "g")
reverse_dna4 = reverse_dna3.replace("G", "c")
reverse_dna = reverse_dna4.upper()
print(reverse_dna)

### Finding length of two fragments after RE Digest ###
print(my_dna.find("GAATTC"))  #Answer is 18 meaning length is 19 until the G, 20 after
fragment_1 = my_dna[0:19]
fragment_2 = my_dna[19:]
print("Fragment 1 length is" , len(fragment_1)) 
print("fragment 2 length is", len(fragment_2))

# OR

frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))

### Splicing out introns 1 ###
other_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
dna_part1 = other_dna[0:64]
dna_part2 = other_dna[92:]
final_dna = dna_part1 + dna_part2
print(final_dna)

### Splicing out introns 2 ###

coding_percent = len(final_dna) / len(other_dna)
print("The coding DNA makes up this percent of final dna", str(coding_percent))

### Splicing out introns 3 ###

non_coding = other_dna[65:92]
non_coding_lower = non_coding.lower()
cleaned_dna = dna_part1 + non_coding_lower + dna_part2
print(cleaned_dna)

# or

exon1 = my_dna[0:64]
intron = my_dna[64:91]
exon2 = my_dna[91:]
print(exon1 + intron.lower() + exon2)