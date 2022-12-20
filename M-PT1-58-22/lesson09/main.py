from typing import Any
import time
from collections import defaultdict
import tasks

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
    @tasks.cashe_creator
    def task_03_cashe(anything: Any) -> Any:
        return anything

    res1 = task_03_cashe("text_to_cashe")
    res3 = task_03_cashe("another text")
    z = [task_03_cashe("text_to_cashe") for _ in range(0, 3)][-1]

    assert z is res1
    assert not z is res3


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
   

def main():

    # test_01()
    # test_03()
    # test_04()
    test_02()


    # [(tasks.test_02.f(), tasks.test_02.g()) for _ in range(0, 3)]
 
    # assert tasks.f(4, 8) == 32
    # assert tasks.f(133, 56) == 7448
    # with pytest.raises(TypeError):
    #     assert tasks.f(2, 2.3)
    # with pytest.raises(TypeError):
    #     assert tasks.g()
        

if __name__ == "__main__":
    main()