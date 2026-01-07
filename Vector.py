class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

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

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y