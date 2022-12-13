import time
import pytest

import tasks

def main():
    # assert tasks.task_01_do_twice("text") == "texttext"
    # assert tasks.task_01_do_twice("python") == "pythonpython"

    # result = tasks.task_02_count_calls()
    counter: int = 0
    assert not counter
    result = [tasks.test_02() for _ in range(0, 3)][-1]
    print(result)

    # res1 = tasks.task_03_cashe("text_to cashe")
    # res3 = tasks.task_03_cashe("another text")
    # z = [tasks.task_03_cashe("text_to cashe") for _ in range(0, 3)][-1]
    # assert z is res1
    # assert not z is res3

    # time_sleep = 2
    # start_time = time.monotonic()
    # tasks.task_04_benchmark(time_sleep)
    # end_time = time.monotonic() - start_time
    # assert abs(end_time - time_sleep)<0.1
    
    # assert tasks.f(4, 8) == 32
    # assert tasks.f(133, 56) == 7448
    # with pytest.raises(TypeError):
    #     assert tasks.f(2, 2.3)
    # with pytest.raises(TypeError):
    #     assert tasks.g()
        

if __name__ == "__main__":
    main()