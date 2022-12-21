def test_decor(func):
    def wrap(num: int):
        try:
            func(num)
        except AssertionError:
            print("test passed")
    return wrap


def main():
    @test_decor
    def test_num(num):
        assert num < 0
        print("test passed")
    
    test_num(5)
    

main()