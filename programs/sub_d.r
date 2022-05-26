# R0 = R0 - R1, if R0 < R1, then R0 = 0, else R1 = 0 
# start
dec 1
jmp >second
jmp >end
# second
dec 0
jmp >start
inc 1
# end
