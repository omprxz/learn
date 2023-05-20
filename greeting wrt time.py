import time
name=input('Enter your name: ')
hr=int(time.strftime('%H'))
if(hr<12):
    print('Good morning',name,'sir')
elif(hr>18):
    print('Good evening',name,'sir')
elif(hr>=12):
    print('Good afternoon',name,'sir')
else:
    print('Time is not valid ;)')
print('Current time is',time.strftime('%H:%M:%S'))
