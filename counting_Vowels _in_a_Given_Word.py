# Counting Vowels in a Given Word

# Adding vowels
vowles = "a e i o u"

# Spilting the vowles
s = vowles.split(" ")

# Taking the inputs from the user
word = input("Enter the word : ")

# Initinals the words
count_vowles = 0
count_consonant = 0

# Loops and if conditions for vowels to match user input
for character in word:
    if character in vowels:
        count_vowles += 1
    else:
        count_consonant += 1
        
# printing the output
print("The vowels count is ", count_vowles)
print("The consonants count is ", count_consonant)
