#PYTHON XII--A DISHITA ADITYA W.
print("List of programs:")
print("01. to input a no. and check whether the no. is >100 or not")
print("02. to input a no. and check if it is -ve or +ve")
print("03. WAP that accepts two integers and checks if the first no. is exactly divisible by the second no.")
print("04. WAP to input a string and count the no. of upper case and lower case letters.")
print("05. wap to input a list where a) no. of elements are known b) no. of elements unknown")
print("06. WAP to input a list and print min, max and avg.")
print('07. create a dict where keys are month names and values are the no. of days in the resp. month')
print('08. to generate fibonacci series through a tuple')
print("09. wap that multiplies two integers without using *")
print("10. wap to calculate factorial of a no. ")
print("11. wap to cal the bill inclusive of gst.")
print("12. wap to input in mile and convert into km.")
print("13. wap to input a no. and display the sum from n to 2n if n is +ve if n is -ve, display sum from 2n to n.")
print("14. wap that shifts: the last letter to the first and other letters to its right.")
print("15. wap to input a dictionary with key as usernames and values as passwords. Ask the user for their login if true then...")
print("16. wap to prompt user to enter a sentence followed by 'ennter' ->print original string ->no. of words ->no. of characters (incl whitespaces.")
print("17. write a short python code that prints the longest word in a list of words.")
print("18. wap which checks the format of a number")
print("19. wap to create a list which has all integers less than 100 and are multiples of 3 or 5")
print("20. wap to swap the values assigned and print the result")
print("21. wap to calculate area of cone and cylinder. add them and hence find the total cost with taxes.")
print("22. program 21 with functions")
print("23. calc simple interest using function, rate = 10% and 2 years")
print("24. mathematical operations on 2 no.s.")
print("25. Print an array and shift it to n places.")
print("26. wap to input an octal no. and change its bases.")
print("27. wap that generates 4 terms of an AP. Provide initial and step values.")
print("28. WAP to accept two numbers from the user and calc LCM and HCF using functions.")
print("29. WAP to calculate the volume of a box using functions.")
print("30. WAP that recieves 2 parameters x & n and returns nth root of x.")
print("31. WAP to convert dollar to rupee.")
x=int(input("Enter your choice:"))

while x==1:
    a=int(input("Enter a no."))
    if a>100:
        print("No. is greater than 100")
    elif a==100:
        print("No. is equal to 100.")
    else:
        print("No. is not greater than 100")
        break
    
while x==2:
    b = int(input("Enter a no.:"))
    if b>0:
        print("No. is positive.")
    elif b==0:
        print("No. is equal to 0.")
    else:
        print("No. is negative.")
        break
    
'''21.3.22
WAP that accepts two integers and checks if the first no.
is exactly divisible by the second no.'''
while x==3:
    p=int(input("Enter first no.:"))
    q=int(input("Enter second no.:"))
    if p%q==0:
        print("First no. is exactly divisible by the second no.")
    else:
        print("First no. is not exactly divisible by the second no.")
        break
    
'''22.3.22
WAP to input a string and count the no.
of upper case and lower case letters'''
while x==4:
    p=input("Enter a string:")
    u=0
    l=0
    for i in range(len(p)):
        if p[i].isupper()==True:
            u +=1
        elif p[i].islower()==True:
            l +=1
    print("Entered string:",p)
    print("No. of upper case characters:", u)
    print("No. of lower case characters:", l)
    break

'''24/03/22
wap to input a list where
a) no. of elements are known
b) no. of elements unknown'''
while x==5:
    a = int(input("No. of elements:"))
    l = []
    for i in range(0,a):
            x=int(input("Enter element:"))
            l.append(x)
    print("List is:",l)
    break

while x==6:
    l=eval(input("Enter list:"))
    m=min(l)
    M=max(l)
    L=len(l)
    s=sum(l)
    avg=s/L
    print("Minimum element:", m)
    print("Maximum element:", M)
    print("Average of the elements:", avg)
    break

#28.2.22 
while x == 7:
      a = ['janauary','febuary','march','april','may','june','july','august','september','october','november','december']
      print('Months:',a)
      b = [31,28,31,30,31,30,31,30,31,30,31,30]
      print('Days:',b)
      c = dict(zip(a,b))
      print('dict:',c)
      break
    
#29.2.22
while x == 8:
    l = [0,1]
    n = int(input('Enter no. of elements'))
    for i in range(0,n-2):
        l.append(l[i]+l[i+1])
    t = tuple(l)
    print(t)
    break

#1.04.22
while x == 9:
    '''wap that multiplies two integers without using *'''
    a = int(input('Enter first number:'))
    b = int(input('Enter second number:'))
    s=0
    for i in range(b):
        s+=a
    print(s)
    break

#2.04.22
while x == 10:
    s=1
    i=1
    k=int(input("Enter a no."))
    while i<=k:
        s=s*i
        i=i+1
    print(s)
    break

'''wap to cal the bill inclusive of gst.'''
while x==11:
    choice='y'
    total=0.0
    while choice=='y' or choice=='Y':
        r=eval(input("Enter amount:"))
        p=eval(input("Enter GST %age:"))
        total= (r+(r*p)/100)
        print("Total amount inclusive of GST=", total,"/-")
        choice=input("Print 'y' to continue or 'n' to stop.")
    break

'''wap to input in mile and convert into km'''
while x==12:
    d=eval(input("Enter a no. in mile:"))
    c = d*1.6
    print(d,"miles =",c, "km")
    break

'''wap to input a no. and display the sum from n to 2n if n is +ve
if n is -ve, display sum from 2n to n.'''
while x==13:
    h=int(input("Enter N:"))
    sum=0
    if h>=0:
        for i in range(h,2*h+1):
            sum+=i
        print("Sum=", sum)
    else:
        num=0
        for j in range(2*h,h+1):
            num+=j
        print("Sum=", num)
    break
'''8.4.22 wap that shifts: the last letter to the first
and other letters to its right.'''
while x==14:
    z=str(input("Enter a list:"))
    m=z[-1]
    for i in range(len(z)-1):
        m+=z[i]  
    print(m)
    break

'''11.4.22 wap to input a dictionary with key as usernames
and values as passwords. Ask the user for their login if true then...'''
while x==15:
        def authenticate(users,loginid,password):
            if loginid in users:
                if users[loginid]==password:
                    res="Access Granted"
                else:
                    res="Wrong credentials"
                return res
        users={'dish':'1234','aditya':'5678','kushal':'6593','ankit':'3571'}
        uid=input("Enter login id:")
        pwd=input("Enter password:")
        l=authenticate(users,uid,pwd)
        print(l,'for',uid)
        break

        
'''12.4.22 wap to prompt user to enter a sentence followed by 'ennter'
->print original string
->no. of words
->no. of characters (incl whitespaces.'''
while x==16:
    d=input("Enter a sentence:")
    wrds=0
    print("Original string:",d)
    for i in d:
        if i==" ":
            wrds+=1
    wrds+=1
    print("No. of words:", wrds)
    print("No. of characters including whitespaces:", len(d))
    break

'''13.4.22 write a short python code that prints the
longest word in a list of words.'''
while x==17:
    p= eval(input("Enter a list of words:"))
    a=p[0]
    for i in p:
        if len(i)>len(a):
            a=i
    print(a)
    break

''' 13.4.22 wap which checks the format of a number '''
while x == 18:
    a =input("enter the number")
    if a[3] and a[7] == '-':
        print("number legal")
    else:
        print('number not legal')
    break

'''13.4.22 wap to create a list which has all integers less than 100 and are multiples of 3 or 5'''
while x == 19:
    a = []
    for i in range(101):
        if i%5 == 0 or i%3 == 0:
            a.append(i)
    print(a)
    break

'''13.4.22 wap to swap the values assigned and prints the result'''   
while x == 20:
    first = "jimmy"
    second = "johny"
    print("original first-",first,"original second-",second)
    first,second = second,first
    print("new first-",first,"new second-",second)
    break

'''19.4.22 wap to calculate area of cone and cylinder.
add them and hence find the total cost with taxes.'''
while x==21:
    print("Enter values for cone.")
    r=float(input("Enter radius of cone/cylinder(in m):"))
    l=float(input("Enter slant height of cone (in m):"))
    aoc=3.14*r*l
    print("Area of cone=",aoc,"m^2.")
    print("Enter values for cylinder.")
    h=float(input("Enter height of cylinder:"))
    aocy=2*3.14*r*h
    print("Area of cylinder=",aocy,"m^2.")
    print("Area of tent=",aoc+aocy,"m^2.")
    o=aoc+aocy
    u=float(input("Enter cost per m^2 of cloth for tent:"))
    print("Total cost of cloth req. for the tent incl of tax=",(u*o)*1.18,"/-")
    break

while x == 22:
    '''program 21 with functions'''
    def cyl(h,r):
        area_cyl= 2*3.14*r*h
        return(area_cyl)
    def con(l,r):
        area_con= 3.14*r*l
        return(area_con)
    def post_tax_price(cost):
        tax = 0.18*cost
        net_price = cost + tax
        return(net_price)
    print("Enter values for cylinder(in m)")
    h = float(input("Enter height of cylinder:"))
    r = float(input("Enter radius of cone/cylinder(in m):"))
    csa_cyl = cyl(h,r)
    l=float(input("Enter slant height of cone (in m):"))
    csa_con = con(l,r)
    canvas_area = csa_cyl + csa_con
    print("Area of canvas",canvas_area,"in m")
    unit_price= float(input("enter cost of cloth per m^2: "))
    total_cost = unit_price*canvas_area
    print("net price tax incl. = ",post_tax_price(total_cost))
    break

while x == 23:
    ''' calc simple interest using function, rate = 10% and 2 years'''
    def interest(principal,time = 2,rate = 0.10):
        return principal*rate*time
    prin=float(input("enter principal amount: "))
    print("simple interest with default roi and time value: ")
    sil= interest(prin)
    print("Rs.",sil)
    roi = float(input("enter rate of interest: "))
    print("simple interest with ur provided roi snd time is: ")
    si2 = interest(prin,time,roi/100)
    print("rs.",si2)
    break

while x == 24:
    def arcalc (x,y):
        return x+y, x-y, x*y, x/y, x%y
    num1=int(input("Enter no.1:"))
    num2=int(input("Enter no.2:"))
    add, sub, mult, div, mod= arcalc(num1, num2)
    print("Sum of given no.s=",add)
    print("Difference of given no.s=",sub)
    print("Product of given no.s=",mult)
    print("Division of given no.s=",div)
    print("Modulo of given no.s=",mod)
    break

'''21.4.22'''
while x==25:
    def LShift(Arr,n):
        L=len(Arr)
        for x in range(0, n):
            y=Arr[0]
            for i in range(0,L-1):
                Arr[i]=Arr[i+1]
            Arr[L-1]=y
        print(Arr)
    array=eval(input("Enter an array:"))
    num=int(input("Enter no. of places to shift:"))
    LShift(array,num)
    break

while x==26:
    def octtoothers(n):
        print("Octal no.:",n)
        numString=str(n)
        decNum=int(numString,8)
        print("No. in decimal:",decNum)
        print("No. in binary:",bin(decNum))
        print("No. in hexadecimal:",hex(decNum))
    num=int(input("Enter an octal no.:"))
    octtoothers(num)
    break

while x==27:
    def ASeries(init,step):
        return init,init+step,init+2*step,init+3*step
    inii=int(input("Enter the first term of AP:"))
    st=int(input("Enter the step value of AP:"))
    print("Series with first term",inii,"&step value",st,"is:")
    t1,t2,t3,t4=ASeries(inii,st)
    print('(',t1,',',t2,',',t3,',',t4,')')
    break
    
'''22.4.22'''
while x==28:
    def HCF(n1,n2):
        count=0
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                count=i
        print("HCF=",count)

    def LCM(n3,n4):
        count1=0
        for i in range(1,n3*n4+1):
            if i%n3==0 and i%n4==0:
                count1=i
                break
        print("LCM=",count1)

    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    HCF(num1,num2)
    LCM(num1,num2)
    break

'''25.4.22'''
while x==29:
    def volume(l,w,h):
        vol_box=l*w*h
        return vol_box
    print("Enter values for the box:")
    l=float(input("Enter length of box:"))
    w=float(input("Enter width of box:"))
    h=float(input("Enter height of box:"))
    volume_box=volume(l,w,h)
    print("Volume of box=",volume_box,"m^3.")
    break

'''26.4.22'''
while x==30:
    def nthRoot (x,n=2):
        print(x**(1/n))
    x=float(input("Enter value for x:"))
    o=input("Do you wish to enter value for n? (y/n):")
    if o=='y':
        n1=float(input("Enter value for n:"))
        nthRoot(x,n1)
    elif o=='n':
        nthRoot(x)
        break

while x==31:
    def dollar (d,r):
        rupee=d*r
        return (rupee)
    print("Enter amount:")
    d1=float(input("Enter value in dollars:"))
    r1=float(input("Enter current value of 1$ in rupee:"))
    m1=dollar(d1,r1)
    print("Dollar converted to rupee=",m1,"/-")
    break

while x==32:
    def equi (a,b):
        d=(b-a)/3
        return a,a+d,a+2*d,a+3*d
    n=float(input("Enter first number:"))
    m=float(input("Enter second number:"))
    a1,a2,a3,a4=equi(n,m)
    print(a1,',',a2,',',a3,',',a4)
    break

    
