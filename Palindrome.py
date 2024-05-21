#Taking the input from the user and converting it into the lowercase
s = input ("Please enter the input : ").lower() 
#Slicing the given string and assign to the reverse
reverse = s[::-1]
#checking the given string is equal to the reverse
if (s == reverse):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
