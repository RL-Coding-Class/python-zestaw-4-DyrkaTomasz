from multipledispatch import dispatch
import math

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        # dokoncz definicje

class Kwadrat(Prostokat):
    def __init__(self, x: int):
        self.x = x
        # dokoncz definicje

class Kolo(Figura):
    def __init__(self, r: float):
        self.r = r
        # dokoncz definicje

# Funkcje pole
@dispatch(Figura)
def pole(instance: Figura):
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
    print("Pole: Prostokat")
    print(instance.x * instance.y)
    return 0

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x: int, y: int):
    print("Pole: Prostokat")
    print(x * y)
    return 0

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    print("Pole: Kwadrat")
    print(instance.x * instance.x)
    return 0

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x: int):
    print("Pole: Kwadrat")
    print(x * x)
    return 0

@dispatch(Kolo)
def pole(instance: Kolo):
    print("Pole: Kolo")
    print(math.pi * instance.r * instance.r)
    return 0

@dispatch(Kolo, float)
def pole(instance: Kolo, r: float):
    print("Pole: Kolo")
    print(math.pi * r * r)
    return 0

# Polimorfizm w czasie wykonywania
def polaPowierzchni(listaFigur):
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

