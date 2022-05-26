# R1 = R0, R2 is temporary
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
