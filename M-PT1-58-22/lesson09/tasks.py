from typing import Any
from typing import Callable
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


def fabric_benchmark(cashe_dict: dict) -> Callable:
    def cashe_creator(func) -> Callable:        
        def inner(*args, **kwargs) -> Any:
            inner.__name__ = func.__name__
            start_time = time.monotonic()
            res = func(*args, **kwargs)
            cashe_dict[inner.__name__] = time.monotonic() - start_time
            return res
        return inner
    return cashe_creator


def cashe_creator(func) -> Callable:
    memory: dict = {}
    def inner(*args, **kwargs) -> Any:
        if args in memory:
            return memory[args]
        else:
            rec_new = func(*args, **kwargs)
            memory[args] = rec_new
            return rec_new
    return inner




def counter_factory(counter_dict: dict) -> Callable:   
    def counter(func) -> Callable:
        counter_dict.setdefault(func.__name__, 0)
        def call_counter() -> Any:  
            call_counter.__name__ = func.__name__          
            res = func() 
            counter_dict[func.__name__] += 1
            return res
        return call_counter
    return counter


def do_twice(func) -> str:
    def doubler(*args, **kwargs):
        text = func(*args, **kwargs)
        restart = func(*args, **kwargs)
        return(f"{text}{restart}")
    return doubler




@typecheck
def g() -> int:
    return "1"


@typecheck
def f(num: int, mul: int) -> int:
    return num * mul
