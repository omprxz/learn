rad=input('Enter the radius of the circle: ')
unit=input('Type unit: ')
if(rad.isdigit()==True):
    rad=int(rad)
    def areaCircle(a):
        area=22*rad*rad/7
        return area
    print('Area of circle having radius is',areaCircle(rad),unit)
else:
    print('!!! Only numbers allowed in radius.')