# Converting an Integer/string into Decimals

# Imporing decimals functions
import decimal
string = input("Enter the number : ")
print(type(string))
number = int(string)
print(type(number))

# This line converts the string '12345' to a Decimal object using the Decimal() constructor provided by the decimal module.
print(decimal.Decimal(number))
print(type(decimal.Decimal(number)))