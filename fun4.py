# Define a function named 'string_reverse' that takes a string 'str1' as input
def reverse_str(str1):
    rstr = ""
    
    index = len(str1)
    while index > 0 :
        rstr += str1[index - 1]
        index = index - 1
    return rstr
print(reverse_str("ANIT"))
print(reverse_str("llab"))
print(reverse_str("bulb"))
        