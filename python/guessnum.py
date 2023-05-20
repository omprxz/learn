import random
print("Guess The Number".center(50))
randNum=random.randint(1,1000)
print(randNum)
inp1=int(input("Guess the number: "))
while(inp1!=randNum):
    if(inp1<=randNum):
        print("You guessed the smaller number.")
        inp1=int(input("Guess the number between 1 and 100: ")) 
    elif(inp1>=randNum):
        print("You guessed the greater number.")
        inp1=int(input("Guess the number between 1 and 100: ")) 
    else:
        print("Invalid guess you dumb ass :(")
print("Wow,You guessed the number correctly :>")