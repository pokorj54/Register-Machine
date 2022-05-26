# R1 = fact(R1), R2, R3 are temporary
$clear 1
inc 1
# fact
dec 0
jmp >mult
jmp >end
#mult
inc 0
$mult 0 1 2 3
dec 0
jmp >fact
#end
