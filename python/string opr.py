string1=input('Enter string: ')
oper=input('Enter operation\n1 for concatenation\n2 for substring extraction => ')
if(oper=='1'):
    string2=input('Enter second string: ')
    print('Concatenated string is => ',string1,string2)
elif(oper=='2'):
    start=input('Enter start index: ')
    if(start==''): start=0
    else: start=int(start)
    end=input('Enter number of chars: ')
    if(end==''): end=len(string1)
    else: end=int(end)
    step=input('Enter step: ')
    if(step==''): step=1
    else: step=int(step)
    print('Extracted substring is',string1[start:end:step])
else:
    print('!!! Invalid operation code !!!')