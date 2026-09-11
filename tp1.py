"""import math
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
"""
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distanceCoord(self, a, b):
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)

    def distancePoint(self, camarade):
        return self.distanceCoord(camarade.x, camarade.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Cercle:
    def __init__(self, rayon, centre=None):
        self.rayon = rayon
        self.centre = centre if centre else Point()

    def diametre(self):
        return 2 * self.rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def surface(self):
        return math.pi * self.rayon ** 2

    def estSecant(self, autre):
        d = self.centre.distancePoint(autre.centre)
        return abs(self.rayon - autre.rayon) < d < self.rayon + autre.rayon

    def contientPoint(self, point):
        return self.centre.distancePoint(point) <= self.rayon


class Rectangle:
    def __init__(self, bas_gauche=None, longueur=1.0, hauteur=1.0, haut_droit=None):
        self.bas_gauche = bas_gauche if bas_gauche else Point()
        if haut_droit:
            self.longueur = haut_droit.x - self.bas_gauche.x
            self.hauteur = haut_droit.y - self.bas_gauche.y
        else:
            self.longueur = longueur
            self.hauteur = hauteur

    def surface(self):
        return self.longueur * self.hauteur

    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    def pointBasGauche(self):
        return self.bas_gauche

    def pointBasDroit(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y)

    def pointHautGauche(self):
        return Point(self.bas_gauche.x, self.bas_gauche.y + self.hauteur)

    def pointHautDroit(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y + self.hauteur)

    def contientPoint(self, point):
        return (self.bas_gauche.x <= point.x <= self.bas_gauche.x + self.longueur and
                self.bas_gauche.y <= point.y <= self.bas_gauche.y + self.hauteur)


class TriangleRectangle:
    def __init__(self, cote1, cote2, point_angle_droit=None):
        self.cote1 = cote1
        self.cote2 = cote2
        self.point_angle_droit = point_angle_droit if point_angle_droit else Point()

    def hypotenuse(self):
        return math.sqrt(self.cote1 ** 2 + self.cote2 ** 2)

    def perimetre(self):
        return self.cote1 + self.cote2 + self.hypotenuse()

    def surface(self):
        return (self.cote1 * self.cote2) / 2

    def estIsocele(self):
        return self.cote1 == self.cote2


def Principale():
    p1 = Point()
    p2 = Point(3, 4)
    print(p1)
    print(p2)
    print(p1.distanceCoord(3, 4))
    print(p1.distancePoint(p2))

    c1 = Cercle(5)
    c2 = Cercle(3, Point(4, 0))
    print(c1.diametre())
    print(c1.perimetre())
    print(c1.surface())
    print(c1.estSecant(c2))
    print(c1.contientPoint(p2))

    r1 = Rectangle()
    r2 = Rectangle(Point(1, 1), 4, 2)
    r3 = Rectangle(Point(0, 0), haut_droit=Point(4, 2))
    print(r2.surface())
    print(r2.perimetre())
    print(r2.pointBasGauche())
    print(r2.pointBasDroit())
    print(r2.pointHautGauche())
    print(r2.pointHautDroit())
    print(r2.contientPoint(p2))

    t1 = TriangleRectangle(3, 4)
    t2 = TriangleRectangle(5, 5, Point(1, 1))
    print(t1.hypotenuse())
    print(t1.perimetre())
    print(t1.surface())
    print(t1.estIsocele())
    print(t2.estIsocele())


if __name__ == "__main__":
    Principale()