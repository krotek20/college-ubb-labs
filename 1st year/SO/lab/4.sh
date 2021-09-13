#!/bin/bash

# ./4.sh -s subiect.txt -m mesaj.txt -l lista.txt

while ! [ $# -eq 0 ]
do
    case $1 in
    -s ) 
	SUB=`cat $2`
	shift 2
	;;
    -m )
	MSG=`cat $2`
	shift 2
	;;
    -l )
	LST=`cat $2`
	shift 2
	;;
    * )
	echo Optiune invalida!
	;;
    esac
done

echo $SUB
echo $MSG
echo $LST

for USER in $LST
do
    mail -s $SUB $USER <<< $MSG
    sleep 5
done
