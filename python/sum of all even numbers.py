i=0
sum=0
while True:
    if(i%2==0):
        sum+=i
        i+=2
    if(i>100):
        break
print('Sum of all even numbers between 1 & 100 is',sum)