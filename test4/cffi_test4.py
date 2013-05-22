''' Testing defines and loading from source'''

from cffi import FFI


def test_verify():
    ffi = FFI()
    header = r'''
    int test(void);
    '''
    ffi.cdef(header)

    source = r'''
    #include <stdio.h>
    #include <math.h>

    #define MY_INT 100

    int test(void) {
        printf("Printing source ugly integer makro %d!\n", MY_INT);
        printf("Printing compile ugly integer makro %d!\n", COMPILE_INT);
    #ifdef COMPILE_FLAG
        printf("Compilition makro works!\n");
    #else
        printf("Compilition makro is off!\n");
    #endif
        return 0;
    }
    '''
    lib = ffi.verify(source, define_macros=[('COMPILE_FLAG', ''), ('COMPILE_INT', '1000')])
    lib.test()

if __name__ == '__main__':
    test_verify()
