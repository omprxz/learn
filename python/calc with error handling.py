print('Calculator with Error handling'.center(50))
fnum=input('Enter the first number: ')
if (fnum.isdigit()==False):
    while(fnum.isdigit()==False):
        print('!!! Invalid value !!!')
        fnum=input('Enter the first number: ')
    fnum=int(fnum)
else:
    fnum=int(fnum)
oper=input('Enter operation to perform ie +,-,*,/ : ')
if (oper not in '+-*/' or oper==''):
    while(oper not in '+-*/' or oper==''):
        print('!!! Invalid operation selected !!!')
        oper=input('Enter operation to perform ie +,-,*,/ : ')
snum=input('Enter the second number: ')
if (snum.isdigit()==False):
    while(snum.isdigit()==False):
        print('!!! Invalid value !!!')
        snum=input('Enter the second number: ')
    snum=int(snum)
else:
    snum=int(snum)
match oper:
    case '+': print(fnum,oper,snum,'=',fnum+snum)
    case '-': print(fnum,oper,snum,'=',fnum-snum)
    case '*': print(fnum,oper,snum,'=',fnum*snum)
    case '/': print(fnum,oper,snum,'=',fnum/snum)