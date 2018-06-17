#!/usr/bin/env python3
import time
import pyshark
import csv

try:
    t_cap = int(sys.argv[1])
except:
    t_cap = 30 #capture time in seconds

cap = pyshark.LiveCapture(interface='eth1',
        output_file="/home/nas/Simone_scripts/out/capture.pcap")#,
        #bpf_filter='udp')

cap.sniff(timeout=t_cap)
print(cap); #print summary of capture

count = len(cap); #number of packets

packet_list = []
packet_element = [];

for i in range(0,count-1):
    packet_element = [cap[i].sniff_timestamp, 0]
    packet_list.append(packet_element)
    #packet_list.append(cap[i].sniff_timestamp)

csvfile = open('./out/timestamps.csv', 'wb')

writer = csv.writer(csvfile)
writer.writerows(packet_list)



#for i in range(0, len(packet_list)-1):
#    print(packet_list[i])


#print(cap[i].sniff_timestamp)


