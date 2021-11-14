# TODO: 260898303
# TODO: ADD OTHER COMMENTS YOU HAVE HERE AT THE TOP OF THIS FILE
# TODO: SEE LABELS FOR PROCEDURES YOU MUST IMPLEMENT AT THE BOTTOM OF THIS FILE

.data
TestNumber:	.word 2		# TODO: Which test to run!
				# 0 compare matrices stored in files Afname and Bfname
				# 1 test Proc using files A through D named below
				# 2 compare MADD1 and MADD2 with random matrices of size Size
				
Proc:		MADD2		# Procedure used by test 2, set to MADD1 or MADD2		
				
Size:		.word 64		# matrix size (MUST match size of matrix loaded for test 0 and 1)

Afname: 		.asciiz "A64.bin"
Bfname: 		.asciiz "B64.bin"
Cfname:		.asciiz "C64.bin"
Dfname:	 	.asciiz "D64.bin"

#################################################################
# Main function for testing assignment objectives.
# Modify this function as needed to complete your assignment.
# Note that the TA will ultimately use a different testing program.
.text
main:		la $t0 TestNumber
		lw $t0 ($t0)
		beq $t0 0 compareMatrix
		beq $t0 1 testFromFile
		beq $t0 2 compareMADD
		li $v0 10 # exit if the test number is out of range
        		syscall	

compareMatrix:	la $s7 Size	
		lw $s7 ($s7)		# Let $s7 be the matrix size n

		move $a0 $s7
		jal mallocMatrix		# allocate heap memory and load matrix A
		move $s0 $v0		# $s0 is a pointer to matrix A
		la $a0 Afname
		move $a1 $s7
		move $a2 $s7
		move $a3 $s0
		jal loadMatrix
	
		move $a0 $s7
		jal mallocMatrix		# allocate heap memory and load matrix B
		move $s1 $v0		# $s1 is a pointer to matrix B
		la $a0 Bfname
		move $a1 $s7
		move $a2 $s7
		move $a3 $s1
		jal loadMatrix
	
		move $a0 $s0
		move $a1 $s1
		move $a2 $s7
		jal check
		
		li $v0 10      	# load exit call code 10 into $v0
        	syscall         	# call operating system to exit	

testFromFile:	la $s7 Size	
		lw $s7 ($s7)		# Let $s7 be the matrix size n

		move $a0 $s7
		jal mallocMatrix		# allocate heap memory and load matrix A
		move $s0 $v0		# $s0 is a pointer to matrix A
		la $a0 Afname
		move $a1 $s7
		move $a2 $s7
		move $a3 $s0
		jal loadMatrix
	
		move $a0 $s7
		jal mallocMatrix		# allocate heap memory and load matrix B
		move $s1 $v0		# $s1 is a pointer to matrix B
		la $a0 Bfname
		move $a1 $s7
		move $a2 $s7
		move $a3 $s1
		jal loadMatrix
	
		move $a0 $s7
		jal mallocMatrix		# allocate heap memory and load matrix C
		move $s2 $v0		# $s2 is a pointer to matrix C
		la $a0 Cfname
		move $a1 $s7
		move $a2 $s7
		move $a3 $s2
		jal loadMatrix
	
		move $a0 $s7
		jal mallocMatrix		# allocate heap memory and load matrix A
		move $s3 $v0		# $s3 is a pointer to matrix D
		la $a0 Dfname
		move $a1 $s7
		move $a2 $s7
		move $a3 $s3
		jal loadMatrix		# D is the answer, i.e., D = AB+C 
	
		# TODO: add your testing code here
		move $a0, $s0	# A
		move $a1, $s1	# B
		move $a2, $s2	# C
		move $a3, $s7	# n
		
		la $ra ReturnHere
		la $t0 Proc	# function pointer
		lw $t0 ($t0)	
		jr $t0		# like a jal to MADD1 or MADD2 depending on Proc definition

ReturnHere:	move $a0 $s2	# C
		move $a1 $s3	# D
		move $a2 $s7	# n
		jal check	# check the answer

		li $v0, 10      	# load exit call code 10 into $v0
	        	syscall         	# call operating system to exit	

compareMADD:	la $s7 Size
		lw $s7 ($s7)	# n is loaded from Size
		mul $s4 $s7 $s7	# n^2
		sll $s5 $s4 2	# n^2 * 4

		move $a0 $s5
		li   $v0 9	# malloc A
		syscall	
		move $s0 $v0
		move $a0 $s5	# malloc B
		li   $v0 9
		syscall
		move $s1 $v0
		move $a0 $s5	# malloc C1
		li   $v0 9
		syscall
		move $s2 $v0
		move $a0 $s5	# malloc C2
		li   $v0 9
		syscall
		move $s3 $v0	
	
		move $a0 $s0	# A
		move $a1 $s4	# n^2
		jal  fillRandom	# fill A with random floats
		move $a0 $s1	# B
		move $a1 $s4	# n^2
		jal  fillRandom	# fill A with random floats
		move $a0 $s2	# C1
		move $a1 $s4	# n^2
		jal  fillZero	# fill A with random floats
		move $a0 $s3	# C2
		move $a1 $s4	# n^2
		jal  fillZero	# fill A with random floats

		move $a0 $s0	# A
		move $a1 $s1	# B
		move $a2 $s2	# C1	# note that we assume C1 to contain zeros !
		move $a3 $s7	# n
		jal MADD1

		move $a0 $s0	# A
		move $a1 $s1	# B
		move $a2 $s3	# C2	# note that we assume C2 to contain zeros !
		move $a3 $s7	# n
		jal MADD2

		move $a0 $s2	# C1
		move $a1 $s3	# C2
		move $a2 $s7	# n
		jal check	# check that they match
	
		li $v0 10      	# load exit call code 10 into $v0
        		syscall         	# call operating system to exit	

###############################################################
# mallocMatrix( int N )
# Allocates memory for an N by N matrix of floats
# The pointer to the memory is returned in $v0	
mallocMatrix: 	mul  $a0, $a0, $a0	# Let $s5 be n squared
		sll  $a0, $a0, 2		# Let $s4 be 4 n^2 bytes
		li   $v0, 9		
		syscall			# malloc A
		jr $ra
	
###############################################################
# loadMatrix( char* filename, int width, int height, float* buffer )
.data
errorMessage: .asciiz "FILE NOT FOUND" 
.text
loadMatrix:	mul $t0 $a1 $a2 	# words to read (width x height) in a2
		sll $t0 $t0  2	  	# multiply by 4 to get bytes to read
		li $a1  0     		# flags (0: read, 1: write)
		li $a2  0     		# mode (unused)
		li $v0  13    		# open file, $a0 is null-terminated string of file name
		syscall
		slti $t1 $v0 0
		beq $t1 $0 fileFound
		la $a0 errorMessage
		li $v0 4
		syscall		  	# print error message
		li $v0 10         	# and then exit
		syscall		
fileFound:	move $a0 $v0     	# file descriptor (negative if error) as argument for read
  		move $a1 $a3     	# address of buffer in which to write
		move $a2 $t0	  	# number of bytes to read
		li  $v0 14       	# system call for read from file
		syscall           	# read from file
		# $v0 contains number of characters read (0 if end-of-file, negative if error).
                	# We'll assume that we do not need to be checking for errors!
		# Note, the bitmap display doesn't update properly on load, 
		# so let's go touch each memory address to refresh it!
		move $t0 $a3	# start address
		add $t1 $a3 $a2  	# end address
loadloop:	lw $t2 ($t0)
		sw $t2 ($t0)
		addi $t0 $t0 4
		bne $t0 $t1 loadloop		
		li $v0 16	# close file ($a0 should still be the file descriptor)
		syscall
		jr $ra	

##########################################################
# Fills the matrix $a0, which has $a1 entries, with random numbers
fillRandom:	li $v0 43
		syscall		# random float, and assume $a0 unmodified!!
		swc1 $f0 0($a0)
		addi $a0 $a0 4
		addi $a1 $a1 -1
		bne  $a1 $zero fillRandom
		jr $ra

##########################################################
# Fills the matrix $a0 , which has $a1 entries, with zero
fillZero:	sw $zero 0($a0)	# $zero is zero single precision float
		addi $a0 $a0 4
		addi $a1 $a1 -1
		bne  $a1 $zero fillZero
		jr $ra



######################################################
# TODO: void subtract( float* A, float* B, float* C, int N )  C = A - B 
subtract: 	
		addi $sp $sp -4 #set stack
		sw $ra 0($sp)
		move $t0 $a0
		move $t1 $a1
		move $t2 $a2
	        move $t3 $a3
	        mul  $t3, $t3, $t3 # set loop time as NxN
		bne $t3 $zero substractNext # if loop time != 0, substract
		lw $ra, 0($sp) #return stack
		add $sp $sp 4
		jr $ra
		
substractNext: 
		beq $t3 $zero stopLoop #if loop time == 0, stop loop
		l.s $f1, ($t0) #load 1 float from matrix A
		l.s $f2, ($t1) #load 1 float from matrix B
		sub.s $f0 $f1 $f2 #substract 
		s.s $f0 ($t2) #store in matrix C
		addi $t0 $t0 4
		addi $t1 $t1 4
		addi $t2 $t2 4
		subi $t3 $t3 1 #move to the next
		j substractNext
stopLoop:
		lw $ra, 0($sp) #return stack
		add $sp $sp 4
		jr $ra

#################################################
# TODO: float frobeneousNorm( float* A, int N )
frobeneousNorm: 
		addi $sp $sp -4 #set stack
		sw $ra 0($sp)
		sub.s $f3 $f3 $f3 #clear the sum
		move $t0 $a0
		move $t1 $a1
		mul  $t1, $t1, $t1 # set loop time as NxN
		bne $t1 $zero addSum #if loop time != 0, start to add
		mov.s $f0 $f3 # if loop time == 0, move the sum to the return register
		jr $ra
		
addSum:
		beq $t1 $zero stopLoop2 #if loop time == 0, stop loop
		l.s $f1, ($t0) #load 1 float from matrix A
		mul.s $f1 $f1 $f1 #square the number
		add.s $f3 $f3 $f1 #add the number to the sum
		addi $t0 $t0 4
		subi $t1 $t1 1 #move to the next
		j addSum
		
stopLoop2:
		sqrt.s $f0 $f3
		lw $ra, 0($sp) #return stack
		add $sp $sp 4
		jr $ra		

#################################################
# TODO: void check ( float* C, float* D, int N )
# Print the forbeneous norm of the difference of C and D
check: 		
	addi $sp $sp -4 #set stack
	sw $ra 0($sp)
	
	move $t4 $a2
	move $a3 $a2 
	move $a2 $a0
	jal subtract #first subtract
	move $a1 $t4
	jal frobeneousNorm #then get the frobenous norm
	
	mov.s $f12 $f0 #print the frobenous norm
	li $v0 2
	syscall	
	
	lw $ra, 0($sp) #return stack
	add $sp $sp 4
	jr $ra

##############################################################
# TODO: void MADD1( float*A, float* B, float* C, N )
MADD1: 	
	move $t0 $a0
	move $t1 $a1
	move $t2 $a2
	move $t3 $a3
	sll $t9 $t3 2
	li $t4 0 #row time
	li $t5 0 #column time
	li $t6 0 #add time
	bne $t4 $t3 loopR #if row loop time reaches N, stop. If not, loop row
	jr $ra
loopR:
	move $t0 $a0 
	mul $t8 $t4 $t9 #move the pointer of matrix A N times, as 0 + row times x N
	add $t0 $t8 $t0
	sub $t5 $t5 $t5 #clear column time
	
	move $t1 $a1
loopC:
	sub $t6 $t6 $t6 #clear add time
loopK:
	l.s $f0 ($t0) #load 1 float from matrix A
	l.s $f2 ($t1) #load 1 float from matrix B
	mul.s $f4 $f0 $f2 #multiply
	l.s $f5 ($t2) #access the original value of the index of matrix C
	add.s $f4 $f5 $f4 #add the value 
	s.s $f4 ($t2) #put the value back to the matrix C
	
	addi $t6 $t6 1 #add time +1
	beq $t6 $t3 addC 
	
	addi $t0 $t0 4 #if no, continue the summation
	add $t1 $t9 $t1 #index of B = x + 4N
	j loopK
addC:
	addi $t2 $t2 4 #move the next index of C
	addi $t5 $t5 1 #increase the column time
	beq $t5 $t3 addR #if column time = N, change row

	
	mul $t7 $t5 4 #$t7 = column time x 4 
	move $t1 $a1
	add $t1 $t1 $t7 #move the pointer of matrix b back to the top
	
	sub $t0 $t0 $t9 #move the pointer of matrix a back to left end
	addi $t0 $t0 4
	
	j loopC
addR:
	addi $t4 $t4 1
	beq $t4 $t3 stop
	j loopR
stop:
	jr $ra
#########################################################
# TODO: void MADD2( float*A, float* B, float* C, N )
MADD2: 		
	move $t0 $a0 #matrix A
	move $t1 $a1 #matrix B
	move $t2 $a2 #matrix C
	
	li $t3 0 #j  
	li $t4 0 #k
	li $t5 0 #i
	
	move $t6 $t3
	mul $t6 $t6 $t6 #jj
	
	move $t7 $t4
	mul $t7 $t7 $t7 #kk
loopJJ: 
	sub $t7 $t7 $t7 # kk = 0
	
loopKK:
	li $t5 0 # i = 0
	
loopI:  
	move $t3 $t6 #j = jj
	
loopJ:	 
	move $t4 $t7 #k = kk
	sub.s $f1 $f1 $f1 #sum = 0.0
loopK2:
	l.s $f0 ($t0) #load 1 float from matrix A
	l.s $f2 ($t1) #load 1 float from matrix B
	mul.s $f4 $f0 $f2 #multiply
	add.s $f1 $f4 $f1 #add to sum
	
	add $t4 $t4 1 #if no, k = k+1
	
	addi $t0 $t0 4 #move A
	mul $t9 $a3 4
	add $t1 $t9 $t1 #move B
	
	move $t8 $t7 
	add $t8 $t8 4 #kk + bsize
	blt $t8 $a3 comparejjb_k #if kk+bsize < N, branch
	bge $t4 $a3 putS #if k >=  N, go sum
	
	j loopK2

comparejjb_k:
	bge $t4 $t8  putS#if k>=kk+bsize, go sum

	j loopK2
putS:
	l.s $f5 ($t2) #C[]
	add.s $f1 $f5 $f1 #sum = sum + C[]
	s.s $f1 ($t2) #put the sum back
	
	addi $t2 $t2 4 #move the next index of C
	
	addi $t3 $t3 1 #j = j+1
	
	move $t0 $a0
	mul $t9 $t5 $a3
	sll $t9 $t9 2
	add $t0 $t0 $t9
	sll $t9 $t7 2
	add $t0 $t9 $t0# a pointer -> A[i, kk]
	
	move $t1 $a1
	move $t9 $t3 #j
	sll $t9 $t9 2
	add $t1 $t1 $t9 
	mul $t9 $t7 $a3 #kk n
	sll $t9 $t9 2 
	add $t1 $t9 $t1#move B[kk, j] as 0+4J
	
	
	add $t9 $t6 4 #jj + bsize
	blt $t9 $a3 comparejjb_j#if jj+bsize < N, branch
	bge $t3 $a3  addI#if j>=N, go addI
	j loopJ

comparejjb_j:
	bge $t3 $t9  addI#if j>=jj+bsize, go addI	
	j loopJ
addI:
	addi $t5 $t5 1 #i = i+1
	beq $t5 $a3 addKK
	
	move $t0 $a0
	mul $t9 $a3 $t5 # ixN
	sll $t9 $t9 2
	add $t0 $t9 $t0 
	sll $t9 $t7 2
	add $t0 $t9 $t0 #move A[i,kk]
	
	move $t1 $a1#move B[kk,jj]
	mul $t9 $t6 4
	add $t1 $t9 $t1
	mul $t9 $t7 $a3
	sll $t9 $t9 2
	add $t1 $t1 $t9
	
	
	move $t2 $a2 
	mul $t9 $t5 $a3 #ixN
	sll $t9 $t9 2
	add $t2 $t9 $t2
	mul $t9 $t6 4
	add $t2 $t9 $t2 #move to C[i,jj] as 4(ixN + JJ)
	
	j loopI
addKK:

	add $t7 $t7 4 # kk = kk + bsize
	bge $t7 $a3 addJJ
	
	move $t2 $a2
	mul $t9 $t6 4
	add $t2 $t2 $t9 #move C[0, jj]
	
	move $t0 $a0 
	sll $t9 $t7 2
	add $t0 $t0 $t9 # move A[0,kk]
	
	move $t1 $a1#move B[kk,jj]
	mul $t9 $t6 4
	add $t1 $t9 $t1
	mul $t9 $t7 $a3
	sll $t9 $t9 2
	add $t1 $t1 $t9
	
	j loopKK
addJJ:
	add $t6 $t6 4 #jj = jj + 4
	bge $t6 $a3 EndLoop
	
	move $t1 $a1#move B[0,jj]
	mul $t9 $t6 4
	add $t1 $t9 $t1
	
	move $t2 $a2
	mul $t9 $t6 4
	add $t2 $t2 $t9 #move C[0, jj]
	
	move $t0 $a0 #move A[0, 0]
	
	j loopJJ
EndLoop:
	jr   $ra
