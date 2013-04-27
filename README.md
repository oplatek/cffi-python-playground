Cffi-python-playground
======================
Playground for learning and testing cffi python interface.
In order to use *cffi* install it! See this page
http://cffi.readthedocs.org/ for more info.

EXAMPLES
--------

###Example 1###
Shows how to build C shared library and use it via cffi.

In order to run *test1* change to directory test1.

```sh
cd test1 && make
```

Then you can execute the `cffi_test.py` from any directory e.g. from the root of this repo.  

Do not forget to set the `LD_LIBRARY_PATH` variable to directory `test1` in this repo. There is located the just compiled shared library. 

```sh
LD_LIBRARY_PATH=test1 python test1/cffi_test1.py
```

###Example 2###
Shows how to wrap simple C++ shared library with C compatible header and use it in cffi.

In order to run *test2* change to directory test2.

```sh
cd test2 && make
```
From that directory you can run
* The `C` program which wraps `C++` library
* The Python program which uses the `C++` library with `C` linkage

```sh
# C program launched from test2 directory
test2$ LD_LIBRARY_PATH=. ./prog my test parameters get printed
I am C program
It works!:
./prog
my
test
parameters
get
printed
```

```sh
# Python program launched from test2 directory
test2$ LD_LIBRARY_PATH=. python cffi_test2.py test parameters get printed
It works!:
cffi_test2.py
test
parameters
get
printed
```

### Example 3###
I tried to use shared library which needs another shared library.
In our example `libtest1.so` needs `libtest2.so`.

I am using `ffi.verify` function. The example works.
*However I am still not satisfied, because I need to change `tmpdir=.`
It means that the temporary c file is compiled at current directory,
so it messes the directory completally*

To compile the library and test the example run following commands.
```sh
cd test3 && make # Compile shared library and testing C program
./prog   # Run the testing C program
LIBRARY_PATH=. ./cffi_test3.py  # Run the example. Set the LIBRARY_PATH variable needed for gcc compilation

```


LINKS
-----
* http://eli.thegreenplace.net/2013/03/09/python-ffi-with-ctypes-and-cffi/
* https://groups.google.com/forum/#!msg/python-cffi/
* https://pypi.python.org/pypi/cffi
* http://cffi.readthedocs.org/

PROJECTS USING CFFI
-------------------
* https://github.com/search?q-cffi+python&type-Repositories&ref-searchresults
* https://github.com/felipecruz/zmqpy  # failing imports
* https://github.com/apendleton/python-lz4-cffi # todo
* https://github.com/SimonSapin/cairocffi  # looks maintened enough

TIPS
----
* Always compile with gcc
* Name your files `*.c` not `*.cc` otherwise `gcc` will compile it like C++ file
* During linking your shared library put `-Lpathtoyourlibdirectory -lyourlibname` as last parameters to `gcc`.
