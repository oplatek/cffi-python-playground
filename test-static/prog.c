// -*- coding: utf-8 -*-
// Author:   Ondrej Platek,2013, code is without any warranty!
// Created:  11:12:05 15/04/2013
// Modified: 11:12:05 15/04/2013

// Modifed after: http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html

#include <stdio.h>
void ctest1(int *);
void ctest2(int *);

int main()
{
    int x;
    ctest1(&x);
    printf("Valx=%d\n",x);

    ctest2(&x);
    printf("Valx=%d\n",x);

    return 0;
}
