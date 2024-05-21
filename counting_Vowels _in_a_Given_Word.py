# Counting Vowels in a Given Word


vowles = "a e i o u"
s = vowles.split(" ")
word = input("Enter the word : ")
count_vowles = 0
count_consonant = 0
for charcter in word:
    if charcter in vowles:
        count_vowles += 1
    else:
        count_consonant += 1
        

print("The vowles count is ", count_vowles)
print("The consonants count is ", count_consonant)