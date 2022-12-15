import time
import pytest
from typing import Any

import tasks

def test_01():

    text = "text"
    another_text = "Python"

    @tasks.do_twice
    def func_doubler(text: str) -> str:
        return text

    modif_text = func_doubler(text)
    modif_another = func_doubler(another_text)
    assert modif_text == "texttext"
    assert modif_another == "PythonPython"


def test_03():

    @tasks.cashe_creator
    def task_03_cashe(anything: Any) -> Any:
        return anything

    res1 = task_03_cashe("text_to_cashe")
    res3 = task_03_cashe("another text")
    z = [task_03_cashe("text_to_cashe") for _ in range(0, 3)][-1]
    print(res1)
    assert z is res1
    assert not z is res3


def test_04():

    
    def benchmark(some_var: Any) -> Any:
        bench_dict: dict = {}
        @tasks.fabric_cashe_n_bench(bench_dict)
        def deleter(some_var):
            res = some_var[0]
            while res > 1:
                res = res / some_var[1]
            return res 
        
        res_dict: dict = deleter(some_var)
        res_dict_bench: dict = deleter(some_var)
        print(res_dict)
        print(res_dict_bench) 
        return res_dict

    time_sleep = 1
    var_test = (52352435234, 1.000001, time_sleep)
    benchmark(var_test)
    # assert abs(end_time - time_sleep) < 0.1

def main():

    # test_01()
    # test_03()
    test_04()

    # result = tasks.task_02_count_calls()
    # counter: int = 0
    # assert not counter
    # result = [(tasks.test_02.f(), tasks.test_02.g()) for _ in range(0, 3)][-1]
    # print(result)

    # [(tasks.test_02.f(), tasks.test_02.g()) for _ in range(0, 3)]
 
    # assert tasks.f(4, 8) == 32
    # assert tasks.f(133, 56) == 7448
    # with pytest.raises(TypeError):
    #     assert tasks.f(2, 2.3)
    # with pytest.raises(TypeError):
    #     assert tasks.g()
        

if __name__ == "__main__":
    main()