# Yimei Yang 260898303
# TODO: ADD OTHER COMMENTS YOU HAVE HERE AT THE TOP OF THIS FILE
# TODO: SEE LABELS FOR PROCEDURES YOU MUST IMPLEMENT AT THE BOTTOM OF THIS FILE
# TODO: NOTICE THE TODO IN THE .DATA SEGMENT
# TODO: RENAME THIS FILE AS PER THE SUBMISSION REQUIREMENTS

# Menu options
# r - read text buffer from file 
# p - print text buffer
# e - encrypt text buffer
# d - decrypt text buffer
# w - write text buffer to file
# g - guess the key
# q - quit

.data
MENU:              .asciiz "Commands (read, print, encrypt, decrypt, write, guess, quit):"
REQUEST_FILENAME:  .asciiz "Enter file name:"
REQUEST_KEY: 	 .asciiz "Enter key (upper case letters only):"
REQUEST_KEYLENGTH: .asciiz "Enter a number (the key length) for guessing:"
REQUEST_LETTER: 	 .asciiz "Enter guess of most common letter:"
ERROR:		 .asciiz "There was an error.\n"


FILE_NAME: 	.space 256	# maximum file name length, should not be exceeded
KEY_STRING: 	.space 256 	# maximum key length, should not be exceeded

.align 2		# ensure word alignment in memory for text buffer (not important)
TEXT_BUFFER:  	.space 10000
.align 2		# ensure word alignment in memory for other data (probably important)
# TODO: define any other spaces you need, for instance, an array for letter frequencies
Alphabet_Frequencies:	.space 104 #an array for storing the frequecies of each alphabet in the input string
Guessed_key:	.space 256 #the string of the guessed key string
PrintError:	.asciiz "print\n"
Print2:		.asciiz "print2\n"
TestBuffer:	.space 104 
##############################################################
.text
		move $s1 $0 	# Keep track of the buffer length (starts at zero)
MainLoop:	li $v0 4		# print string
		la $a0 MENU
		syscall
		li $v0 12	# read char into $v0
		syscall
		move $s0 $v0	# store command in $s0			
		jal PrintNewLine

		beq $s0 'r' read
		beq $s0 'p' print
		beq $s0 'w' write
		beq $s0 'e' encrypt
		beq $s0 'd' decrypt
		beq $s0 'g' guess
		beq $s0 'q' exit
		b MainLoop

read:		jal GetFileName
		li $v0 13	# open file
		la $a0 FILE_NAME 
		li $a1 0		# flags (read)
		li $a2 0		# mode (set to zero)
		syscall
		move $s0 $v0
		bge $s0 0 read2	# negative means error
		li $v0 4		# print string
		la $a0 ERROR
		syscall
		b MainLoop
read2:		li $v0 14	# read file
		move $a0 $s0
		la $a1 TEXT_BUFFER
		li $a2 9999
		syscall
		move $s1 $v0	# save the input buffer length
		bge $s0 0 read3	# negative means error
		li $v0 4		# print string
		la $a0 ERROR
		syscall
		move $s1 $0	# set buffer length to zero
		la $t0 TEXT_BUFFER
		sb $0 ($t0) 	# null terminate the buffer 
		b MainLoop
read3:		la $t0 TEXT_BUFFER
		add $t0 $t0 $s1
		sb $0 ($t0) 	# null terminate the buffer that was read
		li $v0 16	# close file
		move $a0 $s0
		syscall
		la $a0 TEXT_BUFFER
		jal ToUpperCase
print:		la $a0 TEXT_BUFFER
		jal PrintBuffer
		b MainLoop	

write:		jal GetFileName
		li $v0 13	# open file
		la $a0 FILE_NAME 
		li $a1 1		# flags (write)
		li $a2 0		# mode (set to zero)
		syscall
		move $s0 $v0
		bge $s0 0 write2	# negative means error
		li $v0 4		# print string
		la $a0 ERROR
		syscall
		b MainLoop
		
write2:		li $v0 15	# write file
		move $a0 $s0
		la $a1 TEXT_BUFFER
		move $a2 $s1	# set number of bytes to write
		syscall
		bge $v0 0 write3	# negative means error
		li $v0 4		# print string
		la $a0 ERROR
		syscall
		b MainLoop
			
write3:		li $v0 16	# close file
		move $a0 $s0
		syscall
		b MainLoop

encrypt:	jal GetKey
		la $a0 TEXT_BUFFER
		la $a1 KEY_STRING
		jal EncryptBuffer
		la $a0 TEXT_BUFFER
		jal PrintBuffer
		b MainLoop

decrypt:	jal GetKey
		la $a0 TEXT_BUFFER
		la $a1 KEY_STRING
		jal DecryptBuffer
		la $a0 TEXT_BUFFER
		jal PrintBuffer
		b MainLoop

guess:		li $v0 4		# print string
		la $a0 REQUEST_KEYLENGTH
		syscall
		li $v0 5		# read an integer
		syscall
		move $s2 $v0
		
		li $v0 4		# print string
		la $a0 REQUEST_LETTER
		syscall
		li $v0 12	# read char into $v0
		syscall
		move $s3 $v0	# store command in $s0			
		jal PrintNewLine

		move $a0 $s2
		la $a1 TEXT_BUFFER
		la $a2 KEY_STRING
		move $a3 $s3
		jal GuessKey
		li $v0 4		# print String
		la $a0 KEY_STRING
		syscall
		jal PrintNewLine
		b MainLoop

exit:		li $v0 10 	# exit
		syscall

###########################################################
PrintBuffer:	li $v0 4          # print contents of a0
		syscall
		li $v0 11	# print newline character
		li $a0 '\n'
		syscall
		jr $ra

###########################################################
PrintNewLine:	li $v0 11	# print char
		li $a0 '\n'
		syscall
		jr $ra

###########################################################
PrintSpace:	li $v0 11	# print char
		li $a0 ' '
		syscall
		jr $ra

#######################################################
GetFileName:	addi $sp $sp -4
		sw $ra ($sp)
		li $v0 4		# print string
		la $a0 REQUEST_FILENAME
		syscall
		li $v0 8		# read string
		la $a0 FILE_NAME  # up to 256 characters into this memory
		li $a1 256
		syscall
		la $a0 FILE_NAME 
		jal TrimNewline
		lw $ra ($sp)
		addi $sp $sp 4
		jr $ra

###########################################################
GetKey:		addi $sp $sp -4
		sw $ra ($sp)
		li $v0 4		# print string
		la $a0 REQUEST_KEY
		syscall
		li $v0 8		# read string
		la $a0 KEY_STRING  # up to 256 characters into this memory
		li $a1 256
		syscall
		la $a0 KEY_STRING
		jal TrimNewline
		la $a0 KEY_STRING
		jal ToUpperCase
		lw $ra ($sp)
		addi $sp $sp 4
		jr $ra

###########################################################
# Given a null terminated text string pointer in $a0, if it contains a newline
# then the buffer will instead be terminated at the first newline
TrimNewline:	lb $t0 ($a0)
		beq $t0 '\n' TNLExit
		beq $t0 $0 TNLExit	# also exit if find null termination
		addi $a0 $a0 1
		b TrimNewline
		
TNLExit:	sb $0 ($a0)
		jr $ra

##################################################
# converts the provided null terminated buffer to upper case
# $a0 buffer pointer
ToUpperCase:	lb $t0 ($a0)
		beq $t0 $zero TUCExit
		blt $t0 'a' TUCSkip
		bgt $t0 'z' TUCSkip
		addi $t0 $t0 -32	# difference between 'A' and 'a' in ASCII
		sb $t0 ($a0)
TUCSkip:	addi $a0 $a0 1
		b ToUpperCase
TUCExit:		jr $ra

###################################################
# END OF PROVIDED CODE... 
# TODO: use this space below to implement required procedures
###################################################









##################################################
# null terminated buffer is in $a0
# null terminated key is in $a1
EncryptBuffer:	# TODO: Implement this function!
		addi $t3 $a1 0

	RecursiveCall:  
			lb $t0 ($a0) #load 1 letter of the unencrypted string into $t0
			lb $t1 ($a1) #load 1 letter of the key string into $t1
			beq $t0 $zero JumpBack #if we reach the end of the string, return the string
			beq $t1 $zero WrapKey #if the key string reaches to the end, start over
			blt $t0 'A' StringSkip
			bgt $t0 'Z' StringSkip
			sub $t1 $t1 65 #subtract the key letter to get the shift amount
			add $t0 $t0 $t1 #shift the string letter by the shift amount
			bgt $t0 90 WrapAround
			sb $t0 ($a0) #store the shifted letter into the original string repeat the procedure for the nextl etter
			addi $a0 $a0 1 #move to the next letter of the string
			addi $a1 $a1 1 #move to the next letter of the key string
			j RecursiveCall
	WrapAround: 	sub $t0 $t0 90
			add $t0 $t0 64
			sb $t0 ($a0) #store the shifted letter into the original string
			addi $a0 $a0 1 #move to the next letter of the string
			addi $a1 $a1 1 #move to the next letter of the key string
			j RecursiveCall
		 
	WrapKey:	addi $a1 $t3 0
			j RecursiveCall
	StringSkip:	sb $t0 ($a0)
			addi $a0 $a0 1 #move to the next letter of the string
			addi $a1 $a1 1 #move to the next letter of the key string
			j RecursiveCall
	JumpBack:	jr $ra
##################################################
# null terminated buffer is in $a0
# null terminated key is in $a1
DecryptBuffer:	# TODO: Implement this function!
		addi $t3 $a1 0 #copy the original key string

	RecursiveCall2:  
			lb $t0 ($a0) #load 1 letter of the unencrypted string into $t0
			lb $t1 ($a1) #load 1 letter of the key string into $t1
			beq $t0 $zero JumpBack2 #if we reach the end of the string, return the string
			beq $t1 $zero WrapKey2 #if the key string reaches to the end, start over
			blt $t0 'A' StringSkip2 #if the string character is not an alphabet, skip
			bgt $t0 'Z' StringSkip2
			sub $t1 $t1 65 #subtract the key letter to get the shift amount
			sub $t0 $t0 $t1 #shift back the string letter by the shift amount
			blt $t0 65 WrapAround2 #if the shifted letter < A, start from Z
			sb $t0 ($a0) #store the shifted letter into the original string repeat the procedure for the next letter
			addi $a0 $a0 1 #move to the next letter of the string
			addi $a1 $a1 1 #move to the next letter of the key string
			j RecursiveCall2
	WrapAround2: 	add $t0 $t0 90
			sub $t0 $t0 64
			sb $t0 ($a0) #store the shifted letter into the original string
			addi $a0 $a0 1 #move to the next letter of the string
			addi $a1 $a1 1 #move to the next letter of the key string
			j RecursiveCall2
		 
	WrapKey2:	addi $a1 $t3 0
			j RecursiveCall2
	StringSkip2:	sb $t0 ($a0)
			addi $a0 $a0 1 #move to the next letter of the string
			addi $a1 $a1 1 #move to the next letter of the key string
			j RecursiveCall2
	JumpBack2:	jr $ra

###########################################################
# a0 keySize - size of key length to guess
# a1 Buffer - pointer to null terminated buffer to work with
# a2 KeyString - on return will contain null terminated string with guess
# a3 common letter guess - for instance 'E' 
GuessKey:	# TODO: Implement this function!
	addi $sp $sp -4
	sw $ra ($sp)

	la $t7 ($a2) 
	li $t0 0
	
		count_n_loop:
		
		li $t8 0
		li $t3 0
		la $t4 Alphabet_Frequencies
		la $t5 ($a1)
		
		add $t5 $t5 $t0 
		
		la $t6 TestBuffer
		
		bge $t0 $a0 stopLoop #if we loop over n times, we stop
		
			iniArray:
				beq $t3 26 FormFarray
				li $t9 65
				sb $t9 ($t4)
				addi $t4 $t4 1
				addi $t3,$t3,1
				j iniArray
			
			
		
			FormFarray:
			
			#loop the string n times, and each time guesses each index of the key
				#extract the alphabet from the string				
				la $t4 Alphabet_Frequencies	
				lb $t1 ($t5) #gets the alphabet from the string
				

				beq $t1 $zero indexKey #if the string reaches the end, find the alphabet with the most frequency
				
				sub $t1 $t1 65 #make alphabet into index
				#add the frequency by 1
				la $t2 ($t4) #load the address of the frequecy array into $t2
				add $t2 $t2 $t1 #array's pointer moves to the right index
				#li $t3 0 #clear $t3
				lb $t3 0($t2) #extract the value from that index
				addi $t3 $t3 1 #increase the frequency by one
				sb $t3 0($t2) #store the changed value back to the index
				#move to the next alphabet
				add $t5 $a0 $t5 #index = n+index 
				j FormFarray
			indexKey: 	
				la $t2 Alphabet_Frequencies#move the pointer of the array back
				sub $t3 $t3 $t3 #clear 
					FindMostLoop:
					lb $t1 ($t2) #load one frequency from the frequency array
					beq $t1 $zero addIndex #if we reach the end of the array, add the alphabet into the key string
					bgt $t1 $t8 findMax #if frequency 2 > frequency 1, set frequency 2 as MAX
					#sb $zero ($t2) #clear this index of the array
					addi $t2 $t2 1 #if no, move to the next frequency
					j FindMostLoop 
						addIndex:
							la $t4 Alphabet_Frequencies
							sub $t3 $t3 $t4 #most frequent alphabet
							addi $t3 $t3 65
							bgt $t3 $a3 addM
							blt $t3 $a3 addL
							li $t3 65
							sb $t3 ($t7)
							addi $t7 $t7 1 #move the pointer to the next byte of the key string
							addi $t0 $t0 1 #add 1 to the count_n
							j count_n_loop
								addM:
									sub $t3 $t3 $a3
									addi $t3 $t3 65
									sb $t3 ($t7)
									addi $t7 $t7 1 #move the pointer to the next byte of the key string
									addi $t0 $t0 1 #add 1 to the count_n
									j count_n_loop
								addL:
									li $t1 90
									sub $t9 $t1 $a3
									sub $t3 $t3 64
									add $t3 $t9 $t3
									addi $t3 $t3 65
									sb $t3 ($t7)
									addi $t7 $t7 1 #move the pointer to the next byte of the key string
									addi $t0 $t0 1 #add 1 to the count_n
									j count_n_loop
						findMax:
							move $t8 $t1 #set MAX as the larger frequency
							add $t3 $zero $t2 #get the index of the MAX frequency
							#sb $zero ($t2) #clear this index of the array
							addi $t2 $t2 1 #move to the next frequency
							j FindMostLoop	
stopLoop:	
		sb $zero ($t7)
		lw $ra ($sp)
		addi $sp $sp 4
		jr $ra #return the guessed key string
