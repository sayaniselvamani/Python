#write a program to calculate perimeter of the circle with radius 10.2
#c = 2pir
radius = 10.2
pi = 3.14
circlePerimeter = 2*pi*radius
print("Perimeter of circle is:",circlePerimeter)

#write a program to calculate area of circle with radius (float)
#(collect using input function)
#c = pirr
Radius = float(input("please enter the radius for circle:"))
circleArea = pi*Radius*Radius
print("Area of circle is:",circleArea)
print("Area of circle is {1} with Radius{0}".format(Radius,circleArea))

#write a program to calculate perimeter of the circle with radius (float)
#(collect it through input function)
R = float(input("please enter the radius:"))
Perimeter = 2*pi*R
print("Perimeter of circle is:",Perimeter)
print("Perimeter of circle is:",int(Perimeter))

#calculate Area of cone (area of cone = 0.33 * pi * r * r * h) (int)
#Collect radius and height from user
radiusCone = int(input("please enter the radius for cone:"))
heightCone = int(input("please enter the radius for cone:"))
areaOfCone = 0.33 * pi * radiusCone * radiusCone * heightCone
print("Area of cone is:",areaOfCone)

