#!/bin/bash

DIR=$1
SUMA=0
COUNT=0
for FILE in $(ls $DIR)
do
    if file $FILE | grep -q "ASCII text"; then
	LINII=`wc -l $FILE | awk '{print $1}'`
	let SUMA=SUMA+LINII
	let COUNT++
	echo 'file:' $FILE ' - ' $LINII
    fi
done
echo 'Numar mediu de linii:' $[$SUMA/$COUNT]
