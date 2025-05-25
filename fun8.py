#Write a function if a number is even or odd
def check_evenodd(n):
    if n % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

n = int(input("Enter a number : "))
check_evenodd(n)