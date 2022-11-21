
def main():
    print("Triange Verificator\nFor verify triangle you need to input 3 side lengths")
    sides_array = []
    try:
        sides_array.append(float(input("input first side length: ")))
        sides_array.append(float(input("input second side length: ")))
        sides_array.append(float(input("input third side length: ")))
        result = triangle_is_valid(sides_array)
        print(result)
    except ValueError:
        print("Invalid input.")

def triangle_is_valid(arr):
    equilateral = is_equilateral(arr)
    if (equilateral is True):
        return("Triangle is valid. Equilateral triangle is builded")
    arr.sort()
    #To check validity of triangle we need sum of two sides greater than the base 
    if((arr[0]+arr[1]) <= arr[2]):
        return f"Triangle is invalid. The sum of first side {arr[0]} and second side {arr[1]} is {arr[0]+arr[1]} and must be greater than the base {arr[2]}"
    if (arr[0] == arr[1]):
        return(f"Triangle is valid. Isosceles triangle is builded with two equal sides {arr[0]} and base {arr[2]}")
    if (arr[1] == arr[2]):
        return(f"Triangle is valid. Isosceles triangle is builded with two equal sides {arr[1]} and base {arr[0]}")
    else:
        return(f"Triangle is valid. Scalene triangle is builded with {arr[0]} side, {arr[1]} second side and a base {arr[2]}")

def is_equilateral(arr):
    #all sides are equal
    if (arr[0] == arr[1] and arr[0] == arr[2]):
        return True
    return False
   

if __name__ == '__main__':
    main()