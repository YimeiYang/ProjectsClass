#! /bin/bash

if [ $# != 2 ]
then
	echo "Usage ./$0 filename tarfile"
	exit 1
fi

if [ ! -f $2 ]
then
	echo "Error can not found $2"
	exit 1
fi

if [[ `tar -tf $2 | grep $1` ]] 
then
	echo "$1 exists in $2"
else
	echo "$1 does not exist in $2"
fi

