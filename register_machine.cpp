#include "register_machine.hpp"

#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

template <typename T>
T max(T a, T b){
    return ( a < b) ? b : a;
}

register_machine::register_machine(const std::vector<command> & commands, const std::vector<reg_val> & registers)
: commands(commands), registers(registers), PC(0){
    reg_val highest_reg_name;
    for(command c : commands){
        if(c.instr != JMP){
            highest_reg_name = max(highest_reg_name, c.reg);
        }
    }
    //this->registers.reserve(max(highest_reg_name + 1, registers.size()));
}


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
        if(registers[reg] == 0){
            PC += 2;
            return true;
        }
        registers[reg] = registers[reg] - 1;
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
        std::cout <<  val << " ";
    }
    std::cout << std::endl;
}


std::vector<command> read_program(std::istream & is){
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
            {"j",       JMP},
            {"inc",       INC},
            {"dec",       DEC},
            {"print",       PRINT},
            {"jmp",       JMP}
        });
        instruction instr = str_to_instruction.at(instr_str);
        commands.emplace_back(instr, reg);
    }
    return commands;
}


std::vector<reg_val> initialize_registers(std::istream & is){
    std::vector<reg_val> result;
    while(true){
        reg_val val;
        is >> val;
        if(!is.good()){
            break;
        }
        result.push_back(val);
    }
    return result;
}