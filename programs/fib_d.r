# R1 = fib(R0); R2, R3, R4 are temporary
$clear 1
$clear 2
$clear 3
$clear 4
inc 2
inc 3
# fibplusone
dec 0
jmp >addfibs 
jmp >end
# addfibs
$add 3 1 4
$move 2 3 
$copy 1 2 4
jmp >fibplusone
#end
