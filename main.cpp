#include "register_machine.hpp"

#include <iostream>
#include <fstream>
#include <string>

int  main(int argc, char ** argv){
    if(argc < 2 ){
        std::cerr << "run this program as " << argv[0] << " register_machine [debug]" << std::endl;
        return 1;
    }
    std::ifstream program_stream(argv[1]);
    bool debug = argc >= 3 && std::string(argv[2]) == "debug";
    register_machine rm(read_program(program_stream), initialize_registers(std::cin));
    rm.calculate(debug);
    return 0;
}