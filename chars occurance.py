string=input('Enter string: ')
findfor=input('Char to Find For: ')
i=0
z=0
for x in string:
    if(findfor.lower()==x.lower()):
        i+=1
print('Occurance count of',findfor,'in',string,'is',i)