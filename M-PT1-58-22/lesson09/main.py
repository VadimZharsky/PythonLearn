import time
import pytest
from typing import Any
from collections import defaultdict

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
    bench_dict: dict = {}
    
    @tasks.fabric_cashe_n_bench(bench_dict)
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
        time_sleep = some_var[-1]
        @tasks.fabric_cashe_n_bench(bench_dict, time_sleep)
        def deleter(some_var):
            res = some_var[0]
            while res > 1:
                res = res / some_var[1]
            return res 
        deleter(some_var)
        deleter(some_var)
        return bench_dict

    time_sleep = 1
    var_test = (5, 2, time_sleep)
    bench_dict: dict = benchmark(var_test)
    res_orig = bench_dict["orig"]["result"]
    res_cashed = bench_dict["benchmarked"]["result"]
    time_orig = bench_dict["orig"]["end_time"]
    time_cashed = bench_dict["benchmarked"]["end_time"]
   
    assert res_orig == res_cashed 
    assert abs(time_orig - time_sleep) > 0.1
    assert abs(time_cashed - time_sleep) < 0.1

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