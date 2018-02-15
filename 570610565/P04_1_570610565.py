# โปรแกรมตัดเกรด LAB04 570610565

point = int(input("Please enter the student's score : "))
garde = "F"

if point >= 0 and point <= 100 :
    if point >= 40 and point < 50 :
        garde = "D"
    elif point >= 50 and point < 65 :
        garde = "C"
    elif point >= 65 and point < 80 :
        garde = "B"
    elif point >= 80 :
        garde = "A"
    print("Grade : ",garde)    
else:
    print("The score must be at least 0 and not more than 100.")            