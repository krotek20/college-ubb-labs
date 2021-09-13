#!/bin/bash

for FILE in `ls $1`
do
    if file $FILE | grep -q "ASCII text"; then
	echo $FILE
	head -3 $FILE
    fi
done
