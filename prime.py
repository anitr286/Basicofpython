# Define a function named 'test_prime' that checks if a number 'n' is a prime number
def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if (n % x == 0):
                return False
        return True
n = int(input("Enter any number: "))
print(prime(n))