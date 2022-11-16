import os
import clr
import time
from lib import calc
import run_cython
def main ():
    pathDLL = os.getcwd() + "\\Resolver.dll"
    clr.AddReference(pathDLL)
    from Resolver import Resolver

    num = 3435254546254345
    deleter = 1.0000001

    start = time.time()
    result = calc.sum(num, deleter)
    end = time.time()
    printer(result, start, end)

    start = time.time()
    result2 = run_cython.sum(num, deleter)
    end = time.time()
    printer(result2, start, end)

    start = time.time()
    result3 = Resolver.deleter(num, deleter)
    end = time.time()
    printer(result3, start, end)

def printer(result, start, end):
    speed = end - start
    print(result)
    #print(f"start time:{start}\nend time{end}\nspeed:{speed}")
    print(f"speed:{speed}")

if __name__ == '__main__':
    main()