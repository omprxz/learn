# Questions
# Options
# Correct answers
# Winnings
# FInal Winnings

print('KBC'.center(50))
name=input('Whta is your name: ')
name=name.capitalize()
print('Hello',name)
qna=[['Who is the prime mininster of India?',['Lalu','Nitin Gadkari','Narendra Modi','Pranav Mukharji'],3],
     ['Which is the mostly AI based chat bot?',['Google Assistant','Alexa','Siri','ChatGPT'],4],
     ['Who is the CEO of Google?',['Tim Cook','Bill Gates','Sundar Pichai','Warren Buffet'],3],
     ['Which is a back exercise',['Latpull down','Hammer curl','Squats','Plain Bench Press'],1],
     ['The Kerala Story released in which year?',['2000','2023','2022','2010'],2],
     ['Who is not a actor from below personalities?',['Mukesh Ambani','Rock','Peter Halland','Patrick'],1],
     ['Capital of India is',['Patna','Newyork City','Peris','Delhi'],4]]
roman=['i','ii','iii','iv']
winnings=[10000,50000,100000,1000000,5000000,10000000,100000000]
ready=input(name+' Are you ready to play KBC (y or n): ')
if(ready=='n'):
    print('Umhhh! OK Cancelling the game.')
else:
    print('Great',name+',','Now get ready to play...')
    for q in range(len(qna)):
        print(str(q+1)+'.',qna[q][0])
        for o in range(4):
            print(roman[o]+')',qna[q][1][o])
        ans=input('Give the answer '+name+' => ')
        while(ans.isdigit()==False):
            print('!!! Invalid Answer !!!')
            ans=input('Give the answer again '+name+' => ')
        ans=int(ans)
        while(ans<=0 and ans>4):
            ans=input('Give the answer '+name+' => ')
            while(ans.isdigit()==False):
             print('!!! Invalid Answer !!!')
             ans=input('Give the answer again '+name+' => ')
            ans=int(ans)
            print('!!! Invalid Answer !!!')
        if(ans==qna[q][2]):
            print('Wowww! You answered it right',name)
            print('You have won Rs',winnings[q])
            if(q!=6):
                cont=input('If you want to continue to next question then hit enter otherwise type "n": ')
                if(cont=='n'):
                    print('Hurrah',name,'!!! You won decent amount.\nTake your Rs',winnings[q],'to home')
                    break
            else:
                print('Hurrah',name,'!!! You won the KBC.\nTake your 10 crores to home')
        else:
            print('Ihhh! You Lost.\nNo problem Life is all about winnings and losses.\nBetter Luck Next Time'.center(50))
            break
print('KBC'.center(50))
print('Signing Off'.center(50))