inp=input('Enter the word or sentence => ')
inpRef=inp.replace(' ','')
specChars = "!@#$%^&*()_+=-[]{}|\\;:'\"<>,./?"
for chars in specChars:
    inpRef=inpRef.replace(chars,'')
i=len(inpRef)
revInp=''
while(i>0):
    revInp+=inpRef[i-1]
    i-=1
if(inpRef==revInp):
    print('Your given string is =>',inp,'\n & it is a palindrome')
else:
    print('Your given string is =>',inp,'\n & it is not a palindrome')