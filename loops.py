numbers = [2, 4 , 5, 8, 13, 56, 97, 999, 987, 567, 893]
for number in numbers:
    if number == 100:
        break
    if number % 2 == 0:
        print(number)