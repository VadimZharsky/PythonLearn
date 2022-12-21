from typing import Any
import time
import tasks
import pytest
from typing import cast

def test_01()-> None:

    text = "text"
    another_text = "Python"

    @tasks.do_twice
    def func_doubler(text: str) -> str:
        return text

    modif_text = func_doubler(text)
    modif_another = func_doubler(another_text)
    assert modif_text == "texttext"
    assert modif_another == "PythonPython"

def test_02() -> None:
    counter_dict: dict = {}

    @tasks.counter_factory(counter_dict)
    def func_one() -> None:
        pass

    @tasks.counter_factory(counter_dict)
    def func_two() -> None:
        pass

    [func_one() for _ in range(0, 4)]
    [(func_one(), func_two()) for _ in range(0, 5)]

    assert func_one.__name__ == 'func_one'
    assert counter_dict[func_one.__name__] == 9
    assert counter_dict[func_two.__name__] == 5


def test_03()-> None:
    cashe_dict: dict = {}
    @tasks.cashe_factory(cashe_dict)
    def list_append(lst: list) -> Any:
        lst.append(1)
        return lst

    data1: list = []
    data2: list = ["x"]
    data3: list = [1,"wq"]

    [list_append(data1) for _ in "123"]
    [list_append(data2) for _ in "123"]
    [list_append(data3) for _ in "123"]

    assert cashe_dict.get(list_append.__name__) == [
        [
            ([1],),
            {},
            [1],
        ],
        [
            (["x", 1],),
            {},
            ["x", 1],
        ],
        [
            ([1, 'wq', 1],),
            {}, 
            [1, 'wq', 1],
        ],
    ]
    func_res = list_append(data1)
    assert func_res == [1]
    cashe_list = cashe_dict.get(list_append.__name__)
    assert isinstance(cashe_list, list)
    assert [([1],), {}, func_res] in cashe_list

def test_04()-> None:

    
    bench_dict: dict = {}
    @tasks.fabric_benchmark(bench_dict)
    def slow_func(timer: int) -> Any:
        time.sleep(timer)
    
    timer = 1
    start_time = time.monotonic()
    slow_func(timer)
    end_time = time.monotonic() - start_time

    assert abs(end_time - 1) < 0.1

    bench_time = bench_dict.get(slow_func.__name__)

    assert isinstance(bench_time, float)
    assert abs(end_time - bench_time) < 0.1

def test_05() -> None:
    @tasks.typecheck
    def xxx(*, arg: int) -> None:
        assert arg > 0 or arg <= 0

    @tasks.typecheck
    def yyy(*, arg: Any) -> None:
        return cast(None, arg)
        
    assert xxx(arg=10) is None
    assert yyy(arg=None) is None

    with pytest.raises(TypeError):
        xxx(arg="a")

    with pytest.raises(TypeError):
        yyy(arg="a")
   

def main():

    # test_01()
    # test_03()
    # test_04()
    test_05()


    # [(tasks.test_02.f(), tasks.test_02.g()) for _ in range(0, 3)]
 
    # assert tasks.f(4, 8) == 32
    # assert tasks.f(133, 56) == 7448
    # with pytest.raises(TypeError):
    #     assert tasks.f(2, 2.3)
    # with pytest.raises(TypeError):
    #     assert tasks.g()
        

if __name__ == "__main__":
    main()