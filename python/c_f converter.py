inTemp=int(input("Enter Temperature (only numbers or decimal value): "))
tempIn=input("It is in Cencius or Farenhite\nC => Celcius & F => Farenhite :")
if(tempIn=="c"):
    finTemp=(inTemp*9/5)+32
    tempType="Farenhite"
elif(tempIn=="f"):
    finTemp=(inTemp-32)*5/9
    tempType="Celcius"
else:
    print("Invalid temperature type\Closing program")
print("Temperature in ",tempType,"is ",finTemp)
