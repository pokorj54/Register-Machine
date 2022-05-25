#include "register_machine.hpp"

#include <iostream>
#include <unordered_map>
#include <string>

template <typename T>
T max(T a, T b){
    return ( a < b) ? b : a;
}

register_machine::register_machine(int n, const std::vector<command> & commands)
: commands(commands), registers(n), PC(0){}


bool register_machine::do_step(){
    if(PC >= commands.size()){
        return false;
    }
    instruction instr = commands[PC].instr;
    reg_name reg =  commands[PC].reg;
    switch (instr)
    {
    case INC:
        registers[reg] += 1;
        break;
    case DEC:
        registers[reg] = max(registers[reg] - 1, (reg_val)0);
        if(registers[reg] == 0){
            ++PC; 
        }
        break;
    case JMP:
        PC += reg;
        return true;
    case PRINT:
        std::cout << registers[reg] << std::endl;
        break;
    default:
        throw "invalid instruction"; 
    }
    ++PC;
    return true;
}

void  register_machine::calculate(){
    while(do_step());
    for(reg_val val : registers){
        std::cout <<  val << std::endl;
    }
}


register_machine read_program(std::istream & is){
    size_t highest_reg = 0;
    std::vector<command> commands;
    while(is.good()){
        std::string instr_str;
        reg_name reg;
        is >>instr_str >> reg;
        if(!is.good()){
            break;
        }
        std::unordered_map<std::string, instruction> str_to_instruction({
            {"i",       INC},
            {"d",       DEC},
            {"p",       PRINT},
            {"j",       JMP}
        });
        instruction instr = str_to_instruction[instr_str];
        commands.emplace_back(instr, reg);
        if(instr != JMP){
            highest_reg = max(highest_reg, reg);
        }
    }
    return register_machine(highest_reg + 1, commands);
}