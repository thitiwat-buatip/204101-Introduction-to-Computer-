# 570610565 Thitiwat buatip Lab 02 ข้อ 4
print("First Equation")

m1 = float(input("Input m1: "))
b1 = float(input("Input b1: "))

print("Second Equation")

m2 = float(input("Input m2: "))
b2 = float(input("Input b2: "))

temp_m = m1 - m2
temp_b = b1 - b2

x = -temp_b/1

y = m1*x + b1

print('The point of intersection is at x =', "%.2f"%x, 'and y =', "%.2f"%y)