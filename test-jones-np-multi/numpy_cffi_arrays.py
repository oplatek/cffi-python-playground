'''
source: http://arjones6.blogspot.cz/2013/05/passing-multidimensional-numpy-arrays.html
slightly modified by Ondrej Platek - replaced dlopen with verify
'''
import numpy

from cffi import FFI

ffi = FFI()
ffi.cdef("""
void single_test(double *x, int n);
void multi_test(double **x, int n, int m);
""")
with open('simple.c', 'r') as r:
    C = ffi.verify(r.read())


def single_test(x):
    C.single_test(ffi.cast("double *", x.ctypes.data), len(x))


def multi_test_a(x):
    ap = ffi.new("double* [%d]" % (len(x)))
    for i in range(len(x)):
        ap[i] = ffi.cast("double *", x[i].ctypes.data)
    C.multi_test(ap, len(x), len(x[0]))


def multi_test_b(x):
    # dsize = ffi.sizeof("double")
    ap = ffi.new("double* [%d]" % (x.shape[0]))
    ptr = ffi.cast("double *", x.ctypes.data)
    for i in range(x.shape[0]):
        ap[i] = ptr + i * x.shape[1]
    C.multi_test(ap, x.shape[0], x.shape[1])

x = numpy.linspace(1, 10, 10).astype('float64')
print "Before single", x
single_test(x)
print "After single", x

multi_array = [[1.1, 2.2, 1.3, 4.4, 5.5],
               [5.0, 3.0, 2.0, 1.0, 3],
               [6.0, 1.0, -3.2, -1, 2],
               [0.0, 1.0, 1.0, 2.0, 1]]
x = [numpy.array(v, dtype='float64') for v in multi_array]

print "Before multi_a", x
multi_test_a(x)
print "After multi_a", x

x = numpy.array(multi_array, dtype='float64')
print "Before multi_b", x, x.shape
multi_test_b(x)
print "After multi_b", x
