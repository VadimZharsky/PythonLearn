from itertools import starmap, repeat, compress
from operator import eq
import time

def main():
    line = "one two three eleven one two three eleven one two three eleven"
    words = line.split(" ")

    start = time.time()
    result = max_finder(words)
    end = time.time()
    speed = end - start
    print(f"cycle max:\n{result}\nended with {speed}\n\n")
    
    start = time.time()
    result = for_finder(words)
    end = time.time()
    speed = end - start
    print(f"cycle for_finder:\n{result}\nended with {speed}\n\n")

    start = time.time()
    result = without_for(words)
    end = time.time()
    speed = end - start
    print(f"cycle without_for:\n{result}\nended with {speed}\n\n")



def without_for(words):
    lengths = list(map(len, words))
    max_length = max(lengths)
    max_indices = starmap(eq, zip(lengths, repeat(max_length)))
    max_words = list(compress(words, max_indices))
    return max_words

def max_finder(words):
    curmax = 0
    result = []
    for w in words:
        lw = len(w)
        if lw < curmax:
            continue
        
        if lw == curmax:
            result.append(w)
            continue

        if lw > curmax:
            curmax = lw
            result = [w]
    
    return result

def for_finder(words):
    max_length = max(map(len, words))
    result = [
        w
        for w in words
        if len(w) == max_length
        ]
    return result


if __name__ =="__main__":
    main()