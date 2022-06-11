#Python Program to calculate arithmetic operation on two number using user defined function
def arcalc(x, y):
    return x + y, x - y, x * y, x / y, x % y


num1 = int(input("Enter no.1:"))
num2 = int(input("Enter no.2:"))
add, sub, mult, div, mod = arcalc(num1, num2)
print("Sum of given no.s=", add)
print("Difference of given no.s=", sub)
print("Product of given no.s=", mult)
print("Division of given no.s=", div)
print("Modulo of given no.s=", mod)
