#Write a Python function to multiply all the numbers in a list
def mult(numbers):
    total = 1
    for x in numbers :
        total = total*x
    return total
print(mult((1,2,2,2)))