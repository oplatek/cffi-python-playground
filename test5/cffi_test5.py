from cffi import FFI

# TODO look at passing multidimensional arrays from numpy
# http://arjones6.blogspot.cz/2013/05/passing-multidimensional-numpy-arrays.html

ffi = FFI()

header = '''
typedef char mychar;
typedef unsigned long mysize;
int testInt(void);
void testInt2(int * x);
void testArray(double * x, int length);

void save_to_buffer(mychar ** buff, mysize * size, char * msg);
void save_to_DoubleBuffer(double ** buff, mysize * size, char * msg);
'''
ffi.cdef(header)

with open('source.c', 'r') as s:
    lib = ffi.verify(s.read())


# returning Int by value
print lib.testInt()

# int filled by pointer
ip = ffi.new('int *')
ip[0] = 9
print ip[0]
lib.testInt2(ip)
print ip[0]

# array simple example
ar = ffi.new("int[]", 10)
ar[3] = 3
list_from_ar = list(ar)
print ar, len(ar), list_from_ar

# char simple example
x = ffi.new("char[]", "hello")
print x, len(x)
print ffi.string(x)

# filling double array simple
lenght = 8
print 'Double array lenght %d' % lenght
arp = ffi.new('double[]', lenght)
lib.testArray(arp, lenght)
for i in xrange(lenght):
    print 'arp[i]= %f' % arp[i]
print 'Double array %s ! ' % str(arp)

# Returning array of doubles from C
buffer_pointer, buffer_size = ffi.new('double **'), ffi.new('mysize *')
lib.save_to_DoubleBuffer(buffer_pointer, buffer_size, ffi.new('char[]', b'junk_msg'))
mybytes = ffi.buffer(buffer_pointer[0], buffer_size[0])
mybytes = mybytes[:]
print 'printing returned doubles %s as string. TODO How to convert them?' % mybytes
print 'buffer %d' % buffer_size[0]

# Returning char array (string) from C
buffer_pointer, buffer_size = ffi.new('mychar **'), ffi.new('mysize *')
lib.save_to_buffer(buffer_pointer, buffer_size, ffi.new('char[]', b'Ondra'))
mybytes = ffi.string(buffer_pointer[0], buffer_size[0])
print 'printing returned char %s' % mybytes
print 'string %d' % buffer_size[0]
