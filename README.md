Cffi-python-playground
======================
Playground for learning and testing cffi python interface.
In order to use *cffi* install it! See this page
http://cffi.readthedocs.org/en/release-0.6/ for more info.

EXAMPLES
--------
In order to run *test1* change to directory test1

```sh
cd test1 && make
```

Then you can execute the `cffi_test.py` from any directory e.g. from the root of this repo.  

Do not forget to set the `LD_LIBRARY_PATH` variable to directory `test1` in this repo. There is located the just compiled shared library. 

```sh
LD_LIBRARY_PATH=test1 python test1/cffi_test1.py
```

LINKS
-----
* http://eli.thegreenplace.net/2013/03/09/python-ffi-with-ctypes-and-cffi/
* https://groups.google.com/forum/#!msg/python-cffi/
* https://pypi.python.org/pypi/cffi
* http://cffi.readthedocs.org/en/release-0.6/

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
