import cython

cpdef sum (double a,double b):
    while(a>0.1):
        a = a / b
    return a