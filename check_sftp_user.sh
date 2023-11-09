#!/bin/bash

IFS=$'\n'
array_data=($(cat data.txt))

available_users=()
not_available_users=()

for (( i=0; i<${#array_data[@]}; i++ ))
do
    output=$(id sftp_${array_data[$i]})
    if [[ $output == *"uid"* ]]
    then
        #echo "${array_data[$i]} user id is available"
        available_users+=(${array_data[$i]})
    else
        #echo "${array_data[$i]} user id is not available"
        not_available_users+=(${array_data[$i]})
    fi
done

echo "\n================================"
echo "Available users list:"
echo "================================"

for (( j=0; j<${#available_users[@]}; j++ ))
do
    echo "${available_users[$j]}"
done

echo "\n==============================="
echo "Not available users list:"
echo "================================"
for (( k=0; k<${#not_available_users[@]}; k++ ))
do
    echo "${not_available_users[$k]}"
done
