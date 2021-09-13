#!/bin/bash

for FILE in `ls $1`
do
    if cat $FILE | grep -q '[0-9]\{5,\}'; then
	echo $FILE
    fi
done
