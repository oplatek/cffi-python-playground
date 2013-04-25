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
%.o: %.c 
	    $(CC) -Wall -fPIC -c -o $@ $<
%.o: %.cc
	    $(CXX) -Wall -fPIC -c -o $@ $<

# $(LDD_FILE): test.o ctest.o myclass.o
# 	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

$(LDD_FILE): test.o myclass.o
	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

prog: prog.c test.h test.o prog.o $(LDD_FILE)
	$(CC) -o $@  prog.o -L. -l$(LDD_NAME)
