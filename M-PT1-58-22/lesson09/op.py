class Person:
    def __init__(self, name):
        self.__name__ = name
        self.__hidden_string__ = 18

    def get_name(self):
        return self.__name__
    
    def get_hidden(self, name):
        return self.__hidden_string__



def main():
    one = Person("Bob")
    print(one.get_name())
    print(one.get_hidden("Bob"))

main()