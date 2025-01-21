class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def describe(self):
        return (f"{self.brand} buty, rozmiar {self.size}. Brak szczegółowych informacji")

class Sneaker(Shoe):
    def describe(self):
        return (f"{self.brand} Sneaker, rozmiar {self.size} - idealne do biegania")

class Boot(Shoe):
    def describe(self):
        return (f"{self.brand} Boot, rozmiar {self.size} - idealne na zimę")

class Heels(Shoe):
    def describe(self):
        return (f"{self.brand} Heels, rozmiar {self.size} - idealne na eleganckie wyjścia")
