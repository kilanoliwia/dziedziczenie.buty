class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def describe(self):
        return f"{self.brand} buty, rozmiar {self.size}. Brak szczegółowych informacji."