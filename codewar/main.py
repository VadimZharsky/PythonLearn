from user import User

def solution(number: int) -> int:
    if number <= 0:
        return 0

    result: int = 0
    for num in range (1, number):
        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result

def digit_sum(n: int) -> int:
    sum: int = 0
    for num in str(n):
        sum += int(num)
    
    return sum

def count_consonants(text: str) -> int:
    vowels: str = "aeiou!@#$%^&*()';:.,<>?/ "
    counter: int = 0
    cons: list = []
    txt = text.lower()
    
    for ch in txt:
        if ch not in vowels and ch not in cons:
            cons.append(ch)
            counter += 1

    return counter

def count_bits(n: int) -> int:
    bin_repr: str = "{0:b}".format(n)
    print(bin_repr)
    bits_counter: int = 0
    for i in bin_repr:
        if i == '1':
            bits_counter += 1
    return bits_counter

def array_diff(a: list, b: list):
    result: list = []
    for num in a:
        if num not in b:
            result.append(num)
    return result

def main():
    # res = array_diff([1,2,2], [2])
    # res = count_bits(7)
    # res = count_consonants("Count my unique consonants!!")
    # res = solution(200)
    user = User()
    user.inc_progress(7)
    print(user.progress)
    user.inc_progress(7)
    print(user.progress)

if __name__ == "__main__":
    main()