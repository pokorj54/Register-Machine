import subprocess
import os
import preprocessor

executable = "./r.out"

ANY = -1

TESTS_COUNT = 0
SUCCESS_COUNT = 0

class COLOR:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def color_print(color, text, file=None):
    print(color + text, COLOR.RESET, file=file)


def compile():
    subprocess.run("make")

def string_to_numbers(s):
    return [int(x) for x in s.strip().split(' ')]

def nubers_to_string(l):
    s = ""
    for i in l:
        s += str(l) + " "
    return s

def get_answer(program, program_input):
    with subprocess.Popen([executable, program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8') as proc:
        proc.stdin.write(program_input)
        proc.stdin.close()
        output = proc.stdout.read()
        return string_to_numbers(output)

def get_program_file(program):
    program_file = './tmp/test/{}.r'.format(program)
    if not os.path.exists(program_file):
        source_file = './programs/{}.r'.format(program)
        preprocessor.preprocess_file(source_file, program_file)
    return program_file

def compare_answers(ref, output):
    for i in range(len(ref)):
        if ref[i] == ANY:
            continue
        if ref[i] != output[i]:
            return False
    return True

def test(program, program_input, ref):
    global TESTS_COUNT
    global SUCCESS_COUNT
    TESTS_COUNT += 1
    program_file = get_program_file(program)
    output = get_answer(program_file, nubers_to_string(program_input))
    to_print = "program: {}, input: {}, ref: {}, status: ".format(program, program_input, ref)
    if compare_answers(ref, output):
        SUCCESS_COUNT += 1
        color = COLOR.GREEN
        to_print += "OK"
    else:
        color = COLOR.RED
        to_print += "ERROR, got {} instead".format(output)
    color_print(color, to_print)


test("clear", [0], [0])
test("clear", [1], [0])
test("clear", [5], [0])
test("clear", [10], [0])
