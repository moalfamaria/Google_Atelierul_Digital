from Animal import Animal
class cat:
    legs = 4

    def __str__(self):
        return f'{type(self)}:{self.__name}'

    def set_name(self, name):
        #check permissions
        return self.__name

    # @property -> getter
    # @name.setter
    # @name.deleter

    def get_name(self):
        return self.__name

    @staticmethod
    def speak():
        print("miau")
#self = instanta curenta
# instanta = un  obiect de acel tip
# obiect intr o variabila

#my_cat = cat(name='julia')
print(my_cat.get_name()) #acces direct la atributele unei instante => il facem privat

my_cat = cat('julia2')
print(my_cat.get_name())
print(my_cat._cat__name)
my_cat.speak()
cat.speak()
print(my_cat.legs)
print(cat.legs)
#atribute statice legs=4