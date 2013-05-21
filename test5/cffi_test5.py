from cffi import FFI

ffi = FFI()

header = '''
    int testInt(void);
    void testInt2(int * x);
    int testArray(int * x);
'''
ffi.cdef(header)

with open('source.c', 'r') as s:
    lib = ffi.verify(s.read())

print lib.testInt()

ip = ffi.new('int *')
ip[0] = 9
print ip[0]
lib.testInt2(ip)
print ip[0]

arp = ffi.new('int[20]')
lenght = lib.testArray(arp)
print lenght
for i in range(lenght):
    print arp[i]

# array simple example
ar = ffi.new("int[]", 10)
ar[3] = 3
list_from_ar = list(ar)
print ar, len(ar), list_from_ar


# char simple example
x = ffi.new("char[]", "hello")
print x, len(x)
print ffi.string(x)


# cp = ffi.new('char *')
# cp = lib.fillString(ip)
# s = ffi.string(cp)
