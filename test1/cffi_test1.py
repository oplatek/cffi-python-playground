#!/usr/bin/env python
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  12:34:55 15/04/2013
# Modified: 12:35:21 15/04/2013

from cffi import FFI


def test_simple():
    ffi = FFI()
    ffi.cdef("""
             void ctest2(int *i);
             void ctest1(int *i);
             """)
    lib = ffi.dlopen('libctest.so')

    vari = ffi.new('int *')

    lib.ctest2(vari)
    # Derefferencing pointer is always done like this in cffi
    print vari[0]

    lib.ctest1(vari)
    # Derefferencing pointer is always done by x[0] instead of *x
    print vari[0]

if __name__ == '__main__':
    test_simple()
