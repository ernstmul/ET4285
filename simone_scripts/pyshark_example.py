#!/usr/bin/env python3
import time
import pyshark
import csv
import threading
from subprocess import call


try:
    t_cap = int(sys.argv[1])
except:
    t_cap = 60*5 #capture time in seconds

def capture_func(t_cap):
    print("started capture")
    cap = pyshark.LiveCapture(interface='eth1',
            output_file="/home/nas/Simone_scripts/out/capture.pcap",
            bpf_filter='udp')

    cap.sniff(timeout=t_cap)
    
    print("Sniffing finished at: " + str(time.time()))
    print(cap); #print summary of capture

    count = len(cap); #number of packets
    packet_list = []
    packet_element = [];

    for i in range(0,count-1):
        packet_element = [cap[i].sniff_timestamp, cap[i]['ip'].src, cap[i]['ip'].dst]
        packet_list.append(packet_element)

    csvfile = open('./out/timestamps.csv', 'wb')

    writer = csv.writer(csvfile)
    writer.writerows(packet_list)



def client_func():
    print("started client")

    path_s = "/home/nas/chromium/src/out/Default/quic_client"
    no_cert = "--disable-certificate-verification"
    server_ip = "--host=172.16.9.1"
    port = "--port=6121"
    url = "https://www.example.org/"
    quiet_opt = "--quiet"
    call([path_s, no_cert, server_ip, port, quiet_opt, url])

    
    print("client finished at: " + str(time.time()))

t1 = threading.Thread(target=capture_func, args=[t_cap])
t2 = threading.Thread(target=client_func, args=[])

#starting capture thread
t1.start()

#wait a bit just to make sure capture already running when starting the client
time.sleep(30)

#starting client
t2.start()


#for i in range(0, len(packet_list)-1):
#    print(packet_list[i])


#print(cap[i].sniff_timestamp)


