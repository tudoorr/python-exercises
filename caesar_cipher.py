import string

word = input("What word do you want to encode?: ")
try:
    shift = input("How many places do you want to shift it? (non negative): ")
    if "-" in shift:
        print("It cannot be a negative number!")
        exit(0)
    shift = int(shift)
except TypeError:
    print("It needs to be a number!")
    exit(0)
result = ""

for char in word:
    if char.islower():
        result += string.ascii_lowercase[(list(string.ascii_lowercase).index(char) + shift) % 26]
    elif char.isupper():
        result += string.ascii_uppercase[(list(string.ascii_uppercase).index(char) + shift) % 26]
    elif char == " ":
        result += " "
    else:
        print("You can't have special characters!")
        exit(0)

print(result)
