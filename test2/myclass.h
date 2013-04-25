#ifndef __MYCLASS_H__
#define __MYCLASS_H__

#include <string>

class myclass {
  private:
    int i_;
    std::string s_;
    int * ip_;
  public:
    void set_ip(int * ip);
    int * get_ip();
    void set(const std::string & s, int i); 
    void print_s_and_i();
};

#endif  // __MYCLASS_H__
