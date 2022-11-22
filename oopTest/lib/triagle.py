import math

class Triangle:

    arr_sides =[]

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.sides(a, b, c)

    def sides(self, a, b, c):
        try:
            self.arr_sides.append(float(a))
            self.arr_sides.append(float(b))
            self.arr_sides.append(float(c))
            self.arr_sides.sort()
        except ValueError:
            print("Invalid Input")
            self.arr_sides = None
    
    def get_sides(self):
        return self.arr_sides

    def is_valid(self):
        if((self.arr_sides[0] + self.arr_sides[1]) <= self.arr_sides[2]):
            print(f"Triangle is invalid. Sum of sides {self.arr_sides[0]} and {self.arr_sides[1]} is {self.arr_sides[0] + self.arr_sides[1]} and must be greater than {self.arr_sides[2]}")
        elif((self.arr_sides[0] == self.arr_sides[1]) and (self.arr_sides[0] == self.arr_sides[2])):
            print(f"Tringle is Equilateral")
        elif((self.arr_sides[0] == self.arr_sides[1])):
            print(f"Tringle is Isosceles with equal sides {self.arr_sides[0]} and base {self.arr_sides[2]}")
        elif((self.arr_sides[1] == self.arr_sides[2])):
            print(f"Tringle is Isosceles with equal sides {self.arr_sides[1]} and base {self.arr_sides[0]}")
        else:
            print(f"Tringle is Scalene with side {self.arr_sides[0]}, side {self.arr_sides[1]} and base {self.arr_sides[2]}")


    def get_angles(self):
        a = self.arr_sides[0]
        b = self.arr_sides[1]
        c = self.arr_sides[2]
        alfa  = ((math.acos(((a ** 2 + b ** 2) - (c ** 2)) / (2 * a * b)))*180)/math.pi
        beta  = ((math.acos(((b ** 2 + c ** 2) - (a ** 2)) / (2 * b * c)))*180)/math.pi
        gamma  = ((math.acos(((c ** 2 + a ** 2) - (b ** 2)) / (2 * c * a)))*180)/math.pi
        angles = {
            "alfa" : alfa,
            "beta" : beta,
            "gamma" : gamma
        }
        print(angles)


