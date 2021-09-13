#!/bin/bash

for ARG in $@
do
    if [ -f $ARG ]; then
	echo -n $ARG
	echo -en '\t' `cat $ARG | wc -m`
	echo -e '\t' `cat $ARG | wc -l`
    elif [ -d $ARG ]; then
	echo -n $ARG
	echo -e '\t' `ls -l $ARG | grep -c '^-'`
    fi
done
