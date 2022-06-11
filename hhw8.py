#WAP that counts the number of alphabets and digits, uppercase letters, lowercase letter, spaces and other characters in the string entered.
a = input('Enter a string: ')
lower = upper = digit = space = special = 0

for i in a:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    elif i == ' ':
        space += 1
    else:
        special += 1
print('The number of alphabets:', upper + lower)
print('The number of uppercase letters:', upper)
print('The number of lowercase letters:', lower)
print('The number of digits:', digit)
print('The number of whitespace characters:', space)
print('The number of special characters',special)