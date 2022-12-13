from typing import Any
from time import sleep
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


def cashe_creator(func):
    memory = {}
    def inner(*args):
        if args in memory:
            return memory[args]
        else:
            rec_new = func(*args)
            memory[args] = rec_new
            return rec_new
    return inner


class ExecutionCounter:
    call_count:int = 0 
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.call_count


def execute_counter(func) -> int:
    call_count:int = 0 
    def __call__():
        call_count += 1
        return call_count
    return __call__


def do_twice(func) -> str:
    def doubler(*args, **kwargs):
        text = func(*args, **kwargs)
        restart = func(*args, **kwargs)
        return(f"{text}{restart}")
    return doubler


@do_twice
def task_01_do_twice(text: str) -> str:
    return(text)


class test_02:

    @ExecutionCounter
    def f() -> int:
        return {"f", }

    @ExecutionCounter
    def g() -> int:
        return {"g", }


@cashe_creator
def task_03_cashe(anything: Any) -> Any:
    return anything


@cashe_creator
def task_04_benchmark(sleep_time: int) -> Any:
    sleep(sleep_time)
    return sleep_time


@typecheck
def g() -> int:
    return "1"


@typecheck
def f(num: int, mul: int) -> int:
    return num * mul
