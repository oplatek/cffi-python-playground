#include <iostream>

#include "myclass.h"


void myclass::set_ip(int * ip) {
    this->ip_ = ip;
}

int * myclass::get_ip() {
    return this->ip_;
}

void myclass::set(const std::string & s, int i) { 
    this->s_ = s;
    this->i_= i;
}

void myclass::print_s_and_i() {
    std::cout << "printing s\n" << this->s_  << "\n printing i" << this->i_ << std::endl;
}
