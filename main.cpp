#include "register_machine.hpp"

#include <iostream>

int  main(void){
    register_machine rm = read_program(std::cin);
    rm.calculate();
    return 0;
}