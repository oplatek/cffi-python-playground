# -*- coding: utf-8 -*-
# Author:   Ondrej Platek,2013, code is without any warranty!
# Created:  11:13:40 15/04/2013
# Modified: 11:13:40 15/04/2013

# Created after: http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html

CXX = g++
CC = gcc
LDD_NAME1 = test1
LDD_FILE1 = lib$(LDD_NAME1).so
LDD_NAME2 = test2
LDD_FILE2 = lib$(LDD_NAME2).so
LDD_NAME3 = test3
LDD_FILE3 = lib$(LDD_NAME3).so

all: prog 

clean:
	rm -f *.so *.o prog

### Default patterns
%.o: %.c %.h
	    $(CC) -Wall -fPIC -c -o $@ $<
%.o: %.cc %.h
	    $(CXX) -Wall -fPIC -c -o $@ $<

### Test3 logic
$(LDD_FILE1): test1.o 
	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

$(LDD_FILE2): test2.o 
	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

$(LDD_FILE3): test3.o 
	$(CXX) -fPIC -shared -Wl,-export-dynamic -o $@ $^

prog: prog.o $(LDD_FILE1) $(LDD_FILE2) $(LDD_FILE3)
	$(CC) -o $@ $< -L. -l$(LDD_NAME1) -l$(LDD_NAME2) -l$(LDD_NAME3)
