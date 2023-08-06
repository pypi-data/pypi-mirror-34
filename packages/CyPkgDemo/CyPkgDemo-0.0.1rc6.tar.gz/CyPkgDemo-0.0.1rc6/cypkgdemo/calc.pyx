from cypkgdemo.atoi cimport parse_charptr_to_py_int
from cypkgdemo.sin cimport sin

cpdef double c_sa(double x):
    if x == 0:
        return 1
    else:
        return sin(x) / x

cpdef double c_sa_str(char*str):
    cdef double x = parse_charptr_to_py_int(str)
    return c_sa(x)
