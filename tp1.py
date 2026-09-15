import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def distanceCoord(self, a, b):
        return math.sqrt((self._x - a) ** 2 + (self._y - b) ** 2)

    def distancePoint(self, camarade):
        return self.distanceCoord(camarade.x, camarade.y)

    def __str__(self):
        return f"({self._x}, {self._y})"


class Cercle:
    def __init__(self, rayon, centre=None):
        self._rayon = rayon
        self._centre = centre if centre else Point()

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, value):
        self._rayon = value

    @property
    def centre(self):
        return self._centre

    @centre.setter
    def centre(self, value):
        self._centre = value

    def diametre(self):
        return 2 * self._rayon

    def perimetre(self):
        return 2 * math.pi * self._rayon

    def surface(self):
        return math.pi * self._rayon ** 2

    def estSecant(self, autre):
        d = self._centre.distancePoint(autre.centre)
        return abs(self._rayon - autre.rayon) < d < self._rayon + autre.rayon

    def contientPoint(self, point):
        return self._centre.distancePoint(point) <= self._rayon

class Rectangle:
    def __init__(self, bas_gauche=None, longueur=1.0, hauteur=1.0, haut_droit=None):
        self._bas_gauche = bas_gauche if bas_gauche else Point()
        if haut_droit:
            self._longueur = haut_droit.x - self._bas_gauche.x
            self._hauteur = haut_droit.y - self._bas_gauche.y
        else:
            self._longueur = longueur
            self._hauteur = hauteur

    @property
    def bas_gauche(self):
        return self._bas_gauche

    @bas_gauche.setter
    def bas_gauche(self, point):
        self._bas_gauche = point

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, value):
        self._longueur = value

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, value):
        self._hauteur = value

    def surface(self):
        return self._longueur * self._hauteur

    def perimetre(self):
        return 2 * (self._longueur + self._hauteur)

    def pointBasGauche(self):
        return self._bas_gauche

    def pointBasDroit(self):
        return Point(self._bas_gauche.x + self._longueur, self._bas_gauche.y)

    def pointHautGauche(self):
        return Point(self._bas_gauche.x, self._bas_gauche.y + self._hauteur)

    def pointHautDroit(self):
        return Point(self._bas_gauche.x + self._longueur, self._bas_gauche.y + self._hauteur)

    def contientPoint(self, point):
        dans_x = self._bas_gauche.x <= point.x <= self._bas_gauche.x + self._longueur
        dans_y = self._bas_gauche.y <= point.y <= self._bas_gauche.y + self._hauteur
        return dans_x and dans_y


class TriangleRectangle:
    def __init__(self, cote1, cote2, point_angle_droit=None):
        self._cote1 = cote1
        self._cote2 = cote2
        self._point_angle_droit = point_angle_droit if point_angle_droit else Point()

    @property
    def cote1(self):
        return self._cote1

    @cote1.setter
    def cote1(self, value):
        self._cote1 = value

    @property
    def cote2(self):
        return self._cote2

    @cote2.setter
    def cote2(self, value):
        self._cote2 = value

    @property
    def point_angle_droit(self):
        return self._point_angle_droit

    @point_angle_droit.setter
    def point_angle_droit(self, point):
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
    try:
        p1 = Point("lala", 4)
    except TypeError:
        print("UNE STRING N'EST PAS UN POINT ! ")
    except Exception as e:
        print(f"Erreur : {e}")
    else:
        print("le point cree est : {p1} ")


    try:
        c1 = Cercle(-5)
    except TypeError as t :
        print(f"error de type: {t}")
    except ValueError as v:
        print(f"value error : {v}")
    except Exception as e :
        print(f"Error : {e}")

    try:
        r1 = Rectangle(Point(4, 4), haut_droit=Point(1, 1))  # haut_droit mal placé
    except TypeError as t:
        print(f"Erreur de type : {t}")
    except ValueError as v:
        print(f"Erreur de valeur : {v}")
    except Exception as e:
        print(f"Erreur : {e}")
    else:
        print(f"success, surface = {r1.surface()}")

    try:
        t1 = TriangleRectangle(-3, 4)
    except TypeError as t:
        print(f"Erreur de type : {t}")
    except ValueError as v:
        print(f"Erreur de valeur : {v}")
    except Exception as e:
        print(f"Erreur inconnue : {e}")
    else:
        print(f"hypotenuse = {t1.hypotenuse()}")
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
