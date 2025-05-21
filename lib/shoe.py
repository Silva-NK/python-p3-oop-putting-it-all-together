#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        self._size = size
    

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

shoe1 = Shoe("Manolo Blahnik", "43")

print(shoe1.brand)
print(shoe1.size)
shoe1.cobble()