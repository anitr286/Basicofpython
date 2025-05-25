#Write a PytWrite a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.hon function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def fact(number):
    if number == 0 :
        return 1
    else:
        return number*fact(number - 1)
number = int(input("Enter any number : "))  
print(fact(number))
    
