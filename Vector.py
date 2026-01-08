class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __init__(self, vector):
        self.__x = vector.getX()
        self.__y = vector.getY()

    def scale(self, scalar):
        self.__x *= scalar
        self.__y *= scalar

    def div(self, scalar):
        self.__x /= scalar
        self.__y /= scalar

    def add(self, vector):
        self.__x += vector.getX()
        self.__y += vector.getY()

    def sub(self, vector):
        self.__x -= vector.getX()
        self.__y -= vector.getY()

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def __str__(self):
        return f"({self.__x},{self.__y})"