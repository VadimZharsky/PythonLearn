import math

class Triangle:

    

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__arr_sides = self.sides(a, b, c)


    def sides(self, a, b, c):
        try:
            arr_sides = []
            arr_sides.append(float(a))
            arr_sides.append(float(b))
            arr_sides.append(float(c))
            arr_sides.sort()
            return arr_sides
        except ValueError:
            print("Invalid Input")
            arr_sides = None
    
    def get_sides(self):
        return self.__arr_sides  

    def is_valid(self):
        a = self.__arr_sides[0]
        b = self.__arr_sides[1]
        c = self.__arr_sides[2]
        if((a + b) <= c):
            print(f"Triangle is invalid. Sum of sides {a} and {b} is {b} and must be greater than {c}")
        elif((a == b) and (a == c)):
            print(f"Tringle is Equilateral")
        elif((a == b)):
            print(f"Tringle is Isosceles with equal sides {a} and base {c}")
        elif((b == c)):
            print(f"Tringle is Isosceles with equal sides {b} and base {a}")
        else:
            print(f"Tringle is Scalene with side {a}, side {b} and base {c}")

    def get_angles(self):
        a = self.__arr_sides[0]
        b = self.__arr_sides[1]
        c = self.__arr_sides[2]
        alfa = self.angle_finder(a, b, c)
        beta = self.angle_finder(b, c, a)
        gamma = self.angle_finder(a, c, b)
        angles = {
            "alfa" : alfa,
            "beta" : beta,
            "gamma" : gamma
        }
        print(angles)
        angle_sum : float = 0.0
        for value in angles.values():
            angle_sum += value
        print(f"total sum of 3 angles:  {angle_sum}")

    def angle_finder(self, a, b, c):
        result = ((math.acos(((a ** 2 + b ** 2) - (c ** 2)) / (2 * a * b)))*180)/math.pi
        return result



