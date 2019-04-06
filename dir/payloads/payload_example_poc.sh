#!/bin/bash

sendPing () {
    curl 127.0.0.1:5000/cmd?id=21
}

sendResult () {
    curl 127.0.0.1:5000/cmd?r=test
}


while true
do
    sendPing
    sleep 2
done

#loop () {
#   curl 127.0.0.1:5000/cmd?id=525351
#
#}
#
#
#while true
#do
#    clear
# 	loop
# 	sleep 2
#done




# echo $(sudo dmidecode -t 4 | grep ID | sed 's/.*ID://;s/ //g') \
#       $(ifconfig | grep eth1 | awk '{print $NF}' | sed 's/://g') | sha256sum |
#  awk '{print $1}'
# $(ifconfig | grep wlp2s0 | awk '{print $NF}' | sed 's/://g') | md5sum | awk '{print $1}'