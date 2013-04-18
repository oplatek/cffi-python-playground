#!/usr/bin/env python
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  12:34:55 15/04/2013
# Modified: 12:35:21 15/04/2013

from cffi import FFI


def test_simple():
    ffi = FFI()
    with open('test.h') as r:
        header = r.read()
    header = '''int cpp_like_main(int argc, char *argv[]); '''

    ffi.cdef(header)
    lib = ffi.dlopen('libcpp.so')

    args = ['testing', 'arguments', ':)']
    lib.cpp_like_main(len(args), args)

if __name__ == '__main__':
    test_simple()
