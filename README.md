# Register Machine

Semestral work for NI-VYC at FIT CTU.


## The register machine

The register machine is a machine composed of integer registers and a program made of instructions.

Four instructions are supported:
- `inc r`: increments the value stored in register `r` by 1.
- `dec r`: decrements the value stored in register `r` by 1.
- `print r`: prints the value stored in register `r`.
- `jmp x`: changes the program counter by `x`.

The program can be made only from these instructions, one per line, everything else is undefined behaviur. Programs in folder `programs` has to be preprocessed before running.

## Preprocessor

The preprocessor is made to make it easier to write more complicated code and it allows to reuse existing programs and to labels to jumps.

### Reusing programs

Only programs that are in `programs` can be included. To include the program use `$` before it's name and then follow it with the register mapping. Be sure that right amount of registers is mapped, sometimes program needs also to have temporary register allocated.


This is file `programs/clear.r`.

```bash
# sets register 0 to 0
dec 0
jmp -1
```

And this is how to use it in program that sets the register 0 to 3.
```bash
# set register 0 to 3
$clear 0
inc 1
inc 1
inc 1
```
### Jump labels

Jump labels start with the symbol `#`, which is followed by a name. Every term that starts with the symbol `>`, which is followed by a name of a label, is replaced by the distance (number of instruction from label down to the jump) from the label of specified name. Since the labels are removed after preprocessing, they can be also used as comments.


Example of using labels - adding register 0 to the register 1.
```bash
# R1 = R0 + R1; R2 is temporary
$move 0 2
# decrby1
dec 2
jmp >add1both
jmp >end
# add1both
inc 0
inc 1
jmp >decrby1
# end
```

### How to run

To compile the register machine run `make`, to run it call `./r.out`

To run the preprocessor run `python3 preprocessor.py input_program.t output_program.r`.

Preprocessing and running a program is combined in single command `./r.sh program.r`.




