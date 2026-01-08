import math
from ARES.Vector import Vector

class Ship:
    def __init__(self, x, y):
        self.__position = Vector(x, y)
        self.__velocity = Vector(0, 0)
        self.__fuel = 200.0
        self.__mass = 700.0
        self.__thrust = 280.0 # mass flow rate * exhaust velocity, 3500 * 0.08
        self.__orientation = 0.0
        self.__angularVelocity = 0.0
        self.__inertia = 1200
        self.__rotationalThrust = 40

    def getPosition(self): 
        return self.__position
    
    def getVelocity(self): 
        return self.__velocity
    
    def getAmountOfFuel(self): 
        return self.__fuel
    
    def forwardThruster(self, throttle):
        # throttle is a double in the range 1 - 0 inclusive
        # make sure there is fuel
        if (self.__fuel <= 0):
            return
        
        force = throttle * self.__thrust
        # find acceleration based on direction
        # get direction vector based on orientation
        acceleration = Vector(math.cos(self.__orientation), math.sin(self.__orientation))
        # acceleration = (force * directionVector) / mass
        acceleration.scale(force / self.__mass)
        self.__velocity.add(acceleration.scale(0.01))
        # create temp velocity var to avoid changing previous
        vel = Vector(self.__velocity)
        self.__position.add(vel.scale(0.01))

        # get amount of fuel burned
        fuel_burned = 0.08 * throttle * 0.01
        self.__fuel - fuel_burned
        # cant go lower than 0 fuel
        if (self.__fuel < 0): self.__fuel = 0

    def reverseThruster(self, throttle):
        # throttle is a double in the range 1 - 0 inclusive
        # make sure there is fuel
        if (self.__fuel <= 0):
            return
        
        force = throttle * self.__thrust
        # find acceleration based on direction
        # get direction vector based on orientation
        acceleration = Vector(-math.cos(self.__orientation), -math.sin(self.__orientation))
        # acceleration = (force * directionVector) / mass
        acceleration.scale(force / self.__mass)
        self.__velocity.add(acceleration.scale(0.01))
        # create temp velocity var to avoid changing previous
        vel = Vector(self.__velocity)
        self.__position.add(vel.scale(0.01))

        # get amount of fuel burned
        fuel_burned = 0.08 * throttle * 0.01
        self.__fuel - fuel_burned
        # cant go lower than 0 fuel
        if (self.__fuel < 0): self.__fuel = 0

    def turnRight(self, throttle):
        # angular momentum = torque / inertia
        torque = -throttle * self.__rotationalThrust
        angularMomentum = torque / self.__inertia
        self.__angularVelocity += (angularMomentum * 0.01) * 0.995

    def turnLeft(self, throttle):
        # angular momentum = torque / inertia
        torque = throttle * self.__rotationalThrust
        angularMomentum = torque / self.__inertia
        self.__angularVelocity += (angularMomentum * 0.01) * 0.995

    def updateRotation(self):
        self.__orientation += self.__angularVelocity * 0.01