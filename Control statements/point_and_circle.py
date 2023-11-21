# Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) and 
# determine whether the point is inside the circle, on the circle or outside the circle

a=int(input("x coordinate of centre "))
b=int(input("y coordinate of centre "))
r=int(input("Radius "))
x=int(input("x coordinate of point "))
y=int(input("y coordinate of point "))
d=((x-a)**2 + (y-b)**2)**0.5
if d<r:
    print('Inside')
elif d==r:
    print('On the circle')
else:
    print('Outside the circle')