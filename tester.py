import subprocess
import os
import shutil
import preprocessor

TEST_FOLDER = './tmp/test/'
EXECUTABLE = "./r.out"

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


def prepare():
    subprocess.run("make")
    shutil.rmtree(TEST_FOLDER)
    os.mkdir(TEST_FOLDER)


def string_to_numbers(s):
    return [int(x) for x in s.strip().split(' ')]

def nubers_to_string(l):
    s = ""
    for i in l:
        s += str(i) + " "
    return s

def get_answer(program, program_input):
    with subprocess.Popen([EXECUTABLE, program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8') as proc:
        proc.stdin.write(program_input)
        proc.stdin.close()
        output = proc.stdout.read()
        return string_to_numbers(output)

def get_program_file(program):
    program_file = '{}{}.r'.format(TEST_FOLDER, program)
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
        color = ""
        to_print += "OK"
    else:
        color = COLOR.RED
        to_print += "ERROR, got {} instead".format(output)
    color_print(color, to_print)

prepare()

test("clear", [0], [0])
test("clear", [1], [0])
test("clear", [5], [0])
test("clear", [10], [0])


test("move", [0, 0], [0, 0])
test("move", [0, 2], [0, 0])
test("move", [1, 0], [0, 1])
test("move", [20, 0], [0, 20])
test("move", [10, 5], [0, 10])

test("copy", [0, 0], [0, 0])
test("copy", [0, 2], [0, 0])
test("copy", [1, 0], [1, 1])
test("copy", [20, 0], [20, 20])
test("copy", [10, 5], [10, 10])

test("add_d", [0, 0], [0, 0])
test("add_d", [5, 0], [0, 5])
test("add_d", [0, 10], [0, 10])
test("add_d", [7, 6], [0, 13])

test("add", [0, 0], [0, 0])
test("add", [5, 0], [5, 5])
test("add", [0, 10], [0, 10])
test("add", [7, 6], [7, 13])


test("mult", [0, 0], [0, 0])
test("mult", [1, 0], [1, 0])
test("mult", [0, 1], [0, 0])
test("mult", [2, 3], [2, 6])
test("mult", [7, 6], [7, 42])


test("fact_d", [0], [ANY, 1])
test("fact_d", [1], [ANY, 1])
test("fact_d", [2], [ANY, 2])
test("fact_d", [3], [ANY, 6])
test("fact_d", [4], [ANY, 24])
test("fact_d", [5], [ANY, 120])

test("fib_d", [0], [ANY, 0])
test("fib_d", [1], [ANY, 1])
test("fib_d", [2], [ANY, 1])
test("fib_d", [3], [ANY, 2])
test("fib_d", [4], [ANY, 3])
test("fib_d", [5], [ANY, 5])
test("fib_d", [6], [ANY, 8])
test("fib_d", [7], [ANY, 13])
test("fib_d", [8], [ANY, 21])
test("fib_d", [9], [ANY, 34])


test("pow_d", [0, 0], [ANY, ANY, 1])
test("pow_d", [0, 1], [ANY, ANY, 0])
test("pow_d", [1, 0], [ANY, ANY, 1])
test("pow_d", [1, 10], [ANY, ANY, 1])
test("pow_d", [2, 0], [ANY, ANY, 1])
test("pow_d", [2, 1], [ANY, ANY, 2])
test("pow_d", [2, 2], [ANY, ANY, 4])
test("pow_d", [2, 3], [ANY, ANY, 8])
test("pow_d", [2, 4], [ANY, ANY, 16])
test("pow_d", [3, 3], [ANY, ANY, 27])
test("pow_d", [5, 3], [ANY, ANY, 125])


test("sub", [0, 0], [0, 0, 0])
test("sub", [5, 0], [5, 0, 5])
test("sub", [0, 10], [0, 10, 0])
test("sub", [7, 6], [7, 6, 1])
test("sub", [2, 2], [2, 2, 0])
test("sub", [5, 8], [5, 8, 0])


test("diff", [0, 0], [0, 0, 0])
test("diff", [5, 0], [5, 0, 5])
test("diff", [0, 10], [0, 10, 10])
test("diff", [7, 6], [7, 6, 1])
test("diff", [2, 2], [2, 2, 0])
test("diff", [5, 8], [5, 8, 3])


test("max", [0, 0], [0, 0, 0])
test("max", [5, 0], [5, 0, 5])
test("max", [0, 10], [0, 10, 10])
test("max", [7, 6], [7, 6, 7])
test("max", [2, 2], [2, 2, 2])
test("max", [5, 8], [5, 8, 8])


test("min", [0, 0], [0, 0, 0])
test("min", [5, 0], [5, 0, 0])
test("min", [0, 10], [0, 10, 0])
test("min", [7, 6], [7, 6, 6])
test("min", [2, 2], [2, 2, 2])
test("min", [5, 8], [5, 8, 5])

color = COLOR.GREEN if TESTS_COUNT == SUCCESS_COUNT else COLOR.RED
color_print(color, '{}/{} tests correct'.format(SUCCESS_COUNT, TESTS_COUNT))
