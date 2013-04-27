#!/usr/bin/env python
# Author:   Ondrej Platek,2013, code is without any warranty!

from cffi import FFI


def test_simple():
    ffi = FFI()

    ffi.cdef("int main(void);")
    try:
        with open('prog.c') as r:
            src = r.read()
            # The tmpdir needs to set to '.' otherwise headers are not found
            lib = ffi.verify(src, tmpdir='.', libraries=['test1', 'test2', 'test3'])
            # The main function is here treated as common library function
            lib.main()
    except Exception as inst:
        # useful for printing gcc compiling errors in ffi.verify
        print inst

if __name__ == '__main__':
    test_simple()
