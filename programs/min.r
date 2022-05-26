# R2 = min(R0,R1); R3, r4 are temporary
$sub 0 1 2 3 4
dec 2
jmp >second
$copy 0 2 3
jmp >end
#second
$copy 1 2 3
#end
