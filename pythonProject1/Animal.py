class Animal:
    legs = 4

    def __init__(self, name, color=None, breed=None):  # constructor
        self.__name = name
        self.color = color
        self.breed = breed
        self.legs = 3

    def __str__(self):
        return f'{type(self)}:{self.__name}'

    def set_name(self, name):
        # check permissions
        return self.__name

    # @property -> getter
    # @name.setter
    # @name.deleter

    def get_name(self):
        return self.__name
