#include "register_machine.hpp"

#include <iostream>
#include <fstream>

int  main(int argc, char ** argv){
    if(argc != 2 ){
        std::cerr << "run this program as ./ " << argv[0] << " register_machine" << std::endl;
        return 1;
    }
    std::ifstream program_stream(argv[1]);
    register_machine rm(read_program(program_stream), initialize_registers(std::cin));
    rm.calculate();
    return 0;
}