

def triangle_is_valid(a, b, c):
    if (a+b)<=c:
        return f"Triangle is invalid. The sum of first side {a} and second side {b} is {a+b} and must be greater than third side {c}" 
    if (a+c)<=b:
        return f"Triangle is invalid. The sum of first side {a} and third side {c} is {a+c} and must be greater than second side {b}"
    if (b+c)<=a:
        return f"Triangle is invalid. The sum of second side {b} and third side {c} is {b+c} and must be greater than first side {a}"
    return "triangle is valid"

def main():
    print("Triange Verificator\nFor verify triangle you need to input 3 side lengths")
    try:
        first_side = float(input("input first side length: "))
        second_side = float(input("input second side length: "))
        third_side = float(input("input third side length: "))
        result = triangle_is_valid(first_side, second_side, third_side)
        print(result)
    except ValueError:
        print("Invalid input.")

    

if __name__ == '__main__':
    main()