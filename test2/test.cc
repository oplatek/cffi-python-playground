// -*- coding: utf-8 -*-
// Author:   Ondrej Platek,2013, code is without any warranty!
// Created:  11:10:29 15/04/2013
// Modified: 11:10:29 15/04/2013

#include "test.h"
#include <iostream>

int cpp_like_main(int argc, char *argv[]) {
    std::cout<< "It works!:" << std::endl;
    for (int i = 0 ; i < argc; ++i) 
        std::cout << argv[i] << std::endl;

    return 0;
}
