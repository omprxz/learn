print("Rectangle Area Calculator".center(50))
w=int(input("Enter the rectangle width: "))
l=int(input("Enter the rectangle lengeth: "))

def recArea(w,l):
    area=w*l
    return area
print("Area of the rectangle is: ",recArea(w,l))