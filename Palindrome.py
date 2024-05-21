# def is_palindrome(s):
#     s = ''.join(c.lower() for c in s if c.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
#     return s == s[::-1]

# # Test the function
# print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(input(is_palindrome("Enter the input : ")))  # Output: True

#Taking the input fro the user and converting into the lower case
s = input ("Please enter the input : ").lower() 
#Slicing the given string and assign to the reverse
reverse = s[::-1]
#checking the given string is equal to reverse
if (s == reverse):
    print("It is a palindrome")
else:
    print("It is not a palindrome")