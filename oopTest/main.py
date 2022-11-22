from lib.triagle import Triangle

def main():
    triange1 = Triangle(6, 6, 8.4852)
    print(triange1.get_sides())
    triange1.is_valid()
    triange1.get_angles()


if __name__ == '__main__':
    main()