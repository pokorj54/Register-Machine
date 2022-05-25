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
    register_machine(const std::vector<command> & commands, const std::vector<reg_val> & registers);

    bool do_step();

    void calculate();
    
    private:
        const std::vector<command> commands;
        std::vector<reg_val> registers;
        size_t PC;
};

std::vector<command> read_program(std::istream & is);

std::vector<reg_val> initialize_registers(std::istream & is);