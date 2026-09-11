import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        self._y = y

    def distanceCoord(self, a, b):
        return math.sqrt((self._x - a) ** 2 + (self._y - b) ** 2)

    def distancePoint(self, camarade):
        return self.distanceCoord(camarade.getX(), camarade.getY())

    def __str__(self):
        return f"({self._x}, {self._y})"


class Cercle:
    def __init__(self, rayon, centre=None):
        self._rayon = rayon
        self._centre = centre if centre else Point()

    def getRayon(self):
        return self._rayon

    def setRayon(self, rayon):
        self._rayon = rayon

    def getCentre(self):
        return self._centre

    def setCentre(self, centre):
        self._centre = centre

    def diametre(self):
        return 2 * self._rayon

    def perimetre(self):
        return 2 * math.pi * self._rayon

    def surface(self):
        return math.pi * self._rayon ** 2

    def estSecant(self, autre):
        d = self._centre.distancePoint(autre.getCentre())
        return abs(self._rayon - autre.getRayon()) < d < self._rayon + autre.getRayon()

    def contientPoint(self, point):
        return self._centre.distancePoint(point) <= self._rayon


class Rectangle:
    def __init__(self, bas_gauche=None, longueur=1.0, hauteur=1.0, haut_droit=None):
        self._bas_gauche = bas_gauche if bas_gauche else Point()
        if haut_droit:
            self._longueur = haut_droit.getX() - self._bas_gauche.getX()
            self._hauteur = haut_droit.getY() - self._bas_gauche.getY()
        else:
            self._longueur = longueur
            self._hauteur = hauteur

    def getBasGauche(self):
        return self._bas_gauche

    def setBasGauche(self, point):
        self._bas_gauche = point

    def getLongueur(self):
        return self._longueur

    def setLongueur(self, longueur):
        self._longueur = longueur

    def getHauteur(self):
        return self._hauteur

    def setHauteur(self, hauteur):
        self._hauteur = hauteur

    def surface(self):
        return self._longueur * self._hauteur

    def perimetre(self):
        return 2 * (self._longueur + self._hauteur)

    def pointBasGauche(self):
        return self._bas_gauche

    def pointBasDroit(self):
        return Point(self._bas_gauche.getX() + self._longueur, self._bas_gauche.getY())

    def pointHautGauche(self):
        return Point(self._bas_gauche.getX(), self._bas_gauche.getY() + self._hauteur)

    def pointHautDroit(self):
        return Point(self._bas_gauche.getX() + self._longueur, self._bas_gauche.getY() + self._hauteur)

    def contientPoint(self, point):
        dans_x = self._bas_gauche.getX() <= point.getX() <= self._bas_gauche.getX() + self._longueur
        dans_y = self._bas_gauche.getY() <= point.getY() <= self._bas_gauche.getY() + self._hauteur
        return dans_x and dans_y


class TriangleRectangle:
    def __init__(self, cote1, cote2, point_angle_droit=None):
        self._cote1 = cote1
        self._cote2 = cote2
        self._point_angle_droit = point_angle_droit if point_angle_droit else Point()

    def getCote1(self):
        return self._cote1

    def setCote1(self, cote1):
        self._cote1 = cote1

    def getCote2(self):
        return self._cote2

    def setCote2(self, cote2):
        self._cote2 = cote2

    def getPointAngleDroit(self):
        return self._point_angle_droit

    def setPointAngleDroit(self, point):
        self._point_angle_droit = point

    def hypotenuse(self):
        return math.sqrt(self._cote1 ** 2 + self._cote2 ** 2)

    def perimetre(self):
        return self._cote1 + self._cote2 + self.hypotenuse()

    def surface(self):
        return (self._cote1 * self._cote2) / 2

    def estIsocele(self):
        return self._cote1 == self._cote2


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