cpdef int test(int x):
    cdef y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y