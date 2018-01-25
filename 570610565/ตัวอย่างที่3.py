arrayNum = [0,0,0]
arrayString = ["first","second","third"]

for i in range(0,3) :
    arrayNum[i]= float(input("Input " + arrayString[i] +" number : "))

print("Average = ",sum(arrayNum)/len(arrayNum))