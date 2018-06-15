import math
from turtle import *

##Law of Cosine
def myTriangle():
    firstSide = int(input("Insert first side length:"))
    secondSide = int(input("Insert second side length:"))
    firstAngle = int(input("Insert an angle:"))

    thirdSide = (pow(firstSide, 2)) + (pow(secondSide, 2)) - ((2)*(firstSide)*(secondSide)*(math.cos(math.radians(firstAngle))))
    thirdSide1 = (pow(thirdSide , 0.5))

    secondAngle = math.acos(((pow(secondSide, 2)) - (pow(firstSide, 2)) - (pow(thirdSide1, 2)))/ ((-2)*(firstSide)*(thirdSide1)))
    secondAngle1 = math.degrees(secondAngle)

    thirdAngle = 180 - firstAngle - secondAngle1

    print ("Third Side:")
    print (thirdSide1)
    print ("Second Angle:")
    print (secondAngle1)

    ## Turtle Drawing ##
    ness = Turtle()
    ness.goto = (0,0)
    ness.down()
    ness.forward(firstSide)
    ness.left(180-thirdAngle)
    ness.forward(secondSide)
    ness.left(180-firstAngle)
    ness.forward(thirdSide1)

    print ("First Angle:")
    print (firstAngle)
    print ("Second Angle")
    print (secondAngle)
    print ("Third Angle")
    print (thirdAngle)

if __name__ == "__main__":
    myTriangle()
