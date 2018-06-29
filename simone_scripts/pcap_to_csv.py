#!/usr/bin/env python3
import pyshark
import csv
import time

def pcap_to_list(path):
    cap = pyshark.FileCapture(input_file=path, keep_packets=False)

    pkt_list = []

    packet_no_n = 0

    while True:
        try:
            pkt = cap.next()
        except:
            break
        if pkt == None:
            break
        else:
            try:
                list_element = [pkt.sniff_timestamp, pkt.quic.packet_number]
                pkt_list.append(list_element)
            except:
                packet_no_n = packet_no_n + 1

    print("Packets without a number: " + str(packet_no_n))

    return pkt_list

def write_list_to_cap(path, list_t):
    csvfile = open(path, 'wb')

    writer = csv.writer(csvfile)
    writer.writerows(list_t)

def one_time(t):
    sec = int(t)%60
    minutes = int(t/60)%60
    return str(minutes)+ "." + str(sec) + "m"



t_start = time.time()


#############################################################
#                   Client received                         #
#############################################################

client_received_file = 'out_client/client_rec_capture.pcap'

client_received = pcap_to_list(client_received_file)


for i in range(1, 12):
    file_name = 'out_client/client_rec_capture.pcap' + str(i)

    client_received = client_received + pcap_to_list(file_name)

csv_file = 'out_client/client_rec_capture.csv'

write_list_to_cap(csv_file, client_received)


#############################################################
#                      Client sent                          #
#############################################################

client_sent_file = 'out_client/client_sent_capture.pcap'

client_sent = pcap_to_list(client_sent_file)

csv_file = 'out_client/client_sent_capture.csv'

write_list_to_cap(csv_file, client_sent)


#############################################################
#                       Server sent                         #
#############################################################

server_sent_file = 'out_server/server_sent_capture.pcap'

server_sent = pcap_to_list(server_sent_file)

for i in range(1, 12):
    file_name = 'out_server/server_sent_capture.pcap' + str(i)

    server_sent = server_sent + pcap_to_list(file_name)

csv_file = 'out_server/server_sent_capture.csv'

write_list_to_cap(csv_file, server_sent)


#############################################################
#                   Server received                         #
#############################################################

server_received_file = 'out_server/server_rec_capture.pcap'

server_received = pcap_to_list(server_received_file)

csv_file = 'out_server/server_rec_capture.csv'

write_list_to_cap(csv_file, server_received)



#############################################################
#                           Log                             #
#############################################################

duration = time.time() - t_start
print("Processing took: " + one_time(duration))

print(len(client_sent))
print(len(client_received))

print(len(server_sent))
print(len(server_received))

print("Packets from server to client lost: " + str(len(server_sent) - len(client_received)))

print("Packets from client to server lost: " + str(len(client_sent) - len(server_received)))









