#!/bin/bash

#set -x

au_clips_path="/root/test/au"
clips_list=($(ls ${au_clips_path}/*.au))
clips_output_path="/var/tmp"

clips_size=${#clips_list[@]}
echo "Total clips are: ${clips_size}"

function copy_clips
{
        `mkdir -p ${clips_output_path}/clips_${file_duration}_second/`
        `cp ${clips_list[$i]} ${clips_output_path}/clips_${file_duration}_second/`
         #echo "File: ${clips_list[$i]}   Duration: ${file_duration}"
}

for (( i=0; i<${#clips_list[@]}; i++ ))
do
	file_duration=$(soxi -D ${clips_list[$i]} | awk -F '.' '{print $1}')
        if [[ $file_duration -ge 0 && $file_duration -lt 1 ]]
	then
		copy_clips
	elif [[ $file_duration -ge 1 && $file_duration -lt 2 ]]
	then
		copy_clips
	elif [[ $file_duration -ge 2 && $file_duration -lt 3 ]]
        then
                copy_clips
	elif [[ $file_duration -ge 3 && $file_duration -lt 4 ]]
        then
                copy_clips
	elif [[ $file_duration -ge 4 && $file_duration -lt 5 ]]
        then
                copy_clips
	elif [[ $file_duration -ge 5 && $file_duration -lt 6 ]]
        then
                copy_clips
	elif [[ $file_duration -ge 6 && $file_duration -lt 7 ]]
        then
                copy_clips
	else
		copy_clips
	fi

done

