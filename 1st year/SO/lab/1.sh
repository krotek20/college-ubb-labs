#!/bin/bash

if ! [ $# -eq 1 ]; then
    echo da-mi un numar
    exit 1
fi

N=1
while [ $N -le $1 ]
do
    touch file_$N.txt
    sed -n "$N,+5p" passwd.fake > file_$N.txt
    let N++
done
