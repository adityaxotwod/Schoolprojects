# WAP to accept a string and display whether it is a palindrome
a = input("Enter string to check")
b = list(a)
d = b.copy()
c = d.reverse()
if b == d:
    print("String is palindrome")
else:
    print("String is not palindrome")
