#Python Program to Calculate diameter and area of circle using user defined function
def circle(r):
    area = 3.14*r**2
    diameter = r*2
    return(diameter,area)
a = int(input("Radius of circle(cm) = "))
c,d = circle(a)
print("diameter(cm) = ",c)
print("area(cm^2)= ",d)