from multipledispatch import dispatch
import math

class Figura(object):
    def __init__(self):
        """ Konstruktor 1 """
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x: int, y: int):
        """ Konstruktor 2 """
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x: int):
        """ Konstruktor 3 """
        self.x = x

class Kolo(Figura):
    def __init__(self, r: float):
        """ Konstruktor 4 """
        self.r = r

# Funkcje pole
@dispatch(Figura)
def pole(instance: Figura):
    """ dispatch domyslny """
    print("Pole: Figura")
    return 0

# Napisz wersje 'pole' dla:
# - Prostokat (bez podania argumentów boków)
# - Prostokat (z podaniem argumentów boków jako int, int)
# - Kwadrat (bez podania argumentów boku)
# - Kwadrat (z podaniem argumentów boku jako int)
# - Kolo (bez podania argumentów promienia)
# - Kolo (z podaniem argumentów promienia jako float)
# Uzywaj print() do weryfikacji wywolan

@dispatch(Prostokat)
def pole(instance: Prostokat):
    """ dispatch Prostokat 1 """
    print("Pole: " + str(type(instance)))
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    """ dispatch Prostokat 2 """
    print("Pole: " + str(type(instance)))
    return x * y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    """ dispatch Kwadrat 1 """
    print("Pole: " + str(type(instance)))
    return instance.x * instance.x

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    """ dispatch Kwadrat 2 """
    print("Pole: " + str(type(instance)))
    return x * x

@dispatch(Kolo)
def pole(instance: Kolo):
    """ dispatch Kolo 1 """
    print("Pole: " + str(type(instance)))
    return math.pi * instance.r * instance.r

@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    """ dispatch Kolo 2 """
    return math.pi * r * r

# Polimorfizm w czasie wykonywania
def polaPowierzchni(listaFigur):
    """ zarzadzanie polami """
    for i in listaFigur:
        print(f"Pole obiektu: {pole(i)}")

if __name__ == "__main__":
    # Tworzenie obiektów
    print("=== Tworzenie obiektów ===")
    a, b, c, d = Figura(), Prostokat(2, 4), Kwadrat(2), Kolo(3)

    # Wywołania funkcji pole
    print("\n=== Wywołania funkcji pole ===")
    print(f"Pole prostokąta (2x4): {pole(b)}")
    print(f"Pole kwadratu (bok=2): {pole(c)}")
    print(f"Pole koła (r=3): {pole(d)}")

    # Zmiana wymiarów za pomocą funkcji pole
    print("\n=== Zmiana wymiarów ===")
    print(f"Pole prostokąta po zmianie na 5x6: {pole(b, 5, 6)}")
    print(f"Pole kwadratu po zmianie boku na 7: {pole(c, 7)}")
    print(f"Pole koła po zmianie promienia na 4: {pole(d, 4.0)}")

    # Polimorfizm
    print("\n=== Polimorfizm w czasie wykonywania ===")
    polaPowierzchni([a, b, c, d])

