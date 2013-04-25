// -*- coding: utf-8 -*-
// Author:   Ondrej Platek,2013, code is without any warranty!
// Created:  11:10:29 15/04/2013
// Modified: 11:10:29 15/04/2013

#include <iostream>
#include <string>

#include "test.h"
#include "myclass.h"


int cpp_test(int argc, char *argv[]) {

    std::cout<< "It works!:" << std::endl;
    for (int i = 0 ; i < argc; ++i) 
        std::cout << argv[i] << std::endl;

    int *p = new int[10];
    std::string s("ahoj");
    myclass c;

    c.set_ip(p);
    c.set(s, 99);
    c.print_s_and_i();
    delete []p;

    return 0;
}

// int main(int argc, char *argv[]) {
//     return cpp_test(argc, argv);
// }

