#!/usr/bin/env python3
import time
import pyshark
import csv
import threading
from subprocess import call

 #Capture time in seconds
try:
    t_cap = int(sys.argv[1])
except:
    t_cap = 7*60

def one_time(t):
    sec = int(t)%60
    min = int(t/60)%60
    return str(min)+ "." + str(sec) + "m"

def time_func(time1):
    time2 = time.time()
    sec = (int(time2)%60)
    min = (int(time2/60)%60)
    diff = int(time2-time1)
    diff_min = (int(diff/60)%60)
    diff_sec = (int(diff)%60)

    return [str(diff_min)+ "." + str(diff_sec) + "m", str(min)+ "." + str(sec) + "m"]


def capture_func(t_cap):
    time1 = time.time()
    print("Client started capture at: " + one_time(time1) + ", duration: " + one_time(t_cap))

    cap = pyshark.LiveCapture(interface='eth1',
            output_file="/home/nas/simone_scripts/out_client/client18_capture.pcap",
            bpf_filter='udp port 443')

    cap.sniff(timeout=t_cap)

    times = time_func(time1)
    print("Client sniffing finished in: " + times[0] + ", at: " + times[1])
    time1 = time.time()
    print("Client started parsing")
    print(cap); #print summary of capture

    count = len(cap); #number of packets
    packet_list = []
    packet_element = [];

    for i in range(0,count):
        try:
            packet_element = [cap[i].sniff_timestamp, cap[i]['ip'].src,
                                cap[i].quic.packet_number, cap[i].quic.cid]
            packet_list.append(packet_element)
        except:
            try:
                packet_element = [cap[i].sniff_timestamp, cap[i]['ip'].src,
                                    cap[i].quic.packet_number]
                packet_list.append(packet_element)
            except:
                pass

    csvfile = open('./out_client/client18_capture.csv', 'wb')

    writer = csv.writer(csvfile)
    writer.writerows(packet_list)

    times = time_func(time1)
    print("Client parsing finished in: " + times[0] + ", at: " + times[1])

def client_func():
    time1 = time.time()
    print("Client started at: " + one_time(time1))

    path_s = "/home/nas/chromium/src/out/Default/quic_client"
    no_cert = "--disable-certificate-verification"
    server_ip = "--host=172.16.9.1"
    port = "--port=443"#"--port=6121"
    url = "https://www.example.org/"
    quiet_opt = "--quiet"
    call([path_s, no_cert, server_ip, port, quiet_opt, url])

    times = time_func(time1)
    print("Client transmission finished in: " + times[0] + ", at: " + times[1])



t1 = threading.Thread(target=capture_func, args=[t_cap])
t2 = threading.Thread(target=client_func, args=[])

#starting capture thread
#t1.start()

#wait a bit just to make sure capture already running when starting the client
time.sleep(30)

#starting client
t2.start()
