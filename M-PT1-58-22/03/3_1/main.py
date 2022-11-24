
def main():
    line = "one two three eleven one two three eleven one two three eleven"
    result = max_finder(line)
    print(result)

def max_finder(line):
    words= line.split(" ")
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

if __name__ =="__main__":
    main()