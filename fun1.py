#Write a Python function to find the maximum of two numbers.
def find_great(x,y):
    if x > y :
        return x
    else :
        return y
       
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
max = find_great(num1,num2)
print(f"The great between {num1} and {num2} is {max}")

