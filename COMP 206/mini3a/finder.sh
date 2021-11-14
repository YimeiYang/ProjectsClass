#!/bin/bash

#check whether the file a3config exists under the current directory
if [[ ! -f a3config ]]; then
	echo "Error cannot find a3config"
	exit 1
fi

source a3config
#check whether the a3config has the variable EXTENSION

if [[ ! -n $EXTENSION || -z "$EXTENSION" ]]; then
	echo " Extension -Error DIRNAME and EXTENSION must be set."
	exit 2
elif [[ ! -n $DIRNAME || -z "$DIRNAME" ]]; then
	echo "Dirname - Error DIRNAME and EXTENSION must be set."
	exit 2
fi

#check whether the directory is valid
if [[ ! -d $DIRNAME ]]; then
	echo "Error directory $DIRNAME does not exist"
	exit 3
fi

#check whether the script can locate any corresponding file
if [[ ! `ls $DIRNAME | grep $EXTENSION` ]]; then
	echo "Unable to locate any files with extention $EXTENSION in $DIRNAME"
	exit 0
fi
#check whether SHOW is true. If yes, display the contend. If no, idsplay the directory
if [[ $SHOW == true ]]; then
	X=`ls $DIRNAME | grep .*\.$EXTENSION$`
	for i in $X
	do 
		echo "$DIRNAME/$i"
		cat $DIRNAME/$i
	done
	exit 0
elif [[ $SHOW != true || -z $SHOW ]]; then
	X=`ls $DIRNAME | grep .*\.$EXTENSION$`
        for i in $X
        do
                echo "$DIRNAME/$i"
        done
        exit 0
fi

