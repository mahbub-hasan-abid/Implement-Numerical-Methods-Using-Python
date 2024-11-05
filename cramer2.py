a1=float(input("Enter a1: "))
b1=float(input("Enter b1: "))
c1=float(input("Enter c1: "))
d1=float(input("Enter d1: "))

a2=float(input("Enter a2: "))
b2=float(input("Enter b2: "))
c2=float(input("Enter c2: "))
d2=float(input("Enter d2: "))

a3=float(input("Enter a3: "))
b3=float(input("Enter b3: "))
c3=float(input("Enter c3: "))
d3=float(input("Enter d3: "))
def determinate(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    return a1*(b2*c3-b3*c2)-b1*(a2*c3-a3*c2)+c1*(a2*b3-a3*b2)
D= determinate(a1,a2,a3,b1,b2,b3,c1,c2,c3)
Dx=determinate(d1,d2,d3,b1,b2,b3,c1,c2,c3)
Dy=determinate(a1,a2,a3,d1,d2,d3,c1,c2,c3)
Dz=determinate(a1,a2,a3,b1,b2,b3,d1,d2,d3)
if D!=0:
 x=Dx/D
 y=Dy/D
 z=Dz/D

 print("solution     ")
 print("the value of x ", x)
 print("the value of y ", y)
 print("the value of z ", z)

else:
    print("the determinant is zero,no unique solution exist")



