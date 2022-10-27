
#ex1
class Cerc:
# Atribute
    raza = 0
    culoare = None
# Constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
# Metode
    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare} si are raza de {self.raza} cm.')
    def aria(self):
        PI = 3.14
        return PI * (self.raza ** 2)
    def diametru(self):
        return 2 * self.raza
    def circumferinta(self):
        PI = 3.14
        return 2 * PI * self.raza

cerculet_1 = Cerc(2, 'neagra')
print(f'Aria cercului 1: {cerculet_1.aria()}')
print(f'Diametrul cercului 1: {cerculet_1.diametru()}')
print(f'Circumferinta cercului 1: {cerculet_1.circumferinta()}')
cerculet_1.descrie_cerc()
print(' ')
cerculet_2 = Cerc(6, 'rosu')
print(f'Aria cercului 2: {cerculet_2.aria()}')
print(f'Diametrul cercului 2: {cerculet_2.diametru()}')
print(f'Circumferinta cercului 2: {cerculet_2.circumferinta()}')
cerculet_2.descrie_cerc()

#ex.2

