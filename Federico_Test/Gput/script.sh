#! /bin/bash

filenum=$1
d=$2

start=$SECONDS
netstat -s | grep segments > output$filenum.txt
 
sudo tshark -i eth1 -a duration:$d -T fields -e tcp.len -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmission -e tcp.analysis.spurious_retransmission -Y "ip.src == 172.16.5.1" > example$filenum.csv

netstat -s | grep segments >> output$filenum.txt
