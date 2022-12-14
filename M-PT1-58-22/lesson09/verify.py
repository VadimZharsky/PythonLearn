import time
from collections import defaultdict
from typing import Any

import pytest

import ver as les9


def test_01() -> None:
    @les9.task_01_do_twice
    def func(data: list) -> None:
        data.append(1)

    xxx: list = []
    func(xxx)

    assert xxx == [1, 1]


def test_02() -> None:
    calls: dict = {}

    @les9.task_02_count_calls(calls)
    def func1() -> None:
        pass

    @les9.task_02_count_calls(calls)
    def func2() -> None:
        pass

    [func1() for _ in "123"]
    [(func1(), func2()) for _ in "123"]

    assert calls == {
        func1.__name__: 6,
        func2.__name__: 3,
    }


def test_03() -> None:
    benchmarks: dict = {}

    @les9.task_03_benchmark(benchmarks)
    def slowpoke(timeout: int) -> None:
        time.sleep(timeout)

    t0 = time.monotonic()
    slowpoke(3)
    dt = time.monotonic() - t0

    assert abs(dt - 3) < 0.1

    bt = benchmarks.get(slowpoke.__name__)
    assert isinstance(bt, float)
    assert abs(dt - bt) < 0.1
    print(f"dt: {dt}\nbt:{bt}")


def test_04() -> None:
    @les9.task_04_typecheck
    def xxx(*, arg: int) -> None:
        pass

    @les9.task_04_typecheck
    def yyy(*, arg: Any) -> None:
        return arg  # type: ignore

    assert xxx(arg=10) is None
    assert yyy(arg=None) is None

    with pytest.raises(TypeError):
        xxx(arg="a")

    with pytest.raises(TypeError):
        yyy(arg="a")


def test_05() -> None:
    cache: dict = defaultdict(list)

    @les9.task_05_cache(cache)
    def func1(arg: list) -> list:
        arg.append(1)
        return arg

    data1: list = []
    data2: list = ["x"]

    [func1(data1) for _ in "123"]
    [func1(data2) for _ in "123"]
    assert cache.get(func1.__name__) == [
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
    ]

    ret = func1(data1)
    assert ret == [1]

    cached_calls = cache.get(func1.__name__)
    assert isinstance(cached_calls, list)
    assert [([1],), {}, ret] in cached_calls

def main():
    # test_01()
    # test_02()
    test_04()

main()
