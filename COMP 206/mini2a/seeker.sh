#! /bin/bash

#if there is no argument, report an error
if [[ $# -eq 0 ]]
then
	echo -e "Error missing the pattern argument\nUsage ./seeker.sh [-c] [-a] pattern [path]"
	exit 1
#if there is only 1 argument and it is not the pattern, report an error
elif [[ $# -eq 1 ]]
then
	if [[ $1 = "-c" || $1 = "-a" ]]
	then
		echo -e "Error missing the pattern argument\nUsage ./seeker.sh [-c] [-a] pattern [path]"
		exit 1
	fi
#if there is 2 arguments but there is no patter, report an error
elif [[ $# -eq 2 ]]
then
	if [[ $2 = "-a" ]]
	then
		echo -e "Error missing the pattern argument\nUsage ./seeker.sh [-c] [-a] pattern [path]"
		exit 1
	fi
fi

#if there is only one argument, check whether this is a path and whether it is valid
if [[ $# -eq 1 ]]
then
	if [[ $1 == */* && ! -d $1 ]]
	then
		echo "Error $1 is not a valid directory"
		exit 1
	fi
#if there are 2 arguments, check whether the last argument is a path and whether it is valid
elif [[ $# -eq 2 ]]
then
	if [[ $2 == */* && ! -d $2 ]]
	then
		echo "Error $2 is not a valid directory"
		exit 1
	fi
#if there are 3 arguments, check whether the last argument is a path and whether it is valid
elif [[ $# -eq 3 ]]
then
       	if [[ $3 == */* && ! -d $3 ]]
	then
		echo "Error $3 is not a valid directory"
		exit 1
	fi
#if there are 4 arguments, check whether the last argument is a path and whether it is valid
elif [[ $# -eq 4 ]]
then
	if [[ $4 == */* && ! -d $4 ]]
	then
		echo "Error $4 is not a valid directory"
		exit 1
	fi
fi

#if there are 2 arguments, check whether a path exist
if [[ $# -eq 2 ]]
then 
	#if exist, check whether the pattern can be found
	if [[ $2 == */* ]]
	then
		if [[ ! `ls $2 | grep $1` ]]
		then
			echo "Unable to locate any files that has pattern $1 in its name in $2"
			exit 1
		else
			#if yes, display one random result
			find $2 | grep -m 1 $1
			exit 0
		fi
	else
		#if the path does not exist
		if [[ $1 = "-c" ]]
		then
			#display the content of a random result if the first argument is -c
			if [[ ! `ls $(pwd) | grep $2` ]]
			then 
				echo "Unable to locate anyfiles that has pattern $2 in its name in $(pwd)"
				exit 1
			else
				A=`ls $(pwd) | grep -m 1 $2`
				echo "=== Contents of: "$(pwd)/$A" ==="
				cat $A
				echo -e "\n"
				exit 0
			fi
		elif [[ $1 = "-a" ]]
		then
			#display the path of all the applicable results if the first argument is -a
			if [[ ! `ls $(pwd) | grep $2` ]]
			then
				echo "Unable to locate any files that has pattern $2 in its name in $(pwd)"
				exit 1
			else
				find $(pwd) | grep $2
				exit 0
			fi
		fi
	fi
#if there is only one argument
elif [[ $# -eq 1 ]]
then
	#look for pattern under the current directory
	if [[ ! `ls $(pwd) | grep $1` ]]
	then
		echo "Unable to locate any files that has pattern $2 in its name in $(pwd)"
		exit 1
	else
		#and display the path of a random result
		A=`ls $(pwd) | grep -m 1 $1`
		echo "=== Contents of: "$(pwd)/$A" ==="
		cat $A
		echo -e "\n"
		exit 0
	fi
#if there is 3 arguments,check whether a path exists
elif [[ $# -eq 3 ]]
then
	#if yes and the first argument is -c 
	if [[ $3 == */* && $1 = "-c" ]]
	then
		if [[ ! `ls $3 | grep $2` ]]
		then 
			echo "Unable to locate any files that has pattern $2 in its name in $3"
			exit 1
		else
			#display the content of a random result
			A=`ls $3 | grep -m 1 $2`
			echo "=== Contents of: "$3/$A" ==="
			cat $3/$A
			echo -e "\n"
			exit 0
		fi
	#if yes and the first argument is -a
	elif [[ $3 == */* && $1 == "-a" ]]
	then
		#display the path of all the applicable results.
		if [[ ! `ls $3 | grep $2` ]]
		then
			echo "Unable to locate any files that has pattern $2 in its name in $3"
			exit 1
		else
			find $3 | grep $2
			exit 0
		fi
	else
		#if the path does not exist
		if [[ ! `ls $(pwd) | grep $3` ]]
		then
			echo "Unable to locate anyfiles that has pattern $2 in its name in $(pwd)"
			exit 1
		else
			#display the contents of all the applicable results
			A=`ls $(pwd) | grep $3`
			for i in $A
			do
				echo "=== Contents of: "$(pwd)/$i" ==="
				cat $i
				echo -e "\n"
			done
			exit 0
		fi
	fi
#if there are 4 arguments
elif [[ $# -eq 4 ]]
then
	if [[ $4 == */* ]]
	then
		if [[ ! `ls $4 | grep $3` ]]
		then
			echo "Unable to locate any files that has pattern $3 in its name in $4"
			exit 1
		else
			#display the contents of all the applicable results
			A=`ls $4 | grep $3`
                        for i in $A
                        do
                                echo "=== Contents of: "$4/$i" ==="
                                cat $4/$i
				echo -e "\n"
                        done
			exit 0
		fi	
	fi
fi

