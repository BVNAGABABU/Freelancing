#!/bin/bash

#set -x

au_clips_path="/root/test/au"
clips_list=($(ls ${au_clips_path}/*.au))
clips_output_path="/var/tmp"

clips_size=${#clips_list[@]}
echo "Total clips are: ${clips_size}"

for (( i=0; i<${#clips_list[@]}; i++ ))
do
        file_duration=$(soxi -D ${clips_list[$i]} | awk -F '.' '{print $1}')
        if [[ ! -d "${clips_output_path}/clips_${file_duration}_second/" ]]
        then
                `mkdir ${clips_output_path}/clips_${file_duration}_second/`
        fi
        `cp ${clips_list[$i]} ${clips_output_path}/clips_${file_duration}_second/`
done
