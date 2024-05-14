#!/bin/sh

Partition(){
    local pivot=${arr[$2]}
    local i=$(($1 - 1))
    
    for ((j=$1;j<$2;j++)); do
        if [ ${arr[$j]} -le $pivot ]; then
            ((i++))
            tmpVal=${arr[$j]}
            arr[$j]=${arr[$i]}
            arr[$i]=$tmpVal
        fi
    done
    ((i++))
    local tmpVal=${arr[$2]}
    arr[$2]=${arr[$i]}
    arr[$i]=$tmpVal

    Gpiv=$i
}

Quicksort(){
    if [ $1 -lt $2 ]; then
        Partition $1 $2
        local piv=$Gpiv
        Quicksort $1 $(($piv - 1))
        Quicksort $(($piv + 1)) $2
    fi
}

arr=($@)
Quicksort 0 $((${#arr[*]} - 1))
echo ${arr[*]}