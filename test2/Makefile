# -*- coding: utf-8 -*-
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  11:13:40 15/04/2013
# Modified: 11:13:40 15/04/2013

# Created after: http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html

CXX = g++
CC = gcc
LDD_NAME = cpptest
LDD_FILE = lib$(LDD_NAME).so

all: prog 

clean:
	rm -f *.so *.o prog

### Default patterns
%.o: %.c %.h
	    $(CC) -Wall -fPIC -c -o $@ $<
%.o: %.cc %.h
	    $(CXX) -Wall -fPIC -c -o $@ $<

### Test2 logic
$(LDD_FILE): test.o myclass.o
	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

prog: prog.o $(LDD_FILE)
	$(CC) -o $@  prog.o -L. -l$(LDD_NAME)
