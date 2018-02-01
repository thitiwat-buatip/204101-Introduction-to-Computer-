# 570610565 Thitiwat buatip Lab 02 ข้อ 3
#BMIProgram

weight = float(input("Input weight in kg: "))
height = float(input("Input height in cm: "))

bmi = weight/((height/100)**2)

print("Weight = ", "%.2f"%weight, "Kg., Height = ", "%.2f"%height ,"cm., BMI = ", "%.2f"%bmi )