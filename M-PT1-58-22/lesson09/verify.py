import time
from typing import Any
from typing import Callable


def time_cache_factory(time_cache: dict) -> Callable:
    def task_03_benchmark(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            t_start = time.perf_counter()
            res = func(*args, **kwargs)
            time_spent = time.perf_counter() - t_start
            time_cache[func.__name__] = time_spent
            return res

        return wrapper

    return task_03_benchmark

def main():
    function_time_cache: dict[str, float] = {}


    @time_cache_factory(function_time_cache)
    def slowpoke(n03: int) -> None:
        time.sleep(n03)



    slowpoke(1)
    assert abs(function_time_cache["slowpoke"] - 1) < 0.05

main()

