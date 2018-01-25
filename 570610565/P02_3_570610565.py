#570610565 Thitiwat Buatip
#BMIProgram

weight = float(input("Input weight in kg: "))
height = float(input("Input height in cm: "))

bmi = weight/((height/100)**2)

print("Weight = ", round(weight,2), "Kg., Height = ", round(height,2) ,"cm, BMI = ", round(bmi,2) )