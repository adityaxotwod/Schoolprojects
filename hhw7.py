#WAP to accept the percentage of a student and display its grade accordingly.
a = int(input("What is your percentage?= "))
if a>= 80:
    print("Grade A")
elif a >= 60:
    print("Grade B")
elif a >= 40:
    print("Grade C")
elif a >= 20:
    print("Grade D")
elif a >= 10:
    print("Grade E")
elif a >= 0:
    print("Grade F")
else:
    print("Please enter a valid %")