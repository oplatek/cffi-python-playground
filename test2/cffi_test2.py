#!/usr/bin/env python
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  12:34:55 15/04/2013
# Modified: 12:35:21 15/04/2013

from cffi import FFI
import sys


def test_simple():
    ffi = FFI()
    # Cannot load header directly
    # cffi does not parse directives yet
    header = '''int cpp_test(int argc, char **argv); '''
    ffi.cdef(header)
    lib = ffi.dlopen('libcpptest.so')

    args = sys.argv
    argv_keepalive = [ffi.new("char[]", arg) for arg in args]
    argv = ffi.new("char *[]", argv_keepalive)

    lib.cpp_test(len(args), argv)

if __name__ == '__main__':
    test_simple()
