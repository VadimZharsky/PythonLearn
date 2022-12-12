
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

@execute_counter
def task_02_count_calls() -> int:
    return 0