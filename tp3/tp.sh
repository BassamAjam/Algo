#!/bin/bash

OPTIONS=""
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -k)
    RATE="$2"
    shift
    ;;
    -e)
    EX_PATH="$2"
    shift
    ;;
    -p)
    OPTIONS="${OPTIONS}${1} "
    ;;
    *)
        echo "Argument inconnu: ${1}"
        exit
    ;;
esac
shift
done

g++ -o code code.cpp&code.exe -e $EX_PATH -k $RATE $OPTIONS

# ./code -e $EX_PATH -k $RATE $OPTIONS

