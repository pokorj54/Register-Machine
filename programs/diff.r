# R2 = | R0 - R1 |; R3, R4 are temporary
$sub 0 1 2 3 4
dec 2 
jmp >correct
$sub 1 0 2 3 4
jmp >end
#correct
inc 2
#end