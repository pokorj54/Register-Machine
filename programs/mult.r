# R1 = R0 * R1, R2 and R3 are temporary
$clear 2
# mult
dec 1
jmp >addR0toR2
jmp >end
# addR0toR2
$add 0 2 3
jmp >mult
# end
$move 2 1
