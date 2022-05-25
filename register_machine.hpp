#include <vector>
#include <cstdlib>
#include <iostream>

using reg_name = size_t;
using reg_val = size_t;

enum instruction {
    INC,
    DEC,
    JMP,
    PRINT
};

struct command{
    instruction instr;
    reg_name reg;
    command(instruction i, reg_name reg): instr(i), reg(reg){}
};

struct register_machine
{
    register_machine(int n, const std::vector<command> & commands);

    bool do_step();

    void calculate();
    
    private:
        const std::vector<command> commands;
        std::vector<reg_val> registers;
        size_t PC;
};

register_machine read_program(std::istream & is);