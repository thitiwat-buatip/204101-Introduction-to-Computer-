# LAB 03 1. – Circle or Square 570610565

# input type
input_Type = input("“Input c if you want to calculate the area of a circle, others for square : ")

# calculate 
if input_Type == "c" or input_Type == "C" :
    r = float(input("Radius : "))
    area = 3.14159*(r**2)

else :
    side = float(input("Side : "))
    area = side**2

# Display
print("Area = ", area) 