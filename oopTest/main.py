from lib.triagle import Triangle


def main():
    instructor("tringle1", [4, 5, 6])
    instructor("tringle2", [8, 9, 8])
    instructor("tringle3", [34, 15, 20])
    instructor("tringle4", [15, 15, 15])
    instructor("tringle5", [24, 28, 30])


def instructor(name, sides):
    name = Triangle(sides[0], sides[1], sides[2])
    print(name.get_sides())
    name.is_valid()
    name.get_angles()


if __name__ == '__main__':
    main()
