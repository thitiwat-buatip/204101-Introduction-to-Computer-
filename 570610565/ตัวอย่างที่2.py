# สลับค่าในตัวแปร


a = float(input("Input variable A : "))
b = float(input("Input variabel B : "))
# Display Original Values of 2 Variables
print("----- Befor swap process -----")
print("A -> ",a)
print("B -> ",b)

# Swaping process of 2 variables
a , b = b , a

print("----- After swap process -----")
print("A -> ",a)
print("B -> ",b)