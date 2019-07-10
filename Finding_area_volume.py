import math

radius = int(input("please enter the radius : "))



def volume(radius):
    formula = 4/3*math.pi*radius**3
    return formula

def area(radius):
    formula = 4*math.pi*radius**2
    return formula

print (str(volume(radius))+": this is volume")

print (str(area(radius))+": this is area")

 




