print('Factorial'.center(50))
num=input('Enter number: ')
if(num.isdigit()==True):
    num=int(num)
    mainNum=num
    if(num==0 or num==1):
        factorial=1
    else:
        factorial=1
        while(num>1):
            factorial=factorial*num
            num-=1
    print('Factorial of',mainNum,'is',factorial)
else:
    print('!!! Only numbers are allowed !!!')