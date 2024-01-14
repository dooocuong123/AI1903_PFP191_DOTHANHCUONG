import math

#Q1 input 
aStr, bStr, cStr, xStr = input(). split()
a= float(aStr)
b= float(bStr)
c= float(cStr)
x= float(xStr)
#Q2 calculate S1
S1 = a*x**2 +b*x+c
#Q3 calculate S2
if b ** 2 - 4 * a * c > 0:
    S2 = math.sqrt(b ** 2 - 4 * a * c)
else:
    S2=0
#4 check are three sides of triangle
result = True if a + b > c and a + c > b and b + c > a else False
#5
if result:
    perimeter = a + b + c
    #use Heron formula
    p = perimeter / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
else:
    print(f"{a}, {b}, {c} are not sides of a triangle")







