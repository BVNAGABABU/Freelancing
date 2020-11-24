#!/bin/bash

#set -x

ip_list=("ip_1" "ip_2" "ip_3" "ip_4" "ip_5" "ip_6" "ip_7" "ip_8" "ip_9" "ip_10")

for (( i=0; i<${#ip_list[@]}; i++ ))
do
        echo "Configuring ssh key for ${ip_list[$i]}"
        #Please configure remote server username in the user_name field below as per your requirement
        ssh user_name@${ip_list[$i]} "mkdir -p /home/user_name/.ssh; chmod 700 /home/user_name/.ssh; echo \"<confiugre MAIN ANSIBLE SERVER PUBLIC KEY AVAILABLE IN /USER_HOME_DIRECTORY/.ssh/id_rsa.pub here>\" >> /home/user_name/.ssh/authorized_keys; chmod 640 /home/user_name/.ssh/authorized_keys"
done
