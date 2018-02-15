# LAB03 2. – What Counter 570610565

x = 0 #Creat variable count

# input data 
input_1 = input("Say what : ")
if input_1 == "what" or input_1 == "What" :
    x += 1
input_1 = input("Say what : ")
if input_1 == "what" or input_1 == "What" :
    x += 1  
input_1 = input("Say what : ")
if input_1 == "what" or input_1 == "What" :
    x += 1      
input_1 = input("Say what : ")
if input_1 == "what" or input_1 == "What" :
    x += 1

# Display 
if x >= 1 :
    print("You said what ",x," time")
else :
    print("You haven't said what once")