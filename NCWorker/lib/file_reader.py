

class Reader:

    def open_file(name: str) -> list:
        
        with open (name) as reader:
            temp = reader.read().split("\n")
            return temp