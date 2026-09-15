import math
print("Je vais diviser ces nombres tu vas me donner : ")
a= int(input("Donne moi une nombre: "))
b =int(input("Donne moi une autre nombre : "))

try:
    division = a / b
except ZeroDivisionError:
    print("C'est pas possible de diviser par zero !")
except ValueError:
    print("Le nombre n'est pas le bon valeur")
except TypeError:
    print("Vous n'avez pas mis un nombre bad boy")
except Exception as e:
    print(f"Je sais pas qu'est que t'as fait mais cest haram : {e}")
else:
    print(f"le resultat est : {division} ")


