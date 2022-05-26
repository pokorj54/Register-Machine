import sys

PROGRAMS_DIR = './programs/'


def read_program(filename):
    with open(filename, "r") as file:
        return file.readlines()

def save_program(program, filename):
    with open(filename, "w") as file:
        file.writelines(program)

def get_program(name):
    return read_program(PROGRAMS_DIR + name.lower() + '.r')

def program_replace_register(program, to_be_replaced, replacement):
    for i in range(len(program)):
        if program[i][0]== 'j':
            continue
        # dont accidentaly replace smaller register name
        program[i] = program[i].replace(' {} '.format(to_be_replaced), ' {} '.format(replacement))
        program[i] = program[i].replace(' {}\n'.format(to_be_replaced), ' {}\n'.format(replacement))

def expand_call(line):
    items = line.strip().split(' ')
    program = get_program(items[0][1:])
    program = to_low_level(program)
    c = 0
    for register in items[1:]:
        program_replace_register(program, c, '~{}~'.format(register))
        c+= 1
    c = 0
    for register in items[1:]:
        program_replace_register(program, '~{}~'.format(register), register)
        c+= 1
    return program

def expand_calls(program):
    expanded = []
    for line in program:
        if("$" in line):
            expanded += expand_call(line)
        else:
            expanded.append(line)
    return expanded

def handle_labels(program):
    ic = 0
    labels = dict()
    without_labels = []
    for line  in program:
        if line[0] == '#':
            labels[line[1:].strip()] = ic
        else:
            ic+=1
            without_labels.append(line)
    for id in range(len(without_labels)):
        line = without_labels[id]
        if '>' in line:
            char_index = line.index('>')
            label = line[line.index('>') + 1:]
            abs_pos = labels[label.strip()]
            rel_jmp = abs_pos-id
            line = line[0: char_index] + str(rel_jmp) + '\n'
        without_labels[id] = line
    return without_labels



def to_low_level(program):
    expanded = expand_calls(program)
    return handle_labels(expanded)

def preprocess_file(input_file, output_file):
    program = read_program(input_file)
    program = to_low_level(program)
    save_program(program, output_file)

def main():
    if len(sys.argv) != 3:
        print("run this program as {} input_file output_file".format(sys.argv[0]))
        exit(1)

    preprocess_file(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()