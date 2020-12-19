class Fractie:
    def __init__(self, numitor, numarator):
        if numitor == 0:
            raise ValueError("numitor != 0")
        self.numitor = numitor
        self.numarator = numarator

    def __str__(self):
        print(self.numitor)
        print("---")
        print(self.numarator)

    def __add__(self, other):
        return self.numarator * other.numitor + self.numitor * other.numarator, self.numitor * other.numitor

    def __sub__(self, other):
        return self.numarator * other.numitor - self.numitor * other.numarator, self.numitor * other.numitor

    def inverse(self):
        return self.numarator/self.numitor

my_fraction = Fractie(10,2)
my_fraction2= Fractie(10,2)
print(my_fraction.numitor)
print(my_fraction.numarator)

Fractie.__str__(my_fraction)
print(my_fraction.inverse())
print(Fractie.__add__(my_fraction, my_fraction2))
print(Fractie.__sub__(my_fraction, my_fraction2))
