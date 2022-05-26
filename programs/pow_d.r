# R2 = pow(R0, R1); R3, R4 are temporary
$clear 2
inc 2
# pow
dec 1
jmp >mult
jmp >end
#mult
$mult 0 2 3 4
jmp >pow
#end
