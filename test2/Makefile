# -*- coding: utf-8 -*-
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  11:13:40 15/04/2013
# Modified: 11:13:40 15/04/2013

# Created after: http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html

CXX = g++
CC = gcc
SRCS = test.cc  
# cc files has to wrapped for C usage
LDD_NAME = cpptest
LDD_FILE = lib$(LDD_NAME).so

LIB_LOCATION = $(PWD) 

all: prog 

clean:
	rm -f *.so *.o

### Default patterns
%.o: %.c 
	    $(CC) -Wall -fPIC -c -o $@ $<
%.o: %.cc
	    $(CXX) -Wall -fPIC -c -o $@ $<

$(LDD_FILE): test.o 
	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

prog: prog.c test.h test.o prog.o $(LDD_FILE)
	gcc -o $@  prog.o -L. -l$(LDD_NAME)
