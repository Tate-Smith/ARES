import math
from ARES.Ship import Ship
from ARES.Vector import Vector

class Space:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__center = Vector(0,0)
        self.__ship = Ship(0, 0)
        self.__target = Vector(0,0)

    def atLocation(self):
        # determine if the ship has succesfully reached the location
        position = self.__ship.getPosition
        velocity = self.__ship.getVelocity
        return position.getX() == self.__target.getX() and position.getY() == self.__target.getY and velocity.getX() == 0 and velocity.getY() == 0
    
    def setShipPosition(self, x, y):
        self.__ship.setPositon(x, y)

    def setTargetPosition(self, x, y):
        self.__target.setPosition(x, y)

    def calculateDistance(self):
        # get the distance between the target and ship
        shipPosition = self.__ship.getPosition
        x = shipPosition.getX() - self.__target.getX()
        y = shipPosition.getY() - self.__target.getY()
        x *= x
        y *= y
        return math.sqrt(x + y)