from typing import Any
import time
import pytest



def typecheck(func):
    def checker(*args):
        if len(args) != 0:
            if ([isinstance(x, int) for x in args][-1]):
                return func(args[0], args[1])
            else:
                raise TypeError(f"{args=!r} is not type of int")
        else:
            raise TypeError(f"{args=!r} is not type of int")
    return checker


def fabric_cashe_n_bench(cashe_dict: dict):

    def cashe_creator(func):
        memory = {}
        timer = {}
        def inner(*args):
            func_name = func.__name__
            start_time = time.monotonic()
            if args in memory:
                time.sleep(args[0][2])
                end_time = time.monotonic() - start_time
                print(func_name)
                return {"result": memory[args], "end_time": end_time}
            else:
                rec_new = func(*args)
                memory[args] = rec_new
                time.sleep(args[0][2])
                end_time = time.monotonic() - start_time
                print(func_name)
                return {"result": rec_new, "end_time": end_time}
        return inner
    return cashe_creator


class ExecutionCounter:
    call_count:int = 0 
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.call_count

def counter(func, counter_dict = {}):
    counter_dict[func] = 0
    def call_counter():
        counter_dict[func] += 1
        print(f"func: {func.__name__} called {counter_dict[func]} times")
        return func()
    return call_counter


def do_twice(func) -> str:
    def doubler(*args, **kwargs):
        text = func(*args, **kwargs)
        restart = func(*args, **kwargs)
        return(f"{text}{restart}")
    return doubler



class test_02:
    counter_dict = {}
    @counter
    def f() -> int:
        return {"f", }

    @counter
    def g() -> int:
        return {"g", }


@typecheck
def g() -> int:
    return "1"


@typecheck
def f(num: int, mul: int) -> int:
    return num * mul
