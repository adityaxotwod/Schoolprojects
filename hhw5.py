#WAP to print the sum of the series = 1+x1/1!+x2/2!+.......xn/(n)!- exponential series.
def sum(num):
   a = 0
   b = 1
   for i in range(1, num+1):
      b *= i
      a = a + (i / b)
   return a
n = int(input("Input value of n:"))
x = int(input("Input value of x:"))
print("Sum: ", 1 + x*sum(n))
