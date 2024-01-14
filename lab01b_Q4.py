import math
#0 input 
aStr, bStr, cStr = input(). split()
a= float(aStr)
b= float(bStr)
c= float(cStr)
#1 find min max
min_value = min(a, b, c)
max_value = max(a, b, c)
print(f"min = {min_value}")
print(f"max = {max_value}")
#2 arrange in ascending order
sorted_values = sorted([a, b, c])
print(f"arrange in ascending order:{sorted_values}")






