# -*- coding: utf-8 -*-
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  11:13:40 15/04/2013
# Modified: 11:13:40 15/04/2013

# Created after: http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html

CXX = g++
CC = gcc
SRCS = test.cc  
# cc files has to wrapped for C usage
LDD_FILE = libcpptest.so

LIB_LOCATION = $(PWD) 

all: $(LDD_FILE) 

clean:
	rm -f *.so *.o

### Default patterns
%.o: %.c 
	    $(CC) -Wall -fPIC -c -o $@ $<
%.o: %.cc
	    $(CXX) -Wall -fPIC -c -o $@ $<

$(LDD_FILE): test.o 
	$(CC) -shared -Wl,-soname,$@ -o $@ $^
