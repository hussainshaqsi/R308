import math
class Point:
    def __init__(self,x:float=0.0,y:float=0.0):
        self.__x = x
        self.__y = y

    def distanceCoord(self,x:float,y:float)-> float:
        return math.sqrt((self.__x_x) * (self.__x_x) + (self.__y_y) * (self.__y_y))

    def distancePoint(self,camarade: Point )-> float:
        return self.distanceCoord(camarade.x,camarade.y)

    def __str__(self):
        return f"Point(x={self.__x},y={self.__y})"

    if __name__ == "__main__":
        p1:Point = Point()
        p2:Point = Point(2,3)
        print(p2.distancePoint(p1))
        print(p1.distanceCoord(2,2))

