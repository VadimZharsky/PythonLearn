
def main():
    s = "rrr eee www"
    result = var1(s)
    result2 = var2(s)
    result3 = var3(s)
    print(result) 
    print(result2)
    print(result3)


def var1 (s : str) -> str:
    words = s.split(" ")
    lengths = list(map(len, words)) #[2,3,1,2,10,3,0]
    max_length = max(lengths) #10
    pos = lengths.index(max_length) #4
    words = [   
        w
      for i, w in enumerate(words)
        if i == pos
    ]
    return "".join(words)


def var2 (s : str) -> str:
    words = s.split(" ")
    lengths = list(map(len, words)) #[2,3,1,2,10,3,0]
    max_length = max(lengths) #10
    pos = lengths.index(max_length) #4
    indices = []
    
    for count, num in enumerate(lengths):
        indices.append(count)

    result = list(filter(lambda l: l == pos, indices))
    result = words[result[0]]
    
    return "".join(str(result))

def var3(s : str):
    words = s.split(" ")
    m = max(words, key=len)
    return m

if __name__ =="__main__":
    main()