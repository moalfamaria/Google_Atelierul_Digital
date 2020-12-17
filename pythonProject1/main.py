from cat import cat
from Dog import Dog

print(cat.legs)
print(Dog.legs
      # in python exista doar overriding, decoratori
#polimorfism clasic
print(len('abc'))
print(len([1,2,3,4]))
#apelare metoda din parinte prin super

#interatori, la baze niste clase
#iterabil, instanta de clasa, le parcurgem
#interator = clasa,
class MyIterator:
    pass

my_iterable = None
for i in [1,2,3]:
    print(i)